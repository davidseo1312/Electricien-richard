# -*- coding: utf-8 -*-
"""
Silo geographique : 6 departements STRICTEMENT (22, 29, 35, 56, 44, 49).
Aucun departement voisin ne doit etre ajoute ici (le build echoue sinon).
Chaque ville dispose d'un contenu redige specifiquement : contexte local,
type d'habitat, besoins electriques frequents, FAQ locale.
Aucune donnee non verifiable (delai d'intervention, tarif, avis) n'y figure.
"""

DEPARTEMENTS = [
    # =====================================================================
    {
        "code": "22",
        "name": "Côtes-d'Armor",
        "slug": "cotes-d-armor",
        "prep": "dans les Côtes-d'Armor",
        "prefecture": "Saint-Brieuc",
        "lat": 48.45, "lon": -2.85,
        "title": "Électricien Côtes-d'Armor (22) — Dépannage, installation, rénovation",
        "desc": ("Électricien dans les Côtes-d'Armor : dépannage électrique, recherche de panne, "
                 "installation, rénovation et mise aux normes à Saint-Brieuc, Lannion, Dinan, "
                 "Guingamp et Lamballe-Armor."),
        "h1": "Électricien dans les Côtes-d'Armor (22)",
        "chapo": ("Electricien Richard intervient dans l'ensemble des Côtes-d'Armor, de la baie "
                  "de Saint-Brieuc au Trégor et à la vallée de la Rance, pour le dépannage "
                  "électrique, l'installation, la rénovation et la mise en sécurité des "
                  "installations."),
        "contexte": """
<p>Les Côtes-d'Armor combinent un habitat ancien important — maisons en pierre du Trégor,
bourgs médiévaux de Dinan ou de Guingamp, longères rénovées de l'arrière-pays — et un
littoral très exposé. Cette double réalité conditionne fortement les travaux électriques
menés dans le département.</p>

<p>Sur la bande côtière, l'air chargé en sel accélère la corrosion des matériels installés
à l'extérieur : coffrets de branchement, prises de terrasse, luminaires de façade,
alimentations d'abris de jardin ou de pontons. Un matériel dont l'indice de protection
est insuffisant se dégrade en quelques saisons, ce qui provoque des déclenchements
répétés du différentiel, souvent par temps humide.</p>

<p>Dans l'intérieur du département, la problématique dominante est différente : de
nombreuses maisons anciennes conservent des installations posées avant les évolutions
majeures de la norme NF C 15-100. On y retrouve encore des tableaux à fusibles à broche,
des circuits sans conducteur de protection, ou des extensions successives réalisées au fil
des décennies sans reprise d'ensemble. La rénovation partielle ou complète de
l'installation y est un besoin fréquent, notamment lors d'un achat immobilier.</p>
""",
        "besoins": [
            "Reprise d'installations anciennes dans l'habitat en pierre et les longères rénovées",
            "Remplacement de tableaux à fusibles par un tableau à disjoncteurs et différentiels",
            "Protection des circuits extérieurs exposés aux embruns du littoral",
            "Mise en sécurité avant vente ou mise en location d'un bien",
            "Installation de bornes de recharge en maison individuelle",
            "Éclairage extérieur de jardins, terrasses et accès",
        ],
        "faq": [
            ("Intervenez-vous dans tout le département des Côtes-d'Armor ?",
             "<p>Oui. Le périmètre d'intervention couvre l'ensemble du département : le pays "
             "briochin, le Trégor autour de Lannion, le pays de Dinan, le Guingampais, le pays "
             "de Lamballe ainsi que le Centre-Bretagne costarmoricain. Précisez votre commune "
             "lors de la prise de contact pour organiser le rendez-vous.</p>"),
            ("Pourquoi les installations électriques extérieures se dégradent-elles vite près de la côte ?",
             "<p>L'air marin transporte des particules salines qui se déposent sur les parties "
             "métalliques et les contacts. Le sel est hygroscopique : il retient l'humidité et "
             "favorise l'oxydation, puis les défauts d'isolement. C'est pourquoi les matériels "
             "posés en extérieur doivent présenter un indice de protection adapté (IP et IK), "
             "avec des presse-étoupes correctement serrés et des boîtiers réellement étanches.</p>"),
            ("Faut-il refaire toute l'électricité d'une maison ancienne dans le 22 ?",
             "<p>Pas systématiquement. Tout dépend de l'état des conducteurs, de la présence "
             "d'un conducteur de protection, de la nature du tableau et des sections de câbles. "
             "Un diagnostic permet de distinguer ce qui peut être conservé de ce qui doit être "
             "repris. Dans beaucoup de maisons anciennes, une rénovation ciblée du tableau et "
             "des circuits sensibles suffit dans un premier temps.</p>"),
        ],
        "cities": [
            {
                "slug": "electricien-saint-brieuc",
                "name": "Saint-Brieuc",
                "lat": 48.5136, "lon": -2.7653,
                "title": "Électricien Saint-Brieuc (22) — Dépannage et installation électrique",
                "desc": ("Électricien à Saint-Brieuc : dépannage électrique, recherche de panne, "
                         "tableau électrique, rénovation et mise aux normes. Intervention à "
                         "Saint-Brieuc et dans l'agglomération briochine."),
                "h1": "Électricien à Saint-Brieuc",
                "intro": ("Dépannage, installation, rénovation et mise en sécurité électrique à "
                          "Saint-Brieuc et dans les communes de la baie."),
                "contexte": """
<p>Saint-Brieuc présente un tissu urbain très contrasté sur le plan électrique. Le
centre-ville et les faubourgs anciens comptent de nombreuses maisons de ville et petits
immeubles dont les installations ont été modifiées par étapes successives. Il n'est pas
rare d'y trouver un tableau récent alimentant des circuits, eux, restés d'origine : la
protection est modernisée, mais les conducteurs et les boîtes de dérivation ne suivent
pas.</p>

<p>Le quartier de Robien, cité-jardin construite dans l'entre-deux-guerres, et les
secteurs pavillonnaires de Cesson, Ginglin ou la Croix Saint-Lambert posent une autre
question : celle de la puissance disponible et du nombre de circuits. Ces logements ont
été conçus avant la généralisation des équipements actuels — plaque induction, lave-linge,
sèche-linge, four, informatique, recharge de véhicule. Les tableaux d'origine arrivent
saturés, sans emplacement libre pour ajouter un circuit dédié.</p>

<p>Enfin, la proximité immédiate de la baie expose les installations extérieures de
Plérin, Langueux ou Hillion à un environnement salin, avec les problèmes de corrosion et
de défaut d'isolement qui en découlent.</p>
""",
                "secteurs": ["Centre-ville", "Robien", "Cesson", "Ginglin", "Croix Saint-Lambert",
                             "Plérin", "Trégueux", "Langueux", "Ploufragan", "Yffiniac", "Hillion"],
                "besoins": [
                    ("Tableaux saturés dans le pavillonnaire",
                     "Ajout d'un circuit dédié (plaque, borne de recharge, atelier) impossible "
                     "faute d'emplacement libre : le remplacement ou l'extension du tableau "
                     "devient nécessaire."),
                    ("Circuits d'origine sous tableau récent",
                     "Cas fréquent dans l'habitat de centre-ville : la protection a été refaite "
                     "mais les conducteurs et raccordements anciens restent en place."),
                    ("Matériel extérieur corrodé en bord de baie",
                     "Prises, hublots et coffrets exposés aux embruns provoquent des "
                     "déclenchements différentiels récurrents par temps humide."),
                ],
                "faq": [
                    ("Intervenez-vous dans l'agglomération de Saint-Brieuc ?",
                     "<p>Oui, à Saint-Brieuc même comme dans les communes voisines : Plérin, "
                     "Trégueux, Langueux, Ploufragan, Yffiniac, Hillion et les communes "
                     "limitrophes de la baie.</p>"),
                    ("Mon disjoncteur saute quand il pleut, est-ce lié à l'humidité ?",
                     "<p>C'est un scénario classique lorsqu'un circuit extérieur présente un "
                     "défaut d'isolement. L'humidité crée un chemin de fuite vers la terre que "
                     "le différentiel détecte, d'où un déclenchement lié à la météo. "
                     "L'identification du circuit fautif se fait en isolant les départs un à un, "
                     "puis en mesurant l'isolement à l'aide d'un contrôleur.</p>"),
                    ("Puis-je faire vérifier une installation avant d'acheter à Saint-Brieuc ?",
                     "<p>Oui. Un examen de l'installation en complément du diagnostic "
                     "obligatoire permet de hiérarchiser les travaux à prévoir : ce qui relève "
                     "de la sécurité immédiate, ce qui peut être planifié, et ce qui peut "
                     "attendre une rénovation d'ensemble.</p>"),
                ],
            },
            {
                "slug": "electricien-lannion",
                "name": "Lannion",
                "lat": 48.7325, "lon": -3.4589,
                "title": "Électricien Lannion (22) — Dépannage, installation, rénovation",
                "desc": ("Électricien à Lannion et dans le Trégor : dépannage électrique, "
                         "recherche de panne, tableau électrique, rénovation et mise aux normes."),
                "h1": "Électricien à Lannion",
                "intro": ("Interventions électriques à Lannion, dans la vallée du Léguer et sur "
                          "la côte de Granit rose."),
                "contexte": """
<p>Lannion associe un centre ancien dense — maisons à pans de bois, immeubles étroits en
bord de Léguer — et une agglomération marquée par l'activité technologique du Trégor. Les
besoins électriques y sont donc de deux ordres : la reprise d'installations anciennes dans
le cœur de ville, et des demandes plus techniques côté locaux professionnels et bureaux.</p>

<p>Dans l'habitat ancien du centre, la contrainte principale est le cheminement des
câbles. Les murs en pierre épais, les planchers bois et l'absence de gaines techniques
imposent des solutions adaptées : goulottes discrètes, passage en plinthes, reprise lors
d'une réfection de doublage. Une rénovation électrique s'y prépare toujours en coordination
avec les autres corps d'état.</p>

<p>Sur le littoral proche — Perros-Guirec, Trébeurden, Trégastel, Pleumeur-Bodou — une part
notable du parc est constituée de résidences secondaires. Ces logements posent un enjeu
particulier : une installation qui reste inoccupée plusieurs mois voit ses défauts
s'aggraver sans que personne ne les constate. Les remises en service de début de saison
révèlent souvent des différentiels qui ne tiennent plus.</p>
""",
                "secteurs": ["Centre-ville", "Ker Uhel", "Servel", "Buhulien", "Perros-Guirec",
                             "Trébeurden", "Trégastel", "Pleumeur-Bodou", "Ploubezre", "Louannec"],
                "besoins": [
                    ("Rénovation dans le bâti ancien du centre",
                     "Passage des circuits dans des murs en pierre sans saignées destructrices, "
                     "reprise des boîtes de dérivation et création d'une liaison équipotentielle."),
                    ("Remise en service de résidences secondaires",
                     "Contrôle d'isolement et vérification des protections après plusieurs mois "
                     "d'inoccupation, avant remise sous tension complète."),
                    ("Besoins tertiaires et locaux professionnels",
                     "Alimentation de postes de travail, éclairage de bureaux, reprise de "
                     "tableaux divisionnaires dans les locaux d'activité."),
                ],
                "faq": [
                    ("Faut-il refaire l'électricité d'une maison en pierre à Lannion ?",
                     "<p>Cela dépend de l'état réel des circuits. Dans le bâti ancien, la "
                     "question centrale est la présence — ou non — d'un conducteur de "
                     "protection sur l'ensemble des circuits, et l'état de l'isolement des "
                     "conducteurs. Un contrôle permet de décider entre une reprise ciblée et une "
                     "rénovation complète.</p>"),
                    ("Que vérifier avant de rouvrir une résidence secondaire ?",
                     "<p>Avant de remettre l'installation en service, il est prudent de tester "
                     "le bouton test des différentiels, de contrôler l'absence d'humidité dans "
                     "les boîtiers extérieurs, et de vérifier qu'aucun rongeur n'a endommagé de "
                     "câble dans les combles. En cas de déclenchement immédiat au réarmement, "
                     "il faut faire mesurer l'isolement plutôt que forcer.</p>"),
                    ("Intervenez-vous sur la côte de Granit rose ?",
                     "<p>Oui, sur Perros-Guirec, Trébeurden, Trégastel, Pleumeur-Bodou et les "
                     "communes du Trégor situées dans les Côtes-d'Armor.</p>"),
                ],
            },
            {
                "slug": "electricien-dinan",
                "name": "Dinan",
                "lat": 48.4553, "lon": -2.0464,
                "title": "Électricien Dinan (22) — Dépannage et rénovation électrique",
                "desc": ("Électricien à Dinan : dépannage, recherche de panne, rénovation "
                         "électrique dans le bâti ancien, tableau électrique et mise aux normes."),
                "h1": "Électricien à Dinan",
                "intro": ("Travaux électriques à Dinan, dans la cité historique, le port sur la "
                          "Rance et les communes voisines."),
                "contexte": """
<p>Dinan possède l'un des centres anciens les mieux conservés de Bretagne : maisons à pans
de bois, immeubles en pierre, rues étroites en pente vers le port sur la Rance. Ce
patrimoine impose des méthodes de travail particulières. Dans un secteur protégé, on ne
traite pas une rénovation électrique comme dans une construction récente : les
interventions sur les façades, les menuiseries et parfois les cloisonnements sont
encadrées.</p>

<p>Techniquement, le bâti dinannais cumule plusieurs difficultés : épaisseur des murs,
planchers anciens, combles aménagés, et surtout circuits ajoutés au fil des générations.
On rencontre régulièrement des installations mixtes où cohabitent plusieurs époques de
câblage sous un même tableau.</p>

<p>Le secteur du port et les abords de la Rance ajoutent une contrainte d'humidité :
caves, rez-de-chaussée bas et locaux semi-enterrés y sont sensibles aux remontées, ce qui
influence directement le choix des matériels et la mise à la terre.</p>
""",
                "secteurs": ["Centre historique", "Le port", "Saint-Sauveur", "Lanvallay",
                             "Quévert", "Taden", "Léhon", "Trélivan", "Aucaleuc"],
                "besoins": [
                    ("Rénovation en secteur patrimonial",
                     "Cheminements discrets, respect des supports anciens, coordination avec "
                     "les autres travaux du logement."),
                    ("Locaux humides et rez-de-chaussée bas",
                     "Choix de matériels adaptés, protection différentielle correcte et "
                     "vérification de la mise à la terre."),
                    ("Installations hétérogènes",
                     "Circuits de plusieurs époques sous un même tableau : identification, "
                     "repérage et remise en cohérence."),
                ],
                "faq": [
                    ("Peut-on rénover l'électricité d'une maison classée ou en secteur protégé ?",
                     "<p>Oui, mais les modalités doivent être adaptées : on privilégie les "
                     "cheminements réversibles et peu invasifs, et toute modification visible "
                     "sur l'extérieur du bâtiment peut relever d'une autorisation d'urbanisme. "
                     "Il est recommandé de se rapprocher du service urbanisme de la commune "
                     "avant travaux.</p>"),
                    ("Comment traiter l'électricité dans une cave humide ?",
                     "<p>Un local humide impose des matériels dont l'indice de protection "
                     "correspond à l'exposition réelle, une protection différentielle 30 mA et "
                     "une liaison équipotentielle correctement réalisée. Les rallonges "
                     "permanentes et les multiprises y sont particulièrement à proscrire.</p>"),
                    ("Intervenez-vous autour de Dinan ?",
                     "<p>Oui : Lanvallay, Quévert, Taden, Léhon, Trélivan et les communes du "
                     "pays de Dinan situées dans les Côtes-d'Armor.</p>"),
                ],
            },
            {
                "slug": "electricien-guingamp",
                "name": "Guingamp",
                "lat": 48.5620, "lon": -3.1509,
                "title": "Électricien Guingamp (22) — Dépannage, tableau, mise aux normes",
                "desc": ("Électricien à Guingamp : dépannage électrique, remplacement de tableau, "
                         "rénovation et mise aux normes dans le Guingampais."),
                "h1": "Électricien à Guingamp",
                "intro": "Interventions électriques à Guingamp et dans les communes du Guingampais.",
                "contexte": """
<p>Guingamp est une ville de taille moyenne au parc immobilier majoritairement ancien.
Le centre concentre des immeubles de rapport et des maisons de ville dont beaucoup ont
été divisés en appartements locatifs. Cette division du bâti est une source récurrente de
problèmes électriques : circuits partagés entre logements, tableaux mal repérés, absence
de séparation nette entre parties privatives et communes.</p>

<p>Pour un propriétaire bailleur, ce point est déterminant. La mise en location d'un
logement suppose une installation ne présentant pas de risque manifeste pour la sécurité
des occupants, avec notamment une protection différentielle fonctionnelle et une mise à la
terre effective des circuits qui l'exigent.</p>

<p>Autour de la ville, à Pabu, Ploumagoar, Grâces ou Saint-Agathon, l'habitat pavillonnaire
des années 1970 à 1990 arrive à un âge où les tableaux d'origine et certains circuits
méritent une reprise, en particulier lorsque des équipements récents ont été ajoutés.</p>
""",
                "secteurs": ["Centre-ville", "Rustang", "Pabu", "Ploumagoar", "Grâces",
                             "Saint-Agathon", "Plouisy", "Saint-Adrien"],
                "besoins": [
                    ("Logements locatifs divisés",
                     "Séparation des circuits, repérage du tableau et mise en sécurité avant "
                     "mise en location."),
                    ("Pavillons des années 1970-1990",
                     "Remplacement de tableaux d'origine et ajout de circuits dédiés pour les "
                     "équipements récents."),
                    ("Diagnostic avant travaux",
                     "État des lieux de l'installation pour hiérarchiser les priorités de "
                     "remise en sécurité."),
                ],
                "faq": [
                    ("Quelles obligations électriques pour louer un logement ?",
                     "<p>Le logement doit répondre aux critères du logement décent, ce qui "
                     "implique une installation électrique en bon état d'usage et de "
                     "fonctionnement, ne présentant pas de risques manifestes pour la sécurité. "
                     "Par ailleurs, un diagnostic électrique est requis dans le dossier de "
                     "location lorsque l'installation a plus de quinze ans.</p>"),
                    ("Un tableau non repéré est-il un problème ?",
                     "<p>Oui, sur le plan pratique comme sur celui de la sécurité. Sans "
                     "repérage, il devient difficile de couper le bon circuit avant une "
                     "intervention, et le risque d'erreur augmente. Le repérage des protections "
                     "fait partie des exigences de la norme applicable aux installations.</p>"),
                    ("Intervenez-vous dans les communes autour de Guingamp ?",
                     "<p>Oui : Pabu, Ploumagoar, Grâces, Saint-Agathon, Plouisy et les communes "
                     "voisines du Guingampais.</p>"),
                ],
            },
            {
                "slug": "electricien-lamballe",
                "name": "Lamballe-Armor",
                "lat": 48.4682, "lon": -2.5150,
                "title": "Électricien Lamballe-Armor (22) — Dépannage et installation",
                "desc": ("Électricien à Lamballe-Armor : dépannage électrique, installation, "
                         "rénovation, tableau électrique et mise aux normes."),
                "h1": "Électricien à Lamballe-Armor",
                "intro": ("Interventions électriques à Lamballe-Armor, entre bourgs ruraux et "
                          "façade littorale."),
                "contexte": """
<p>Lamballe-Armor réunit depuis sa création une ville-centre, des bourgs ruraux et un
littoral. Cette diversité se retrouve dans les installations rencontrées : maisons de bourg
anciennes, corps de ferme réhabilités, lotissements récents et logements côtiers à Morieux
ou Planguenoual.</p>

<p>Dans les bâtiments agricoles reconvertis, la difficulté tient souvent à l'origine de
l'installation : conçue pour un usage agricole, elle n'est pas dimensionnée pour un usage
domestique. Sections inadaptées, absence de circuits spécialisés, protections
insuffisantes et mise à la terre incomplète sont des constats fréquents lors des
réhabilitations.</p>

<p>À l'inverse, les constructions récentes des lotissements posent surtout des questions
d'évolution : ajout d'une borne de recharge, alimentation d'un abri de jardin ou d'un
garage, création de circuits pour une extension.</p>
""",
                "secteurs": ["Centre-ville", "Le Haras", "Morieux", "Planguenoual",
                             "Meslin", "Coëtmieux", "Andel", "Trégomar"],
                "besoins": [
                    ("Réhabilitation de bâtiments agricoles",
                     "Reprise complète d'une installation non prévue pour un usage domestique."),
                    ("Extensions et dépendances",
                     "Alimentation d'un garage, d'un atelier ou d'un abri de jardin avec "
                     "protection adaptée."),
                    ("Bornes de recharge en maison individuelle",
                     "Étude de la puissance disponible et création d'un circuit dédié."),
                ],
                "faq": [
                    ("Peut-on réutiliser l'électricité d'un ancien bâtiment agricole ?",
                     "<p>Rarement en l'état. Une installation agricole répond à des usages et à "
                     "des contraintes différentes de celles d'un logement. Lors d'une "
                     "réhabilitation, l'installation est généralement reprise, avec création "
                     "d'un tableau adapté, de circuits spécialisés et d'une mise à la terre "
                     "conforme.</p>"),
                    ("Comment alimenter un abri de jardin ou un garage détaché ?",
                     "<p>Par un circuit dédié, protégé au tableau, avec un câble adapté à la "
                     "pose enterrée sous fourreau et à la distance. Un tableau divisionnaire "
                     "dans la dépendance permet ensuite d'y répartir prises et éclairage.</p>"),
                    ("Intervenez-vous sur le littoral de Lamballe-Armor ?",
                     "<p>Oui, notamment sur les secteurs de Morieux et Planguenoual, ainsi que "
                     "dans les communes voisines du pays de Lamballe.</p>"),
                ],
            },
        ],
    },
]

# =========================================================================
DEPARTEMENTS.append({
    "code": "29",
    "name": "Finistère",
    "slug": "finistere",
    "prep": "dans le Finistère",
    "prefecture": "Quimper",
    "lat": 48.20, "lon": -4.10,
    "title": "Électricien Finistère (29) — Dépannage, installation, rénovation",
    "desc": ("Électricien dans le Finistère : dépannage électrique, recherche de panne, "
             "installation, rénovation et mise aux normes à Brest, Quimper, Morlaix et "
             "Concarneau."),
    "h1": "Électricien dans le Finistère (29)",
    "chapo": ("Electricien Richard intervient dans le Finistère, du pays de Brest au pays "
              "bigouden, pour le dépannage, l'installation, la rénovation et la mise en "
              "sécurité des installations électriques."),
    "contexte": """
<p>Le Finistère est le département breton où la question de l'humidité pèse le plus lourd
sur les installations électriques. Façade maritime étendue, pluviométrie soutenue et vents
dominants chargés d'embruns créent des conditions sévères pour tout matériel installé en
extérieur ou dans un local mal ventilé.</p>

<p>Le parc de logements y est également très marqué par la reconstruction d'après-guerre,
en particulier à Brest et dans une moindre mesure à Morlaix et Concarneau. Les immeubles
des années 1950 et 1960 disposent souvent d'installations initialement conçues pour un
usage domestique limité : éclairage, quelques prises, pas de circuits spécialisés. Les
usages actuels dépassent largement ce dimensionnement.</p>

<p>Dans l'arrière-pays, le bâti en pierre et les fermes réhabilitées posent la question
classique de la mise à la terre et de la présence d'un conducteur de protection sur
l'ensemble des circuits. Ces points sont systématiquement examinés lors d'un diagnostic.</p>
""",
    "besoins": [
        "Reprise d'installations d'immeubles de la reconstruction",
        "Traitement des défauts d'isolement liés à l'humidité",
        "Création de circuits spécialisés dans des logements anciens",
        "Mise en sécurité de logements étudiants et locatifs",
        "Éclairage extérieur résistant aux embruns",
        "Installation de bornes de recharge en maison individuelle",
    ],
    "faq": [
        ("Intervenez-vous dans tout le Finistère ?",
         "<p>Oui, du pays de Brest au pays bigouden, en passant par le Léon, le Trégor "
         "finistérien, la Cornouaille et le Centre-Bretagne finistérien.</p>"),
        ("L'humidité peut-elle faire disjoncter une installation ?",
         "<p>Oui. L'humidité réduit l'isolement entre les conducteurs actifs et la terre. "
         "Lorsque le courant de fuite atteint le seuil du dispositif différentiel, celui-ci "
         "coupe l'alimentation. C'est un fonctionnement normal de la protection : le problème "
         "vient du défaut d'isolement, pas du différentiel.</p>"),
        ("Les immeubles anciens de Brest nécessitent-ils une rénovation complète ?",
         "<p>Pas nécessairement en une seule fois. Beaucoup de copropriétés commencent par le "
         "tableau et les circuits les plus sollicités — cuisine, salle d'eau — avant "
         "d'envisager une reprise complète. L'ordre des travaux doit être défini après un "
         "examen de l'installation existante.</p>"),
    ],
    "cities": [
        {
            "slug": "electricien-brest",
            "name": "Brest",
            "lat": 48.3904, "lon": -4.4861,
            "title": "Électricien Brest (29) — Dépannage électrique et rénovation",
            "desc": ("Électricien à Brest : dépannage électrique, recherche de panne, "
                     "remplacement de tableau, rénovation et mise aux normes dans tous les "
                     "quartiers brestois."),
            "h1": "Électricien à Brest",
            "intro": ("Dépannage, rénovation et mise en sécurité électrique à Brest et dans les "
                      "communes de la métropole."),
            "contexte": """
<p>Brest a été très largement reconstruite après 1945. Cette histoire urbaine a une
conséquence directe et concrète sur le travail d'un électricien : une part importante du
parc de logements du centre — autour de la rue de Siam, du secteur Jaurès et des grands
axes reconstruits — repose sur des installations dont la conception initiale date des
années 1950. À l'époque, un logement était équipé pour l'éclairage et quelques prises. Ni
la plaque de cuisson électrique, ni le lave-vaisselle, ni la recharge d'un véhicule
n'entraient dans le dimensionnement.</p>

<p>Résultat : des tableaux sans circuits spécialisés, des prises multipliées par
rallonges, et des conducteurs de section limitée qui chauffent. Dans ces immeubles, la
rénovation électrique se heurte aussi à la difficulté de passer de nouveaux circuits dans
des cloisons et planchers existants, ce qui suppose une réflexion sur les cheminements dès
le départ.</p>

<p>Les quartiers périphériques — Saint-Marc, Lambézellec, Bellevue, l'Europe — présentent
un profil différent, avec davantage de pavillons et de résidences des années 1960-1980. La
demande y porte souvent sur le remplacement du tableau, la création de circuits dédiés et
l'installation de bornes de recharge. Recouvrance et les secteurs proches de la rade
ajoutent enfin la contrainte de l'exposition maritime.</p>

<p>Ville universitaire, Brest compte également un parc locatif étudiant important, où la
mise en sécurité avant location est une demande récurrente des propriétaires.</p>
""",
            "secteurs": ["Centre-ville / Siam", "Recouvrance", "Saint-Marc", "Lambézellec",
                         "Bellevue", "Europe", "Saint-Pierre", "Guipavas", "Le Relecq-Kerhuon",
                         "Plougastel-Daoulas", "Gouesnou"],
            "besoins": [
                ("Immeubles de la reconstruction",
                 "Installations conçues pour des usages limités : absence de circuits "
                 "spécialisés, tableaux saturés, sections de conducteurs insuffisantes."),
                ("Logements étudiants et locatifs",
                 "Mise en sécurité avant location : protection différentielle, mise à la terre, "
                 "suppression des montages provisoires."),
                ("Exposition maritime en bord de rade",
                 "Corrosion des matériels extérieurs et défauts d'isolement récurrents sur les "
                 "circuits exposés."),
                ("Bornes de recharge en périphérie",
                 "Maisons de Saint-Marc, Lambézellec ou Guipavas : création d'un circuit dédié "
                 "après vérification de la puissance disponible."),
            ],
            "faq": [
                ("Dans quels quartiers de Brest intervenez-vous ?",
                 "<p>Dans l'ensemble de la commune — centre-ville, Recouvrance, Saint-Marc, "
                 "Lambézellec, Bellevue, l'Europe, Saint-Pierre — ainsi que dans les communes "
                 "de la métropole comme Guipavas, Le Relecq-Kerhuon, Plougastel-Daoulas ou "
                 "Gouesnou.</p>"),
                ("Mon appartement brestois n'a que deux circuits, est-ce dangereux ?",
                 "<p>Ce n'est pas dangereux en soi, mais c'est un signe que l'installation n'est "
                 "plus adaptée aux usages actuels. Le risque réel apparaît lorsque des "
                 "appareils puissants sont branchés sur des circuits non prévus pour eux : "
                 "échauffement des conducteurs, des connexions et des prises. Un examen du "
                 "tableau et des sections permet de statuer.</p>"),
                ("Peut-on rénover l'électricité d'un appartement en copropriété ?",
                 "<p>Oui, pour la partie privative. Les travaux sur les colonnes montantes et "
                 "les parties communes relèvent en revanche de la copropriété. La limite se "
                 "situe généralement au niveau du disjoncteur de branchement du logement.</p>"),
                ("Proposez-vous un dépannage électrique urgent à Brest ?",
                 "<p>Oui, les situations urgentes — absence totale de courant, odeur de brûlé, "
                 "échauffement au tableau, disjoncteur impossible à réarmer — sont traitées en "
                 "priorité. Contactez-nous par téléphone pour ces cas plutôt que par "
                 "formulaire.</p>"),
            ],
        },
        {
            "slug": "electricien-quimper",
            "name": "Quimper",
            "lat": 47.9960, "lon": -4.1024,
            "title": "Électricien Quimper (29) — Dépannage, installation, mise aux normes",
            "desc": ("Électricien à Quimper : dépannage électrique, recherche de panne, tableau "
                     "électrique, rénovation et mise aux normes en Cornouaille."),
            "h1": "Électricien à Quimper",
            "intro": "Interventions électriques à Quimper et dans les communes de Cornouaille.",
            "contexte": """
<p>Quimper présente un centre historique dense, organisé autour de la cathédrale et des
rives de l'Odet, où le bâti ancien domine. Les logements y sont souvent répartis sur
plusieurs niveaux étroits, avec des combles aménagés. Cette configuration complique le
passage de nouveaux circuits et impose de définir précisément les cheminements avant tout
chantier de rénovation.</p>

<p>Les quartiers de Penhars, Ergué-Armel et Kerfeunteun, développés au cours de la seconde
moitié du XX<sup>e</sup> siècle, forment un ensemble pavillonnaire et collectif plus
homogène. Les installations y datent fréquemment des années 1970-1980 : elles disposent en
général d'une mise à la terre, mais leur tableau n'offre plus assez de départs pour
accueillir les équipements ajoutés depuis.</p>

<p>Le quartier de Locmaria et les abords de l'Odet posent, comme dans toute vallée, des
questions d'humidité en rez-de-chaussée et en sous-sol, avec les précautions habituelles
sur le choix des matériels et la mise à la terre.</p>
""",
            "secteurs": ["Centre historique", "Locmaria", "Penhars", "Ergué-Armel",
                         "Kerfeunteun", "Ergué-Gabéric", "Plomelin", "Pluguffan", "Briec"],
            "besoins": [
                ("Bâti ancien du centre",
                 "Cheminements contraints, circuits ajoutés au fil du temps, reprise "
                 "progressive de l'installation."),
                ("Pavillons des années 1970-1980",
                 "Tableaux saturés, ajout de circuits spécialisés, remplacement de "
                 "protections vieillissantes."),
                ("Locaux en rez-de-chaussée près de l'Odet",
                 "Matériels adaptés à l'humidité et vérification de la liaison "
                 "équipotentielle."),
            ],
            "faq": [
                ("Intervenez-vous autour de Quimper ?",
                 "<p>Oui : Ergué-Gabéric, Plomelin, Pluguffan, Briec et les communes de "
                 "Quimper Bretagne Occidentale, ainsi que le reste de la Cornouaille "
                 "finistérienne.</p>"),
                ("Combien de circuits faut-il dans une cuisine ?",
                 "<p>La norme NF C 15-100 impose plusieurs circuits distincts dans une cuisine : "
                 "un circuit spécialisé pour la plaque de cuisson, des circuits dédiés pour les "
                 "gros appareils électroménagers, et un nombre minimal de socles de prises "
                 "répartis sur un circuit dédié au plan de travail. C'est l'un des points les "
                 "plus fréquemment non satisfaits dans les logements anciens.</p>"),
                ("Faut-il un permis pour rénover l'électricité en centre ancien ?",
                 "<p>Les travaux intérieurs d'électricité ne nécessitent pas d'autorisation "
                 "d'urbanisme en tant que tels. En revanche, toute modification de l'aspect "
                 "extérieur — passage de câble en façade, pose d'un coffret visible — peut être "
                 "soumise à déclaration, en particulier dans les périmètres protégés.</p>"),
            ],
        },
        {
            "slug": "electricien-morlaix",
            "name": "Morlaix",
            "lat": 48.5779, "lon": -3.8283,
            "title": "Électricien Morlaix (29) — Dépannage et rénovation électrique",
            "desc": ("Électricien à Morlaix : dépannage électrique, rénovation dans le bâti "
                     "ancien, remplacement de tableau et mise aux normes."),
            "h1": "Électricien à Morlaix",
            "intro": "Travaux électriques à Morlaix, dans la vallée et sur les hauteurs de la ville.",
            "contexte": """
<p>Morlaix se caractérise par une topographie marquée : la ville s'étage de part et
d'autre d'une vallée profonde, dominée par le viaduc. Le centre concentre un bâti ancien
remarquable, avec des maisons à pans de bois dont certaines conservent la structure
traditionnelle à cour intérieure et escalier central.</p>

<p>Ces maisons posent des questions techniques précises. Les structures bois anciennes
supportent mal les percements répétés, les volumes intérieurs sont complexes, et les
installations ont été modifiées à plusieurs reprises. La priorité y est presque toujours
la même : garantir une protection différentielle efficace et une mise à la terre effective
avant d'envisager toute extension de l'installation.</p>

<p>Sur les hauteurs et dans les communes voisines — Saint-Martin-des-Champs,
Plourin-lès-Morlaix, Plouigneau — le parc est plus récent et les demandes portent
davantage sur la modernisation des tableaux, l'éclairage extérieur et les circuits dédiés.</p>
""",
            "secteurs": ["Centre-ville", "Saint-Melaine", "Le Viaduc", "Saint-Martin-des-Champs",
                         "Plourin-lès-Morlaix", "Plouigneau", "Taulé", "Pleyber-Christ"],
            "besoins": [
                ("Maisons à pans de bois",
                 "Interventions respectueuses de la structure ancienne, cheminements adaptés."),
                ("Installations remaniées",
                 "Remise en cohérence de circuits ajoutés à différentes époques."),
                ("Modernisation en périphérie",
                 "Remplacement de tableaux, circuits dédiés et éclairage extérieur."),
            ],
            "faq": [
                ("Comment rénover l'électricité d'une maison à pans de bois ?",
                 "<p>En limitant les percements de la structure et en utilisant des cheminements "
                 "adaptés : plinthes techniques, doublages existants, gaines apparentes "
                 "discrètes. Les circuits sont repris depuis un tableau neuf, avec mise à la "
                 "terre et protections différentielles conformes.</p>"),
                ("Mon installation n'a pas de terre, est-ce grave ?",
                 "<p>C'est un défaut majeur de sécurité. Sans conducteur de protection, un "
                 "défaut d'isolement peut mettre la carcasse métallique d'un appareil sous "
                 "tension sans qu'aucune protection ne réagisse. La création d'une prise de "
                 "terre et sa distribution aux circuits est une priorité.</p>"),
                ("Intervenez-vous dans la baie de Morlaix ?",
                 "<p>Oui, à Morlaix et dans les communes environnantes du pays de Morlaix "
                 "situées dans le Finistère.</p>"),
            ],
        },
        {
            "slug": "electricien-concarneau",
            "name": "Concarneau",
            "lat": 47.8757, "lon": -3.9204,
            "title": "Électricien Concarneau (29) — Dépannage et installation électrique",
            "desc": ("Électricien à Concarneau : dépannage électrique, installation, rénovation, "
                     "tableau électrique et mise aux normes en bord de mer."),
            "h1": "Électricien à Concarneau",
            "intro": "Interventions électriques à Concarneau et sur le littoral cornouaillais.",
            "contexte": """
<p>Concarneau est une ville portuaire où l'exposition maritime est directe. Pour les
installations électriques, cela se traduit par une usure accélérée de tout ce qui est
posé à l'extérieur : coffrets, prises de terrasse, éclairages de façade, alimentations
d'annexes et de locaux techniques. Le sel se dépose sur les contacts et l'humidité fait le
reste.</p>

<p>Le second trait marquant de la commune est la part importante de résidences
secondaires et de locations saisonnières. Une installation utilisée quelques semaines par
an vieillit différemment : les défauts s'installent sans être détectés, et la remise en
service de début de saison révèle des différentiels qui déclenchent immédiatement.</p>

<p>La Ville Close et le centre ancien ajoutent enfin les contraintes propres au bâti
historique, tandis que les quartiers pavillonnaires alentour relèvent d'une logique plus
classique de modernisation.</p>
""",
            "secteurs": ["Ville Close", "Centre-ville", "Le Passage", "Le Cabellou",
                         "Beuzec-Conq", "Lanriec", "Trégunc", "Névez", "Rosporden"],
            "besoins": [
                ("Matériels extérieurs exposés aux embruns",
                 "Remplacement par des matériels à indice de protection adapté et reprise des "
                 "raccordements corrodés."),
                ("Résidences secondaires et locations saisonnières",
                 "Contrôle avant remise en service, sécurisation des installations utilisées "
                 "par des occupants successifs."),
                ("Locaux d'activité liés au port",
                 "Éclairage, prises et protections dans des locaux humides ou peu chauffés."),
            ],
            "faq": [
                ("Quel matériel électrique choisir en bord de mer ?",
                 "<p>Il faut privilégier des enveloppes à indice de protection élevé, des "
                 "matériels résistants à la corrosion, et éviter les boîtiers d'intérieur "
                 "détournés vers un usage extérieur. Un point souvent négligé : les "
                 "presse-étoupes doivent être adaptés au diamètre du câble et correctement "
                 "serrés, faute de quoi l'étanchéité annoncée n'est pas assurée.</p>"),
                ("Mon différentiel saute dès que je réarme après l'hiver, que faire ?",
                 "<p>Ne pas insister. Il faut débrancher les appareils, ouvrir les départs un à "
                 "un et identifier le circuit en défaut, puis mesurer son isolement. Un "
                 "déclenchement immédiat au réarmement indique un défaut réel, souvent lié à "
                 "l'humidité ou à un matériel extérieur détérioré.</p>"),
                ("Intervenez-vous à Trégunc, Névez ou Rosporden ?",
                 "<p>Oui, ces communes font partie du périmètre d'intervention en Cornouaille.</p>"),
            ],
        },
    ],
})

# =========================================================================
DEPARTEMENTS.append({
    "code": "35",
    "name": "Ille-et-Vilaine",
    "slug": "ille-et-vilaine",
    "prep": "en Ille-et-Vilaine",
    "prefecture": "Rennes",
    "lat": 48.15, "lon": -1.55,
    "title": "Électricien Ille-et-Vilaine (35) — Dépannage, installation, rénovation",
    "desc": ("Électricien en Ille-et-Vilaine : dépannage électrique, recherche de panne, "
             "installation, rénovation et mise aux normes à Rennes, Saint-Malo, Fougères, "
             "Vitré et Redon."),
    "h1": "Électricien en Ille-et-Vilaine (35)",
    "chapo": ("Electricien Richard intervient en Ille-et-Vilaine, de la métropole rennaise à "
              "la côte d'Émeraude et au pays de Vilaine, pour le dépannage, l'installation, "
              "la rénovation et la mise aux normes électriques."),
    "contexte": """
<p>L'Ille-et-Vilaine est le département le plus dynamique de Bretagne sur le plan
démographique, et cela se lit directement dans la nature des demandes électriques. La
croissance de la métropole rennaise entraîne un volume important de rénovations
d'appartements, de divisions de logements et de remises en état avant location ou mise en
vente.</p>

<p>Le parc immobilier y est très hétérogène. Rennes concentre à la fois du bâti médiéval
en centre-ville, des immeubles des années 1960-1970 dans les grands quartiers d'habitat
collectif, et des constructions récentes en périphérie. Chacune de ces catégories appelle
un type d'intervention différent : mise en sécurité pour les premières, modernisation des
tableaux pour les deuxièmes, adaptation aux nouveaux usages pour les dernières.</p>

<p>La côte, autour de Saint-Malo et de la baie, ajoute la problématique du littoral —
corrosion, humidité, logements occupés par intermittence — tandis que l'est du département,
autour de Vitré et Fougères, présente un habitat ancien de bourgs et de campagne où la
mise à la terre reste un enjeu central.</p>
""",
    "besoins": [
        "Rénovation électrique d'appartements dans la métropole rennaise",
        "Mise en sécurité avant location ou avant vente",
        "Remplacement de tableaux dans les copropriétés des années 1960-1970",
        "Reprise d'installations anciennes dans les bourgs de l'est du département",
        "Circuits extérieurs et éclairage sur la côte d'Émeraude",
        "Installation de bornes de recharge en maison et en copropriété",
    ],
    "faq": [
        ("Intervenez-vous dans toute l'Ille-et-Vilaine ?",
         "<p>Oui : Rennes et sa métropole, le pays malouin, le pays de Fougères, le pays de "
         "Vitré, le pays de Redon et les communes rurales du département.</p>"),
        ("Quels travaux électriques avant de louer un logement en Ille-et-Vilaine ?",
         "<p>L'installation doit être en bon état d'usage et ne pas présenter de risque "
         "manifeste pour la sécurité des occupants : protection différentielle fonctionnelle, "
         "mise à la terre, absence de matériel vétuste ou de montage provisoire. Un diagnostic "
         "électrique est par ailleurs à joindre au dossier de location pour les installations "
         "de plus de quinze ans.</p>"),
        ("La mise aux normes est-elle obligatoire lors d'une vente ?",
         "<p>Non. Le vendeur doit fournir un diagnostic électrique lorsque l'installation a "
         "plus de quinze ans, mais la loi ne l'oblige pas à réaliser les travaux. Les anomalies "
         "relevées sont portées à la connaissance de l'acheteur, qui les intègre souvent à sa "
         "négociation.</p>"),
    ],
    "cities": [
        {
            "slug": "electricien-rennes",
            "name": "Rennes",
            "lat": 48.1173, "lon": -1.6778,
            "title": "Électricien Rennes (35) — Dépannage électrique et rénovation",
            "desc": ("Électricien à Rennes : dépannage électrique, recherche de panne, "
                     "remplacement de tableau, rénovation d'appartement et mise aux normes."),
            "h1": "Électricien à Rennes",
            "intro": ("Dépannage, rénovation et mise en sécurité électrique à Rennes et dans "
                      "les communes de la métropole."),
            "contexte": """
<p>Rennes est une ville où trois parcs immobiliers très différents coexistent, et où le
travail de l'électricien change complètement selon le secteur.</p>

<p>Le centre historique, autour de la place Sainte-Anne et des rues à pans de bois,
comporte des immeubles anciens souvent divisés en petits logements. Les installations y
sont fréquemment le résultat d'ajouts successifs : tableau exigu placé dans un couloir,
circuits mélangés entre pièces, absence de circuits spécialisés pour la cuisine. La
priorité y est la remise en sécurité, pas l'esthétique.</p>

<p>Les grands quartiers d'habitat collectif construits entre 1960 et 1980 — Villejean, Le
Blosne, Maurepas, Cleunay — présentent un profil plus homogène. Les logements y disposent
généralement d'une mise à la terre, mais leur tableau et leurs circuits ont été
dimensionnés pour un équipement ménager bien plus léger qu'aujourd'hui. Le remplacement du
tableau avec ajout de circuits dédiés est la demande la plus courante.</p>

<p>Les secteurs récents comme Beauregard ou la périphérie pavillonnaire posent enfin des
questions d'évolution : ajout d'une borne de recharge, alimentation d'une extension,
domotique, éclairage extérieur.</p>

<p>Enfin, Rennes étant une ville très étudiante, la rotation locative y est forte. De
nombreux propriétaires font vérifier ou reprendre l'installation entre deux locataires,
notamment lorsque le logement a été divisé ou meublé pour la colocation.</p>
""",
            "secteurs": ["Centre historique", "Thabor – Saint-Hélier", "Villejean", "Le Blosne",
                         "Maurepas", "Cleunay", "Beauregard", "Bréquigny", "Saint-Grégoire",
                         "Cesson-Sévigné", "Bruz", "Chantepie"],
            "besoins": [
                ("Appartements anciens du centre",
                 "Tableaux exigus, circuits mélangés, absence de circuits spécialisés en "
                 "cuisine et en salle d'eau."),
                ("Copropriétés des années 1960-1980",
                 "Remplacement du tableau, ajout de circuits dédiés, remplacement de "
                 "protections vieillissantes."),
                ("Logements locatifs et colocations",
                 "Mise en sécurité entre deux locations, adaptation du nombre de prises aux "
                 "usages réels."),
                ("Maisons de périphérie",
                 "Bornes de recharge, extensions, éclairage extérieur et circuits de jardin."),
            ],
            "faq": [
                ("Dans quels quartiers de Rennes intervenez-vous ?",
                 "<p>Dans l'ensemble de la commune — centre, Thabor–Saint-Hélier, Villejean, Le "
                 "Blosne, Maurepas, Cleunay, Beauregard, Bréquigny — et dans les communes de "
                 "Rennes Métropole comme Cesson-Sévigné, Saint-Grégoire, Bruz ou Chantepie.</p>"),
                ("Peut-on remplacer un tableau électrique en appartement ?",
                 "<p>Oui. Le remplacement du tableau relève de la partie privative du logement. "
                 "L'opération suppose une coupure temporaire, le repérage des circuits "
                 "existants et, souvent, la reprise de la liaison à la terre. Les colonnes "
                 "montantes et les parties communes restent du ressort de la copropriété.</p>"),
                ("Que faire si mon logement rennais n'a pas assez de prises ?",
                 "<p>Plutôt que de multiplier les multiprises — principale cause "
                 "d'échauffement — il est préférable d'ajouter des socles sur un circuit "
                 "existant lorsque sa capacité le permet, ou de créer un nouveau circuit depuis "
                 "le tableau. Le choix dépend du nombre de points déjà raccordés et de la "
                 "section des conducteurs.</p>"),
                ("Faites-vous du dépannage électrique en urgence à Rennes ?",
                 "<p>Oui. Les situations qui présentent un risque immédiat — odeur de brûlé, "
                 "échauffement au tableau, coupure totale, disjoncteur qui ne se réarme pas — "
                 "sont prioritaires. Un appel téléphonique permet de qualifier la situation "
                 "plus vite qu'un formulaire.</p>"),
            ],
        },
        {
            "slug": "electricien-saint-malo",
            "name": "Saint-Malo",
            "lat": 48.6493, "lon": -2.0257,
            "title": "Électricien Saint-Malo (35) — Dépannage et rénovation électrique",
            "desc": ("Électricien à Saint-Malo : dépannage électrique, rénovation, tableau "
                     "électrique et mise aux normes à Intra-Muros, Paramé et Saint-Servan."),
            "h1": "Électricien à Saint-Malo",
            "intro": "Interventions électriques à Saint-Malo et sur la côte d'Émeraude.",
            "contexte": """
<p>Saint-Malo cumule deux particularités qui pèsent sur les installations électriques :
une exposition maritime forte et un parc locatif saisonnier important.</p>

<p>Intra-Muros, les immeubles reconstruits après-guerre à l'intérieur des remparts
présentent des logements souvent répartis en étages étroits, avec des installations
remaniées à mesure des changements d'usage — passage en location touristique, division,
création de studios. Ces transformations successives laissent des traces : circuits
surchargés, tableaux mal adaptés, absence de circuit spécialisé pour les équipements.</p>

<p>À Paramé, Rothéneuf et Saint-Servan, l'habitat individuel domine, avec de nombreuses
résidences secondaires. Comme partout sur le littoral, les installations extérieures
souffrent : luminaires de façade, prises de terrasse et alimentations d'annexes se
dégradent plus vite qu'à l'intérieur des terres.</p>

<p>Les logements en location saisonnière justifient une attention particulière. Ils sont
utilisés par des occupants qui ne connaissent pas l'installation, ce qui rend d'autant plus
importante la présence de protections différentielles fonctionnelles et d'un tableau
correctement repéré.</p>
""",
            "secteurs": ["Intra-Muros", "Paramé", "Saint-Servan", "Rothéneuf", "La Découverte",
                         "Saint-Jouan-des-Guérets", "Cancale", "Dinard", "Saint-Coulomb"],
            "besoins": [
                ("Locations saisonnières",
                 "Protections différentielles fiables, tableau repéré, suppression des "
                 "montages provisoires."),
                ("Installations extérieures en bord de mer",
                 "Remplacement de matériels corrodés et reprise des étanchéités."),
                ("Logements divisés Intra-Muros",
                 "Séparation et remise en cohérence des circuits après division."),
            ],
            "faq": [
                ("Quelles précautions électriques pour un logement en location saisonnière ?",
                 "<p>L'essentiel tient en trois points : des dispositifs différentiels 30 mA "
                 "protégeant l'ensemble des circuits, une mise à la terre effective, et un "
                 "tableau clairement repéré pour que l'occupant puisse réarmer sans risque. "
                 "S'y ajoute la suppression de tout montage provisoire — rallonges permanentes, "
                 "dominos apparents, prises multiples en cascade.</p>"),
                ("Pourquoi remplacer un luminaire extérieur qui fonctionne encore ?",
                 "<p>Parce que la corrosion attaque d'abord les joints et les entrées de câble. "
                 "Un luminaire qui éclaire encore peut déjà présenter un défaut d'isolement "
                 "naissant, qui se manifestera par un déclenchement du différentiel à la "
                 "première forte pluie.</p>"),
                ("Intervenez-vous à Cancale, Dinard ou Saint-Jouan ?",
                 "<p>Oui pour les communes situées en Ille-et-Vilaine, comme Cancale, "
                 "Saint-Jouan-des-Guérets ou Saint-Coulomb. Dinard se trouve dans les "
                 "Côtes-d'Armor, également couvertes.</p>"),
            ],
        },
        {
            "slug": "electricien-fougeres",
            "name": "Fougères",
            "lat": 48.3520, "lon": -1.2000,
            "title": "Électricien Fougères (35) — Dépannage, tableau, mise aux normes",
            "desc": ("Électricien à Fougères : dépannage électrique, remplacement de tableau, "
                     "rénovation dans le bâti ancien et mise aux normes."),
            "h1": "Électricien à Fougères",
            "intro": "Interventions électriques à Fougères et dans le pays fougerais.",
            "contexte": """
<p>Fougères est une ville d'histoire dont le bâti reflète les époques successives : quartier
médiéval en contrebas près du château, ville haute plus tardive, et faubourgs marqués par
le passé industriel de la chaussure. Les immeubles ouvriers et les maisons de ville de
cette période constituent une part significative du parc.</p>

<p>Ces logements ont en commun des installations installées ou reprises entre les années
1950 et 1980, aujourd'hui à la limite de leur usage. On y trouve encore des tableaux à
fusibles, parfois complétés d'un différentiel ajouté a posteriori, et des circuits sans
conducteur de protection dans les pièces anciennes.</p>

<p>Autour de la ville, l'habitat rural et les bourgs du pays fougerais présentent le profil
classique des maisons anciennes : mise à la terre insuffisante, dépendances alimentées par
des circuits improvisés, et besoins de reprise lors des réhabilitations.</p>
""",
            "secteurs": ["Ville haute", "Quartier médiéval", "Bonabry", "Saint-Sulpice",
                         "Lécousse", "Javené", "Beaucé", "Romagné"],
            "besoins": [
                ("Maisons de ville et immeubles ouvriers",
                 "Remplacement de tableaux à fusibles et création d'une mise à la terre."),
                ("Réhabilitations en secteur rural",
                 "Reprise complète des circuits et alimentation des dépendances."),
                ("Mise en sécurité avant vente",
                 "Traitement des anomalies relevées au diagnostic électrique."),
            ],
            "faq": [
                ("Un tableau à fusibles doit-il être remplacé ?",
                 "<p>Un tableau à fusibles à broche ne permet ni la protection différentielle "
                 "adaptée, ni un repérage clair, ni l'ajout de circuits. Sur le plan de la "
                 "sécurité, son remplacement par un tableau à disjoncteurs et différentiels "
                 "constitue l'une des améliorations les plus efficaces d'une installation "
                 "ancienne.</p>"),
                ("Comment savoir si mon installation a une terre ?",
                 "<p>La présence d'une broche de terre sur les prises n'est pas une preuve "
                 "suffisante : elle peut ne pas être raccordée. Seule une mesure permet de le "
                 "vérifier, ainsi que le contrôle de la présence d'un piquet ou d'une boucle de "
                 "terre et de la barrette de coupure.</p>"),
                ("Intervenez-vous dans le pays de Fougères ?",
                 "<p>Oui, à Fougères et dans les communes environnantes comme Lécousse, Javené, "
                 "Beaucé ou Romagné.</p>"),
            ],
        },
        {
            "slug": "electricien-vitre",
            "name": "Vitré",
            "lat": 48.1240, "lon": -1.2100,
            "title": "Électricien Vitré (35) — Dépannage, installation, rénovation",
            "desc": ("Électricien à Vitré : dépannage électrique, installation, rénovation, "
                     "tableau électrique et mise aux normes dans le pays de Vitré."),
            "h1": "Électricien à Vitré",
            "intro": "Interventions électriques à Vitré et dans les communes du pays de Vitré.",
            "contexte": """
<p>Vitré associe un centre médiéval remarquablement préservé et une périphérie économique
active. Cette combinaison se traduit par des besoins électriques de nature différente selon
que l'on intervient dans le cœur ancien ou dans les secteurs plus récents.</p>

<p>Dans le centre, les maisons anciennes — dont plusieurs à pans de bois — imposent les
contraintes habituelles du bâti historique : cheminements difficiles, structures fragiles,
et installations modifiées de longue date. La mise en sécurité y prime : protection
différentielle, mise à la terre, remplacement des matériels vétustes.</p>

<p>En périphérie, les lotissements construits depuis les années 1980 et les zones
d'activité génèrent d'autres demandes : circuits spécialisés supplémentaires, éclairage
extérieur, alimentation d'ateliers ou de garages, bornes de recharge.</p>
""",
            "secteurs": ["Centre médiéval", "Rachapt", "Maison Rouge", "Saint-Martin",
                         "Châteaubourg", "Argentré-du-Plessis", "Étrelles", "Pocé-les-Bois"],
            "besoins": [
                ("Bâti ancien du centre",
                 "Mise en sécurité prioritaire : différentiels, terre, matériels vétustes."),
                ("Lotissements récents",
                 "Ajout de circuits dédiés, éclairage extérieur, bornes de recharge."),
                ("Locaux professionnels",
                 "Éclairage, prises et tableaux divisionnaires en zone d'activité."),
            ],
            "faq": [
                ("À quoi sert un dispositif différentiel 30 mA ?",
                 "<p>Il détecte les courants de fuite vers la terre et coupe l'alimentation "
                 "avant qu'un courant dangereux ne traverse une personne. C'est la protection "
                 "principale contre l'électrisation par contact indirect. La norme impose "
                 "aujourd'hui que tous les circuits d'un logement soient protégés par un "
                 "différentiel de sensibilité 30 mA.</p>"),
                ("Peut-on ajouter une prise sur un circuit existant ?",
                 "<p>Oui, dans la limite du nombre de socles admis pour la section du "
                 "conducteur et le calibre de protection du circuit. Au-delà, il faut créer un "
                 "nouveau circuit depuis le tableau. Ajouter des prises sans vérifier cette "
                 "limite conduit à des échauffements.</p>"),
                ("Intervenez-vous autour de Vitré ?",
                 "<p>Oui : Châteaubourg, Argentré-du-Plessis, Étrelles, Pocé-les-Bois et les "
                 "communes du pays de Vitré.</p>"),
            ],
        },
        {
            "slug": "electricien-redon",
            "name": "Redon",
            "lat": 47.6516, "lon": -2.0847,
            "title": "Électricien Redon (35) — Dépannage et rénovation électrique",
            "desc": ("Électricien à Redon : dépannage électrique, rénovation, tableau "
                     "électrique, mise aux normes et traitement des locaux humides."),
            "h1": "Électricien à Redon",
            "intro": "Interventions électriques à Redon, au confluent de la Vilaine et de l'Oust.",
            "contexte": """
<p>Redon occupe une position singulière, au confluent de la Vilaine et de l'Oust, à la
jonction de trois départements. Le port fluvial et le canal structurent la ville, et cette
proximité de l'eau a une incidence directe sur les installations électriques.</p>

<p>Les rez-de-chaussée, caves et locaux bas des quartiers proches des quais sont sensibles
à l'humidité, et le secteur est historiquement exposé aux crues de la Vilaine. Pour une
installation électrique, cette contrainte impose des choix précis : matériels adaptés aux
locaux humides, tableau positionné hors des zones les plus basses lorsque c'est possible,
liaison équipotentielle soignée, et vigilance particulière après tout épisode d'inondation.</p>

<p>Le reste du parc — maisons de ville anciennes du centre, pavillonnaire périphérique,
bourgs alentour — relève des besoins classiques : remplacement de tableaux, création de
circuits dédiés, mise en sécurité avant vente ou location.</p>
""",
            "secteurs": ["Centre-ville", "Le Port", "Bellevue", "Saint-Nicolas-de-Redon",
                         "Sainte-Marie", "Bains-sur-Oust", "Saint-Jean-la-Poterie"],
            "besoins": [
                ("Locaux exposés à l'humidité",
                 "Choix de matériels adaptés, protection différentielle et liaison "
                 "équipotentielle."),
                ("Remise en état après dégât des eaux",
                 "Contrôle d'isolement des circuits touchés avant toute remise sous tension."),
                ("Modernisation de l'habitat ancien",
                 "Tableaux, mise à la terre et circuits spécialisés."),
            ],
            "faq": [
                ("Que faire après une inondation ou un dégât des eaux ?",
                 "<p>Ne pas remettre l'installation sous tension avant vérification. L'eau "
                 "s'infiltre dans les boîtiers, les prises et parfois les conducteurs, et un "
                 "circuit apparemment sec peut conserver un isolement dégradé. La démarche "
                 "consiste à couper l'alimentation, laisser sécher, puis faire mesurer "
                 "l'isolement de chaque circuit avant la remise en service.</p>"),
                ("Quelles règles s'appliquent dans une cave ou un local humide ?",
                 "<p>Les matériels doivent présenter un indice de protection en rapport avec "
                 "l'exposition réelle à l'eau et aux projections, les circuits doivent être "
                 "protégés par un différentiel 30 mA, et les éléments conducteurs doivent être "
                 "reliés à la liaison équipotentielle. Les installations provisoires y sont "
                 "particulièrement dangereuses.</p>"),
                ("Redon est à la limite de trois départements, intervenez-vous alentour ?",
                 "<p>Oui, dans le périmètre couvert : l'Ille-et-Vilaine, mais aussi le Morbihan "
                 "et la Loire-Atlantique tout proches, qui font partie des six départements "
                 "d'intervention.</p>"),
            ],
        },
    ],
})

# =========================================================================
DEPARTEMENTS.append({
    "code": "56",
    "name": "Morbihan",
    "slug": "morbihan",
    "prep": "dans le Morbihan",
    "prefecture": "Vannes",
    "lat": 47.85, "lon": -2.85,
    "title": "Électricien Morbihan (56) — Dépannage, installation, rénovation",
    "desc": ("Électricien dans le Morbihan : dépannage électrique, recherche de panne, "
             "installation, rénovation et mise aux normes à Vannes, Lorient, Pontivy, "
             "Ploërmel et Auray."),
    "h1": "Électricien dans le Morbihan (56)",
    "chapo": ("Electricien Richard intervient dans le Morbihan, du golfe à l'arrière-pays et "
              "au Centre-Bretagne, pour le dépannage, l'installation, la rénovation et la "
              "mise aux normes électriques."),
    "contexte": """
<p>Le Morbihan présente l'un des contrastes les plus nets de la région entre son littoral
et son intérieur. Sur le golfe et la côte, la pression immobilière est forte, les
résidences secondaires nombreuses et les logements souvent rénovés par étapes. À
l'intérieur, autour de Pontivy et de Ploërmel, l'habitat rural ancien domine, avec des
installations qui n'ont parfois jamais fait l'objet d'une reprise d'ensemble.</p>

<p>Le littoral concentre des problématiques bien identifiées : matériels extérieurs
corrodés par les embruns, installations sollicitées uniquement l'été, logements loués en
saison dont la sécurité électrique doit être irréprochable pour des occupants qui ne
connaissent pas les lieux.</p>

<p>Dans l'intérieur, le sujet dominant reste la mise en sécurité : absence ou insuffisance
de la mise à la terre, tableaux anciens, circuits mêlant plusieurs générations de câblage,
dépendances et bâtiments annexes alimentés par des montages de fortune.</p>
""",
    "besoins": [
        "Mise en sécurité d'installations anciennes en habitat rural",
        "Reprise de matériels extérieurs corrodés sur le littoral",
        "Contrôle avant remise en service de résidences secondaires",
        "Remplacement de tableaux et création de circuits spécialisés",
        "Alimentation de dépendances, ateliers et abris de jardin",
        "Installation de bornes de recharge en maison individuelle",
    ],
    "faq": [
        ("Intervenez-vous dans tout le Morbihan ?",
         "<p>Oui : le pays de Vannes et le golfe, le pays de Lorient, le pays d'Auray, "
         "Pontivy et le Centre-Bretagne morbihannais, ainsi que le pays de Ploërmel.</p>"),
        ("Faut-il faire vérifier une maison achetée dans le Morbihan ?",
         "<p>C'est vivement conseillé lorsque l'installation a plus de quinze ans. Le "
         "diagnostic remis à la vente signale les anomalies, mais il ne hiérarchise pas les "
         "travaux ni ne chiffre les reprises. Un examen complémentaire permet de distinguer "
         "l'urgent du souhaitable.</p>"),
        ("Quels sont les défauts les plus fréquents en habitat rural ancien ?",
         "<p>Trois reviennent constamment : une mise à la terre absente ou non raccordée à "
         "l'ensemble des circuits, un tableau ne comportant pas de protection différentielle "
         "adaptée, et des matériels vétustes ou des connexions non protégées, en particulier "
         "dans les dépendances.</p>"),
    ],
    "cities": [
        {
            "slug": "electricien-vannes",
            "name": "Vannes",
            "lat": 47.6587, "lon": -2.7603,
            "title": "Électricien Vannes (56) — Dépannage électrique et rénovation",
            "desc": ("Électricien à Vannes : dépannage électrique, recherche de panne, tableau "
                     "électrique, rénovation et mise aux normes dans le pays vannetais."),
            "h1": "Électricien à Vannes",
            "intro": "Interventions électriques à Vannes, sur le golfe et dans le pays vannetais.",
            "contexte": """
<p>Vannes connaît depuis plusieurs décennies une croissance démographique soutenue, qui se
traduit par une double demande : rénovation du parc existant d'un côté, adaptation de
logements récents aux nouveaux usages de l'autre.</p>

<p>Le centre intra-muros, avec ses maisons à pans de bois et ses immeubles anciens autour
de la cathédrale et du port, concentre les installations les plus délicates. Les logements
y sont souvent petits, parfois transformés en meublés ou en locations de courte durée. Les
reprises portent principalement sur le tableau, la mise à la terre et la création de
circuits spécialisés en cuisine et en salle d'eau.</p>

<p>Les quartiers de Ménimur, Kercado et Saint-Patern, comme les secteurs pavillonnaires
périphériques, relèvent d'une logique de modernisation : remplacement des tableaux
d'origine, ajout de circuits pour les équipements récents, installation de bornes de
recharge.</p>

<p>Le pourtour du golfe ajoute enfin la dimension littorale, avec ses résidences
secondaires et ses installations extérieures exposées.</p>
""",
            "secteurs": ["Intra-muros", "Le Port", "Ménimur", "Kercado", "Saint-Patern",
                         "Séné", "Arradon", "Saint-Avé", "Theix-Noyalo", "Ploeren"],
            "besoins": [
                ("Logements anciens intra-muros",
                 "Tableaux exigus, circuits mélangés, absence de circuits spécialisés."),
                ("Pavillonnaire et périphérie",
                 "Modernisation des tableaux, circuits dédiés, bornes de recharge."),
                ("Résidences du golfe",
                 "Contrôle après période d'inoccupation, matériels extérieurs adaptés."),
            ],
            "faq": [
                ("Intervenez-vous autour du golfe du Morbihan ?",
                 "<p>Oui : Vannes, Séné, Arradon, Saint-Avé, Theix-Noyalo, Ploeren et les "
                 "communes du pourtour du golfe situées dans le Morbihan.</p>"),
                ("Quels circuits spécialisés sont obligatoires dans un logement ?",
                 "<p>La norme NF C 15-100 impose des circuits dédiés notamment pour la plaque "
                 "de cuisson, le lave-linge, le lave-vaisselle et le four, ainsi que des "
                 "circuits distincts pour l'éclairage et les prises. Chaque circuit spécialisé "
                 "dispose de sa propre protection au tableau.</p>"),
                ("Une petite surface doit-elle respecter les mêmes règles ?",
                 "<p>Oui. Les exigences de sécurité — différentiels, mise à la terre, "
                 "protection des circuits — s'appliquent quelle que soit la surface. Certains "
                 "nombres minimaux d'équipements varient selon la taille des pièces, mais les "
                 "principes de protection restent identiques.</p>"),
            ],
        },
        {
            "slug": "electricien-lorient",
            "name": "Lorient",
            "lat": 47.7485, "lon": -3.3702,
            "title": "Électricien Lorient (56) — Dépannage et rénovation électrique",
            "desc": ("Électricien à Lorient : dépannage électrique, remplacement de tableau, "
                     "rénovation et mise aux normes dans les quartiers lorientais."),
            "h1": "Électricien à Lorient",
            "intro": "Interventions électriques à Lorient et dans les communes de l'agglomération.",
            "contexte": """
<p>Comme Brest, Lorient a été reconstruite après 1945. Une grande partie de son parc de
logements date donc des années 1950 et 1960, avec les conséquences électriques que cela
implique : installations dimensionnées pour des usages domestiques limités, tableaux sans
circuits spécialisés, et sections de conducteurs souvent justes au regard des équipements
actuels.</p>

<p>Les quartiers de Keryado, de la Nouvelle Ville et de Merville illustrent bien ce
profil. Les logements y sont solides et bien agencés, mais leur installation électrique a
rarement suivi l'évolution des équipements ménagers. La demande la plus fréquente y
concerne le remplacement du tableau et la création de circuits dédiés.</p>

<p>Le secteur portuaire de Keroman et les activités liées à la pêche génèrent par ailleurs
des besoins en locaux professionnels : éclairage de locaux techniques, prises en ambiance
humide, tableaux divisionnaires. Ces environnements exigent des matériels adaptés et une
attention particulière à la protection différentielle.</p>
""",
            "secteurs": ["Centre-ville", "Keryado", "Nouvelle Ville", "Merville", "Kerentrech",
                         "Lanester", "Ploemeur", "Larmor-Plage", "Quéven", "Hennebont"],
            "besoins": [
                ("Logements de la reconstruction",
                 "Tableaux sans circuits spécialisés et sections de conducteurs limitées."),
                ("Locaux professionnels et techniques",
                 "Matériels adaptés aux ambiances humides et tableaux divisionnaires."),
                ("Copropriétés",
                 "Remplacement de tableaux privatifs et remise en sécurité des logements."),
            ],
            "faq": [
                ("Intervenez-vous dans l'agglomération de Lorient ?",
                 "<p>Oui : Lorient, Lanester, Ploemeur, Larmor-Plage, Quéven, Hennebont et les "
                 "communes voisines du pays de Lorient.</p>"),
                ("Faut-il augmenter la puissance de mon abonnement lors d'une rénovation ?",
                 "<p>Parfois. Si les nouveaux équipements dépassent la puissance souscrite, le "
                 "disjoncteur de branchement déclenchera lors des pointes d'usage. Le calcul "
                 "prend en compte la puissance des appareils et leur simultanéité "
                 "d'utilisation. La modification de la puissance souscrite s'effectue auprès du "
                 "fournisseur d'électricité.</p>"),
                ("Quelle différence entre le disjoncteur de branchement et le tableau ?",
                 "<p>Le disjoncteur de branchement, placé en amont, protège l'installation dans "
                 "son ensemble et limite la puissance appelée : il appartient au gestionnaire "
                 "de réseau. Le tableau de répartition, en aval, distribue et protège chaque "
                 "circuit du logement : il relève de l'installation privative.</p>"),
            ],
        },
        {
            "slug": "electricien-pontivy",
            "name": "Pontivy",
            "lat": 48.0686, "lon": -2.9628,
            "title": "Électricien Pontivy (56) — Dépannage, tableau, mise aux normes",
            "desc": ("Électricien à Pontivy : dépannage électrique, remplacement de tableau, "
                     "rénovation et mise aux normes en Centre-Bretagne."),
            "h1": "Électricien à Pontivy",
            "intro": "Interventions électriques à Pontivy et dans le Centre-Bretagne morbihannais.",
            "contexte": """
<p>Pontivy présente une organisation urbaine peu commune : un centre médiéval autour du
château, prolongé par un quartier au tracé régulier hérité du réaménagement napoléonien.
Cette juxtaposition se retrouve dans le bâti, avec des maisons anciennes d'un côté et des
immeubles plus réguliers du XIX<sup>e</sup> siècle de l'autre.</p>

<p>Pour les installations électriques, l'enjeu principal reste celui de l'habitat ancien :
tableaux dépassés, circuits sans conducteur de protection, matériels vétustes. Beaucoup de
ces logements ont connu plusieurs générations d'occupants et autant de modifications
partielles.</p>

<p>Autour de la ville, le Centre-Bretagne se caractérise par un habitat rural dispersé :
fermes, longères, dépendances. Les alimentations de bâtiments annexes y sont un point de
vigilance constant, car elles ont souvent été réalisées sans protection adaptée ni
liaison à la terre.</p>
""",
            "secteurs": ["Centre ancien", "Quartier napoléonien", "Le Blavet", "Kerimaux",
                         "Le Sourn", "Noyal-Pontivy", "Saint-Thuriau", "Cléguérec"],
            "besoins": [
                ("Habitat ancien du centre",
                 "Remplacement des tableaux, création d'une terre, suppression des matériels "
                 "vétustes."),
                ("Fermes et longères",
                 "Reprise d'ensemble lors des réhabilitations, circuits pour dépendances."),
                ("Alimentations de bâtiments annexes",
                 "Câbles adaptés, protection au départ et tableau divisionnaire."),
            ],
            "faq": [
                ("Comment alimenter correctement une dépendance ?",
                 "<p>Par un circuit dédié partant du tableau principal, protégé par un "
                 "disjoncteur adapté, avec un câble prévu pour la pose enterrée sous fourreau "
                 "et dimensionné selon la distance et la puissance. Un tableau divisionnaire "
                 "dans la dépendance permet ensuite d'y répartir les circuits.</p>"),
                ("Peut-on garder d'anciens câbles lors d'une rénovation ?",
                 "<p>Cela dépend de leur nature et de leur état. Les conducteurs sous isolant "
                 "dégradé, les câbles sans conducteur de protection et les sections "
                 "insuffisantes doivent être remplacés. Une mesure d'isolement, circuit par "
                 "circuit, permet d'objectiver la décision.</p>"),
                ("Intervenez-vous en Centre-Bretagne ?",
                 "<p>Oui, à Pontivy et dans les communes environnantes du Morbihan comme Le "
                 "Sourn, Noyal-Pontivy, Saint-Thuriau ou Cléguérec.</p>"),
            ],
        },
        {
            "slug": "electricien-ploermel",
            "name": "Ploërmel",
            "lat": 47.9310, "lon": -2.3970,
            "title": "Électricien Ploërmel (56) — Dépannage et installation électrique",
            "desc": ("Électricien à Ploërmel : dépannage électrique, installation, rénovation, "
                     "tableau électrique et mise aux normes."),
            "h1": "Électricien à Ploërmel",
            "intro": "Interventions électriques à Ploërmel et dans le pays de Brocéliande.",
            "contexte": """
<p>Ploërmel occupe une position centrale entre Rennes et Vannes, sur un axe routier
important. La commune associe un centre ancien, des lotissements développés au fil des
dernières décennies et des zones d'activité en périphérie.</p>

<p>Cette structure produit deux types de besoins. Dans le centre et les hameaux, ce sont
les installations anciennes qui appellent une reprise : tableaux dépassés, mise à la terre
partielle, circuits insuffisants. Dans les lotissements, les demandes portent plutôt sur
l'ajout d'équipements — borne de recharge, alimentation d'un garage, éclairage extérieur,
extension.</p>

<p>La présence de zones d'activité et de commerces génère par ailleurs des interventions
en local professionnel : éclairage, prises, tableaux divisionnaires et remise en état après
changement d'exploitant.</p>
""",
            "secteurs": ["Centre-ville", "Le lac au Duc", "Zone de Camagnon", "Taupont",
                         "Monterrein", "Loyat", "Josselin", "Guer"],
            "besoins": [
                ("Habitat ancien et hameaux",
                 "Reprise des tableaux et de la mise à la terre."),
                ("Lotissements",
                 "Bornes de recharge, extensions, éclairage extérieur."),
                ("Commerces et locaux d'activité",
                 "Éclairage, prises et tableaux divisionnaires."),
            ],
            "faq": [
                ("Faites-vous des travaux électriques en local commercial ?",
                 "<p>Oui. Les locaux recevant du public répondent à des exigences "
                 "complémentaires, notamment en matière d'éclairage de sécurité et de coupure "
                 "d'urgence. Ces éléments sont examinés au cas par cas selon la nature et la "
                 "catégorie de l'établissement.</p>"),
                ("Combien de temps dure le remplacement d'un tableau ?",
                 "<p>Cela dépend du nombre de circuits, de l'état du câblage existant et de la "
                 "nécessité de reprendre la mise à la terre. Le remplacement s'accompagne d'une "
                 "coupure de courant pendant l'intervention, dont la durée est annoncée avant "
                 "le début des travaux.</p>"),
                ("Intervenez-vous vers Josselin et Guer ?",
                 "<p>Oui, ces communes du Morbihan font partie du périmètre d'intervention.</p>"),
            ],
        },
        {
            "slug": "electricien-auray",
            "name": "Auray",
            "lat": 47.6684, "lon": -2.9819,
            "title": "Électricien Auray (56) — Dépannage, rénovation, mise aux normes",
            "desc": ("Électricien à Auray : dépannage électrique, rénovation, tableau "
                     "électrique et mise aux normes dans le pays d'Auray."),
            "h1": "Électricien à Auray",
            "intro": "Interventions électriques à Auray, Saint-Goustan et dans le pays d'Auray.",
            "contexte": """
<p>Auray s'organise entre une ville haute et le quartier portuaire de Saint-Goustan, en
contrebas, au bord de la rivière. Ce dernier concentre un bâti ancien dense, en pierre, où
les logements sont souvent de petite taille et répartis sur plusieurs niveaux.</p>

<p>La proximité de l'eau et l'ancienneté des constructions se conjuguent : humidité dans
les niveaux bas, murs épais rendant les cheminements difficiles, installations reprises par
morceaux au fil du temps. La mise en sécurité — différentiels, mise à la terre, matériels
adaptés aux locaux humides — y constitue la priorité.</p>

<p>Le pays d'Auray, très touristique, compte une forte proportion de résidences secondaires
et de locations saisonnières, notamment vers la côte. Ces logements posent la question de
l'entretien d'installations peu utilisées et de leur sécurité pour des occupants de
passage.</p>
""",
            "secteurs": ["Centre-ville", "Saint-Goustan", "Le Loch", "Kerbois", "Brech",
                         "Pluneret", "Crach", "Carnac", "Quiberon"],
            "besoins": [
                ("Bâti ancien de Saint-Goustan",
                 "Humidité, cheminements contraints, installations reprises par morceaux."),
                ("Locations saisonnières",
                 "Sécurité pour des occupants de passage et tableau clairement repéré."),
                ("Résidences secondaires",
                 "Contrôle avant remise en service après plusieurs mois d'inoccupation."),
            ],
            "faq": [
                ("Une installation peu utilisée se dégrade-t-elle ?",
                 "<p>Oui. L'absence d'usage n'empêche ni l'humidité, ni la corrosion, ni les "
                 "dégradations dues aux rongeurs dans les combles. Un logement fermé plusieurs "
                 "mois par an mérite un contrôle périodique, en particulier des dispositifs "
                 "différentiels et de l'isolement des circuits extérieurs.</p>"),
                ("Faut-il tester les différentiels régulièrement ?",
                 "<p>Oui. Le bouton test présent sur chaque dispositif différentiel permet de "
                 "vérifier son déclenchement. Un test périodique — de l'ordre d'une fois par "
                 "mois — est recommandé par les fabricants, car un différentiel resté longtemps "
                 "inutilisé peut se bloquer mécaniquement.</p>"),
                ("Intervenez-vous vers Carnac et Quiberon ?",
                 "<p>Oui, ces communes du Morbihan font partie du périmètre d'intervention du "
                 "pays d'Auray.</p>"),
            ],
        },
    ],
})

# =========================================================================
DEPARTEMENTS.append({
    "code": "44",
    "name": "Loire-Atlantique",
    "slug": "loire-atlantique",
    "prep": "en Loire-Atlantique",
    "prefecture": "Nantes",
    "lat": 47.35, "lon": -1.75,
    "title": "Électricien Loire-Atlantique (44) — Dépannage, installation, rénovation",
    "desc": ("Électricien en Loire-Atlantique : dépannage électrique, recherche de panne, "
             "installation, rénovation et mise aux normes à Nantes, Saint-Nazaire, "
             "Saint-Herblain, Rezé et Ancenis."),
    "h1": "Électricien en Loire-Atlantique (44)",
    "chapo": ("Electricien Richard intervient en Loire-Atlantique, de la métropole nantaise à "
              "l'estuaire et au vignoble, pour le dépannage, l'installation, la rénovation et "
              "la mise aux normes électriques."),
    "contexte": """
<p>La Loire-Atlantique est le département le plus peuplé des six couverts, et son marché
immobilier est en tension constante. Cela se traduit par un volume élevé de rénovations
d'appartements et de maisons de ville, souvent réalisées à l'occasion d'un achat.</p>

<p>Nantes concentre un patrimoine bâti varié : immeubles du XIX<sup>e</sup> siècle,
maisons de ville nantaises, grands ensembles des années 1960-1970 et opérations récentes
sur l'Île de Nantes. Chaque strate pose des questions électriques distinctes, du tableau
saturé à l'absence pure et simple de conducteur de protection dans les logements les plus
anciens.</p>

<p>L'estuaire, autour de Saint-Nazaire, présente un profil marqué par la reconstruction
d'après-guerre et par l'activité industrielle. Enfin, le vignoble et le pays d'Ancenis
conservent un habitat ancien où les réhabilitations de longères et de maisons de bourg
génèrent des reprises complètes d'installation.</p>
""",
    "besoins": [
        "Rénovation électrique d'appartements et de maisons de ville",
        "Remplacement de tableaux dans les copropriétés",
        "Mise en sécurité avant location ou avant vente",
        "Reprise d'installations dans l'habitat ancien du vignoble et du pays d'Ancenis",
        "Bornes de recharge en maison individuelle et en copropriété",
        "Éclairage intérieur et extérieur, circuits spécialisés",
    ],
    "faq": [
        ("Intervenez-vous dans toute la Loire-Atlantique ?",
         "<p>Oui : Nantes et sa métropole, l'estuaire et la région nazairienne, le pays "
         "d'Ancenis, le vignoble nantais et le reste du département.</p>"),
        ("Peut-on installer une borne de recharge en copropriété ?",
         "<p>Oui. Le droit à la prise permet à un copropriétaire ou à un locataire de faire "
         "installer un point de recharge sur sa place de stationnement, à ses frais, après en "
         "avoir informé le syndic selon la procédure prévue. L'installation doit être réalisée "
         "dans les règles de l'art, sur un circuit dédié.</p>"),
        ("Combien de temps prend une rénovation électrique complète ?",
         "<p>La durée dépend de la surface, du nombre de circuits à créer et de la nature du "
         "bâti. Elle est également liée à l'état du logement : une rénovation menée dans un "
         "logement vide avance plus vite qu'une reprise réalisée en site occupé. Le planning "
         "est précisé lors de l'établissement du devis.</p>"),
    ],
    "cities": [
        {
            "slug": "electricien-nantes",
            "name": "Nantes",
            "lat": 47.2184, "lon": -1.5536,
            "title": "Électricien Nantes (44) — Dépannage électrique et rénovation",
            "desc": ("Électricien à Nantes : dépannage électrique, recherche de panne, "
                     "remplacement de tableau, rénovation d'appartement et mise aux normes."),
            "h1": "Électricien à Nantes",
            "intro": ("Dépannage, rénovation et mise en sécurité électrique à Nantes et dans "
                      "les communes de la métropole."),
            "contexte": """
<p>Nantes est une ville où l'électricien rencontre presque toutes les configurations
possibles, tant le parc immobilier y est stratifié.</p>

<p>Les immeubles de rapport du centre et des quartiers Hauts-Pavés – Saint-Félix ou
Canclaux, construits pour l'essentiel entre le XIX<sup>e</sup> siècle et l'entre-deux-
guerres, présentent des logements aux belles hauteurs sous plafond mais aux installations
souvent héritées de plusieurs campagnes de travaux. Les moulures et parquets d'origine
compliquent le passage de nouveaux circuits, ce qui suppose d'anticiper les cheminements.</p>

<p>Les maisons de ville nantaises, très présentes à Chantenay, Doulon ou Saint-Donatien,
posent un autre problème : leur organisation en longueur, sur plusieurs niveaux, produit
des installations étirées où le tableau se trouve rarement au bon endroit. Les extensions
successives — véranda, combles aménagés, garage transformé — y ont souvent été raccordées
au plus simple plutôt qu'au plus sûr.</p>

<p>Les grands ensembles des années 1960-1970, à Malakoff, Bellevue ou Le Breil,
correspondent au profil classique : mise à la terre présente mais tableau sous-dimensionné,
sans circuits spécialisés pour l'électroménager actuel.</p>

<p>Enfin, l'Île de Nantes et les opérations récentes relèvent d'une logique différente :
installations conformes à la norme en vigueur, où les demandes portent sur l'ajout de
points d'éclairage, la domotique ou l'installation d'un point de recharge en parking
collectif.</p>
""",
            "secteurs": ["Centre-ville", "Île de Nantes", "Hauts-Pavés – Saint-Félix",
                         "Chantenay", "Doulon – Bottière", "Malakoff", "Le Breil", "Nantes Nord",
                         "Saint-Herblain", "Rezé", "Orvault", "Saint-Sébastien-sur-Loire"],
            "besoins": [
                ("Immeubles anciens du centre",
                 "Cheminements contraints par les parquets et moulures, circuits hérités de "
                 "plusieurs campagnes de travaux."),
                ("Maisons de ville nantaises",
                 "Installations étirées sur plusieurs niveaux, extensions raccordées sans "
                 "reprise du tableau."),
                ("Grands ensembles des années 1960-1970",
                 "Tableaux sous-dimensionnés et absence de circuits spécialisés."),
                ("Programmes récents",
                 "Ajout de points d'éclairage, domotique, recharge en parking collectif."),
            ],
            "faq": [
                ("Dans quels quartiers de Nantes intervenez-vous ?",
                 "<p>Dans l'ensemble de la commune — centre, Île de Nantes, Hauts-Pavés – "
                 "Saint-Félix, Chantenay, Doulon – Bottière, Malakoff, Le Breil, Nantes Nord — "
                 "et dans les communes de la métropole comme Saint-Herblain, Rezé, Orvault ou "
                 "Saint-Sébastien-sur-Loire.</p>"),
                ("Comment rénover l'électricité d'un appartement ancien sans tout casser ?",
                 "<p>En exploitant les cheminements existants — gaines, plinthes techniques, "
                 "doublages, combles — et en regroupant les créations de circuits sur les zones "
                 "où des travaux sont déjà prévus, en particulier la cuisine et la salle "
                 "d'eau. Une visite préalable permet d'identifier ces passages et de limiter "
                 "les reprises de finition.</p>"),
                ("Mon logement date des années 1970, faut-il tout refaire ?",
                 "<p>Rarement en totalité. Ces logements disposent généralement d'une mise à la "
                 "terre et de conducteurs en bon état. Les travaux portent le plus souvent sur "
                 "le tableau, l'ajout de circuits spécialisés et la reprise des points "
                 "sensibles — cuisine, salle d'eau, extérieur.</p>"),
                ("Proposez-vous un dépannage électrique en urgence à Nantes ?",
                 "<p>Oui. Les situations à risque immédiat — odeur de brûlé, échauffement au "
                 "tableau, coupure totale, disjoncteur impossible à réarmer — sont traitées en "
                 "priorité, sur appel téléphonique.</p>"),
            ],
        },
        {
            "slug": "electricien-saint-nazaire",
            "name": "Saint-Nazaire",
            "lat": 47.2735, "lon": -2.2135,
            "title": "Électricien Saint-Nazaire (44) — Dépannage et rénovation",
            "desc": ("Électricien à Saint-Nazaire : dépannage électrique, remplacement de "
                     "tableau, rénovation et mise aux normes dans l'estuaire."),
            "h1": "Électricien à Saint-Nazaire",
            "intro": "Interventions électriques à Saint-Nazaire, dans l'estuaire et sur la côte.",
            "contexte": """
<p>Saint-Nazaire a été reconstruite après 1945 selon un plan d'urbanisme régulier. Le
centre-ville se compose donc majoritairement d'immeubles de cette période, avec des
installations électriques d'origine conçues pour des usages sans commune mesure avec ceux
d'aujourd'hui.</p>

<p>Dans ces immeubles, les demandes portent principalement sur le remplacement du tableau,
la création de circuits spécialisés pour la cuisine et la reprise des salles d'eau, où les
règles de volumes de protection sont fréquemment mal respectées dans les installations
anciennes.</p>

<p>Les quartiers plus pavillonnaires — Méan-Penhoët, Villès-Martin, Saint-Marc-sur-Mer —
et le front de mer ajoutent la dimension littorale : matériels extérieurs exposés,
alimentation d'annexes et de garages, éclairage de jardin. La proximité de l'océan y
accélère l'usure des équipements installés dehors.</p>
""",
            "secteurs": ["Centre-ville", "Méan-Penhoët", "Villès-Martin", "Saint-Marc-sur-Mer",
                         "Kerlédé", "Trignac", "Pornichet", "Montoir-de-Bretagne", "La Baule"],
            "besoins": [
                ("Immeubles de la reconstruction",
                 "Tableaux d'origine, absence de circuits spécialisés, salles d'eau à "
                 "reprendre."),
                ("Pavillonnaire et front de mer",
                 "Matériels extérieurs exposés, alimentation d'annexes et de garages."),
                ("Locaux professionnels",
                 "Éclairage et circuits en zone d'activité et locaux techniques."),
            ],
            "faq": [
                ("Quelles règles s'appliquent dans une salle de bains ?",
                 "<p>La norme définit des volumes autour de la baignoire et de la douche, dans "
                 "lesquels seuls certains matériels sont admis selon leur indice de protection. "
                 "S'y ajoutent l'obligation d'une liaison équipotentielle locale et la "
                 "protection de tous les circuits par un différentiel 30 mA. C'est l'un des "
                 "points les plus souvent non conformes dans les logements anciens.</p>"),
                ("Intervenez-vous à Pornichet, La Baule ou Trignac ?",
                 "<p>Oui, ces communes de Loire-Atlantique font partie du périmètre "
                 "d'intervention.</p>"),
                ("Comment protéger une prise extérieure ?",
                 "<p>Par un matériel prévu pour l'extérieur, avec couvercle et joint, un indice "
                 "de protection adapté à l'exposition, une fixation qui évite les infiltrations "
                 "par l'arrière, et une alimentation protégée par un différentiel 30 mA. Le "
                 "câble doit être adapté à la pose extérieure ou enterrée.</p>"),
            ],
        },
        {
            "slug": "electricien-saint-herblain",
            "name": "Saint-Herblain",
            "lat": 47.2172, "lon": -1.6486,
            "title": "Électricien Saint-Herblain (44) — Dépannage et installation",
            "desc": ("Électricien à Saint-Herblain : dépannage électrique, tableau électrique, "
                     "rénovation, mise aux normes et borne de recharge."),
            "h1": "Électricien à Saint-Herblain",
            "intro": "Interventions électriques à Saint-Herblain et à l'ouest de la métropole nantaise.",
            "contexte": """
<p>Deuxième commune de Loire-Atlantique par sa population, Saint-Herblain associe des
quartiers d'habitat collectif, un tissu pavillonnaire étendu et l'une des plus importantes
zones commerciales et tertiaires de la métropole.</p>

<p>Dans le pavillonnaire — construit pour l'essentiel entre les années 1970 et 1990 — les
installations disposent d'une mise à la terre et de circuits séparés, mais leur tableau
arrive saturé dès que l'on souhaite ajouter un usage : borne de recharge, atelier, pompe de
piscine, climatisation. La question posée est presque toujours celle de la place
disponible au tableau et de la puissance souscrite.</p>

<p>Dans les quartiers collectifs de Bellevue et du Sillon de Bretagne, les demandes portent
davantage sur la modernisation des tableaux privatifs et la mise en sécurité des
logements.</p>

<p>Les zones d'activité génèrent enfin des interventions en local professionnel :
éclairage, prises, tableaux divisionnaires, reprises après changement d'occupant.</p>
""",
            "secteurs": ["Bellevue", "Sillon de Bretagne", "Preux", "Le Tillay", "La Bourgonnière",
                         "Atlantis", "Couëron", "Orvault", "Indre"],
            "besoins": [
                ("Pavillons des années 1970-1990",
                 "Tableaux saturés, ajout de circuits dédiés, augmentation des usages."),
                ("Bornes de recharge",
                 "Circuit dédié, vérification de la puissance disponible et de la protection."),
                ("Locaux d'activité",
                 "Éclairage, prises et tableaux divisionnaires en zone tertiaire."),
            ],
            "faq": [
                ("Que faire si mon tableau n'a plus de place disponible ?",
                 "<p>Deux solutions existent : ajouter une rangée si le coffret le permet, ou "
                 "remplacer le tableau par un modèle offrant davantage de modules. Le choix "
                 "dépend de l'état du tableau existant, de la répartition des différentiels et "
                 "du nombre de circuits à créer.</p>"),
                ("Quelle puissance faut-il pour une borne de recharge ?",
                 "<p>Une borne domestique est le plus souvent installée en 3,7 kW ou 7,4 kW en "
                 "monophasé, ou jusqu'à 22 kW en triphasé lorsque le raccordement le permet. Le "
                 "choix dépend de la puissance souscrite, de la capacité du véhicule à "
                 "l'accepter et des autres usages simultanés du logement.</p>"),
                ("Intervenez-vous à Couëron, Orvault ou Indre ?",
                 "<p>Oui, ces communes de la métropole nantaise font partie du périmètre "
                 "d'intervention.</p>"),
            ],
        },
        {
            "slug": "electricien-reze",
            "name": "Rezé",
            "lat": 47.1836, "lon": -1.5490,
            "title": "Électricien Rezé (44) — Dépannage, rénovation, mise aux normes",
            "desc": ("Électricien à Rezé : dépannage électrique, rénovation, remplacement de "
                     "tableau et mise aux normes au sud de Nantes."),
            "h1": "Électricien à Rezé",
            "intro": "Interventions électriques à Rezé, Trentemoult et au sud de la Loire.",
            "contexte": """
<p>Rezé, sur la rive sud de la Loire, présente un parc immobilier composite. Le quartier de
Trentemoult, ancien village de pêcheurs aux maisons basses et serrées, contraste avec les
secteurs pavillonnaires plus récents et avec l'habitat collectif de Pont-Rousseau et du
Château.</p>

<p>À Trentemoult et dans les secteurs anciens en bord de Loire, les logements sont souvent
compacts, avec des murs épais et parfois des niveaux bas sensibles à l'humidité. Les
reprises portent sur la mise à la terre, la protection différentielle et le remplacement de
matériels vétustes.</p>

<p>Dans le pavillonnaire des années 1960 à 1990, la demande est plus classique :
remplacement de tableaux d'origine, création de circuits spécialisés, installation de
points de recharge, éclairage extérieur et alimentation de dépendances.</p>
""",
            "secteurs": ["Trentemoult", "Pont-Rousseau", "Château", "Ragon", "La Blordière",
                         "Les Sorinières", "Bouguenais", "Vertou"],
            "besoins": [
                ("Habitat ancien en bord de Loire",
                 "Mise à la terre, protection différentielle, matériels adaptés à l'humidité."),
                ("Pavillonnaire",
                 "Remplacement de tableaux, circuits dédiés, bornes de recharge."),
                ("Dépendances et extensions",
                 "Alimentation protégée et tableau divisionnaire."),
            ],
            "faq": [
                ("Comment savoir si mon tableau électrique est trop ancien ?",
                 "<p>Plusieurs indices sont parlants : présence de fusibles à broche, absence "
                 "d'interrupteur différentiel, absence de repérage des circuits, coffret en "
                 "matériau vieilli ou déformé, traces de chaleur ou de noircissement. Un seul "
                 "de ces signes justifie un examen.</p>"),
                ("Faut-il couper le courant pour ajouter un circuit ?",
                 "<p>Oui, toute intervention au tableau se fait hors tension. La coupure est "
                 "limitée à la durée du raccordement et son moment est convenu à l'avance, "
                 "notamment lorsque des appareils sensibles ou du matériel professionnel sont "
                 "alimentés.</p>"),
                ("Intervenez-vous au sud de Nantes ?",
                 "<p>Oui : Rezé, Bouguenais, Les Sorinières, Vertou et les communes voisines de "
                 "la rive sud.</p>"),
            ],
        },
        {
            "slug": "electricien-ancenis",
            "name": "Ancenis-Saint-Géréon",
            "lat": 47.3667, "lon": -1.1767,
            "title": "Électricien Ancenis-Saint-Géréon (44) — Dépannage et rénovation",
            "desc": ("Électricien à Ancenis-Saint-Géréon : dépannage électrique, rénovation, "
                     "tableau électrique et mise aux normes au bord de la Loire."),
            "h1": "Électricien à Ancenis-Saint-Géréon",
            "intro": "Interventions électriques à Ancenis-Saint-Géréon et dans le pays d'Ancenis.",
            "contexte": """
<p>Ancenis-Saint-Géréon, au bord de la Loire, associe un centre ancien, des quartiers
résidentiels et un tissu industriel notable. Le pays d'Ancenis, largement rural, complète
ce tableau avec des bourgs et un habitat dispersé.</p>

<p>Dans le centre et les bourgs alentour, les maisons anciennes présentent les
caractéristiques habituelles du bâti ligérien : murs épais, caves, dépendances. Les
installations y ont fréquemment été étendues sans reprise d'ensemble, et la mise à la terre
constitue le premier point à vérifier.</p>

<p>Les zones résidentielles plus récentes appellent des travaux d'adaptation :
remplacement de tableau, circuits spécialisés, bornes de recharge, alimentation de garages
et d'ateliers. Le tissu industriel et artisanal génère par ailleurs des besoins en locaux
professionnels.</p>
""",
            "secteurs": ["Centre-ville", "Saint-Géréon", "Les Ardennes", "Le Pont",
                         "Oudon", "Le Loroux-Bottereau", "Varades", "Ligné"],
            "besoins": [
                ("Maisons anciennes en bord de Loire",
                 "Mise à la terre, reprise des circuits étendus sans cohérence, caves humides."),
                ("Zones résidentielles",
                 "Tableaux, circuits spécialisés, bornes de recharge, ateliers."),
                ("Artisanat et industrie",
                 "Éclairage, prises et tableaux divisionnaires en local professionnel."),
            ],
            "faq": [
                ("Quels sont les premiers travaux à envisager dans une maison ancienne ?",
                 "<p>Dans l'ordre : vérifier l'existence et la qualité de la mise à la terre, "
                 "installer ou remplacer le tableau avec des différentiels 30 mA, puis reprendre "
                 "les circuits des pièces d'eau et de la cuisine. Le reste de l'installation "
                 "peut ensuite être traité par étapes.</p>"),
                ("Peut-on étaler une rénovation électrique dans le temps ?",
                 "<p>Oui, à condition de suivre un ordre cohérent : le tableau et la mise à la "
                 "terre d'abord, car ils conditionnent la sécurité de l'ensemble, puis les "
                 "circuits pièce par pièce. Cette approche évite de refaire deux fois les mêmes "
                 "travaux.</p>"),
                ("Intervenez-vous dans le pays d'Ancenis ?",
                 "<p>Oui, à Ancenis-Saint-Géréon et dans les communes environnantes de "
                 "Loire-Atlantique comme Oudon, Ligné, Varades ou Le Loroux-Bottereau.</p>"),
            ],
        },
    ],
})

# =========================================================================
DEPARTEMENTS.append({
    "code": "49",
    "name": "Maine-et-Loire",
    "slug": "maine-et-loire",
    "prep": "en Maine-et-Loire",
    "prefecture": "Angers",
    "lat": 47.40, "lon": -0.55,
    "title": "Électricien Maine-et-Loire (49) — Dépannage, installation, rénovation",
    "desc": ("Électricien en Maine-et-Loire : dépannage électrique, recherche de panne, "
             "installation, rénovation et mise aux normes à Angers, Cholet et Saumur."),
    "h1": "Électricien en Maine-et-Loire (49)",
    "chapo": ("Electricien Richard intervient en Maine-et-Loire, d'Angers au Saumurois et au "
              "Choletais, pour le dépannage, l'installation, la rénovation et la mise aux "
              "normes électriques."),
    "contexte": """
<p>Le Maine-et-Loire se distingue par son bâti en tuffeau, cette pierre calcaire tendre
caractéristique du Val de Loire. Ce matériau a une conséquence directe pour l'électricien :
il se travaille facilement, ce qui a longtemps favorisé les saignées et les modifications
successives, mais il est aussi sensible à l'humidité, notamment dans les niveaux bas et les
caves.</p>

<p>Le département compte par ailleurs un nombre important de caves creusées dans le
coteau, en particulier dans le Saumurois. Ces espaces — utilisés pour le vin, le stockage
ou parfois l'habitation troglodytique — présentent des conditions d'humidité permanente qui
imposent des choix de matériels et de protections spécifiques.</p>

<p>Angers, ville étudiante et pôle économique, concentre pour sa part une forte demande de
rénovation d'appartements et de mise en sécurité de logements locatifs, tandis que le
Choletais, plus industriel, génère des besoins en locaux professionnels comme en habitat
pavillonnaire.</p>
""",
    "besoins": [
        "Rénovation électrique dans le bâti en tuffeau",
        "Installations en caves et locaux troglodytiques humides",
        "Mise en sécurité de logements locatifs et étudiants",
        "Remplacement de tableaux et création de circuits spécialisés",
        "Bornes de recharge en maison individuelle",
        "Éclairage intérieur et extérieur",
    ],
    "faq": [
        ("Intervenez-vous dans tout le Maine-et-Loire ?",
         "<p>Oui : Angers et son agglomération, le Saumurois, le Choletais, le Segréen et les "
         "communes rurales du département.</p>"),
        ("Le tuffeau pose-t-il des problèmes pour l'électricité ?",
         "<p>Le tuffeau lui-même se perce et se saigne facilement. La difficulté vient plutôt "
         "de son comportement vis-à-vis de l'humidité : il absorbe l'eau et la restitue "
         "lentement. Dans les murs enterrés ou mal ventilés, cette humidité peut dégrader les "
         "matériels encastrés et provoquer des défauts d'isolement.</p>"),
        ("Quelles précautions dans une cave troglodytique ?",
         "<p>L'humidité y est permanente. Les matériels doivent présenter un indice de "
         "protection adapté, les circuits être protégés par un différentiel 30 mA, et les "
         "éléments conducteurs reliés à la liaison équipotentielle. Les installations "
         "provisoires — rallonges, multiprises, dominos — y sont particulièrement "
         "dangereuses.</p>"),
    ],
    "cities": [
        {
            "slug": "electricien-angers",
            "name": "Angers",
            "lat": 47.4784, "lon": -0.5632,
            "title": "Électricien Angers (49) — Dépannage électrique et rénovation",
            "desc": ("Électricien à Angers : dépannage électrique, recherche de panne, tableau "
                     "électrique, rénovation d'appartement et mise aux normes."),
            "h1": "Électricien à Angers",
            "intro": ("Dépannage, rénovation et mise en sécurité électrique à Angers et dans "
                      "l'agglomération angevine."),
            "contexte": """
<p>Angers présente un parc immobilier où le bâti ancien en tuffeau tient une place
importante, notamment dans le centre et le quartier de la Doutre, sur la rive droite de la
Maine. Ces immeubles anciens, souvent divisés en appartements, cumulent des installations
reprises à plusieurs reprises et des contraintes de cheminement liées à l'épaisseur des
murs et aux planchers bois.</p>

<p>La ville accueille une population étudiante nombreuse, ce qui se traduit par un parc
locatif important, avec de petites surfaces et des colocations. Pour les propriétaires
bailleurs, la mise en sécurité entre deux locations est une demande régulière : protection
différentielle, mise à la terre effective, nombre de prises suffisant pour éviter le
recours permanent aux multiprises.</p>

<p>Les quartiers de Belle-Beille, Monplaisir et les Justices, développés entre les années
1950 et 1970, présentent le profil habituel des grands ensembles de cette période :
installations dotées d'une terre mais tableaux sous-dimensionnés. En périphérie, le
pavillonnaire génère des demandes d'adaptation — bornes de recharge, extensions, éclairage
extérieur.</p>

<p>Enfin, la présence de caves sous une partie du bâti ancien, creusées dans le tuffeau,
impose une attention particulière aux matériels installés dans ces volumes humides.</p>
""",
            "secteurs": ["Centre-ville", "La Doutre", "Belle-Beille", "Monplaisir", "Les Justices",
                         "Saint-Serge", "Ney – Chalouère", "Avrillé", "Trélazé", "Les Ponts-de-Cé",
                         "Beaucouzé"],
            "besoins": [
                ("Immeubles anciens en tuffeau",
                 "Cheminements contraints, installations reprises par étapes, caves humides."),
                ("Parc locatif étudiant",
                 "Mise en sécurité entre deux locations et nombre de prises adapté."),
                ("Grands ensembles des années 1950-1970",
                 "Tableaux sous-dimensionnés et absence de circuits spécialisés."),
                ("Pavillonnaire périphérique",
                 "Bornes de recharge, extensions, éclairage extérieur."),
            ],
            "faq": [
                ("Dans quels quartiers d'Angers intervenez-vous ?",
                 "<p>Dans toute la commune — centre, La Doutre, Belle-Beille, Monplaisir, Les "
                 "Justices, Saint-Serge, Ney – Chalouère — ainsi qu'à Avrillé, Trélazé, Les "
                 "Ponts-de-Cé, Beaucouzé et les communes de l'agglomération.</p>"),
                ("Combien de prises faut-il dans un studio ou un petit logement ?",
                 "<p>La norme fixe des nombres minimaux par pièce en fonction de leur surface, "
                 "avec des exigences renforcées dans la cuisine et le séjour. Dans la pratique, "
                 "un logement correctement équipé est surtout un logement où le locataire n'a "
                 "pas besoin de multiprises en cascade : c'est le meilleur indicateur.</p>"),
                ("Quelles vérifications avant de louer un logement à Angers ?",
                 "<p>Contrôler la présence et le bon fonctionnement des dispositifs "
                 "différentiels, la continuité de la mise à la terre, l'état du tableau et son "
                 "repérage, ainsi que l'absence de matériel vétuste ou de montage provisoire. "
                 "Un diagnostic est par ailleurs requis pour les installations de plus de "
                 "quinze ans.</p>"),
                ("Faites-vous du dépannage électrique urgent à Angers ?",
                 "<p>Oui. Les situations présentant un risque immédiat sont traitées en "
                 "priorité, sur appel téléphonique : odeur de brûlé, échauffement au tableau, "
                 "coupure totale, disjoncteur qui refuse de se réarmer.</p>"),
            ],
        },
        {
            "slug": "electricien-cholet",
            "name": "Cholet",
            "lat": 47.0594, "lon": -0.8797,
            "title": "Électricien Cholet (49) — Dépannage, installation, rénovation",
            "desc": ("Électricien à Cholet : dépannage électrique, installation, rénovation, "
                     "tableau électrique et mise aux normes dans le Choletais."),
            "h1": "Électricien à Cholet",
            "intro": "Interventions électriques à Cholet et dans les communes du Choletais.",
            "contexte": """
<p>Cholet s'est construite autour d'une longue tradition industrielle, notamment textile.
Cette histoire a laissé un parc immobilier particulier : maisons ouvrières groupées,
anciens ateliers reconvertis, et un tissu pavillonnaire développé au fil de la croissance
économique de la ville.</p>

<p>Les maisons ouvrières anciennes présentent les caractéristiques habituelles de leur
époque : installations reprises plusieurs fois, tableaux placés dans des espaces exigus,
circuits sans conducteur de protection dans les parties les plus anciennes. Les
reconversions d'ateliers en logements ou en locaux d'activité impliquent, elles, des
reprises complètes, l'installation d'origine n'étant pas adaptée au nouvel usage.</p>

<p>Le pavillonnaire des dernières décennies appelle des demandes plus classiques :
remplacement de tableaux, ajout de circuits, bornes de recharge, alimentation de garages et
d'abris. Le tissu économique local génère par ailleurs des interventions en locaux
professionnels et commerciaux.</p>
""",
            "secteurs": ["Centre-ville", "Les Turbaudières", "Bretagne", "Bostangis",
                         "Le Puy-Saint-Bonnet", "La Séguinière", "Saint-Léger-sous-Cholet",
                         "Trémentines"],
            "besoins": [
                ("Maisons ouvrières anciennes",
                 "Tableaux exigus, circuits sans conducteur de protection, reprises "
                 "successives."),
                ("Reconversions de locaux",
                 "Installation d'origine inadaptée au nouvel usage, reprise complète."),
                ("Pavillonnaire et dépendances",
                 "Tableaux, circuits dédiés, garages, abris et bornes de recharge."),
            ],
            "faq": [
                ("Peut-on transformer un ancien atelier en logement ?",
                 "<p>Oui, mais l'installation électrique doit être entièrement repensée. Un "
                 "local d'activité et un logement ne répondent pas aux mêmes exigences : "
                 "nombre et nature des circuits, protections, volumes de sécurité dans les "
                 "pièces d'eau. Dans la pratique, l'installation est reprise à neuf.</p>"),
                ("Quelle protection pour un atelier ou un garage ?",
                 "<p>Un circuit dédié protégé au tableau, un différentiel 30 mA, et des "
                 "matériels adaptés à l'ambiance — poussière, humidité, chocs. Pour les "
                 "machines, un circuit spécialisé dimensionné à la puissance de l'appareil est "
                 "nécessaire.</p>"),
                ("Intervenez-vous autour de Cholet ?",
                 "<p>Oui : La Séguinière, Saint-Léger-sous-Cholet, Trémentines, Le "
                 "Puy-Saint-Bonnet et les communes du Choletais.</p>"),
            ],
        },
        {
            "slug": "electricien-saumur",
            "name": "Saumur",
            "lat": 47.2600, "lon": -0.0769,
            "title": "Électricien Saumur (49) — Dépannage, rénovation, caves et tuffeau",
            "desc": ("Électricien à Saumur : dépannage électrique, rénovation dans le bâti en "
                     "tuffeau, installations en cave, tableau électrique et mise aux normes."),
            "h1": "Électricien à Saumur",
            "intro": "Interventions électriques à Saumur, dans le Saumurois et le Val de Loire.",
            "contexte": """
<p>Saumur est sans doute la ville du département où les contraintes électriques liées au
bâti sont les plus spécifiques. La pierre de tuffeau y est omniprésente, et le coteau est
creusé de caves et de galeries utilisées pour la viticulture, le stockage, la culture des
champignons ou l'habitation troglodytique.</p>

<p>Dans ces volumes creusés, les conditions sont constantes : température fraîche et
humidité élevée toute l'année. Une installation électrique y subit une contrainte
permanente. Les matériels d'intérieur ordinaires s'y dégradent rapidement, les connexions
s'oxydent et les défauts d'isolement finissent par apparaître. Le choix de matériels à
indice de protection adapté, la protection différentielle et une liaison équipotentielle
soignée y sont indispensables.</p>

<p>Dans le centre-ville et les quartiers anciens, les maisons en tuffeau posent les
questions classiques du bâti ancien : installations reprises par étapes, mise à la terre
partielle, tableaux dépassés. Les logements avec cave ou sous-sol combinent souvent les
deux problématiques.</p>

<p>Enfin, l'activité viticole et touristique du Saumurois génère des besoins en locaux
professionnels : chais, caves de dégustation, hébergements, où les exigences de sécurité
électrique se cumulent avec des ambiances humides.</p>
""",
            "secteurs": ["Centre-ville", "Bagneux", "Saint-Hilaire-Saint-Florent", "Les Ponts",
                         "Nantilly", "Distré", "Varrains", "Chacé", "Montreuil-Bellay"],
            "besoins": [
                ("Caves et galeries troglodytiques",
                 "Humidité permanente : matériels à indice de protection adapté, différentiels, "
                 "liaison équipotentielle."),
                ("Maisons en tuffeau",
                 "Mise à la terre partielle, tableaux dépassés, reprises successives."),
                ("Chais et locaux viticoles",
                 "Éclairage et prises en ambiance humide, tableaux divisionnaires."),
            ],
            "faq": [
                ("Comment installer l'électricité dans une cave troglodytique ?",
                 "<p>En traitant l'humidité comme une donnée permanente et non comme un "
                 "incident : matériels à indice de protection adapté, boîtiers étanches avec "
                 "presse-étoupes correctement montés, câbles prévus pour ces conditions, "
                 "protection par différentiel 30 mA et liaison équipotentielle des éléments "
                 "conducteurs. Les installations provisoires sont à proscrire.</p>"),
                ("L'humidité peut-elle abîmer une installation neuve ?",
                 "<p>Oui, si les matériels ne sont pas adaptés. Une installation neuve mais "
                 "réalisée avec du matériel d'intérieur dans un local humide se dégradera en "
                 "quelques années. Le choix du matériel prime sur son ancienneté.</p>"),
                ("Intervenez-vous dans le Saumurois ?",
                 "<p>Oui : Saumur, Distré, Varrains, Chacé, Montreuil-Bellay et les communes "
                 "environnantes du Maine-et-Loire.</p>"),
            ],
        },
    ],
})

# ---- Verification stricte du perimetre geographique ----------------------
from content.site import DEPARTEMENTS_AUTORISES  # noqa: E402

for _d in DEPARTEMENTS:
    assert _d["code"] in DEPARTEMENTS_AUTORISES, (
        "Departement hors perimetre autorise : %s" % _d["code"])
assert len(DEPARTEMENTS) == 6, "Le site doit couvrir exactement 6 departements"


def all_cities():
    for dep in DEPARTEMENTS:
        for city in dep["cities"]:
            yield dep, city


def city_url(dep, city):
    return "/zones/%s/%s/" % (dep["slug"], city["slug"])


def dept_url(dep):
    return "/zones/%s/" % dep["slug"]


def map_points(scope=None):
    """Points de la carte interactive. scope=None -> tout le perimetre."""
    pts = []
    for dep in DEPARTEMENTS:
        if scope and scope != dep["slug"]:
            continue
        pts.append({"name": "%s (%s)" % (dep["name"], dep["code"]),
                    "lat": dep["lat"], "lon": dep["lon"], "type": "dept",
                    "sub": "Département couvert", "url": dept_url(dep)})
        for city in dep["cities"]:
            pts.append({"name": city["name"], "lat": city["lat"], "lon": city["lon"],
                        "type": "city", "sub": "%s (%s)" % (dep["name"], dep["code"]),
                        "url": city_url(dep, city)})
    return pts
