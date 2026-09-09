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


# =========================================================================
# PHOTOS REELLES FOURNIES PAR LE CLIENT
# -------------------------------------------------------------------------
# Chaque constante ci-dessous correspond a une photo reelle d'intervention.
# Le nom de fichier est definitif : deposer la photo a ce chemin exact, puis
# relancer `python3 tools/build.py`. Les ALT decrivent ce que montre
# reellement la photo (verifie visuellement, aucun mot-cle ajoute).
# Format conseille : WebP, ratio 3/2, 1600 px de large minimum.
# =========================================================================

PHOTO_LED_CUISINE = "assets/images/eclairage/installation-bandeau-led-cuisine.webp"
PHOTO_LED_PLAFOND = "assets/images/eclairage/installation-eclairage-led-plafond-chambre.webp"
PHOTO_AMPOULE_SALON = "assets/images/eclairage/remplacement-ampoule-luminaire-salon.webp"
PHOTO_APPAREILLAGE_MUR = "assets/images/prises/raccordement-prises-interrupteurs-mur.webp"
PHOTO_POSE_PRISE = "assets/images/prises/installation-prise-courant-sejour.webp"
PHOTO_COMPTEUR_LINKY = ("assets/images/tableau-electrique/"
                        "intervention-disjoncteur-branchement-compteur.webp")

# Regle : une photo = un seul emplacement. Aucune photo n'est reutilisee
# a plusieurs endroits du site.


def slot(file, alt, width=1200, height=800, caption=None, sujet=None):
    return {"file": file, "alt": alt, "width": width, "height": height,
            "caption": caption, "sujet": sujet}


IMAGES = {
    # ---- Accueil ----------------------------------------------------------
    # ---- PHOTO REELLE : cuisine, pose d'un bandeau LED sous meubles hauts
    "hero": slot(
        PHOTO_LED_CUISINE,
        "Électricien fixant un bandeau LED sous les meubles hauts d'une cuisine",
        1536, 1024,
        sujet="Cuisine grise, plan de travail bois : pose d'un ruban LED sous meubles hauts"),
    # ---- Galerie d'accueil : emplacements dedies.
    # Aucune photo deja affectee a une page de prestation n'y est reprise :
    # la galerie attend ses propres prises de vue. La section entiere reste
    # masquee tant qu'aucune photo n'y est deposee.
    "home_gallery_1": slot(
        "assets/images/interventions/electricien-chantier-renovation.webp",
        "Électricien au travail sur un chantier de rénovation", 1200, 800,
        sujet="PHOTO ATTENDUE : vue d'ensemble d'un chantier en cours"),
    "home_gallery_2": slot(
        "assets/images/depannage/recherche-panne-mesure-isolement.webp",
        "Mesure d'isolement d'un circuit à l'aide d'un contrôleur", 1200, 800,
        "La mesure d'isolement permet de localiser un défaut sans démonter.",
        sujet="PHOTO ATTENDUE : appareil de mesure en main sur un circuit"),
    "home_gallery_3": slot(
        "assets/images/installation/installation-electrique-cablage-circuits.webp",
        "Câblage de circuits électriques avant fermeture des cloisons", 1200, 800,
        "Les cheminements se préparent avant la fermeture des cloisons.",
        sujet="PHOTO ATTENDUE : gaines et conducteurs avant fermeture des cloisons"),
    "home_gallery_4": slot(
        "assets/images/renovation/renovation-electrique-maison-ancienne.webp",
        "Reprise de l'installation électrique dans une maison ancienne", 1200, 800,
        sujet="PHOTO ATTENDUE : rénovation dans du bâti ancien"),
    "home_gallery_5": slot(
        "assets/images/bornes/installation-borne-recharge-vehicule-electrique.webp",
        "Borne de recharge murale installée dans un garage", 1200, 800,
        "Point de recharge raccordé sur un circuit dédié.",
        sujet="PHOTO ATTENDUE : borne de recharge posée en garage ou en façade"),
    "home_gallery_6": slot(
        "assets/images/tableau-electrique/remplacement-tableau-electrique-chantier.webp",
        "Électricien intervenant sur un tableau électrique", 1200, 800,
        "Remplacement d'un tableau : chaque circuit est repéré avant raccordement.",
        sujet="PHOTO ATTENDUE : tableau électrique ouvert pendant l'intervention"),
    "before": slot(
        "assets/images/avant-apres/tableau-electrique-avant-renovation.webp",
        "Ancien tableau électrique équipé de fusibles avant remplacement",
        1000, 750,
        sujet="PHOTO ATTENDUE : tableau ancien AVANT travaux, vue de face, porte ouverte"),
    "after": slot(
        "assets/images/avant-apres/tableau-electrique-apres-renovation.webp",
        "Tableau électrique neuf après remplacement, circuits repérés",
        1000, 750,
        sujet="PHOTO ATTENDUE : le MÊME tableau APRÈS travaux, même cadrage"),
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
        "Passage de nouveaux circuits lors d'une rénovation électrique", 1200, 800,
        sujet="PHOTO ATTENDUE : passage de gaines ou saignées en rénovation"),
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
        PHOTO_COMPTEUR_LINKY,
        "Électricien intervenant sur le disjoncteur de branchement d'un coffret "
        "extérieur équipé d'un compteur Linky",
        1536, 1152,
        "Le disjoncteur de branchement, situé en amont du tableau, protège "
        "l'installation dans son ensemble. Toute intervention à ce niveau se fait "
        "avec casque, gants isolants et outillage isolé."),
    "svc_court-circuit": slot(
        "assets/images/depannage/court-circuit-connexion-endommagee.webp",
        "Connexion électrique endommagée à l'origine d'un défaut", 1200, 800),
    "svc_prise-electrique": slot(
        PHOTO_POSE_PRISE,
        "Électricien installant une prise de courant dans un séjour",
        1536, 1024,
        "Pose d'une prise : le conducteur de protection est raccordé au mécanisme."),
    "svc_interrupteur": slot(
        PHOTO_APPAREILLAGE_MUR,
        "Électricien raccordant une rangée de prises et d'interrupteurs encastrés",
        1536, 1024,
        "Raccordement de l'appareillage : chaque conducteur est repéré avant serrage."),
    "svc_eclairage": slot(
        PHOTO_LED_PLAFOND,
        "Électricien posant un ruban LED dans une corniche de plafond, dans une chambre",
        1536, 1024,
        "Éclairage indirect par ruban LED : la source reste invisible, seule la lumière "
        "réfléchie éclaire la pièce."),
    "svc_luminaire": slot(
        PHOTO_AMPOULE_SALON,
        "Électricien remplaçant l'ampoule d'une suspension au plafond d'un salon",
        1536, 1024,
        "Toute intervention sur un point lumineux se fait circuit coupé, "
        "après vérification de l'absence de tension."),
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
