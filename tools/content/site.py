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
    # Ces donnees alimentent UNIQUEMENT la page mentions legales ; elles ne sont
    # jamais injectees dans les donnees structurees.
    #
    # >>> A COMPLETER AVANT MISE EN LIGNE PUBLIQUE <<<
    # L'article 6-III de la loi pour la confiance dans l'economie numerique
    # impose d'identifier l'editeur du site : denomination, forme juridique,
    # adresse, numero d'immatriculation (SIREN/SIRET), et nom du directeur de
    # la publication. Tant que ces champs valent None, la page affiche un
    # marqueur "a completer" visible plutot qu'une information inventee.
    "legal": {
        # Nom commercial sous lequel l'activite est presentee au public.
        "exploitant": "Electricien Richard",
        "forme": None,                 # A_COMPLETER : ex. "Entrepreneur individuel"
        "siren": None,                 # A_COMPLETER
        "siret": None,                 # A_COMPLETER
        "ape_code": None,              # A_COMPLETER
        "ape_label": None,             # A_COMPLETER
        "rcs": None,                   # A_COMPLETER : greffe d'immatriculation
        "adresse_siege": None,         # A_COMPLETER : adresse du siege social
        "tva": None,                   # A_COMPLETER : TVA intracommunautaire
        "directeur_publication": None, # A_COMPLETER : personne physique responsable
        "ape_coherent": True,
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
    "logo": "/assets/images/logo/electricien-richard-logo-512.png",
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
