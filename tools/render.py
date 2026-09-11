# -*- coding: utf-8 -*-
"""Moteur de rendu : layout, composants reutilisables, donnees structurees."""

import html
import json
import os
import re

from content.site import SITE, has_phone

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def esc(txt):
    return html.escape(str(txt), quote=True)


def abs_url(path):
    """/electricien.html -> https://electricien-richard.fr/electricien.html"""
    if path.startswith("http"):
        return path
    if not path.startswith("/"):
        path = "/" + path
    return SITE["base_url"] + path


def url_for(path):
    """Chemin de fichier -> URL servie (index.html devient un repertoire)."""
    path = path.lstrip("/")
    if path == "index.html":
        return "/"
    if path.endswith("/index.html"):
        return "/" + path[: -len("index.html")]
    return "/" + path


def slugify(txt):
    txt = txt.lower()
    for a, b in (("àâä", "a"), ("éèêë", "e"), ("îï", "i"), ("ôö", "o"),
                 ("ùûü", "u"), ("ç", "c"), ("'’", "-")):
        for ch in a:
            txt = txt.replace(ch, b)
    txt = re.sub(r"[^a-z0-9]+", "-", txt)
    return txt.strip("-")


# ---------------------------------------------------------------- images ---
IMAGE_DIR = os.path.join(ROOT, "assets", "images")
MISSING_IMAGES = {}          # rempli au build : {chemin: {"alt":..., "sujet":...}}


def webp_size(path):
    """Dimensions reelles d'un WebP, sans dependance externe.

    Gere les trois variantes du format (VP8 simple, VP8L sans perte, VP8X
    etendu). Retourne None si le fichier n'est pas lisible : les valeurs
    declarees dans le manifeste servent alors de repli.
    """
    try:
        with open(path, "rb") as fh:
            head = fh.read(32)
        if head[:4] != b"RIFF" or head[8:12] != b"WEBP":
            return None
        tag = head[12:16]
        if tag == b"VP8 ":
            w = int.from_bytes(head[26:28], "little") & 0x3FFF
            h = int.from_bytes(head[28:30], "little") & 0x3FFF
            return w, h
        if tag == b"VP8L":
            b = int.from_bytes(head[21:25], "little")
            return (b & 0x3FFF) + 1, ((b >> 14) & 0x3FFF) + 1
        if tag == b"VP8X":
            w = int.from_bytes(head[24:27], "little") + 1
            h = int.from_bytes(head[27:30], "little") + 1
            return w, h
    except Exception:                                   # noqa: BLE001
        return None
    return None


def has_photo(slot):
    """True si le fichier photo existe reellement dans le depot."""
    return os.path.exists(os.path.join(ROOT, slot["file"].lstrip("/")))


def picture(slot, sizes="(min-width: 900px) 640px, 100vw", eager=False,
            caption=None, classes=""):
    """
    Rend une image reelle si le fichier existe dans /assets/images/,
    sinon un emplacement neutre indiquant le nom de fichier attendu.
    Aucun visuel n'est jamais invente ni presente comme une photo reelle.
    slot = dict(file, alt, width, height, caption)
    """
    rel = slot["file"].lstrip("/")
    disk = os.path.join(ROOT, rel)
    alt = esc(slot["alt"])
    w, h = slot.get("width", 1200), slot.get("height", 800)
    cap = caption if caption is not None else slot.get("caption")
    cls = ' class="%s"' % esc(classes) if classes else ""

    if os.path.exists(disk):
        # Les dimensions reelles priment sur celles declarees : le ratio
        # affiche correspond ainsi toujours au fichier livre (CLS nul).
        reelles = webp_size(disk) if rel.lower().endswith(".webp") else None
        if reelles:
            w, h = reelles
        base, ext = os.path.splitext(rel)
        srcset = []
        for width in (480, 800, 1200, 1600):
            variant = "%s-%dw%s" % (base, width, ext)
            if os.path.exists(os.path.join(ROOT, variant)):
                srcset.append("/%s %dw" % (variant, width))
        srcset_attr = ' srcset="%s" sizes="%s"' % (", ".join(srcset), esc(sizes)) if srcset else ""
        img = (
            '<img src="/%s" alt="%s" width="%d" height="%d"%s '
            'loading="%s" decoding="async"%s>'
            % (rel, alt, w, h, srcset_attr,
               "eager" if eager else "lazy",
               ' fetchpriority="high"' if eager else "")
        )
    else:
        MISSING_IMAGES.setdefault(slot["file"], {"alt": slot["alt"],
                                                 "sujet": slot.get("sujet")})
        # Emplacement neutre : il annonce la photo attendue, sans jamais simuler
        # une photo ni afficher de faux contenu.
        sujet = slot.get("sujet") or slot["alt"]
        img = (
            '<div class="media-placeholder" role="img" aria-label="%s" '
            'style="aspect-ratio:%d/%d"><b>Photo à venir</b>'
            '<span>%s</span></div>'
            % (esc("Emplacement réservé à une photo : " + slot["alt"]), w, h, esc(sujet))
        )

    if cap:
        return '<figure%s>%s<figcaption>%s</figcaption></figure>' % (cls, img, cap)
    return '<figure%s>%s</figure>' % (cls, img)


# ------------------------------------------------------------ composants ---
def icon(name, size=22):
    """Petites icones SVG inline (pas de librairie externe)."""
    paths = {
        "bolt": '<path d="M13 2 4.5 13.5H11l-1 8.5 8.5-11.5H12l1-8.5Z"/>',
        "shield": '<path d="M12 2 4 5.5v6c0 4.6 3.2 8.7 8 10.5 4.8-1.8 8-5.9 8-10.5v-6L12 2Z"/>',
        "clock": ('<path d="M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18Zm0 2a7 7 0 1 1 0 14 7 7 0 0 1 0-14Z"/>'
                  '<path d="M11 7h2v5.1l3.3 1.9-1 1.7L11 13.3V7Z"/>'),
        "phone": '<path d="M6.6 3h3.1l1.6 4-2 1.4a12.4 12.4 0 0 0 5.3 5.3l1.4-2 4 1.6v3.1c0 1-.8 1.8-1.8 1.6C10.9 17.4 6.6 13.1 5 5.8 4.8 4.8 5.6 3 6.6 3Z"/>',
        "check": '<path d="M9.6 16.2 5.4 12l-1.4 1.4 5.6 5.6L20.4 8.2 19 6.8Z"/>',
        "tools": '<path d="M14.7 2a5.5 5.5 0 0 0-5 7.8L2.9 16.6a1.5 1.5 0 0 0 0 2.1l2.4 2.4a1.5 1.5 0 0 0 2.1 0l6.8-6.8A5.5 5.5 0 0 0 20 4.6l-3 3-2.6-2.6 3-3A5.5 5.5 0 0 0 14.7 2Z"/>',
        "home": '<path d="M12 3 2 11h3v10h6v-6h2v6h6V11h3L12 3Z"/>',
        "map": '<path d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7Zm0 9.5A2.5 2.5 0 1 1 12 6a2.5 2.5 0 0 1 0 5.5Z"/>',
        "doc": '<path d="M6 2h8l4 4v16H6V2Zm7 1.5V7h3.5L13 3.5ZM8 11h8v2H8v-2Zm0 4h8v2H8v-2Z"/>',
        "plug": '<path d="M8 2v6H6v3a6 6 0 0 0 5 5.9V22h2v-5.1A6 6 0 0 0 18 11V8h-2V2h-2v6h-4V2H8Z"/>',
        "car": '<path d="M5 11 6.6 6.4A2 2 0 0 1 8.5 5h7a2 2 0 0 1 1.9 1.4L19 11h1v7h-3v-2H7v2H4v-7h1Zm2.5 4a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm9 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM7.4 10h9.2l-1.1-3H8.5l-1.1 3Z"/>',
        "bulb": '<path d="M9 20h6v1.5H9V20Zm3-18a7 7 0 0 0-4 12.7V17h8v-2.3A7 7 0 0 0 12 2Z"/>',
        "search": '<path d="M10.5 3a7.5 7.5 0 1 0 4.6 13.4l4.2 4.3 1.5-1.5-4.3-4.2A7.5 7.5 0 0 0 10.5 3Zm0 2a5.5 5.5 0 1 1 0 11 5.5 5.5 0 0 1 0-11Z"/>',
        "building": '<path d="M4 21V4a1 1 0 0 1 1-1h9a1 1 0 0 1 1 1v4h4a1 1 0 0 1 1 1v12H4Zm3-3h3v-3H7v3Zm0-5h3v-3H7v3Zm0-5h3V5H7v3Zm5 10h3v-3h-3v3Zm0-5h3v-3h-3v3Zm0-5h3V5h-3v3Zm5 10h2v-3h-2v3Zm0-5h2v-3h-2v3Z"/>',
        "euro": '<path d="M15.5 6.3A6 6 0 0 0 8.6 10H14v2H8.2v1H14v2H8.6a6 6 0 0 0 6.9 3.7l.5 2A8 8 0 0 1 6.5 15H4v-2h2.1v-1H4v-2h2.5a8 8 0 0 1 9.5-5.7l-.5 2Z"/>',
        "star": '<path d="m12 2 2.9 6.3 6.8.8-5 4.6 1.3 6.8L12 17.2 6 20.5l1.3-6.8-5-4.6 6.8-.8L12 2Z"/>',
    }
    d = paths.get(name, paths["bolt"])
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="%d" '
            'height="%d" fill="currentColor" aria-hidden="true" focusable="false">%s</svg>'
            % (size, size, d))


def phone_link(label=None, classes="btn btn--primary", with_icon=True):
    label = label or ("Appeler le %s" % SITE["phone_display"])
    ic = icon("phone", 20) + " " if with_icon else ""
    return '<a class="%s" href="tel:%s">%s%s</a>' % (
        classes, SITE["phone_tel"], ic, esc(label))


def quick_answer(title, answer_html, facts=None, heading_level=2):
    """Bloc 'Reponse rapide' : lisible par les humains, Google et les IA."""
    out = ['<div class="quick-answer">']
    out.append('<h%d>%s %s</h%d>' % (heading_level, icon("bolt", 20), esc(title), heading_level))
    out.append(answer_html)
    if facts:
        out.append('<ul class="quick-facts">')
        for label, value in facts:
            out.append("<li><b>%s</b><span>%s</span></li>" % (esc(label), value))
        out.append("</ul>")
    out.append("</div>")
    return "\n".join(out)


def geo_card(rows):
    """Fiche d'identite factuelle (Qui / Quoi / Ou / Comment...) pour les moteurs IA."""
    body = "".join("<tr><th scope=\"row\">%s</th><td>%s</td></tr>" % (esc(k), v)
                   for k, v in rows)
    return (
        '<div class="table-wrap"><table class="geo-table">'
        '<caption>Fiche d\'information</caption><tbody>%s</tbody></table></div>' % body
    )


def table(caption, headers, rows):
    th = "".join("<th scope=\"col\">%s</th>" % esc(h) for h in headers)
    trs = []
    for r in rows:
        tds = "".join("<td>%s</td>" % c for c in r)
        trs.append("<tr>%s</tr>" % tds)
    return ('<div class="table-wrap"><table><caption>%s</caption>'
            "<thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>"
            % (esc(caption), th, "".join(trs)))


def callout(title, body_html, kind=""):
    cls = "callout" + (" callout--%s" % kind if kind else "")
    return '<div class="%s"><strong>%s</strong>%s</div>' % (cls, esc(title), body_html)


def steps_block(items):
    lis = "".join("<li><h3>%s</h3><p>%s</p></li>" % (esc(t), b) for t, b in items)
    return '<ol class="steps">%s</ol>' % lis


def checks(items):
    return '<ul class="checks">%s</ul>' % "".join("<li>%s</li>" % i for i in items)


def faq_block(items, title="Questions fréquentes", level=2, anchor="faq"):
    if not items:
        return ""
    out = ['<section class="faq-section" id="%s">' % anchor]
    if title:
        out.append("<h%d>%s</h%d>" % (level, esc(title), level))
    out.append('<div class="faq">')
    for q, a in items:
        out.append("<details><summary>%s</summary><div class=\"faq-body\">%s</div></details>"
                   % (esc(q), a))
    out.append("</div></section>")
    return "\n".join(out)


def cta_band(title, text, secondary=("Demander un devis", "/devis-electricien.html")):
    btns = [phone_link(classes="btn btn--primary")] if has_phone() else []
    if not has_phone():
        btns.append(phone_link(classes="btn btn--primary"))
    btns.append('<a class="btn btn--outline-light" href="%s">%s</a>'
                % (secondary[1], esc(secondary[0])))
    return (
        '<div class="cta-band"><div><h2>%s</h2><p>%s</p></div>'
        '<div class="btn-row">%s</div></div>' % (esc(title), text, "".join(btns))
    )


def cta_inline(text, label="Demander un devis", href="/devis-electricien.html"):
    return ('<div class="cta-inline"><p>%s</p><div class="btn-row">%s'
            '<a class="btn btn--ghost" href="%s">%s</a></div></div>'
            % (text, phone_link("Appeler", classes="btn btn--dark"), href, esc(label)))


def link_cloud(links):
    lis = "".join('<li><a href="%s">%s</a></li>' % (h, esc(l)) for l, h in links)
    return '<ul class="link-cloud">%s</ul>' % lis


LEAFLET_LOCAL_JS = "assets/vendor/leaflet/leaflet.js"
LEAFLET_LOCAL_CSS = "assets/vendor/leaflet/leaflet.css"
LEAFLET_CDN_JS = "https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
LEAFLET_CDN_CSS = "https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"


def leaflet_sources():
    """Utilise une copie locale de Leaflet si elle existe, sinon le CDN.

    Pour supprimer toute requete vers un tiers, executer :
        bash tools/vendor-leaflet.sh
    puis relancer le build.
    """
    if (os.path.exists(os.path.join(ROOT, LEAFLET_LOCAL_JS))
            and os.path.exists(os.path.join(ROOT, LEAFLET_LOCAL_CSS))):
        return "/" + LEAFLET_LOCAL_CSS, "/" + LEAFLET_LOCAL_JS
    return LEAFLET_CDN_CSS, LEAFLET_CDN_JS


def map_block(points, height_note=True):
    data = esc(json.dumps(points, ensure_ascii=False))
    css_src, js_src = leaflet_sources()
    note = ('<ul class="map-legend"><li><span class="dot"></span> Départements et villes '
            "couverts par Electricien Richard</li></ul>") if height_note else ""
    return (
        '<div class="map-wrap"><div id="map" data-points="%s" data-css="%s" data-js="%s" '
        'role="application" aria-label="Carte des zones d\'intervention">'
        '<p class="map-fallback">Chargement de la carte des zones d\'intervention…</p>'
        "</div></div>%s" % (data, esc(css_src), esc(js_src), note)
    )


# ------------------------------------------------------------ JSON-LD ------
BUSINESS_ID = SITE["base_url"] + "/#electricien-richard"
WEBSITE_ID = SITE["base_url"] + "/#website"


def business_node(area_served=None):
    node = {
        "@type": "Electrician",
        "@id": BUSINESS_ID,
        "name": SITE["name"],
        "url": SITE["base_url"] + "/",
        "description": SITE["description_courte"],
        "image": abs_url(SITE["og_default"]),
        "logo": abs_url(SITE["logo"]),
        "priceRange": "$$",
    }
    if has_phone():
        node["telephone"] = SITE.get("phone_e164", SITE["phone_tel"])
    if not SITE["email_is_placeholder"]:
        node["email"] = SITE["email"]
    if SITE["address"]:
        a = SITE["address"]
        node["address"] = {
            "@type": "PostalAddress",
            "streetAddress": a["street"],
            "postalCode": a["postal_code"],
            "addressLocality": a["city"],
            "addressRegion": a.get("region", ""),
            "addressCountry": "FR",
        }
    if SITE["geo"]:
        node["geo"] = {"@type": "GeoCoordinates",
                       "latitude": SITE["geo"]["lat"], "longitude": SITE["geo"]["lon"]}
    if SITE["opening_hours"]:
        node["openingHoursSpecification"] = SITE["opening_hours"]
    if SITE["social"]:
        node["sameAs"] = SITE["social"]
    node["areaServed"] = area_served or [
        {"@type": "AdministrativeArea", "name": n}
        for n in ["Côtes-d'Armor", "Finistère", "Ille-et-Vilaine",
                  "Morbihan", "Loire-Atlantique", "Maine-et-Loire"]
    ]
    return node


def website_node():
    return {
        "@type": "WebSite",
        "@id": WEBSITE_ID,
        "url": SITE["base_url"] + "/",
        "name": SITE["name"],
        "inLanguage": "fr-FR",
        "publisher": {"@id": BUSINESS_ID},
    }


def breadcrumb_node(trail, page_url):
    items = []
    for i, (label, href) in enumerate(trail, start=1):
        entry = {"@type": "ListItem", "position": i, "name": label}
        entry["item"] = abs_url(href) if href else abs_url(page_url)
        items.append(entry)
    return {"@type": "BreadcrumbList",
            "@id": abs_url(page_url) + "#breadcrumb", "itemListElement": items}


def faq_node(items, page_url):
    return {
        "@type": "FAQPage",
        "@id": abs_url(page_url) + "#faq",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer",
                                "text": re.sub(r"<[^>]+>", " ", a).replace("&nbsp;", " ").strip()}}
            for q, a in items
        ],
    }


def breadcrumb_html(trail):
    lis = []
    for label, href in trail:
        if href:
            lis.append('<li><a href="%s">%s</a></li>' % (href, esc(label)))
        else:
            lis.append('<li><span aria-current="page">%s</span></li>' % esc(label))
    return ('<nav class="breadcrumb" aria-label="Fil d\'Ariane"><div class="container">'
            "<ol>%s</ol></div></nav>" % "".join(lis))


# ------------------------------------------------------------- layout ------
NAV_LINKS = [
    ("Électricien", "/electricien.html"),
    ("Dépannage", "/electricien-depannage.html"),
    ("Urgence", "/electricien-urgence.html"),
    ("Installation", "/installation-electrique.html"),
    ("Rénovation", "/renovation-electrique.html"),
    ("Zones", "/zones-d-intervention.html"),
    ("Tarifs", "/tarifs.html"),
    ("Blog", "/blog/"),
    ("Contact", "/contact.html"),
]

# ---------------------------------------------------------------- marque ---
LOGO_DIR = "assets/images/logo"
MARQUE_SVG_PATH = os.path.join(LOGO_DIR, "electricien-richard-marque.svg")


def _lire_marque():
    """Marque vectorielle inline : une seule source de verite, aucun requete HTTP."""
    chemin = os.path.join(ROOT, MARQUE_SVG_PATH)
    if os.path.exists(chemin):
        svg = open(chemin, encoding="utf-8").read()
        svg = re.sub(r"<\?xml.*?\?>|<!--.*?-->", "", svg, flags=re.S)
        return svg.strip()
    return ""


MARQUE = _lire_marque()
# Version pour fonds sombres : les elements anthracite passent en blanc,
# sans quoi le R, le cable et la prise disparaissent dans le pied de page.
MARQUE_INVERSE = MARQUE.replace("#111827", "#FFFFFF")


def svg_dimensions(path):
    """Largeur/hauteur d'un SVG, depuis les attributs ou le viewBox."""
    try:
        head = open(path, encoding="utf-8").read(1200)
    except Exception:                                   # noqa: BLE001
        return None
    w = re.search(r'\swidth="([\d.]+)', head)
    h = re.search(r'\sheight="([\d.]+)', head)
    if w and h:
        return float(w.group(1)), float(h.group(1))
    vb = re.search(r'viewBox="[\d.\-]+\s+[\d.\-]+\s+([\d.]+)\s+([\d.]+)"', head)
    if vb:
        return float(vb.group(1)), float(vb.group(2))
    return None


def logo_fichier():
    """Logo fourni par le client, s'il a ete depose. Prioritaire sur la marque."""
    for ext in ("svg", "webp", "png", "jpg"):
        rel = "%s/electricien-richard-logo.%s" % (LOGO_DIR, ext)
        if os.path.exists(os.path.join(ROOT, rel)):
            return rel
    return None


def brand_lockup(hauteur=42, inverse=False):
    """Bloc de marque de l'en-tete et du pied de page.

    Si le logo complet du client est present dans assets/images/logo/, il est
    utilise tel quel. Sinon, la marque vectorielle est affichee a cote du nom,
    compose en texte reel (lisible par les moteurs et les lecteurs d'ecran).
    """
    fichier = logo_fichier()
    if fichier:
        dims = (svg_dimensions(os.path.join(ROOT, fichier)) if fichier.endswith(".svg")
                else webp_size(os.path.join(ROOT, fichier)))
        attrs = ""
        if dims:
            ratio = dims[0] / dims[1]
            attrs = ' width="%d" height="%d"' % (round(hauteur * ratio), hauteur)
        return ('<img class="brand-logo" src="/%s" alt="Electricien Richard"%s '
                'decoding="async">' % (fichier, attrs))

    cls = " brand-text--inverse" if inverse else ""
    return (
        '<span class="brand-mark" aria-hidden="true">%s</span>'
        '<span class="brand-text%s"><span class="brand-l1">ÉLECTRICIEN</span>'
        '<span class="brand-l2">RICHARD</span>'
        '<span class="brand-l3">Dépannage · Installation · Rénovation</span></span>'
        % (MARQUE_INVERSE if inverse else MARQUE, cls))


def header(current_url):
    nav_items = []
    for label, href in NAV_LINKS:
        cur = ' aria-current="page"' if href == current_url else ""
        nav_items.append('<li><a href="%s"%s>%s</a></li>' % (href, cur, esc(label)))
    return """
<a class="skip-link" href="#main">Aller au contenu principal</a>
<div class="topbar"><div class="container">
  <span>%s <strong>Intervention en Bretagne et en Pays de la Loire</strong> — 22 · 29 · 35 · 56 · 44 · 49</span>
  <span>Un besoin urgent ? <a href="tel:%s">%s</a></span>
</div></div>
<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="/" aria-label="Electricien Richard, accueil">%s</a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">
      %s<span>Menu</span>
    </button>
    <nav class="nav" id="site-nav" aria-label="Navigation principale">
      <ul>%s</ul>
      <div class="nav-cta">%s<a class="btn btn--ghost" href="/devis-electricien.html">Demander un devis</a></div>
    </nav>
    <a class="btn btn--primary btn--sm header-cta" href="tel:%s">%s %s</a>
  </div>
</header>""" % (
        icon("map", 16), SITE["phone_tel"], SITE["phone_display"], brand_lockup(44),
        icon("bolt", 18) if False else
        '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2.4" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
        "".join(nav_items), phone_link(classes="btn btn--primary"),
        SITE["phone_tel"], icon("phone", 18), SITE["phone_display"])


FOOTER_SERVICES = [
    ("Dépannage électrique", "/electricien-depannage.html"),
    ("Électricien en urgence", "/electricien-urgence.html"),
    ("Recherche de panne", "/recherche-panne.html"),
    ("Installation électrique", "/installation-electrique.html"),
    ("Rénovation électrique", "/renovation-electrique.html"),
    ("Mise aux normes", "/mise-aux-normes-electrique.html"),
    ("Tableau électrique", "/tableau-electrique.html"),
    ("Borne de recharge", "/borne-recharge.html"),
]

FOOTER_ZONES = [
    ("Côtes-d'Armor (22)", "/zones/cotes-d-armor/"),
    ("Finistère (29)", "/zones/finistere/"),
    ("Ille-et-Vilaine (35)", "/zones/ille-et-vilaine/"),
    ("Morbihan (56)", "/zones/morbihan/"),
    ("Loire-Atlantique (44)", "/zones/loire-atlantique/"),
    ("Maine-et-Loire (49)", "/zones/maine-et-loire/"),
]

FOOTER_INFO = [
    ("À propos", "/a-propos.html"),
    ("Tarifs et devis", "/tarifs.html"),
    ("Questions fréquentes", "/faq.html"),
    ("Zones d'intervention", "/zones-d-intervention.html"),
    ("Blog", "/blog/"),
    ("Contact", "/contact.html"),
]


def footer():
    def ul(links):
        return "".join('<li><a href="%s">%s</a></li>' % (h, esc(l)) for l, h in links)

    contact_bits = ['<a href="tel:%s">%s</a>' % (SITE["phone_tel"], SITE["phone_display"])]
    return """
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="brand brand--footer" href="/" aria-label="Electricien Richard, accueil">%s</a>
        <p>Artisan électricien intervenant chez les particuliers, les commerces et les
        professionnels dans les Côtes-d'Armor, le Finistère, l'Ille-et-Vilaine, le Morbihan,
        la Loire-Atlantique et le Maine-et-Loire.</p>
        <p class="footer-contact"><strong>%s</strong></p>
      </div>
      <div><h2>Prestations</h2><ul>%s</ul></div>
      <div><h2>Départements</h2><ul>%s</ul></div>
      <div><h2>Informations</h2><ul>%s</ul></div>
    </div>
    <div class="footer-bottom">
      <span>© %s Electricien Richard — electricien-richard.fr</span>
      <ul>
        <li><a href="/mentions-legales.html">Mentions légales</a></li>
        <li><a href="/politique-de-confidentialite.html">Politique de confidentialité</a></li>
        <li><a href="/plan-du-site.html">Plan du site</a></li>
      </ul>
    </div>
  </div>
</footer>
<nav class="sticky-cta" aria-label="Contact rapide">
  <a class="btn btn--primary" href="tel:%s" aria-label="Appeler le %s">%s
    <span class="sticky-num">%s</span><span class="sticky-short">Appeler</span></a>
  <a class="btn btn--dark" href="/devis-electricien.html">Demander un devis</a>
</nav>""" % (brand_lockup(40, inverse=True), "".join(contact_bits), ul(FOOTER_SERVICES), ul(FOOTER_ZONES),
             ul(FOOTER_INFO), 2026, SITE["phone_tel"], SITE["phone_display"],
             icon("phone", 18), SITE["phone_display"])


FONT_DIR = "assets/fonts"


def font_head():
    """Police auto-hebergee si presente dans /assets/fonts, sinon Google Fonts.

    Deposer inter-400.woff2, inter-600.woff2, inter-700.woff2, inter-800.woff2
    dans assets/fonts/ supprime toute requete vers un tiers, ameliore le LCP et
    permet de retirer la mention Google Fonts de la politique de confidentialite.
    """
    poids = [("400", "normal"), ("600", "normal"), ("700", "normal"), ("800", "normal")]
    locaux = [(w, st) for w, st in poids
              if os.path.exists(os.path.join(ROOT, FONT_DIR, "inter-%s.woff2" % w))]
    if len(locaux) == len(poids):
        faces = "".join(
            "@font-face{font-family:Inter;font-style:%s;font-weight:%s;font-display:swap;"
            "src:url(/%s/inter-%s.woff2) format('woff2')}" % (st, w, FONT_DIR, w)
            for w, st in locaux)
        return ('<link rel="preload" as="font" type="font/woff2" '
                'href="/%s/inter-400.woff2" crossorigin>\n<style>%s</style>'
                % (FONT_DIR, faces))
    href = ("https://fonts.googleapis.com/css2?"
            "family=Inter:wght@400;600;700;800;900&display=swap")
    return (
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '<link rel="preload" as="style" href="%s">\n'
        '<link rel="stylesheet" href="%s" media="print" onload="this.media=\'all\'">\n'
        '<noscript><link rel="stylesheet" href="%s"></noscript>' % (href, href, href))


PAGE_TPL = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
{robots}<meta name="theme-color" content="{theme}">
<meta name="author" content="{site_name}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{site_name}">
<meta property="og:locale" content="fr_FR">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{og_title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{og_image}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/assets/images/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/assets/images/apple-touch-icon.png">
{fonts}
<link rel="stylesheet" href="/assets/css/style.css">
<script type="application/ld+json">{jsonld}</script>
</head>
<body>
{header}
{breadcrumb}
<main id="main">
{content}
</main>
{footer}
<script src="/assets/js/site.js" defer></script>
</body>
</html>
"""


def resolve_og(og_image):
    """N'utilise une image de partage que si le fichier existe reellement."""
    if og_image:
        candidate = og_image.lstrip("/")
        if os.path.exists(os.path.join(ROOT, candidate)):
            return "/" + candidate
    return SITE["og_default"]


def render_page(path, title, description, content, trail=None, schema_nodes=None,
                og_type="website", og_image=None, noindex=False, og_title=None):
    page_url = url_for(path)
    graph = [business_node(), website_node(), {
        "@type": "WebPage",
        "@id": abs_url(page_url) + "#webpage",
        "url": abs_url(page_url),
        "name": title,
        "description": description,
        "inLanguage": "fr-FR",
        "isPartOf": {"@id": WEBSITE_ID},
        "about": {"@id": BUSINESS_ID},
    }]
    if trail:
        graph.append(breadcrumb_node(trail, page_url))
        graph[2]["breadcrumb"] = {"@id": abs_url(page_url) + "#breadcrumb"}
    if schema_nodes:
        graph.extend(schema_nodes)

    return PAGE_TPL.format(
        fonts=font_head(),
        title=esc(title),
        og_title=esc(og_title or title),
        description=esc(description),
        canonical=abs_url(page_url),
        robots='<meta name="robots" content="noindex, follow">\n' if noindex
               else '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">\n',
        theme=SITE["theme_color"],
        site_name=esc(SITE["name"]),
        og_type=og_type,
        og_image=abs_url(resolve_og(og_image)),
        jsonld=json.dumps({"@context": "https://schema.org", "@graph": graph},
                          ensure_ascii=False, separators=(",", ":")),
        header=header(page_url if not path.endswith("index.html") else page_url),
        breadcrumb=breadcrumb_html(trail) if trail else "",
        content=content,
        footer=footer(),
    )
