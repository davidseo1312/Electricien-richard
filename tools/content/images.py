# -*- coding: utf-8 -*-
"""
Manifeste des photos du site.

Principe : chaque emplacement de photo est declare ici avec son nom de fichier
attendu, son texte alternatif, ses dimensions et sa legende.

- Si le fichier existe dans /assets/images/... -> une vraie balise <img> est
  generee (avec srcset si des variantes -480w / -800w / -1200w / -1600w existent).
- Sinon -> un emplacement neutre est affiche. Aucune image d'illustration n'est
  inventee et aucune photo n'est simulee.

Pour ajouter une photo reelle : deposer le fichier au chemin indique, puis
relancer `python3 tools/build.py`. Rien d'autre a modifier.
La liste des fichiers attendus est regeneree a chaque build dans
PHOTOS-A-FOURNIR.md.

Les ALT decrivent la photo attendue. Ils doivent etre ajustes si la photo
reellement fournie montre autre chose : un ALT doit decrire l'image, pas
contenir des mots-cles.
"""


def slot(file, alt, width=1200, height=800, caption=None):
    return {"file": file, "alt": alt, "width": width, "height": height, "caption": caption}


IMAGES = {
    # ---- Accueil ----------------------------------------------------------
    "hero": slot(
        "assets/images/electricien/electricien-richard-intervention-tableau-electrique.webp",
        "Électricien raccordant les circuits d'un tableau électrique",
        1400, 1000),
    "home_gallery_1": slot(
        "assets/images/tableau-electrique/tableau-electrique-neuf-apres-remplacement.webp",
        "Tableau électrique neuf avec disjoncteurs et interrupteurs différentiels repérés",
        1200, 800,
        "Tableau remplacé et repéré : chaque protection est identifiée."),
    "home_gallery_2": slot(
        "assets/images/depannage/recherche-panne-mesure-isolement.webp",
        "Mesure d'isolement d'un circuit à l'aide d'un contrôleur",
        1200, 800,
        "La mesure d'isolement permet de localiser un défaut sans démonter."),
    "home_gallery_3": slot(
        "assets/images/installation/installation-electrique-cablage-circuits.webp",
        "Câblage de circuits électriques avant fermeture des cloisons",
        1200, 800,
        "Les cheminements se préparent avant la fermeture des cloisons."),
    "home_gallery_4": slot(
        "assets/images/renovation/renovation-electrique-maison-ancienne.webp",
        "Reprise de l'installation électrique dans une maison ancienne",
        1200, 800,
        "Rénovation dans le bâti ancien : le passage des circuits conditionne le chantier."),
    "home_gallery_5": slot(
        "assets/images/bornes/installation-borne-recharge-vehicule-electrique.webp",
        "Borne de recharge murale installée dans un garage",
        1200, 800,
        "Point de recharge raccordé sur un circuit dédié."),
    "home_gallery_6": slot(
        "assets/images/interventions/electricien-intervention-chantier.webp",
        "Électricien au travail sur un chantier de rénovation",
        1200, 800,
        "Interventions chez les particuliers, les commerces et les professionnels."),
    "before": slot(
        "assets/images/tableau-electrique/tableau-electrique-avant-renovation.webp",
        "Ancien tableau électrique équipé de fusibles avant remplacement",
        1000, 750),
    "after": slot(
        "assets/images/tableau-electrique/tableau-electrique-apres-renovation.webp",
        "Tableau électrique neuf après remplacement, circuits repérés",
        1000, 750),
    "about": slot(
        "assets/images/electricien/electricien-richard-vehicule-intervention.webp",
        "Véhicule d'intervention d'Electricien Richard",
        1200, 800),

    # ---- Pages de services ------------------------------------------------
    "svc_electricien": slot(
        "assets/images/electricien/electricien-travaux-electriques.webp",
        "Électricien réalisant des travaux électriques dans un logement", 1200, 800),
    "svc_electricien-urgence": slot(
        "assets/images/depannage/depannage-electrique-urgence-tableau.webp",
        "Intervention sur un tableau électrique lors d'un dépannage", 1200, 800),
    "svc_electricien-depannage": slot(
        "assets/images/depannage/depannage-electrique-diagnostic-circuit.webp",
        "Contrôle d'un circuit électrique lors d'un dépannage", 1200, 800),
    "svc_panne-electrique": slot(
        "assets/images/depannage/panne-electrique-verification-tableau.webp",
        "Vérification des protections d'un tableau après une panne", 1200, 800),
    "svc_recherche-panne": slot(
        "assets/images/depannage/recherche-panne-electrique-mesure.webp",
        "Recherche de panne électrique avec appareil de mesure", 1200, 800),
    "svc_installation-electrique": slot(
        "assets/images/installation/installation-electrique-neuve-tableau.webp",
        "Installation électrique neuve en cours de raccordement", 1200, 800),
    "svc_renovation-electrique": slot(
        "assets/images/renovation/renovation-electrique-passage-circuits.webp",
        "Passage de nouveaux circuits lors d'une rénovation électrique", 1200, 800),
    "svc_mise-aux-normes-electrique": slot(
        "assets/images/renovation/mise-aux-normes-electrique-tableau.webp",
        "Mise en sécurité d'une installation électrique ancienne", 1200, 800),
    "svc_diagnostic-electrique": slot(
        "assets/images/interventions/diagnostic-electrique-controle-installation.webp",
        "Contrôle d'une installation électrique lors d'un diagnostic", 1200, 800),
    "svc_tableau-electrique": slot(
        "assets/images/tableau-electrique/remplacement-tableau-electrique.webp",
        "Remplacement d'un tableau électrique", 1200, 800),
    "svc_disjoncteur": slot(
        "assets/images/tableau-electrique/disjoncteur-tableau-electrique.webp",
        "Disjoncteurs divisionnaires sur un tableau électrique", 1200, 800),
    "svc_court-circuit": slot(
        "assets/images/depannage/court-circuit-connexion-endommagee.webp",
        "Connexion électrique endommagée à l'origine d'un défaut", 1200, 800),
    "svc_prise-electrique": slot(
        "assets/images/prises/installation-prise-electrique.webp",
        "Pose d'une prise de courant avec conducteur de protection", 1200, 800),
    "svc_interrupteur": slot(
        "assets/images/prises/remplacement-interrupteur.webp",
        "Remplacement d'un interrupteur mural", 1200, 800),
    "svc_eclairage": slot(
        "assets/images/eclairage/installation-eclairage-interieur.webp",
        "Installation d'un éclairage intérieur", 1200, 800),
    "svc_luminaire": slot(
        "assets/images/eclairage/installation-luminaire-plafond.webp",
        "Pose et raccordement d'un luminaire au plafond", 1200, 800),
    "svc_borne-recharge": slot(
        "assets/images/bornes/borne-recharge-installation-maison.webp",
        "Borne de recharge pour véhicule électrique installée en maison individuelle",
        1200, 800),
    "svc_vmc": slot(
        "assets/images/installation/raccordement-electrique-vmc.webp",
        "Raccordement électrique d'un caisson de VMC", 1200, 800),
    "svc_electricien-particulier": slot(
        "assets/images/interventions/electricien-intervention-logement.webp",
        "Intervention électrique dans un logement", 1200, 800),
    "svc_electricien-entreprise": slot(
        "assets/images/interventions/electricien-local-professionnel.webp",
        "Travaux électriques dans un local professionnel", 1200, 800),
    "svc_tarifs": slot(
        "assets/images/interventions/devis-travaux-electriques.webp",
        "Établissement d'un devis de travaux électriques", 1200, 800),
}


def dept_image(dept_slug, dept_name):
    """Photo d'illustration d'une page departement."""
    return slot(
        "assets/images/zones/electricien-%s-intervention.webp" % dept_slug,
        "Intervention électrique en %s" % dept_name, 1200, 800)


def city_image(city_slug, city_name):
    """Photo d'illustration d'une page ville."""
    return slot(
        "assets/images/zones/%s-intervention.webp" % city_slug,
        "Intervention électrique à %s" % city_name, 1200, 800)


def blog_image(article):
    return slot(
        "assets/images/blog/%s.webp" % article["slug"],
        article["h1"], 1200, 675)


def get(key):
    return IMAGES[key]
