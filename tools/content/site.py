# -*- coding: utf-8 -*-
"""
Configuration centrale du site electricien-richard.fr

>>> IMPORTANT <<<
Les valeurs marquees "A_COMPLETER" sont des donnees d'entreprise qui ne peuvent
pas etre inventees (numero, adresse, SIRET, avis, tarifs, horaires reels).
Elles doivent etre remplacees par les informations reelles AVANT mise en ligne.
Le numero par defaut appartient a la plage 06 39 98 XX XX reservee par l'ARCEP
a la fiction : il n'appartient a personne et ne peut donc joindre un tiers.
Tant qu'une valeur reste marquee comme placeholder, elle n'est PAS injectee
dans les donnees structurees (pour ne jamais declarer de fausse information a
Google).
"""

SITE = {
    "name": "Electricien Richard",
    "legal_name": "Electricien Richard",          # A_COMPLETER : raison sociale exacte
    "domain": "electricien-richard.fr",
    "base_url": "https://electricien-richard.fr",
    "lang": "fr",
    "locale": "fr_FR",
    "tagline": "Electricien professionnel en Bretagne et Pays de la Loire",
    "description_courte": (
        "Electricien Richard intervient pour le depannage, l'installation, "
        "la renovation et la mise aux normes electriques dans les Cotes-d'Armor, "
        "le Finistere, l'Ille-et-Vilaine, le Morbihan, la Loire-Atlantique "
        "et le Maine-et-Loire."
    ),

    # --- Contact ---------------------------------------------------------
    "phone_display": "02 20 06 00 75",
    # Lien tel: en format national (demande explicite du client).
    "phone_tel": "0220060075",
    # Format E.164 reserve aux donnees structurees (recommandation schema.org).
    "phone_e164": "+33220060075",
    "phone_is_placeholder": False,
    "email": "contact@electricien-richard.fr",   # A_COMPLETER : creer la boite reelle
    "email_is_placeholder": True,

    # --- Identite legale (mentions legales uniquement) --------------------
    # ATTENTION : ces donnees alimentent UNIQUEMENT la page mentions legales.
    # Elles ne sont volontairement PAS injectees comme adresse du LocalBusiness
    # (voir "address" plus bas et le README) : le siege social se situe hors des
    # six departements desservis, l'y declarer brouillerait le referencement local.
    # A VERIFIER par l'exploitant avant publication definitive.
    "legal": {
        "exploitant": "ASSOUL BILAL",
        "forme": "Entrepreneur individuel",
        "siren": "901 133 041",
        "siret": "901 133 041 00011",
        "ape_code": "81.29A",
        "ape_label": "Autres activités de nettoyage n.c.a. "
                     "(désinfection, désinsectisation, dératisation)",
        "rcs": "901 133 041 R.C.S. Nanterre",
        "adresse_siege": "1 rue Albert Simonin, 92400 Courbevoie",
        "tva": None,          # A_COMPLETER : numero de TVA intracommunautaire
        "directeur_publication": "ASSOUL BILAL",
        "source": "https://www.pappers.fr/entreprise/assoul-bilal-901133041",
        # Le code APE enregistre ne couvre pas les travaux d'electricite :
        # a faire modifier aupres de l'INSEE, et verifier que l'assurance
        # (RC pro + decennale) couvre bien l'activite d'electricien.
        "ape_coherent": False,
    },

    # --- Etablissement ---------------------------------------------------
    # Laisser a None tant que l'adresse reelle n'est pas connue :
    # aucune adresse ne sera publiee ni declaree en JSON-LD.
    "address": None,   # ex. {"street": "...", "postal_code": "...", "city": "...", "region": "Bretagne"}
    "geo": None,       # ex. {"lat": 48.1173, "lon": -1.6778}
    "siret": None,     # A_COMPLETER
    "rcs": None,       # A_COMPLETER
    "assurance": None, # A_COMPLETER : assureur + n. de police RC pro / decennale
    "hebergeur": None, # A_COMPLETER : nom + adresse de l'hebergeur (mentions legales)

    # --- Horaires : uniquement s'ils sont reels --------------------------
    # None => aucun horaire affiche, aucun openingHours en JSON-LD.
    "opening_hours": None,

    # --- Reseaux sociaux : uniquement les profils reellement existants ---
    "social": [],      # ex. ["https://www.facebook.com/..."]

    # --- Formulaires -----------------------------------------------------
    # Endpoint de traitement du formulaire (service type Formspree, Netlify Forms,
    # ou script cote serveur). Tant qu'il vaut None, le formulaire bascule sur un
    # envoi par messagerie (mailto) afin de rester fonctionnel sans backend.
    "form_action": None,   # A_COMPLETER : ex. "https://formspree.io/f/xxxxxxx"

    # --- Identite visuelle ----------------------------------------------
    "logo": "/assets/images/electricien-richard-logo.svg",
    "og_default": "/assets/images/og/electricien-richard-og.png",
    "theme_color": "#FACC15",
}

# Les 6 seuls departements couverts. Toute page geographique DOIT appartenir
# a l'un d'eux. Le build echoue si une ville reference un autre departement.
DEPARTEMENTS_AUTORISES = {"22", "29", "35", "56", "44", "49"}


def has_phone():
    return not SITE["phone_is_placeholder"]


def has_real_nap():
    """True seulement si le trio Nom / Adresse / Telephone est reellement connu."""
    return has_phone() and SITE["address"] is not None
