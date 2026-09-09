#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generateur du site electricien-richard.fr

Usage : python3 tools/build.py
Produit des fichiers HTML statiques a la racine du depot, ainsi que
sitemap.xml, robots.txt et PHOTOS-A-FOURNIR.md.
"""

import os
import re
import sys
import json
import shutil
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from render import (ROOT, esc, abs_url, url_for, picture, icon, phone_link, quick_answer,
                    table, callout, steps_block, checks, faq_block, cta_band, cta_inline,
                    link_cloud, map_block, faq_node, render_page, MISSING_IMAGES,
                    BUSINESS_ID, geo_card)
from content.site import SITE, has_phone
from content import images as IMG
from content.zones import DEPARTEMENTS, city_url, dept_url, map_points, all_cities
from content.services import SERVICES, BLOCKS
from content import blog as BLOG

BUILD_DATE = date.today().isoformat()
PAGES = []          # (path, lastmod, priority, changefreq) pour le sitemap

AREA_NAMES = [d["name"] for d in DEPARTEMENTS]
SERVICE_BY_SLUG = {s["slug"]: s for s in SERVICES}


# --------------------------------------------------------------- utilitaires
def write(path, html, indexable=True, priority="0.6", changefreq="monthly"):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(html)
    if indexable:
        PAGES.append((url_for(path), BUILD_DATE, priority, changefreq))


def toc_from_body(body_html, min_items=3):
    """Sommaire genere a partir des <h2 id=...> du corps de page."""
    items = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body_html, re.S)
    if len(items) < min_items:
        return ""
    lis = "".join('<li><a href="#%s">%s</a></li>' % (i, re.sub(r"<[^>]+>", "", t).strip())
                  for i, t in items)
    return ('<nav class="toc" aria-label="Sommaire"><h2>Sur cette page</h2>'
            "<ol>%s</ol></nav>" % lis)


def expand_blocks(html):
    def repl(m):
        key = m.group(1)
        if key in BLOCKS:
            return BLOCKS[key]
        if key == "SERVICES_GRID":
            return services_grid()
        if key == "ZONES_STRIP":
            return zones_strip()
        raise KeyError("Bloc inconnu : %s" % key)
    return re.sub(r"\{\{([A-Z_]+)\}\}", repl, html)


def service_node(svc, page_url):
    return {
        "@type": "Service",
        "@id": abs_url(page_url) + "#service",
        "name": svc.get("service_type", svc["h1"]),
        "serviceType": svc.get("service_type", svc["h1"]),
        "description": svc["desc"],
        "provider": {"@id": BUSINESS_ID},
        "areaServed": [{"@type": "AdministrativeArea", "name": n} for n in AREA_NAMES],
        "url": abs_url(page_url),
    }


# --------------------------------------------------------------- composants
MAIN_SERVICES = ["electricien-depannage", "electricien-urgence", "recherche-panne",
                 "installation-electrique", "renovation-electrique",
                 "mise-aux-normes-electrique", "tableau-electrique", "borne-recharge"]


def service_card(slug):
    s = SERVICE_BY_SLUG[slug]
    return (
        '<article class="card"><div class="card-icon">%s</div>'
        "<h3>%s</h3><p>%s</p>"
        '<a class="card-link" href="/%s">En savoir plus<span class="visually-hidden"> sur %s</span></a>'
        "</article>" % (icon(s.get("icon", "bolt"), 24), esc(s["h1"].split(" :")[0]),
                        esc(s["card_desc"]), s["path"], esc(s["h1"])))


def services_grid(slugs=None, cols="grid--3"):
    slugs = slugs or MAIN_SERVICES
    return '<div class="grid %s">%s</div>' % (cols, "".join(service_card(s) for s in slugs))


def zones_strip(intro=True):
    cards = []
    for d in DEPARTEMENTS:
        cities = "".join('<li><a href="%s">%s</a></li>' % (city_url(d, c), esc(c["name"]))
                         for c in d["cities"])
        cards.append(
            '<article class="zone-card"><span class="dept-code">%s</span>'
            '<h3><a href="%s">%s</a></h3><p>%s</p><ul class="city-links">%s</ul></article>'
            % (d["code"], dept_url(d), esc(d["name"]),
               esc("Interventions %s : dépannage, installation, rénovation et mise aux normes."
                   % d["prep"]), cities))
    head = ("<p>Electricien Richard intervient exclusivement dans ces six départements de "
            "Bretagne et des Pays de la Loire.</p>") if intro else ""
    return head + '<div class="zone-grid">%s</div>' % "".join(cards)


def sidebar_block(related_slugs=None, extra=""):
    cards = []
    cards.append(
        '<div class="card card--plain"><div class="card-icon">%s</div>'
        "<h3>Besoin d'un électricien ?</h3>"
        "<p>Décrivez votre situation : dépannage, travaux ou simple question sur votre "
        "installation.</p>"
        '<div class="btn-row" style="flex-direction:column">%s'
        '<a class="btn btn--ghost btn--sm" href="/devis-electricien.html">Demander un devis</a>'
        "</div></div>" % (icon("phone", 24), phone_link(classes="btn btn--primary btn--sm")))
    if related_slugs:
        links = []
        for slug in related_slugs:
            s = SERVICE_BY_SLUG.get(slug)
            if s:
                links.append('<li><a href="/%s">%s</a></li>' % (s["path"], esc(s["h1"].split(" :")[0])))
        if links:
            cards.append('<div class="card card--plain"><h3>Prestations liées</h3>'
                         '<ul class="checks" style="gap:.35rem">%s</ul></div>' % "".join(links))
    cards.append(
        '<div class="card card--plain"><h3>Zones d\'intervention</h3>'
        "<p>Côtes-d'Armor · Finistère · Ille-et-Vilaine · Morbihan · Loire-Atlantique · "
        "Maine-et-Loire</p>"
        '<a class="card-link" href="/zones-d-intervention.html">Voir les zones</a></div>')
    if extra:
        cards.append(extra)
    return '<aside class="sidebar">%s</aside>' % "".join(cards)


def related_services_block(slugs, title="À consulter également"):
    links = []
    for slug in slugs:
        s = SERVICE_BY_SLUG.get(slug)
        if s:
            links.append((s["h1"].split(" :")[0], "/" + s["path"]))
    if not links:
        return ""
    return "<h2>%s</h2>%s" % (esc(title), link_cloud(links))


def geo_identity_rows(what, where=None, who="Particuliers, commerces et professionnels",
                      how=None, extra=None):
    rows = [
        ("Qui", "Electricien Richard, artisan électricien"),
        ("Quoi", what),
        ("Où", where or ("Côtes-d'Armor (22), Finistère (29), Ille-et-Vilaine (35), "
                         "Morbihan (56), Loire-Atlantique (44), Maine-et-Loire (49)")),
        ("Pour qui", who),
    ]
    if how:
        rows.append(("Comment", how))
    rows.append(("Contact", '<a href="tel:%s">%s</a> — <a href="/devis-electricien.html">'
                            "demande de devis</a>" % (SITE["phone_tel"], SITE["phone_display"])))
    if extra:
        rows.extend(extra)
    return rows


def hero_cta_row(secondary_label="Demander un devis", secondary_href="/devis-electricien.html"):
    return ('<div class="btn-row">%s<a class="btn btn--ghost" href="%s">%s</a></div>'
            % (phone_link(classes="btn btn--primary"), secondary_href, esc(secondary_label)))


# ------------------------------------------------------------ pages services
def build_service_pages():
    for svc in SERVICES:
        path = svc["path"]
        page_url = url_for(path)
        body = expand_blocks(svc["body"])

        trail = [("Accueil", "/")]
        if svc.get("pillar") or svc["slug"] in ("tarifs",):
            trail.append((svc["h1"].split(" :")[0], None))
        else:
            trail.append(("Électricien", "/electricien.html"))
            trail.append((svc["h1"].split(" :")[0], None))

        img = IMG.IMAGES.get("svc_" + svc["slug"])
        media = picture(img, eager=True, sizes="(min-width: 900px) 560px, 100vw") if img else ""

        quick = quick_answer(svc["quick"]["title"], svc["quick"]["answer"],
                             svc["quick"].get("facts"))
        toc = toc_from_body(body)
        geo = geo_card(geo_identity_rows(
            svc.get("service_type", svc["h1"]),
            how="Prise de contact, examen sur place, devis détaillé, réalisation, contrôle"))

        main = """
<section class="hero"><div class="container hero-inner">
  <div>
    <p class="eyebrow">%s</p>
    <h1>%s</h1>
    <p class="lead">%s</p>
    %s
  </div>
  <div class="hero-media">%s</div>
</div></section>

<section class="section"><div class="container layout layout--sidebar">
  <div class="prose prose--wide">
    %s
    %s
    %s
    %s
    %s
    %s
    %s
  </div>
  %s
</div></section>

<section class="section section--soft"><div class="container">%s</div></section>
""" % (esc(svc["category"]), esc(svc["h1"]), esc(svc["intro"]), hero_cta_row(), media,
       quick, toc, body,
       cta_inline("Une question sur votre installation ou un besoin d'intervention ?"),
       faq_block(svc["faq"]),
       geo,
       related_services_block(svc.get("related", [])),
       sidebar_block(svc.get("related", [])),
       cta_band("Besoin d'un électricien ?",
                "Dépannage, travaux ou simple avis sur votre installation : "
                "décrivez votre situation, un devis vous est proposé sans engagement."))

        nodes = [service_node(svc, page_url)]
        if svc.get("faq"):
            nodes.append(faq_node(svc["faq"], page_url))

        html = render_page(path, svc["title"], svc["desc"], main, trail=trail,
                           schema_nodes=nodes,
                           og_image=img["file"] if img else None)
        write(path, html, priority="0.9" if svc.get("pillar") else "0.8",
              changefreq="monthly")


# ------------------------------------------------------------- pages zones
def build_zone_pages():
    # --- Hub principal ---------------------------------------------------
    dept_cards = zones_strip(intro=False)
    stats = ("<ul class=\"stat-row\"><li><b>6</b><span>départements couverts</span></li>"
             "<li><b>%d</b><span>villes avec une page dédiée</span></li>"
             "<li><b>2</b><span>régions : Bretagne et Pays de la Loire</span></li></ul>"
             % sum(len(d["cities"]) for d in DEPARTEMENTS))

    main = """
<section class="hero"><div class="container hero-inner">
  <div>
    <p class="eyebrow">Zones d'intervention</p>
    <h1>Zones d'intervention d'Electricien Richard</h1>
    <p class="lead">Interventions dans six départements de Bretagne et des Pays de la Loire :
    Côtes-d'Armor, Finistère, Ille-et-Vilaine, Morbihan, Loire-Atlantique et Maine-et-Loire.</p>
    %s
  </div>
  <div class="hero-media">%s</div>
</div></section>

<section class="section"><div class="container">
  <div class="prose prose--wide">
  %s
  <h2 id="perimetre">Un périmètre volontairement limité</h2>
  <p>Couvrir six départements n'a de sens que si l'on peut réellement s'y déplacer.
  C'est pourquoi le périmètre s'arrête à ces limites : aucune intervention n'est proposée
  au-delà, y compris dans les départements immédiatement voisins.</p>
  <p>Ce périmètre couvre deux régions et des réalités bâties très différentes — habitat en
  pierre de l'intérieur breton, immeubles de la reconstruction, tuffeau du Val de Loire,
  logements littoraux exposés aux embruns. Ces différences ont des conséquences concrètes
  sur les travaux électriques, détaillées sur chaque page départementale.</p>
  %s
  </div>
</div></section>

<section class="section section--soft"><div class="container">
  <div class="section-head"><h2>Les six départements couverts</h2>
  <p class="lead">Chaque département dispose d'une page détaillant le contexte local, les
  besoins fréquents et les villes couvertes.</p></div>
  %s
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><h2 id="carte">Carte des zones d'intervention</h2>
  <p class="lead">Les points indiquent les départements couverts et les villes disposant
  d'une page dédiée.</p></div>
  %s
</div></section>

<section class="section section--soft"><div class="container">%s</div></section>

<section class="section"><div class="container">%s</div></section>
""" % (hero_cta_row(),
       picture(IMG.IMAGES["home_gallery_6"], eager=True,
               sizes="(min-width: 900px) 560px, 100vw"),
       quick_answer(
           "Où intervient Electricien Richard ?",
           "<p><strong>Electricien Richard intervient dans six départements : les "
           "Côtes-d'Armor (22), le Finistère (29), l'Ille-et-Vilaine (35), le Morbihan (56), "
           "la Loire-Atlantique (44) et le Maine-et-Loire (49).</strong></p>"
           "<p>Aucune intervention n'est réalisée en dehors de ce périmètre.</p>",
           [("Bretagne", "Côtes-d'Armor, Finistère, Ille-et-Vilaine, Morbihan"),
            ("Pays de la Loire", "Loire-Atlantique, Maine-et-Loire"),
            ("Prestations", "Dépannage, installation, rénovation, mise aux normes"),
            ("Clients", "Particuliers, commerces et professionnels")]),
       stats,
       dept_cards,
       map_block(map_points()),
       faq_block([
           ("Intervenez-vous en dehors de ces six départements ?",
            "<p>Non. Le périmètre est volontairement limité aux Côtes-d'Armor, au Finistère, "
            "à l'Ille-et-Vilaine, au Morbihan, à la Loire-Atlantique et au Maine-et-Loire. "
            "Les départements voisins ne sont pas couverts.</p>"),
           ("Comment savoir si ma commune est couverte ?",
            "<p>Si elle se situe dans l'un des six départements listés, elle entre dans le "
            "périmètre d'intervention. Les pages villes existent pour les principales "
            "communes, mais l'intervention n'est pas limitée à ces villes : précisez votre "
            "commune lors de la prise de contact.</p>"),
           ("Le déplacement est-il facturé ?",
            "<p>Le déplacement dépend de la distance et de la nature de l'intervention. Sur un "
            "chantier planifié, il est intégré au devis global. Pour un dépannage, les "
            "conditions sont communiquées avant l'intervention.</p>"),
           ("Pourquoi certaines villes ont-elles une page dédiée et pas d'autres ?",
            "<p>Une page ville n'est créée que lorsqu'il y a réellement quelque chose à dire "
            "sur le contexte local : type d'habitat, problématiques électriques spécifiques, "
            "secteurs concernés. Créer des pages identiques pour des dizaines de communes "
            "n'apporterait rien au lecteur.</p>"),
       ]),
       cta_band("Une intervention à prévoir dans l'un de ces départements ?",
                "Décrivez votre besoin et votre commune : une réponse vous est apportée "
                "avec les conditions applicables."))

    html = render_page(
        "zones-d-intervention.html",
        "Zones d'intervention — Électricien en Bretagne et Pays de la Loire | Electricien Richard",
        ("Zones d'intervention d'Electricien Richard : Côtes-d'Armor, Finistère, "
         "Ille-et-Vilaine, Morbihan, Loire-Atlantique et Maine-et-Loire. Carte et villes "
         "couvertes."),
        main,
        trail=[("Accueil", "/"), ("Zones d'intervention", None)],
        schema_nodes=[faq_node([
            ("Intervenez-vous en dehors de ces six départements ?",
             "Non. Le périmètre est limité aux Côtes-d'Armor, au Finistère, à l'Ille-et-Vilaine, "
             "au Morbihan, à la Loire-Atlantique et au Maine-et-Loire."),
        ], "/zones-d-intervention.html")],
        og_image=IMG.IMAGES["home_gallery_6"]["file"])
    write("zones-d-intervention.html", html, priority="0.9")

    # --- /zones/ : redirection technique vers le hub ----------------------
    redirect = """<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8">
<title>Zones d'intervention — Electricien Richard</title>
<meta name="robots" content="noindex, follow">
<link rel="canonical" href="%s">
<meta http-equiv="refresh" content="0; url=/zones-d-intervention.html">
</head><body><p>Cette page a été déplacée :
<a href="/zones-d-intervention.html">zones d'intervention</a>.</p></body></html>
""" % abs_url("/zones-d-intervention.html")
    write("zones/index.html", redirect, indexable=False)

    # --- Pages departements ----------------------------------------------
    for dep in DEPARTEMENTS:
        build_department_page(dep)
        for city in dep["cities"]:
            build_city_page(dep, city)


def build_department_page(dep):
    path = "zones/%s/index.html" % dep["slug"]
    page_url = url_for(path)
    img = IMG.dept_image(dep["slug"], dep["name"])

    city_cards = "".join(
        '<article class="card"><div class="card-icon">%s</div><h3>%s</h3><p>%s</p>'
        '<a class="card-link" href="%s">Électricien à %s</a></article>'
        % (icon("map", 24), esc(city["name"]), esc(city["intro"]),
           city_url(dep, city), esc(city["name"]))
        for city in dep["cities"])

    besoins = checks([esc(b) for b in dep["besoins"]])

    main = """
<section class="hero"><div class="container hero-inner">
  <div>
    <p class="eyebrow">Département %s</p>
    <h1>%s</h1>
    <p class="lead">%s</p>
    %s
  </div>
  <div class="hero-media">%s</div>
</div></section>

<section class="section"><div class="container layout layout--sidebar">
  <div class="prose prose--wide">
    %s
    <h2 id="contexte">Le contexte électrique du département</h2>
    %s
    <h2 id="besoins">Les besoins les plus fréquents %s</h2>
    %s
    %s
    <h2 id="prestations">Nos prestations %s</h2>
    <p>L'ensemble des prestations est disponible dans le département : dépannage, recherche
    de panne, installation, rénovation, mise aux normes et équipements.</p>
    %s
    <h2 id="villes">Villes couvertes %s</h2>
    <p>Ces villes disposent d'une page détaillant le contexte local. L'intervention n'est
    pas limitée à ces communes : elle couvre l'ensemble du département.</p>
    %s
    %s
    %s
  </div>
  %s
</div></section>

<section class="section section--soft"><div class="container">
  <div class="section-head"><h2 id="carte">Carte du périmètre %s</h2></div>
  %s
</div></section>

<section class="section"><div class="container">%s</div></section>
""" % (esc(dep["code"]), esc(dep["h1"]), esc(dep["chapo"]), hero_cta_row(),
       picture(img, eager=True, sizes="(min-width: 900px) 560px, 100vw"),
       quick_answer(
           "Électricien %s : l'essentiel" % dep["prep"],
           "<p><strong>Electricien Richard intervient %s (%s) pour le dépannage électrique, "
           "la recherche de panne, l'installation, la rénovation et la mise aux normes.</strong></p>"
           "<p>Les interventions concernent les particuliers, les commerces et les "
           "professionnels, dans l'ensemble du département.</p>" % (dep["prep"], dep["code"]),
           [("Département", "%s (%s)" % (dep["name"], dep["code"])),
            ("Préfecture", dep["prefecture"]),
            ("Villes détaillées", ", ".join(c["name"] for c in dep["cities"])),
            ("Prestations", "Dépannage, installation, rénovation, mise aux normes, équipements"),
            ("Contact", '<a href="tel:%s">%s</a>' % (SITE["phone_tel"], SITE["phone_display"]))]),
       dep["contexte"], esc(dep["prep"]), besoins,
       cta_inline("Un besoin d'intervention %s ?" % esc(dep["prep"])),
       esc(dep["prep"]), services_grid(cols="grid--2"), esc(dep["prep"]),
       '<div class="grid grid--3">%s</div>' % city_cards,
       faq_block(dep["faq"], title="Questions fréquentes %s" % dep["prep"]),
       geo_card(geo_identity_rows(
           "Travaux électriques : dépannage, installation, rénovation, mise aux normes",
           where="%s (%s), au sein des six départements couverts" % (dep["name"], dep["code"]),
           how="Prise de contact, examen sur place, devis, réalisation, contrôle")),
       sidebar_block(["electricien-depannage", "installation-electrique",
                      "renovation-electrique", "tableau-electrique"]),
       esc(dep["prep"]), map_block(map_points(scope=dep["slug"])),
       cta_band("Besoin d'un électricien %s ?" % esc(dep["prep"]),
                "Décrivez votre besoin et votre commune : un devis vous est proposé sans "
                "engagement."))

    nodes = [{
        "@type": "Service",
        "@id": abs_url(page_url) + "#service",
        "name": "Électricien %s" % dep["prep"],
        "serviceType": "Travaux d'électricité",
        "description": dep["desc"],
        "provider": {"@id": BUSINESS_ID},
        "areaServed": {"@type": "AdministrativeArea", "name": dep["name"]},
        "url": abs_url(page_url),
    }, faq_node(dep["faq"], page_url)]

    html = render_page(path, dep["title"], dep["desc"], main,
                       trail=[("Accueil", "/"),
                              ("Zones d'intervention", "/zones-d-intervention.html"),
                              (dep["name"], None)],
                       schema_nodes=nodes, og_image=img["file"])
    write(path, html, priority="0.8")


def build_city_page(dep, city):
    path = "zones/%s/%s/index.html" % (dep["slug"], city["slug"])
    page_url = url_for(path)
    img = IMG.city_image(city["slug"], city["name"])

    secteurs = '<ul class="link-cloud" style="margin-bottom:1.4rem">%s</ul>' % "".join(
        "<li><span style=\"display:inline-block;padding:.5rem .9rem;background:#fff;"
        "border:1px solid #E5E7EB;border-radius:10px;font-size:.9rem;font-weight:600\">"
        "%s</span></li>" % esc(s) for s in city["secteurs"])

    besoins = "".join(
        '<article class="card card--plain"><h3>%s</h3><p>%s</p></article>' % (esc(t), esc(d))
        for t, d in city["besoins"])

    other_cities = [c for c in dep["cities"] if c["slug"] != city["slug"]]
    other_links = link_cloud([("Électricien à %s" % c["name"], city_url(dep, c))
                              for c in other_cities]) if other_cities else ""

    services_links = link_cloud([
        ("Dépannage électrique à %s" % city["name"], "/electricien-depannage.html"),
        ("Électricien en urgence à %s" % city["name"], "/electricien-urgence.html"),
        ("Installation électrique à %s" % city["name"], "/installation-electrique.html"),
        ("Rénovation électrique à %s" % city["name"], "/renovation-electrique.html"),
        ("Mise aux normes à %s" % city["name"], "/mise-aux-normes-electrique.html"),
        ("Tableau électrique à %s" % city["name"], "/tableau-electrique.html"),
        ("Recherche de panne à %s" % city["name"], "/recherche-panne.html"),
        ("Borne de recharge à %s" % city["name"], "/borne-recharge.html"),
    ])

    main = """
<section class="hero"><div class="container hero-inner">
  <div>
    <p class="eyebrow">%s (%s)</p>
    <h1>%s</h1>
    <p class="lead">%s</p>
    %s
  </div>
  <div class="hero-media">%s</div>
</div></section>

<section class="section"><div class="container layout layout--sidebar">
  <div class="prose prose--wide">
    %s
    <h2 id="contexte">L'électricité à %s : ce que l'on rencontre</h2>
    %s
    <h2 id="secteurs">Secteurs et communes couverts</h2>
    <p>L'intervention couvre %s et les secteurs environnants :</p>
    %s
    <h2 id="besoins">Besoins électriques fréquents à %s</h2>
    <div class="grid grid--2">%s</div>
    %s
    <h2 id="prestations">Prestations disponibles à %s</h2>
    %s
    %s
    <h2 id="departement">Électricien %s</h2>
    <p>Cette page fait partie du périmètre <a href="%s">%s (%s)</a>, l'un des six
    départements couverts par Electricien Richard.</p>
    %s
    %s
  </div>
  %s
</div></section>

<section class="section section--soft"><div class="container">
  <div class="section-head"><h2 id="carte">%s sur la carte des zones d'intervention</h2></div>
  %s
</div></section>

<section class="section"><div class="container">%s</div></section>
""" % (esc(dep["name"]), esc(dep["code"]), esc(city["h1"]), esc(city["intro"]),
       hero_cta_row(),
       picture(img, eager=True, sizes="(min-width: 900px) 560px, 100vw"),
       quick_answer(
           "Électricien à %s : l'essentiel" % city["name"],
           "<p><strong>Electricien Richard intervient à %s et dans les communes voisines "
           "pour le dépannage électrique, la recherche de panne, l'installation, la "
           "rénovation et la mise aux normes.</strong></p>"
           "<p>Les interventions concernent les particuliers, les commerces et les "
           "professionnels.</p>" % city["name"],
           [("Ville", "%s — %s (%s)" % (city["name"], dep["name"], dep["code"])),
            ("Prestations", "Dépannage, recherche de panne, installation, rénovation, "
                            "mise aux normes, tableau, éclairage, borne de recharge"),
            ("Secteurs", ", ".join(city["secteurs"][:6])),
            ("Contact", '<a href="tel:%s">%s</a> — <a href="/devis-electricien.html">'
                        "demande de devis</a>" % (SITE["phone_tel"], SITE["phone_display"]))]),
       esc(city["name"]), city["contexte"], esc(city["name"]), secteurs,
       esc(city["name"]), besoins,
       cta_inline("Une panne ou des travaux électriques à %s ?" % esc(city["name"])),
       esc(city["name"]), services_links,
       faq_block(city["faq"], title="Questions fréquentes — %s" % city["name"]),
       esc(dep["prep"]), dept_url(dep), esc(dep["name"]), esc(dep["code"]),
       ("<h3>Autres villes du département</h3>" + other_links) if other_links else "",
       geo_card(geo_identity_rows(
           "Travaux électriques : dépannage, installation, rénovation, mise aux normes",
           where="%s et communes voisines — %s (%s)" % (city["name"], dep["name"], dep["code"]),
           how="Prise de contact, examen sur place, devis, réalisation, contrôle")),
       sidebar_block(["electricien-depannage", "electricien-urgence", "tableau-electrique",
                      "renovation-electrique"]),
       esc(city["name"]),
       map_block([{"name": city["name"], "lat": city["lat"], "lon": city["lon"],
                   "type": "dept", "sub": "%s (%s)" % (dep["name"], dep["code"]), "url": ""}]
                 + [{"name": c["name"], "lat": c["lat"], "lon": c["lon"], "type": "city",
                     "sub": dep["name"], "url": city_url(dep, c)} for c in other_cities],
                 height_note=False),
       cta_band("Besoin d'un électricien à %s ?" % esc(city["name"]),
                "Dépannage, travaux ou avis sur votre installation : décrivez votre "
                "situation pour obtenir une réponse adaptée."))

    nodes = [{
        "@type": "Service",
        "@id": abs_url(page_url) + "#service",
        "name": "Électricien à %s" % city["name"],
        "serviceType": "Travaux d'électricité",
        "description": city["desc"],
        "provider": {"@id": BUSINESS_ID},
        "areaServed": {"@type": "City", "name": city["name"],
                       "containedInPlace": {"@type": "AdministrativeArea", "name": dep["name"]}},
        "url": abs_url(page_url),
    }, faq_node(city["faq"], page_url)]

    html = render_page(path, city["title"], city["desc"], main,
                       trail=[("Accueil", "/"),
                              ("Zones d'intervention", "/zones-d-intervention.html"),
                              (dep["name"], dept_url(dep)),
                              (city["name"], None)],
                       schema_nodes=nodes, og_image=img["file"])
    write(path, html, priority="0.7")


# --------------------------------------------------------------- pages blog
FR_MONTHS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août",
             "septembre", "octobre", "novembre", "décembre"]


def fr_date(iso):
    y, m, d = iso.split("-")
    return "%d %s %s" % (int(d), FR_MONTHS[int(m) - 1], y)


def article_card(article):
    cat = BLOG.category_by_slug(article["category"])
    return (
        '<article class="article-card">%s<div class="body">'
        '<p class="cat">%s</p><h3><a href="%s">%s</a></h3><p>%s</p>'
        '<p class="meta">Publié le %s</p></div></article>'
        % (picture(IMG.blog_image(article), sizes="(min-width: 900px) 380px, 100vw"),
           esc(cat["name"]), BLOG.article_url(article), esc(article["title"]),
           esc(article["chapo"]), fr_date(article["date"])))


def build_blog():
    # --- Index du blog ----------------------------------------------------
    cat_links = link_cloud([(c["name"], BLOG.category_url(c)) for c in BLOG.CATEGORIES])
    articles = sorted(BLOG.ARTICLES, key=lambda a: a["date"], reverse=True)
    cards = "".join(article_card(a) for a in articles)

    main = """
<section class="section section--tint"><div class="container">
  <div class="section-head">
    <p class="eyebrow">Blog</p>
    <h1>Conseils et guides en électricité</h1>
    <p class="lead">Des articles pratiques rédigés à partir des situations réellement
    rencontrées sur le terrain : pannes, sécurité, rénovation, normes et équipements.</p>
  </div>
  %s
</div></section>

<section class="section"><div class="container">
  <div class="section-head"><h2>Tous les articles</h2></div>
  <div class="grid grid--3">%s</div>
</div></section>

<section class="section section--soft"><div class="container">%s</div></section>
""" % (cat_links, cards,
       cta_band("Une question qui n'est pas traitée ici ?",
                "Décrivez votre situation : la réponse est souvent plus rapide qu'une "
                "recherche."))

    html = render_page(
        "blog/index.html",
        "Blog électricité — Conseils, pannes, sécurité et rénovation | Electricien Richard",
        ("Blog d'Electricien Richard : dépannage, sécurité électrique, rénovation, normes, "
         "prix et bornes de recharge. Des guides pratiques et vérifiables."),
        main, trail=[("Accueil", "/"), ("Blog", None)],
        schema_nodes=[{
            "@type": "Blog",
            "@id": abs_url("/blog/") + "#blog",
            "name": "Blog Electricien Richard",
            "url": abs_url("/blog/"),
            "publisher": {"@id": BUSINESS_ID},
            "blogPost": [{"@type": "BlogPosting",
                          "headline": a["title"],
                          "url": abs_url(BLOG.article_url(a)),
                          "datePublished": a["date"]} for a in articles],
        }])
    write("blog/index.html", html, priority="0.7", changefreq="weekly")

    # --- Pages categories -------------------------------------------------
    for cat in BLOG.CATEGORIES:
        posts = sorted(BLOG.articles_by_category(cat["slug"]),
                       key=lambda a: a["date"], reverse=True)
        cards = "".join(article_card(a) for a in posts)
        others = link_cloud([(c["name"], BLOG.category_url(c))
                             for c in BLOG.CATEGORIES if c["slug"] != cat["slug"]])
        path = "blog/%s/index.html" % cat["slug"]
        main = """
<section class="section section--tint"><div class="container">
  <div class="section-head">
    <p class="eyebrow">Catégorie</p>
    <h1>%s</h1>
    <p class="lead">%s</p>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="grid grid--3">%s</div>
</div></section>

<section class="section section--soft"><div class="container">
  <div class="section-head"><h2>Autres catégories</h2></div>
  %s
</div></section>

<section class="section"><div class="container">%s</div></section>
""" % (esc(cat["name"]), esc(cat["intro"]), cards, others,
       cta_band("Besoin d'un électricien ?",
                "Dépannage, travaux ou question sur votre installation : décrivez votre "
                "situation."))
        html = render_page(path, cat["title"], cat["desc"], main,
                           trail=[("Accueil", "/"), ("Blog", "/blog/"), (cat["name"], None)])
        write(path, html, priority="0.5")

    # --- Articles ---------------------------------------------------------
    for article in BLOG.ARTICLES:
        build_article(article)


def build_article(article):
    cat = BLOG.category_by_slug(article["category"])
    path = BLOG.article_url(article).lstrip("/")
    page_url = url_for(path)
    img = IMG.blog_image(article)
    body = article["body"]

    meta = ['<span>Publié le %s</span>' % fr_date(article["date"])]
    if article.get("updated"):
        meta.append("<span>Mis à jour le %s</span>" % fr_date(article["updated"]))
    meta.append('<span><a href="%s">%s</a></span>' % (BLOG.category_url(cat), esc(cat["name"])))

    others = [a for a in BLOG.ARTICLES if a["slug"] != article["slug"]][:3]

    main = """
<article class="section"><div class="container layout layout--sidebar">
  <div class="prose prose--wide">
    <p class="eyebrow">%s</p>
    <h1>%s</h1>
    <p class="article-meta">%s</p>
    <p class="lead" style="color:var(--text)">%s</p>
    %s
    %s
    %s
    %s
    %s
    %s
    %s
  </div>
  %s
</div></article>

<section class="section section--soft"><div class="container">
  <div class="section-head"><h2>À lire également</h2></div>
  <div class="grid grid--3">%s</div>
</div></section>

<section class="section"><div class="container">%s</div></section>
""" % (esc(cat["name"]), esc(article["h1"]), "".join(meta), esc(article["chapo"]),
       picture(img, eager=True, sizes="(min-width: 1000px) 760px, 100vw"),
       quick_answer("Réponse rapide", article["quick"]),
       toc_from_body(body),
       body,
       cta_inline("Besoin d'un avis sur votre installation ou d'une intervention ?"),
       faq_block(article["faq"]),
       related_services_block(article.get("related_services", []), "Prestations concernées"),
       sidebar_block(article.get("related_services", [])[:4]),
       "".join(article_card(a) for a in others),
       cta_band("Une situation à faire examiner ?",
                "Décrivez votre installation et votre commune : une réponse vous est "
                "apportée avec les conditions applicables."))

    nodes = [{
        "@type": "BlogPosting",
        "@id": abs_url(page_url) + "#article",
        "headline": article["title"],
        "description": article["desc"],
        "articleSection": cat["name"],
        "datePublished": article["date"],
        "dateModified": article.get("updated") or article["date"],
        "inLanguage": "fr-FR",
        "mainEntityOfPage": {"@id": abs_url(page_url) + "#webpage"},
        "author": {"@id": BUSINESS_ID},
        "publisher": {"@id": BUSINESS_ID},
        "image": abs_url(img["file"]),
        "isPartOf": {"@id": abs_url("/blog/") + "#blog"},
    }, faq_node(article["faq"], page_url)]

    html = render_page(path, article["meta_title"], article["desc"], main,
                       trail=[("Accueil", "/"), ("Blog", "/blog/"),
                              (cat["name"], BLOG.category_url(cat)),
                              (article["title"], None)],
                       schema_nodes=nodes, og_type="article", og_image=img["file"],
                       og_title=article["title"])
    write(path, html, priority="0.7")


# ------------------------------------------------------------ page d'accueil
def build_home():
    reviews = """
<div class="reviews-empty">
  <p><strong>Aucun avis n'est publié pour le moment.</strong></p>
  <p>Cette section est prévue pour accueillir de véritables avis clients. Aucun témoignage,
  note ou commentaire n'est inventé : tant qu'aucun avis vérifiable n'a été recueilli, rien
  n'est affiché ici.</p>
  <p>Vous avez fait appel à Electricien Richard ? Votre retour permettra de compléter cette
  page.</p>
</div>"""

    gallery = '<div class="gallery">%s</div>' % "".join(
        picture(IMG.IMAGES[k], sizes="(min-width: 1000px) 360px, 100vw")
        for k in ["home_gallery_1", "home_gallery_2", "home_gallery_3",
                  "home_gallery_4", "home_gallery_5", "home_gallery_6"])

    before_after = """
<div class="before-after">
  <figure><span class="tag">Avant</span>%s
  <figcaption>Tableau ancien à fusibles : aucune protection différentielle adaptée, aucun
  repérage possible.</figcaption></figure>
  <figure><span class="tag">Après</span>%s
  <figcaption>Tableau remplacé : différentiels 30 mA, protection de chaque circuit et
  repérage complet.</figcaption></figure>
</div>""" % (picture(IMG.IMAGES["before"], sizes="(min-width: 800px) 480px, 100vw", caption=False)
             .replace("<figure>", "").replace("</figure>", ""),
             picture(IMG.IMAGES["after"], sizes="(min-width: 800px) 480px, 100vw", caption=False)
             .replace("<figure>", "").replace("</figure>", ""))

    recent = sorted(BLOG.ARTICLES, key=lambda a: a["date"], reverse=True)[:3]

    main = """
<section class="hero"><div class="container hero-inner">
  <div>
    <p class="eyebrow">%s Bretagne · Pays de la Loire</p>
    <h1>Électricien professionnel pour vos dépannages et installations</h1>
    <p class="lead">Interventions électriques, dépannage, rénovation et mise en sécurité
    dans les Côtes-d'Armor, le Finistère, l'Ille-et-Vilaine, le Morbihan, la Loire-Atlantique
    et le Maine-et-Loire.</p>
    <ul class="hero-badges">
      <li>%s Devis détaillé avant travaux</li>
      <li>%s Interventions urgentes traitées en priorité</li>
      <li>%s Particuliers, commerces et professionnels</li>
      <li>%s 6 départements couverts</li>
    </ul>
    %s
  </div>
  <div class="hero-media">%s</div>
</div></section>

<section class="section section--dark" style="padding-block:clamp(1.6rem,3vw,2.4rem)">
  <div class="container">
    <div class="grid grid--2" style="align-items:center">
      <div>
        <h2 style="margin-bottom:.3em;font-size:clamp(1.2rem,2.4vw,1.6rem)">Une urgence
        électrique ?</h2>
        <p style="margin:0;color:#CBD5E1">Odeur de brûlé, échauffement au tableau, coupure
        totale ou disjoncteur impossible à réarmer : coupez l'alimentation concernée et
        appelez plutôt que d'insister.</p>
      </div>
      <div class="btn-row">%s
      <a class="btn btn--outline-light" href="/electricien-urgence.html">Que faire en cas
      d'urgence</a></div>
    </div>
  </div>
</section>

<section class="section"><div class="container">
  <div class="section-head center">
    <p class="eyebrow">Prestations</p>
    <h2>Ce que nous réalisons</h2>
    <p class="lead">Du dépannage ponctuel à la rénovation complète d'une installation.</p>
  </div>
  %s
  <p class="text-center" style="margin-top:1.6rem"><a class="btn btn--ghost"
  href="/electricien.html">Voir toutes les prestations</a></p>
</div></section>

<section class="section section--tint"><div class="container">
  <div class="layout layout--sidebar">
    <div class="prose prose--wide">
      %s
      <h2>Interventions courantes</h2>
      <p>Certaines situations reviennent constamment, quel que soit le département. Elles
      ont en commun de porter sur la sécurité des personnes bien plus que sur le confort.</p>
      %s
      <h2>Pourquoi faire appel à Electricien Richard</h2>
      %s
    </div>
    %s
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head center">
    <p class="eyebrow">Nos interventions</p>
    <h2>Photos de chantiers et d'interventions</h2>
    <p class="lead">Des situations réelles rencontrées chez les particuliers, dans les
    commerces et les locaux professionnels.</p>
  </div>
  %s
  <h3 style="margin-top:2.5rem">Avant / après : remplacement d'un tableau</h3>
  %s
</div></section>

<section class="section section--soft"><div class="container">
  <div class="section-head">
    <p class="eyebrow">Zones d'intervention</p>
    <h2 id="zones">Où intervenons-nous ?</h2>
    <p class="lead">Six départements, deux régions. Aucun département voisin n'est couvert
    en dehors de cette liste.</p>
  </div>
  %s
  <div style="margin-top:2rem">%s</div>
  <p style="margin-top:1.4rem"><a class="btn btn--ghost"
  href="/zones-d-intervention.html">Toutes les zones d'intervention</a></p>
</div></section>

<section class="section"><div class="container">
  <div class="section-head center">
    <p class="eyebrow">Déroulement</p>
    <h2>Comment se passe une intervention</h2>
  </div>
  %s
</div></section>

<section class="section section--tint"><div class="container">
  <div class="section-head">
    <p class="eyebrow">Avis clients</p>
    <h2>Ce que disent nos clients</h2>
  </div>
  %s
</div></section>

<section class="section"><div class="container">
  <div class="section-head center"><h2>Questions fréquentes</h2></div>
  <div style="max-width:80ch;margin-inline:auto">%s</div>
  <p class="text-center" style="margin-top:1.6rem"><a class="btn btn--ghost"
  href="/faq.html">Voir toutes les questions</a></p>
</div></section>

<section class="section section--soft"><div class="container">
  <div class="section-head">
    <p class="eyebrow">Blog</p>
    <h2>Articles récents</h2>
    <p class="lead">Des guides pratiques sur les pannes, la sécurité et la rénovation
    électrique.</p>
  </div>
  <div class="grid grid--3">%s</div>
</div></section>

<section class="section"><div class="container">%s</div></section>
""" % (icon("map", 15),
       icon("doc", 16), icon("clock", 16), icon("home", 16), icon("map", 16),
       hero_cta_row(),
       picture(IMG.IMAGES["hero"], eager=True, sizes="(min-width: 900px) 560px, 100vw"),
       phone_link(classes="btn btn--primary"),
       services_grid(),
       quick_answer(
           "Electricien Richard en bref",
           "<p><strong>Electricien Richard est un artisan électricien qui intervient chez les "
           "particuliers, dans les commerces et auprès des professionnels pour le dépannage, "
           "l'installation, la rénovation et la mise aux normes des installations "
           "électriques.</strong></p>"
           "<p>Le périmètre d'intervention couvre six départements de Bretagne et des Pays de "
           "la Loire.</p>",
           [("Prestations", "Dépannage, recherche de panne, installation, rénovation, mise aux "
                            "normes, tableau électrique, éclairage, borne de recharge, VMC"),
            ("Zones", "Côtes-d'Armor (22), Finistère (29), Ille-et-Vilaine (35), Morbihan (56), "
                      "Loire-Atlantique (44), Maine-et-Loire (49)"),
            ("Clients", "Particuliers, commerces, professionnels"),
            ("Référence technique", "Norme NF C 15-100"),
            ("Devis", "Écrit, détaillé, gratuit et sans engagement")]),
       checks([
           "Disjoncteur ou différentiel qui déclenche de façon répétée",
           "Coupure totale ou partielle sans cause identifiée",
           "Tableau à fusibles ou dépourvu de protection différentielle 30 mA",
           "Installation sans mise à la terre effective",
           "Prise ou interrupteur qui chauffe, noircit ou crépite",
           "Manque de prises et recours permanent aux multiprises",
           "Projet d'installation d'une borne de recharge",
           "Mise en sécurité avant une location ou après un achat",
       ]),
       checks([
           "<strong>Un diagnostic avant un devis.</strong> Aucun chiffrage n'est annoncé sans "
           "avoir vu l'installation : les écarts entre deux logements sont trop importants.",
           "<strong>Des explications compréhensibles.</strong> Ce qui a été constaté, ce qui a "
           "été fait, et ce qui reste éventuellement à prévoir.",
           "<strong>La priorité à la sécurité.</strong> Mise à la terre et protection "
           "différentielle avant le confort, systématiquement.",
           "<strong>Un tableau repéré en fin d'intervention.</strong> Pour savoir ce que "
           "protège chaque disjoncteur.",
           "<strong>Un périmètre assumé.</strong> Six départements, pas davantage : c'est la "
           "condition pour intervenir sérieusement.",
       ]),
       sidebar_block(["electricien", "electricien-depannage", "renovation-electrique",
                      "tarifs"]),
       gallery, before_after,
       zones_strip(intro=False), map_block(map_points()),
       BLOCKS["PROCESS_STEPS"],
       reviews,
       faq_block([
           ("Combien coûte l'intervention d'un électricien ?",
            "<p>Le coût dépend de la nature du travail, du temps nécessaire et des "
            "fournitures. Aucune grille n'est affichée ici car un prix annoncé sans avoir vu "
            "l'installation n'engage personne. Le devis est en revanche gratuit et détaillé. "
            "Voir la page <a href=\"/tarifs.html\">tarifs</a>.</p>"),
           ("Intervenez-vous en urgence ?",
            "<p>Oui. Les situations présentant un risque immédiat — odeur de brûlé, "
            "échauffement au tableau, coupure totale, disjoncteur impossible à réarmer — sont "
            "traitées en priorité, sur appel téléphonique.</p>"),
           ("Que faire quand un disjoncteur saute ?",
            "<p>Débranchez les appareils du circuit concerné, puis réarmez une seule fois. "
            "S'il tient, rebranchez les appareils un par un pour identifier le fautif. S'il "
            "déclenche immédiatement même à vide, n'insistez pas : le défaut est dans "
            "l'installation.</p>"),
           ("Dans quels départements intervenez-vous ?",
            "<p>Dans six départements uniquement : Côtes-d'Armor (22), Finistère (29), "
            "Ille-et-Vilaine (35), Morbihan (56), Loire-Atlantique (44) et Maine-et-Loire "
            "(49).</p>"),
           ("La mise aux normes est-elle obligatoire ?",
            "<p>Il n'existe pas d'obligation générale de mise aux normes d'une installation "
            "existante. L'obligation naît des travaux : une installation neuve ou entièrement "
            "rénovée doit respecter la norme en vigueur. En location, le logement doit par "
            "ailleurs être décent.</p>"),
       ], title="", level=2, anchor="faq-accueil"),
       "".join(article_card(a) for a in recent),
       cta_band("Un besoin en électricité ?",
                "Dépannage, installation, rénovation ou simple avis sur votre installation : "
                "décrivez votre situation et votre commune."))

    home_faq = [
        ("Combien coûte l'intervention d'un électricien ?",
         "Le coût dépend de la nature du travail, du temps nécessaire et des fournitures. "
         "Le devis est gratuit et détaillé, établi après examen de l'installation."),
        ("Intervenez-vous en urgence ?",
         "Oui. Les situations présentant un risque immédiat sont traitées en priorité, sur "
         "appel téléphonique."),
        ("Dans quels départements intervenez-vous ?",
         "Côtes-d'Armor (22), Finistère (29), Ille-et-Vilaine (35), Morbihan (56), "
         "Loire-Atlantique (44) et Maine-et-Loire (49)."),
    ]

    html = render_page(
        "index.html",
        "Électricien en Bretagne et Pays de la Loire — Dépannage, installation | Electricien Richard",
        ("Electricien Richard : dépannage électrique, recherche de panne, installation, "
         "rénovation et mise aux normes dans les Côtes-d'Armor, le Finistère, "
         "l'Ille-et-Vilaine, le Morbihan, la Loire-Atlantique et le Maine-et-Loire."),
        main, trail=None,
        schema_nodes=[faq_node(home_faq, "/")],
        og_image=IMG.IMAGES["hero"]["file"])
    write("index.html", html, priority="1.0", changefreq="weekly")


# ---------------------------------------------------------- pages annexes
def contact_form(compact=False, form_id="devis"):
    """Formulaire de demande. Fonctionne sans backend (bascule messagerie)."""
    action = SITE.get("form_action")
    if action:
        attrs = 'action="%s" method="post"' % esc(action)
        note = ("Les informations transmises servent uniquement à traiter votre demande. "
                "Voir la <a href=\"/politique-de-confidentialite.html\">politique de "
                "confidentialité</a>.")
    else:
        attrs = ('action="mailto:%s" method="post" enctype="text/plain"' % esc(SITE["email"]))
        note = ("L'envoi ouvre votre logiciel de messagerie. Pour une demande urgente, "
                "l'appel téléphonique reste le moyen le plus rapide.")

    services_options = "".join(
        '<option value="%s">%s</option>' % (esc(s["h1"].split(" :")[0]), esc(s["h1"].split(" :")[0]))
        for s in SERVICES if s["category"] in ("Dépannage", "Travaux", "Équipements", "Sécurité"))
    dept_options = "".join('<option value="%s">%s (%s)</option>'
                           % (esc(d["name"]), esc(d["name"]), d["code"]) for d in DEPARTEMENTS)

    return """
<form class="form" %s id="form-%s">
  <div class="row row--2">
    <div class="field">
      <label for="%s-nom">Nom et prénom <span aria-hidden="true">*</span></label>
      <input type="text" id="%s-nom" name="nom" autocomplete="name" required>
    </div>
    <div class="field">
      <label for="%s-tel">Téléphone <span aria-hidden="true">*</span></label>
      <input type="tel" id="%s-tel" name="telephone" autocomplete="tel" required>
    </div>
  </div>
  <div class="row row--2">
    <div class="field">
      <label for="%s-email">Adresse e-mail</label>
      <input type="email" id="%s-email" name="email" autocomplete="email">
    </div>
    <div class="field">
      <label for="%s-ville">Commune <span aria-hidden="true">*</span></label>
      <input type="text" id="%s-ville" name="commune" autocomplete="address-level2" required>
    </div>
  </div>
  <div class="row row--2">
    <div class="field">
      <label for="%s-dept">Département</label>
      <select id="%s-dept" name="departement">
        <option value="">Sélectionner…</option>
        %s
      </select>
      <span class="hint">Six départements couverts uniquement.</span>
    </div>
    <div class="field">
      <label for="%s-type">Nature de la demande</label>
      <select id="%s-type" name="type_demande">
        <option value="">Sélectionner…</option>
        <option value="Dépannage urgent">Dépannage urgent</option>
        %s
        <option value="Autre">Autre demande</option>
      </select>
    </div>
  </div>
  <div class="field">
    <label for="%s-message">Décrivez votre besoin <span aria-hidden="true">*</span></label>
    <textarea id="%s-message" name="message" required
      placeholder="Type de logement, âge approximatif de l'installation, nature du tableau, symptômes constatés, travaux envisagés…"></textarea>
    <span class="hint">Plus la description est précise, plus la réponse sera utile.</span>
  </div>
  <div class="consent">
    <input type="checkbox" id="%s-consent" name="consentement" required>
    <label for="%s-consent">J'accepte que ces informations soient utilisées pour traiter ma
    demande.</label>
  </div>
  <div class="btn-row">
    <button class="btn btn--primary" type="submit">Envoyer ma demande</button>
    %s
  </div>
  <p class="form-note">%s</p>
</form>""" % ((attrs, form_id) + (form_id,) * 10 + (dept_options,) + (form_id,) * 2
              + (services_options,) + (form_id,) * 4
              + (phone_link("Appeler", classes="btn btn--ghost"), note))


def build_contact_pages():
    # ---------------- Devis ----------------
    main = """
<section class="hero"><div class="container hero-inner">
  <div>
    <p class="eyebrow">Devis</p>
    <h1>Demander un devis à un électricien</h1>
    <p class="lead">Le devis est gratuit, détaillé et sans engagement. Il est établi après
    examen de l'installation, seule manière d'annoncer un prix qui tienne.</p>
    %s
  </div>
  <div class="hero-media">%s</div>
</div></section>

<section class="section"><div class="container layout layout--sidebar">
  <div>
    %s
    <h2>Formulaire de demande</h2>
    %s
  </div>
  <div class="sidebar">
    <div class="card card--plain"><div class="card-icon">%s</div>
      <h3>Demande urgente ?</h3>
      <p>Pour une coupure totale, une odeur de brûlé ou un échauffement, l'appel
      téléphonique est nettement plus rapide qu'un formulaire.</p>
      %s
    </div>
    <div class="card card--plain"><h3>Ce qui accélère la réponse</h3>
      %s
    </div>
    <div class="card card--plain"><h3>Ce que contient le devis</h3>
      %s
    </div>
  </div>
</div></section>

<section class="section section--soft"><div class="container">
  <div class="prose prose--wide">%s</div>
</div></section>
""" % (hero_cta_row("Nous appeler", "tel:" + SITE["phone_tel"]),
       picture(IMG.IMAGES["svc_tarifs"], eager=True, sizes="(min-width: 900px) 560px, 100vw"),
       quick_answer(
           "Comment obtenir un devis",
           "<p><strong>Décrivez votre besoin par téléphone ou via le formulaire ci-dessous. "
           "Une visite permet ensuite d'examiner l'installation, puis un devis écrit et "
           "détaillé vous est transmis.</strong></p>"
           "<p>Aucun travaux n'est engagé avant votre accord.</p>",
           [("Coût", "Gratuit et sans engagement"),
            ("Délai", "Selon la nature du projet et la charge en cours"),
            ("Contenu", "Prestations détaillées, fournitures, main-d'œuvre, TVA, durée de validité"),
            ("Zone", "Les six départements couverts uniquement")]),
       contact_form(form_id="devis"),
       icon("phone", 24), phone_link(classes="btn btn--primary btn--sm"),
       checks(["Le type de logement et son année approximative",
               "La nature du tableau : fusibles ou disjoncteurs",
               "Les symptômes constatés, s'il s'agit d'une panne",
               "Des photos du tableau et de la zone concernée",
               "Votre commune"]),
       checks(["Le détail des prestations, ligne par ligne",
               "La distinction fournitures / main-d'œuvre",
               "Les caractéristiques du matériel prévu",
               "Le taux de TVA applicable",
               "La durée de validité de l'offre"]),
       faq_block([
           ("Le devis est-il vraiment gratuit ?",
            "<p>Oui, l'établissement d'un devis est gratuit et sans engagement. Lorsqu'une "
            "étude technique approfondie est nécessaire — recherche de panne complexe, examen "
            "détaillé d'une installation ancienne — les conditions sont annoncées avant "
            "l'intervention.</p>"),
           ("Puis-je obtenir une estimation sans visite ?",
            "<p>Un ordre de grandeur est parfois possible à partir d'une description précise "
            "et de photos. Un prix ferme, en revanche, suppose d'avoir vu l'installation : "
            "l'état de l'existant et l'accessibilité des cheminements font varier le chiffrage "
            "dans des proportions importantes.</p>"),
           ("Combien de temps le devis est-il valable ?",
            "<p>La durée de validité figure sur le document. Elle tient compte de la "
            "variabilité du prix des fournitures.</p>"),
           ("Que se passe-t-il si un imprévu apparaît en cours de chantier ?",
            "<p>Tout élément non prévu au devis fait l'objet d'une information et, si des "
            "travaux supplémentaires sont nécessaires, d'un avenant ou d'un devis "
            "complémentaire. Rien n'est réalisé sans accord préalable.</p>"),
       ]))

    html = render_page(
        "devis-electricien.html",
        "Demande de devis électricien — Gratuit et sans engagement | Electricien Richard",
        ("Demandez un devis à un électricien : gratuit, détaillé et sans engagement. "
         "Intervention dans les six départements couverts en Bretagne et Pays de la Loire."),
        main, trail=[("Accueil", "/"), ("Demander un devis", None)])
    write("devis-electricien.html", html, priority="0.8")

    # ---------------- Contact ----------------
    contact_rows = [("Téléphone", '<a href="tel:%s">%s</a>' % (SITE["phone_tel"],
                                                              SITE["phone_display"]))]
    contact_rows.append(("E-mail", '<a href="mailto:%s">%s</a>' % (SITE["email"], SITE["email"])))
    contact_rows.append(("Zone d'intervention",
                         "Côtes-d'Armor (22), Finistère (29), Ille-et-Vilaine (35), "
                         "Morbihan (56), Loire-Atlantique (44), Maine-et-Loire (49)"))
    contact_rows.append(("Clients", "Particuliers, commerces et professionnels"))

    main = """
<section class="hero"><div class="container hero-inner">
  <div>
    <p class="eyebrow">Contact</p>
    <h1>Contacter Electricien Richard</h1>
    <p class="lead">Par téléphone pour les situations urgentes, par formulaire pour les
    demandes de travaux et les questions sur une installation.</p>
    %s
  </div>
  <div class="hero-media">%s</div>
</div></section>

<section class="section"><div class="container layout layout--sidebar">
  <div>
    %s
    <h2>Nous écrire</h2>
    %s
  </div>
  <div class="sidebar">
    <div class="card card--plain"><div class="card-icon">%s</div>
      <h3>Par téléphone</h3>
      <p>Le moyen le plus direct, en particulier pour un dépannage.</p>
      %s
    </div>
    <div class="card card--plain"><h3>Coordonnées</h3>%s</div>
    <div class="card card--plain"><h3>Zones couvertes</h3>
      <p>Six départements de Bretagne et des Pays de la Loire.</p>
      <a class="card-link" href="/zones-d-intervention.html">Voir le détail</a></div>
  </div>
</div></section>

<section class="section section--soft"><div class="container">
  <div class="prose prose--wide">
  <h2>Avant d'appeler pour une panne</h2>
  <p>Quelques informations permettent de qualifier la situation beaucoup plus vite :</p>
  %s
  <div class="callout callout--danger"><strong>En cas de danger immédiat</strong>
  <p>Odeur de brûlé, fumée, échauffement, arc électrique : coupez le disjoncteur général
  avant d'appeler. En cas de départ de feu ou d'accident corporel, appelez d'abord les
  secours au <strong>18</strong> ou au <strong>112</strong>.</p></div>
  </div>
</div></section>
""" % (hero_cta_row("Demander un devis", "/devis-electricien.html"),
       picture(IMG.IMAGES["about"], eager=True, sizes="(min-width: 900px) 560px, 100vw"),
       quick_answer(
           "Comment nous joindre",
           "<p><strong>Par téléphone au %s pour toute demande urgente, ou par le formulaire "
           "ci-dessous pour une demande de devis ou une question.</strong></p>"
           "<p>Précisez toujours votre commune : elle détermine les conditions "
           "d'intervention.</p>" % SITE["phone_display"],
           contact_rows),
       contact_form(form_id="contact"),
       icon("phone", 24), phone_link(classes="btn btn--primary btn--sm"),
       '<div class="table-wrap"><table><tbody>%s</tbody></table></div>' % "".join(
           "<tr><th scope=\"row\">%s</th><td>%s</td></tr>" % (esc(k), v) for k, v in contact_rows),
       checks([
           "L'étendue de la panne : tout le logement, une pièce, un seul appareil",
           "Le dispositif déclenché au tableau : disjoncteur de branchement, différentiel ou "
           "disjoncteur de circuit",
           "Ce qui s'est passé juste avant : appareil mis en route, orage, pluie, travaux",
           "Si la panne est permanente ou intermittente",
           "L'âge approximatif de l'installation et le type de tableau",
           "Votre commune et les conditions d'accès",
       ]))

    html = render_page(
        "contact.html",
        "Contact — Électricien en Bretagne et Pays de la Loire | Electricien Richard",
        ("Contacter Electricien Richard : téléphone pour les urgences, formulaire pour les "
         "demandes de devis. Interventions dans six départements."),
        main, trail=[("Accueil", "/"), ("Contact", None)])
    write("contact.html", html, priority="0.7")


def build_about_faq():
    # ---------------- À propos ----------------
    main = """
<section class="hero"><div class="container hero-inner">
  <div>
    <p class="eyebrow">À propos</p>
    <h1>Electricien Richard, artisan électricien</h1>
    <p class="lead">Une activité d'électricité générale au service des particuliers, des
    commerces et des professionnels, sur un périmètre volontairement limité à six
    départements.</p>
    %s
  </div>
  <div class="hero-media">%s</div>
</div></section>

<section class="section"><div class="container layout layout--sidebar">
  <div class="prose prose--wide">
    %s
    <h2 id="activite">Notre activité</h2>
    <p>Electricien Richard intervient sur l'ensemble du champ de l'électricité du bâtiment :
    dépannage et recherche de panne, installation neuve, rénovation d'installations
    existantes, mise en sécurité, et pose d'équipements — tableaux, éclairage, bornes de
    recharge, ventilation.</p>
    <p>Les clients sont des particuliers — propriétaires occupants, bailleurs, acquéreurs —
    ainsi que des commerces et des professionnels dont les locaux appellent des exigences
    spécifiques.</p>

    <h2 id="approche">Notre façon de travailler</h2>
    <p>Trois principes structurent chaque intervention.</p>

    <h3>Comprendre avant d'agir</h3>
    <p>Une panne ne se règle pas en rétablissant le courant. Tant que la cause n'est pas
    identifiée, le problème réapparaît. C'est pourquoi un dépannage commence par un
    diagnostic, et un chantier par un examen de l'existant.</p>

    <h3>La sécurité avant le confort</h3>
    <p>Lorsqu'une installation présente à la fois un défaut de sécurité et un manque de
    confort, l'ordre est toujours le même : mise à la terre et protection différentielle
    d'abord, prises supplémentaires et éclairage ensuite. Cet ordre évite aussi de refaire
    deux fois les mêmes travaux.</p>

    <h3>Expliquer ce qui a été fait</h3>
    <p>Un tableau repéré, un constat expliqué, des travaux complémentaires signalés sans
    pression : l'objectif est que vous compreniez l'état de votre installation, y compris ce
    qui n'a pas été traité.</p>

    <h2 id="perimetre">Pourquoi seulement six départements</h2>
    <p>Le périmètre couvre les Côtes-d'Armor, le Finistère, l'Ille-et-Vilaine, le Morbihan,
    la Loire-Atlantique et le Maine-et-Loire. Il s'arrête là, y compris pour les départements
    immédiatement voisins.</p>
    <p>Ce choix est assumé : annoncer une couverture plus large qu'on ne peut réellement
    assurer conduit à des délais qui ne tiennent pas. Ce périmètre couvre déjà deux régions
    et des situations bâties très diverses — habitat en pierre de l'intérieur breton,
    immeubles de la reconstruction à Brest, Lorient ou Saint-Nazaire, tuffeau du Val de
    Loire, logements littoraux exposés aux embruns.</p>

    <h2 id="informations">Informations sur l'entreprise</h2>
    %s
    %s
  </div>
  %s
</div></section>

<section class="section section--soft"><div class="container">
  <div class="section-head"><h2>Nos prestations</h2></div>
  %s
</div></section>

<section class="section"><div class="container">%s</div></section>
""" % (hero_cta_row(),
       picture(IMG.IMAGES["about"], eager=True, sizes="(min-width: 900px) 560px, 100vw"),
       quick_answer(
           "Electricien Richard en bref",
           "<p><strong>Electricien Richard est un artisan électricien intervenant en "
           "dépannage, installation, rénovation et mise aux normes électriques.</strong></p>"
           "<p>Le périmètre couvre six départements de Bretagne et des Pays de la Loire, pour "
           "les particuliers, les commerces et les professionnels.</p>",
           [("Activité", "Électricité générale du bâtiment"),
            ("Prestations", "Dépannage, recherche de panne, installation, rénovation, mise aux "
                            "normes, tableau, éclairage, borne de recharge, VMC"),
            ("Zones", "22 · 29 · 35 · 56 · 44 · 49"),
            ("Clients", "Particuliers, commerces, professionnels"),
            ("Référence technique", "Norme NF C 15-100")]),
       callout("Informations légales à compléter",
               "<p>Les mentions administratives de l'entreprise — raison sociale, numéro "
               "SIRET, assurances — figurent sur la page "
               "<a href=\"/mentions-legales.html\">mentions légales</a>. Elles doivent être "
               "renseignées avant la mise en ligne du site.</p>"),
       faq_block([
           ("Depuis quand exercez-vous ?",
            "<p>Cette information doit être renseignée avec les données réelles de "
            "l'entreprise avant la mise en ligne du site. Aucune ancienneté n'est affichée "
            "tant qu'elle ne peut pas être vérifiée.</p>"),
           ("Êtes-vous assuré ?",
            "<p>Un professionnel du bâtiment doit disposer d'une assurance de responsabilité "
            "civile professionnelle et, pour les travaux relevant de la garantie décennale, "
            "d'une assurance décennale. Les attestations peuvent être demandées avant le "
            "début des travaux.</p>"),
           ("Intervenez-vous pour les professionnels ?",
            "<p>Oui, en commerce comme en local d'activité. Voir la page "
            "<a href=\"/electricien-entreprise.html\">électricien pour entreprises et "
            "commerces</a>.</p>"),
       ], title="Questions sur l'entreprise"),
       sidebar_block(["electricien", "electricien-depannage", "renovation-electrique",
                      "tarifs"]),
       services_grid(),
       cta_band("Un projet ou une panne à traiter ?",
                "Décrivez votre situation et votre commune : un devis vous est proposé sans "
                "engagement."))

    html = render_page(
        "a-propos.html",
        "À propos — Electricien Richard, artisan électricien | Electricien Richard",
        ("Electricien Richard : artisan électricien intervenant en dépannage, installation, "
         "rénovation et mise aux normes dans six départements de Bretagne et des Pays de la "
         "Loire."),
        main, trail=[("Accueil", "/"), ("À propos", None)],
        og_image=IMG.IMAGES["about"]["file"])
    write("a-propos.html", html, priority="0.6")

    # ---------------- FAQ ----------------
    faq_sections = [
        ("Prix et devis", "euro", [
            ("Combien coûte un électricien ?",
             "<p>Il n'existe pas de prix unique : le coût dépend de la nature du travail, du "
             "temps nécessaire, des fournitures et de l'accessibilité du chantier. Le devis "
             "est gratuit et détaillé. Voir la page <a href=\"/tarifs.html\">tarifs</a> pour "
             "le détail de ce qui compose un prix.</p>"),
            ("Quel est le prix d'un dépannage électrique ?",
             "<p>Il dépend du temps de recherche du défaut, des fournitures nécessaires et de "
             "l'horaire de l'intervention. Une intervention en soirée, un week-end ou un jour "
             "férié relève de conditions spécifiques, annoncées avant l'intervention.</p>"),
            ("Combien coûte la rénovation électrique d'un logement ?",
             "<p>Les écarts sont considérables selon le périmètre retenu — reprise du tableau "
             "seul ou remplacement de l'ensemble des circuits — et selon l'accessibilité des "
             "cheminements. Un chiffrage fiable suppose une visite.</p>"),
            ("Le devis est-il payant ?",
             "<p>Non, il est gratuit et sans engagement. Lorsqu'une étude technique "
             "approfondie est nécessaire, les conditions sont annoncées avant "
             "l'intervention.</p>"),
        ]),
        ("Pannes et dépannage", "tools", [
            ("Que faire lorsqu'un disjoncteur saute ?",
             "<p>Débranchez les appareils du circuit concerné, réarmez une seule fois, puis "
             "rebranchez les appareils un par un. Si la protection déclenche immédiatement "
             "même sans appareil branché, n'insistez pas : le défaut est dans "
             "l'installation.</p>"),
            ("Pourquoi mon disjoncteur saute-t-il ?",
             "<p>Trois causes principales : une surcharge du circuit, un court-circuit, ou une "
             "fuite de courant vers la terre détectée par un différentiel. Le dispositif qui a "
             "déclenché indique déjà laquelle. Voir "
             "<a href=\"/disjoncteur.html\">disjoncteur qui saute</a>.</p>"),
            ("Comment trouver une panne électrique ?",
             "<p>Par élimination : on divise l'installation, on teste chaque partie, et on "
             "réduit progressivement le périmètre. Les mesures d'isolement et de continuité "
             "permettent de localiser le défaut sans démonter. Voir "
             "<a href=\"/recherche-panne.html\">recherche de panne</a>.</p>"),
            ("Un électricien intervient-il en urgence ?",
             "<p>Oui. Les situations présentant un risque immédiat — odeur de brûlé, "
             "échauffement au tableau, coupure totale, disjoncteur impossible à réarmer — sont "
             "traitées en priorité. L'appel téléphonique est alors préférable au "
             "formulaire.</p>"),
            ("Ma panne vient-elle du réseau ou de mon installation ?",
             "<p>Si vos voisins sont également sans électricité, la coupure vient du réseau "
             "public et doit être signalée au gestionnaire de réseau. Si vous êtes seul "
             "concerné, le défaut est chez vous.</p>"),
        ]),
        ("Sécurité et normes", "shield", [
            ("Comment savoir si une installation électrique est dangereuse ?",
             "<p>Cinq signes doivent alerter : un tableau à fusibles à broche, l'absence de "
             "dispositif différentiel 30 mA, l'absence de mise à la terre, des traces "
             "d'échauffement, et des montages provisoires devenus permanents. Un seul de ces "
             "éléments justifie un examen.</p>"),
            ("La mise aux normes est-elle obligatoire ?",
             "<p>Il n'existe pas d'obligation générale pour une installation existante. "
             "L'obligation naît des travaux : une installation neuve ou entièrement rénovée "
             "doit respecter la norme en vigueur. En location, le logement doit par ailleurs "
             "être décent.</p>"),
            ("Quand faut-il refaire une installation électrique ?",
             "<p>Lorsque la mise à la terre est absente, que le tableau ne comporte pas de "
             "protection différentielle adaptée, que les conducteurs présentent un isolant "
             "dégradé, ou que des traces d'échauffement apparaissent. Un "
             "<a href=\"/diagnostic-electrique.html\">diagnostic</a> permet de trancher entre "
             "reprise partielle et rénovation complète.</p>"),
            ("Comment mettre une installation aux normes ?",
             "<p>En traitant les points dans l'ordre : mise à la terre, tableau et "
             "différentiels 30 mA, pièces d'eau, circuits vétustes, puis confort. Cet ordre "
             "évite de refaire deux fois les mêmes travaux.</p>"),
            ("Combien de temps est valable un diagnostic électrique ?",
             "<p>Trois ans dans le cadre d'une vente, six ans dans le cadre d'une "
             "location.</p>"),
            ("À quoi sert le bouton test d'un différentiel ?",
             "<p>Il vérifie que le dispositif déclenche encore. Un test mensuel est "
             "recommandé : un différentiel resté longtemps sans manœuvre peut se bloquer. S'il "
             "ne déclenche pas au test, il ne protège plus personne.</p>"),
        ]),
        ("Travaux et équipements", "home", [
            ("Quand faut-il changer un tableau électrique ?",
             "<p>Lorsqu'il comporte des fusibles à broche, ne dispose pas de différentiel "
             "30 mA, présente des traces d'échauffement, ou n'offre plus aucun emplacement "
             "libre. Voir <a href=\"/tableau-electrique.html\">tableau électrique</a>.</p>"),
            ("Peut-on installer une borne de recharge ?",
             "<p>Oui, en maison individuelle comme en copropriété. En copropriété, le droit à "
             "la prise permet l'installation à ses frais après information du syndic. Une "
             "borne se raccorde sur un circuit dédié avec une protection adaptée.</p>"),
            ("Peut-on remplacer un tableau en appartement ?",
             "<p>Oui, la partie privative du logement relève du propriétaire. Les colonnes "
             "montantes et les installations des parties communes dépendent en revanche de la "
             "copropriété.</p>"),
            ("Combien de circuits faut-il dans un logement ?",
             "<p>Cela dépend de la surface et des équipements. La norme impose des circuits "
             "spécialisés pour la plaque de cuisson et les gros appareils, ainsi que des "
             "circuits distincts pour l'éclairage et les prises, avec un nombre maximal de "
             "points par circuit.</p>"),
            ("Peut-on étaler des travaux électriques dans le temps ?",
             "<p>Oui, à condition de respecter l'ordre de priorité : mise à la terre et "
             "tableau d'abord, pièces d'eau et cuisine ensuite, confort en dernier.</p>"),
        ]),
        ("Interventions et zones", "map", [
            ("Dans quels départements intervenez-vous ?",
             "<p>Dans six départements uniquement : Côtes-d'Armor (22), Finistère (29), "
             "Ille-et-Vilaine (35), Morbihan (56), Loire-Atlantique (44) et Maine-et-Loire "
             "(49). Aucun autre département n'est couvert.</p>"),
            ("Combien coûte une intervention hors horaires habituels ?",
             "<p>Une intervention en soirée, la nuit, un week-end ou un jour férié fait l'objet "
             "de conditions tarifaires spécifiques, communiquées avant l'intervention.</p>"),
            ("Intervenez-vous chez les professionnels ?",
             "<p>Oui, en commerce et en local d'activité, avec les exigences propres aux "
             "établissements recevant du public et aux locaux de travail. Voir "
             "<a href=\"/electricien-entreprise.html\">électricien pour entreprises</a>.</p>"),
            ("Faut-il être présent pendant les travaux ?",
             "<p>Votre présence est utile au début, pour valider l'implantation, et à la fin, "
             "pour la remise et les explications. Entre les deux, elle n'est pas indispensable "
             "dès lors que l'accès est organisé.</p>"),
        ]),
    ]

    all_faq = [qa for _, _, items in faq_sections for qa in items]
    sections_html = "".join(
        '<section class="section%s"><div class="container">'
        '<div class="section-head"><p class="eyebrow">%s %s</p><h2>%s</h2></div>'
        '<div style="max-width:82ch">%s</div></div></section>'
        % (" section--soft" if i % 2 else "", icon(ic, 14), esc(name), esc(name),
           faq_block(items, title="", anchor="faq-%d" % i))
        for i, (name, ic, items) in enumerate(faq_sections))

    main = """
<section class="hero"><div class="container hero-inner">
  <div>
    <p class="eyebrow">FAQ</p>
    <h1>Questions fréquentes sur l'électricité</h1>
    <p class="lead">Les questions les plus souvent posées sur les pannes, la sécurité, les
    normes, les travaux et les conditions d'intervention.</p>
    %s
  </div>
  <div class="hero-media">%s</div>
</div></section>
%s
<section class="section"><div class="container">%s</div></section>
""" % (hero_cta_row(),
       picture(IMG.IMAGES["svc_diagnostic-electrique"], eager=True,
               sizes="(min-width: 900px) 560px, 100vw"),
       sections_html,
       cta_band("Votre question n'est pas traitée ?",
                "Décrivez votre situation : la réponse est souvent plus rapide qu'une "
                "recherche."))

    html = render_page(
        "faq.html",
        "FAQ électricité — Questions fréquentes | Electricien Richard",
        ("Questions fréquentes sur l'électricité : prix, dépannage, disjoncteur qui saute, "
         "sécurité, mise aux normes, tableau électrique et bornes de recharge."),
        main, trail=[("Accueil", "/"), ("Questions fréquentes", None)],
        schema_nodes=[faq_node(all_faq, "/faq.html")])
    write("faq.html", html, priority="0.7")


def build_legal_pages():
    todo = ('<span style="background:#FEF9C3;border:1px solid #EAB308;border-radius:4px;'
            'padding:0 .3rem;font-weight:700">à compléter</span>')

    # ---------------- Mentions légales ----------------
    main = """
<section class="section"><div class="container prose">
  <h1>Mentions légales</h1>
  <p class="lead">Informations légales relatives au site electricien-richard.fr.</p>

  <div class="callout"><strong>Informations à compléter avant mise en ligne</strong>
  <p>Les éléments signalés ci-dessous doivent être renseignés avec les données réelles de
  l'entreprise. Aucune information administrative n'a été inventée.</p></div>

  <h2>Éditeur du site</h2>
  <div class="table-wrap"><table><tbody>
    <tr><th scope="row">Dénomination</th><td>Electricien Richard</td></tr>
    <tr><th scope="row">Forme juridique</th><td>%s</td></tr>
    <tr><th scope="row">Adresse du siège</th><td>%s</td></tr>
    <tr><th scope="row">Téléphone</th><td><a href="tel:%s">%s</a></td></tr>
    <tr><th scope="row">Adresse e-mail</th><td><a href="mailto:%s">%s</a></td></tr>
    <tr><th scope="row">Numéro SIRET</th><td>%s</td></tr>
    <tr><th scope="row">Numéro de TVA intracommunautaire</th><td>%s</td></tr>
    <tr><th scope="row">Directeur de la publication</th><td>%s</td></tr>
  </tbody></table></div>

  <h2>Assurances professionnelles</h2>
  <div class="table-wrap"><table><tbody>
    <tr><th scope="row">Responsabilité civile professionnelle</th><td>%s</td></tr>
    <tr><th scope="row">Assurance décennale</th><td>%s</td></tr>
    <tr><th scope="row">Couverture géographique</th><td>France métropolitaine</td></tr>
  </tbody></table></div>

  <h2>Hébergement</h2>
  <div class="table-wrap"><table><tbody>
    <tr><th scope="row">Hébergeur</th><td>%s</td></tr>
    <tr><th scope="row">Adresse</th><td>%s</td></tr>
  </tbody></table></div>

  <h2>Propriété intellectuelle</h2>
  <p>L'ensemble des contenus présents sur ce site — textes, mise en page, éléments
  graphiques, photographies — est protégé par le droit d'auteur. Toute reproduction ou
  représentation, totale ou partielle, sans autorisation préalable est interdite.</p>

  <h2>Responsabilité</h2>
  <p>Les informations techniques publiées sur ce site ont une vocation d'information
  générale. Elles ne se substituent pas à l'examen d'une installation par un professionnel :
  chaque installation présente des caractéristiques propres qui conditionnent le diagnostic
  et les travaux à réaliser.</p>
  <p>Les interventions sur une installation électrique sous tension présentent un risque
  d'électrisation et d'incendie. Aucun contenu de ce site ne doit être interprété comme une
  incitation à intervenir soi-même sur une installation.</p>

  <h2>Liens externes</h2>
  <p>Ce site peut contenir des liens vers des sites tiers. Leur contenu n'engage que leurs
  éditeurs respectifs.</p>

  <h2>Données personnelles</h2>
  <p>Le traitement des données transmises via les formulaires est décrit dans la
  <a href="/politique-de-confidentialite.html">politique de confidentialité</a>.</p>

  <h2>Médiation de la consommation</h2>
  <p>Conformément au code de la consommation, un consommateur peut recourir gratuitement à
  un médiateur de la consommation en vue de la résolution amiable d'un litige. Les
  coordonnées du médiateur compétent doivent être renseignées ici : %s</p>
</div></section>
""" % ((todo,), (SITE["address"] or todo), SITE["phone_tel"], SITE["phone_display"],
       SITE["email"], SITE["email"], SITE["siret"] or todo, todo, todo,
       SITE["assurance"] or todo, SITE["assurance"] or todo,
       SITE["hebergeur"] or todo, todo, todo)
    html = render_page("mentions-legales.html",
                       "Mentions légales | Electricien Richard",
                       "Mentions légales du site electricien-richard.fr : éditeur, "
                       "assurances, hébergement et responsabilité.",
                       main, trail=[("Accueil", "/"), ("Mentions légales", None)])
    write("mentions-legales.html", html, priority="0.2", changefreq="yearly")

    # ---------------- Politique de confidentialité ----------------
    main = """
<section class="section"><div class="container prose">
  <h1>Politique de confidentialité</h1>
  <p class="lead">Cette page décrit les données collectées par le site
  electricien-richard.fr et l'usage qui en est fait.</p>

  <h2>Responsable du traitement</h2>
  <p>Electricien Richard, éditeur du site, dont les coordonnées figurent dans les
  <a href="/mentions-legales.html">mentions légales</a>.</p>

  <h2>Données collectées</h2>
  <p>Les seules données collectées sont celles que vous transmettez volontairement via les
  formulaires de contact et de demande de devis :</p>
  <ul>
    <li>nom et prénom ;</li>
    <li>numéro de téléphone ;</li>
    <li>adresse e-mail, si vous la renseignez ;</li>
    <li>commune et département ;</li>
    <li>description de votre demande.</li>
  </ul>
  <p>Aucune donnée n'est collectée à votre insu. Le site n'utilise pas de cookie de mesure
  d'audience ni de traceur publicitaire.</p>

  <h2>Finalité du traitement</h2>
  <p>Ces données servent exclusivement à répondre à votre demande, établir un devis et, le
  cas échéant, organiser une intervention. Elles ne sont ni vendues, ni cédées, ni utilisées
  à des fins de prospection par des tiers.</p>

  <h2>Base légale</h2>
  <p>Le traitement repose sur votre consentement, exprimé par l'envoi du formulaire, et sur
  l'exécution de mesures précontractuelles prises à votre demande.</p>

  <h2>Durée de conservation</h2>
  <p>Les demandes n'ayant pas donné lieu à une intervention sont conservées le temps
  nécessaire à leur traitement, puis supprimées. Les documents liés à une intervention
  réalisée — devis, factures — sont conservés pendant la durée imposée par les obligations
  légales et comptables.</p>

  <h2>Destinataires</h2>
  <p>Les données sont destinées au seul responsable du traitement. Elles peuvent être
  hébergées par le prestataire technique du site ou du service de messagerie, dans le cadre
  de l'exécution de leurs prestations.</p>

  <h2>Vos droits</h2>
  <p>Vous disposez d'un droit d'accès, de rectification, d'effacement, de limitation et
  d'opposition au traitement de vos données, ainsi que d'un droit à la portabilité. Ces
  droits s'exercent par courrier électronique à l'adresse indiquée dans les mentions
  légales.</p>
  <p>Vous pouvez également introduire une réclamation auprès de la Commission nationale de
  l'informatique et des libertés (CNIL).</p>

  <h2>Cookies</h2>
  <p>Le site ne dépose aucun cookie de mesure d'audience ni de cookie publicitaire. La carte
  interactive des zones d'intervention charge des fonds de plan depuis OpenStreetMap : cette
  requête est effectuée par votre navigateur auprès de ce service lorsque vous consultez une
  page comportant une carte.</p>

  <h2>Sécurité</h2>
  <p>Les données transmises via le site circulent en HTTPS. Elles ne sont accessibles qu'aux
  personnes chargées du traitement des demandes.</p>
</div></section>
"""
    html = render_page("politique-de-confidentialite.html",
                       "Politique de confidentialité | Electricien Richard",
                       "Politique de confidentialité du site electricien-richard.fr : "
                       "données collectées, finalités, durée de conservation et droits.",
                       main,
                       trail=[("Accueil", "/"), ("Politique de confidentialité", None)])
    write("politique-de-confidentialite.html", html, priority="0.2", changefreq="yearly")


def build_sitemap_page():
    def ul(links):
        return "<ul>%s</ul>" % "".join('<li><a href="%s">%s</a></li>' % (h, esc(l))
                                       for l, h in links)

    by_cat = {}
    for s in SERVICES:
        by_cat.setdefault(s["category"], []).append(s)

    services_html = "".join(
        "<h3>%s</h3>%s" % (esc(cat), ul([(s["h1"].split(" :")[0], "/" + s["path"])
                                         for s in items]))
        for cat, items in by_cat.items())

    zones_html = "".join(
        "<h3><a href=\"%s\">%s (%s)</a></h3>%s"
        % (dept_url(d), esc(d["name"]), d["code"],
           ul([("Électricien à %s" % c["name"], city_url(d, c)) for c in d["cities"]]))
        for d in DEPARTEMENTS)

    blog_html = "".join(
        "<h3><a href=\"%s\">%s</a></h3>%s"
        % (BLOG.category_url(c), esc(c["name"]),
           ul([(a["title"], BLOG.article_url(a))
               for a in BLOG.articles_by_category(c["slug"])]))
        for c in BLOG.CATEGORIES)

    main = """
<section class="section"><div class="container prose prose--wide">
  <h1>Plan du site</h1>
  <p class="lead">L'ensemble des pages publiées sur electricien-richard.fr.</p>

  <h2>Pages principales</h2>
  %s

  <h2>Prestations</h2>
  %s

  <h2>Zones d'intervention</h2>
  %s

  <h2>Blog</h2>
  %s

  <h2>Informations</h2>
  %s
  <p class="form-note">Un fichier <a href="/sitemap.xml">sitemap.xml</a> est également mis à
  disposition des moteurs de recherche.</p>
</div></section>
""" % (ul([("Accueil", "/"), ("Électricien", "/electricien.html"),
           ("Zones d'intervention", "/zones-d-intervention.html"),
           ("Blog", "/blog/"), ("Tarifs", "/tarifs.html"),
           ("Demander un devis", "/devis-electricien.html"),
           ("Contact", "/contact.html"), ("À propos", "/a-propos.html"),
           ("Questions fréquentes", "/faq.html")]),
       services_html, zones_html, blog_html,
       ul([("Mentions légales", "/mentions-legales.html"),
           ("Politique de confidentialité", "/politique-de-confidentialite.html")]))

    html = render_page("plan-du-site.html", "Plan du site | Electricien Richard",
                       "Plan du site electricien-richard.fr : prestations, zones "
                       "d'intervention, articles de blog et pages d'information.",
                       main, trail=[("Accueil", "/"), ("Plan du site", None)])
    write("plan-du-site.html", html, priority="0.3", changefreq="weekly")


def build_404():
    main = """
<section class="section"><div class="container prose text-center"
  style="margin-inline:auto;max-width:60ch">
  <p class="eyebrow">Erreur 404</p>
  <h1>Cette page n'existe pas</h1>
  <p class="lead">Le lien est peut-être erroné, ou la page a été déplacée.</p>
  <div class="btn-row" style="justify-content:center">
    <a class="btn btn--primary" href="/">Retour à l'accueil</a>
    <a class="btn btn--ghost" href="/plan-du-site.html">Plan du site</a>
  </div>
  <h2 style="margin-top:2.5rem">Pages les plus consultées</h2>
  %s
</div></section>
""" % link_cloud([("Électricien", "/electricien.html"),
                  ("Dépannage électrique", "/electricien-depannage.html"),
                  ("Électricien en urgence", "/electricien-urgence.html"),
                  ("Tableau électrique", "/tableau-electrique.html"),
                  ("Rénovation électrique", "/renovation-electrique.html"),
                  ("Zones d'intervention", "/zones-d-intervention.html"),
                  ("Tarifs", "/tarifs.html"), ("Contact", "/contact.html")])
    html = render_page("404.html", "Page introuvable | Electricien Richard",
                       "La page demandée n'existe pas sur electricien-richard.fr.",
                       main, noindex=True)
    write("404.html", html, indexable=False)


# ------------------------------------------------------- fichiers techniques
def build_sitemap():
    entries = sorted(set(PAGES), key=lambda p: (-float(p[2]), p[0]))
    urls = "".join(
        "  <url><loc>%s</loc><lastmod>%s</lastmod>"
        "<changefreq>%s</changefreq><priority>%s</priority></url>\n"
        % (abs_url(loc), lastmod, changefreq, priority)
        for loc, lastmod, priority, changefreq in entries)
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s</urlset>\n' % urls)
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write(xml)
    return len(entries)


def build_robots():
    txt = """# robots.txt - electricien-richard.fr
User-agent: *
Allow: /
Disallow: /tools/
Disallow: /zones/index.html

# Moteurs de recherche generatifs et assistants IA : acces autorise
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Applebot-Extended
Allow: /

Sitemap: %s/sitemap.xml
""" % SITE["base_url"]
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as fh:
        fh.write(txt)


def build_favicon():
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40">'
           '<rect width="40" height="40" rx="9" fill="#111827"/>'
           '<path d="M22.5 8 14 22h5.2l-1.7 10L27 17.5h-5.4L22.5 8Z" fill="#FACC15"/></svg>')
    with open(os.path.join(ROOT, "favicon.svg"), "w", encoding="utf-8") as fh:
        fh.write(svg)
    logo_path = os.path.join(ROOT, "assets", "images",
                             "electricien-richard-logo.svg")
    os.makedirs(os.path.dirname(logo_path), exist_ok=True)
    with open(logo_path, "w", encoding="utf-8") as fh:
        fh.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 80" '
                 'width="320" height="80" role="img" '
                 'aria-label="Electricien Richard">'
                 '<rect width="80" height="80" rx="18" fill="#111827"/>'
                 '<path d="M45 16 28 44h10.4l-3.4 20L54 35h-10.8L45 16Z" fill="#FACC15"/>'
                 '<text x="96" y="40" font-family="Inter,Arial,sans-serif" font-size="26" '
                 'font-weight="800" fill="#111827">Electricien</text>'
                 '<text x="96" y="66" font-family="Inter,Arial,sans-serif" font-size="26" '
                 'font-weight="800" fill="#CA8A04">Richard</text></svg>')


def build_photo_report():
    """Liste des photos attendues, regeneree a chaque build."""
    lines = [
        "# Photos à fournir",
        "",
        "Ce fichier est **généré automatiquement** à chaque build "
        "(`python3 tools/build.py`).",
        "",
        "Chaque ligne correspond à un emplacement de photo prévu dans le site. "
        "Déposez le fichier au chemin exact indiqué, puis relancez le build : "
        "la photo remplace automatiquement l'emplacement neutre, sans aucune "
        "modification de code.",
        "",
        "## Format recommandé",
        "",
        "- Format **WebP** (ou AVIF), qualité 75 à 85.",
        "- Largeur d'origine : 1600 px minimum pour les photos principales.",
        "- Variantes responsives facultatives mais recommandées : en ajoutant "
        "`nom-480w.webp`, `nom-800w.webp`, `nom-1200w.webp`, `nom-1600w.webp` "
        "à côté du fichier principal, un attribut `srcset` est généré automatiquement.",
        "- Vérifiez le texte alternatif indiqué : il doit décrire ce que montre "
        "réellement la photo fournie. Un ALT ne doit pas être une liste de mots-clés.",
        "",
        "## Emplacements attendus (%d)" % len(MISSING_IMAGES),
        "",
    ]
    for f in sorted(MISSING_IMAGES):
        lines.append("- [ ] `%s`" % f)
    lines.append("")
    with open(os.path.join(ROOT, "PHOTOS-A-FOURNIR.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


def build_htaccess():
    txt = """# electricien-richard.fr - compression, cache et page 404
ErrorDocument 404 /404.html

<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css text/plain text/xml
  AddOutputFilterByType DEFLATE application/javascript application/json
  AddOutputFilterByType DEFLATE image/svg+xml
</IfModule>

<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType text/css "access plus 1 year"
  ExpiresByType application/javascript "access plus 1 year"
  ExpiresByType image/webp "access plus 1 year"
  ExpiresByType image/avif "access plus 1 year"
  ExpiresByType image/svg+xml "access plus 1 year"
  ExpiresByType text/html "access plus 1 hour"
</IfModule>

<IfModule mod_headers.c>
  Header set X-Content-Type-Options "nosniff"
  Header set Referrer-Policy "strict-origin-when-cross-origin"
</IfModule>
"""
    with open(os.path.join(ROOT, ".htaccess"), "w", encoding="utf-8") as fh:
        fh.write(txt)


# ---------------------------------------------------------------- controles
def sanity_checks():
    """Verifications bloquantes executees a chaque build."""
    problems = []

    # 1. Perimetre geographique strict
    allowed = {"22", "29", "35", "56", "44", "49"}
    for dep in DEPARTEMENTS:
        if dep["code"] not in allowed:
            problems.append("Departement hors perimetre : %s" % dep["code"])

    # 2. Titles et descriptions uniques
    titles, descs, urls = {}, {}, set()
    for path, _, _, _ in PAGES:
        urls.add(path)
    for root, _, files in os.walk(ROOT):
        if any(seg in root for seg in (".git", "tools", "assets")):
            continue
        for f in files:
            if not f.endswith(".html"):
                continue
            fp = os.path.join(root, f)
            html = open(fp, encoding="utf-8").read()
            rel = os.path.relpath(fp, ROOT)
            if 'name="robots" content="noindex' in html:
                continue
            t = re.search(r"<title>(.*?)</title>", html, re.S)
            d = re.search(r'<meta name="description" content="(.*?)">', html, re.S)
            h1 = re.findall(r"<h1[^>]*>", html)
            if t:
                titles.setdefault(t.group(1), []).append(rel)
            if d:
                descs.setdefault(d.group(1), []).append(rel)
            if len(h1) != 1:
                problems.append("%s : %d balise(s) H1 (1 attendue)" % (rel, len(h1)))
    for t, pages in titles.items():
        if len(pages) > 1:
            problems.append("Title duplique sur %s : %s" % (pages, t[:60]))
    for d, pages in descs.items():
        if len(pages) > 1:
            problems.append("Meta description dupliquee sur %s" % pages)

    return problems


def check_internal_links():
    """Verifie que chaque lien interne pointe vers un fichier existant."""
    broken = []
    for root, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in (".git", "tools")]
        for f in files:
            if not f.endswith(".html"):
                continue
            fp = os.path.join(root, f)
            rel = os.path.relpath(fp, ROOT)
            html = open(fp, encoding="utf-8").read()
            for href in re.findall(r'href="(/[^"#?]*)"', html):
                target = href.lstrip("/")
                if target == "":
                    target = "index.html"
                elif href.endswith("/"):
                    target = target + "index.html"
                if not os.path.exists(os.path.join(ROOT, target)):
                    broken.append("%s -> %s" % (rel, href))
    return sorted(set(broken))


# --------------------------------------------------------------------- main
def main():
    print("Build electricien-richard.fr")
    build_home()
    build_service_pages()
    build_zone_pages()
    build_blog()
    build_contact_pages()
    build_about_faq()
    build_legal_pages()
    build_sitemap_page()
    build_404()

    build_favicon()
    build_robots()
    build_htaccess()
    n = build_sitemap()
    build_photo_report()

    print("  %d pages indexables ecrites" % n)
    print("  %d emplacements photo en attente (voir PHOTOS-A-FOURNIR.md)"
          % len(MISSING_IMAGES))

    problems = sanity_checks()
    broken = check_internal_links()
    if broken:
        problems.extend("Lien interne casse : %s" % b for b in broken)

    if problems:
        print("\n  %d probleme(s) detecte(s) :" % len(problems))
        for p in problems[:40]:
            print("   - %s" % p)
        return 1
    print("  Controles OK : perimetre, titles/descriptions uniques, H1, liens internes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
