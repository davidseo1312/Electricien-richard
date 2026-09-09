# -*- coding: utf-8 -*-
"""Silo editorial : categories et articles de blog."""

CATEGORIES = [
    {"slug": "depannage-electrique", "name": "Dépannage électrique",
     "title": "Dépannage électrique — Articles et guides | Electricien Richard",
     "desc": ("Articles sur le dépannage électrique : disjoncteur qui saute, panne totale ou "
              "partielle, recherche de défaut et gestes à adopter."),
     "intro": ("Comprendre ce qui se passe quand l'électricité s'arrête : ce que signale une "
               "protection qui déclenche, comment isoler un défaut, et à quel moment il faut "
               "cesser d'essayer soi-même.")},
    {"slug": "installation-electrique", "name": "Installation électrique",
     "title": "Installation électrique — Articles et guides | Electricien Richard",
     "desc": ("Articles sur l'installation électrique : normes, circuits, tableau, "
              "dimensionnement et conception."),
     "intro": ("Comment se conçoit une installation : nombre de circuits, sections, "
               "protections et règles applicables aux logements.")},
    {"slug": "renovation", "name": "Rénovation",
     "title": "Rénovation électrique — Articles et guides | Electricien Richard",
     "desc": ("Articles sur la rénovation électrique : ordre des travaux, préparation d'un "
              "chantier, tableau et circuits à reprendre."),
     "intro": ("Reprendre une installation existante suppose de savoir par quoi commencer. "
               "Ces articles détaillent l'ordre logique des travaux et la préparation d'un "
               "chantier.")},
    {"slug": "securite-electrique", "name": "Sécurité électrique",
     "title": "Sécurité électrique — Articles et guides | Electricien Richard",
     "desc": ("Articles sur la sécurité électrique : installations dangereuses, protection "
              "différentielle, mise à la terre et risques domestiques."),
     "intro": ("Les points qui protègent réellement les personnes : mise à la terre, "
               "dispositifs différentiels, état des matériels et signaux d'alerte.")},
    {"slug": "conseils", "name": "Conseils",
     "title": "Conseils électricité — Articles pratiques | Electricien Richard",
     "desc": ("Conseils pratiques en électricité : choisir un professionnel, lire un devis, "
              "préparer une intervention."),
     "intro": ("Des repères pratiques pour faire des choix informés avant, pendant et après "
               "des travaux électriques.")},
    {"slug": "prix", "name": "Prix",
     "title": "Prix des travaux électriques — Articles | Electricien Richard",
     "desc": ("Articles sur le prix des travaux électriques : ce qui compose un devis et ce "
              "qui fait varier un chiffrage."),
     "intro": ("Comprendre ce qui compose un prix permet de comparer des devis sur leur "
               "contenu plutôt que sur leur seul total.")},
    {"slug": "bornes-de-recharge", "name": "Bornes de recharge",
     "title": "Bornes de recharge — Articles et guides | Electricien Richard",
     "desc": ("Articles sur les bornes de recharge pour véhicule électrique : puissances, "
              "installation, copropriété et protections."),
     "intro": ("Installer un point de recharge chez soi : ce que cela suppose côté "
               "installation électrique, en maison comme en copropriété.")},
    {"slug": "guide-local", "name": "Guide local",
     "title": "Guide local électricité — Bretagne et Pays de la Loire | Electricien Richard",
     "desc": ("Guides locaux : particularités électriques de l'habitat en Bretagne et en "
              "Pays de la Loire."),
     "intro": ("Le bâti local a ses propres contraintes électriques. Ces guides détaillent ce "
               "que l'on rencontre concrètement dans les six départements couverts.")},
]

ARTICLES = []

ARTICLES.append({
    "slug": "pourquoi-mon-disjoncteur-saute",
    "category": "depannage-electrique",
    "date": "2026-02-12",
    "updated": "2026-06-18",
    "title": "Pourquoi mon disjoncteur saute ? Les 6 causes réelles",
    "meta_title": "Pourquoi mon disjoncteur saute ? Causes et solutions | Electricien Richard",
    "desc": ("Disjoncteur qui saute : surcharge, court-circuit, fuite de courant, appareil "
             "défectueux, humidité ou matériel usé. Comment identifier la cause et que "
             "faire."),
    "h1": "Pourquoi mon disjoncteur saute ?",
    "chapo": ("Un disjoncteur qui déclenche n'est pas un caprice : c'est une protection qui "
              "fait exactement ce qu'on attend d'elle. La vraie question est de savoir ce "
              "qu'elle signale."),
    "quick": ("<p><strong>Un disjoncteur saute pour trois raisons principales : une surcharge, "
              "un court-circuit, ou une fuite de courant vers la terre.</strong> Le dispositif "
              "qui a déclenché indique déjà laquelle : un disjoncteur divisionnaire signale "
              "une surcharge ou un court-circuit, un interrupteur différentiel signale une "
              "fuite de courant.</p>"
              "<p>Pour identifier la cause : débranchez tous les appareils du circuit, "
              "réarmez une fois, puis rebranchez les appareils un par un.</p>"),
    "body": """
<h2 id="cause-1">1. La surcharge du circuit</h2>

<p>C'est la cause la plus fréquente et la plus simple. Un circuit est dimensionné pour une
intensité donnée. Lorsque les appareils qui y sont raccordés demandent davantage, le
disjoncteur coupe après un délai qui dépend de l'ampleur du dépassement.</p>

<p>Le scénario typique : dans une cuisine ancienne, le four, la bouilloire et le
micro-ondes partagent le même circuit. Séparément, chacun fonctionne ; ensemble, ils
déclenchent la protection.</p>

<p><strong>Comment la reconnaître :</strong> le déclenchement survient après quelques minutes
d'usage simultané, et jamais lorsqu'un seul appareil fonctionne.</p>

<p><strong>La solution :</strong> créer un circuit spécialisé pour les gros appareils. La
norme l'impose d'ailleurs pour les installations actuelles. Augmenter le calibre du
disjoncteur ne règle rien et supprime la protection du câble.</p>

<h2 id="cause-2">2. Le court-circuit</h2>

<p>Un <a href="/court-circuit.html">court-circuit</a> est un contact direct entre deux
conducteurs, sans passer par un appareil. L'intensité devient très élevée en une fraction de
seconde, et la protection coupe instantanément.</p>

<p><strong>Comment le reconnaître :</strong> le déclenchement est immédiat, souvent au moment
précis d'un branchement, d'un actionnement d'interrupteur ou d'un mouvement de câble. Il
peut s'accompagner d'un bruit sec ou d'une odeur.</p>

<p><strong>La solution :</strong> identifier le point de défaut. S'il s'agit d'un appareil,
il est hors d'usage. S'il s'agit de l'installation, une
<a href="/recherche-panne.html">recherche de panne</a> est nécessaire.</p>

<h2 id="cause-3">3. Une fuite de courant vers la terre</h2>

<p>Ici, ce n'est pas le disjoncteur divisionnaire qui coupe, mais l'interrupteur
différentiel. Il détecte qu'une partie du courant ne revient pas par le neutre : elle
s'échappe vers la terre, par un défaut d'isolement.</p>

<p><strong>Comment la reconnaître :</strong> plusieurs circuits sont coupés d'un coup — tous
ceux que protège le différentiel concerné.</p>

<p><strong>La solution :</strong> isoler le circuit fautif en ouvrant les disjoncteurs un à
un, puis mesurer l'isolement du circuit identifié.</p>

<h2 id="cause-4">4. Un appareil défectueux</h2>

<p>Un appareil dont l'isolement se dégrade provoque des déclenchements du différentiel. Les
plus fréquemment en cause sont ceux qui chauffent de l'eau : chauffe-eau, lave-linge,
lave-vaisselle. La résistance percée laisse fuir un courant vers la terre.</p>

<p><strong>Un indice très parlant :</strong> si la coupure se produit toujours à la même
heure, le chauffe-eau est le premier suspect — il se met en route en heures creuses.</p>

<h2 id="cause-5">5. L'humidité</h2>

<p>L'eau réduit l'isolement. Un circuit extérieur, une prise de terrasse, un luminaire de
façade ou un coffret mal étanche peuvent parfaitement fonctionner par temps sec et faire
déclencher le différentiel après une forte pluie.</p>

<p><strong>Comment la reconnaître :</strong> corrélation nette avec la météo. Les
déclenchements surviennent après la pluie ou en période humide, puis cessent.</p>

<p><strong>La solution :</strong> identifier le circuit extérieur concerné, remplacer les
matériels dont l'étanchéité est compromise et reprendre les raccordements corrodés. Sur le
littoral, la corrosion saline accélère fortement ce phénomène.</p>

<h2 id="cause-6">6. Un dispositif de protection usé</h2>

<p>Les protections vieillissent. Un différentiel peut devenir trop sensible et déclencher
sans défaut réel — ou, plus grave, ne plus déclencher du tout.</p>

<p><strong>Le test qui compte :</strong> chaque différentiel possède un bouton de test. Il
doit provoquer le déclenchement immédiat. S'il ne se passe rien, le dispositif ne protège
plus personne et doit être remplacé sans délai. Ce test est à réaliser environ une fois par
mois.</p>

<h2 id="methode">La méthode pour identifier la cause</h2>

<ol class="steps">
<li><h3>Observer le tableau</h3><p>Repérer quel dispositif est en position basse : divisionnaire, différentiel ou disjoncteur de branchement.</p></li>
<li><h3>Tout débrancher</h3><p>Débrancher les appareils du ou des circuits concernés.</p></li>
<li><h3>Réarmer une fois</h3><p>Une seule tentative. Si le déclenchement est immédiat, ne pas insister.</p></li>
<li><h3>Rebrancher un par un</h3><p>Attendre quelques instants entre chaque appareil pour identifier celui qui provoque la coupure.</p></li>
<li><h3>Conclure</h3><p>Si tout tient sans appareil mais coupe avec l'un d'eux : l'appareil est en cause. Si cela coupe même à vide : le défaut est dans l'installation.</p></li>
</ol>

<div class="callout callout--danger"><strong>Ce qu'il ne faut jamais faire</strong>
<p>Ne remplacez jamais un disjoncteur par un calibre supérieur pour « qu'il ne saute
plus ». Le câble n'est alors plus protégé et peut chauffer jusqu'à l'incendie sans que rien
ne coupe. De même, ne réarmez pas en boucle une protection qui déclenche immédiatement.</p>
</div>
""",
    "faq": [
        ("Mon disjoncteur saute toujours à la même heure, pourquoi ?",
         "<p>Un appareil programmé est presque toujours en cause. Le chauffe-eau, qui démarre "
         "en heures creuses, arrive largement en tête : une résistance dont l'isolement s'est "
         "dégradé fait déclencher le différentiel au moment exact de sa mise en route.</p>"),
        ("Est-ce dangereux si mon disjoncteur saute souvent ?",
         "<p>Le déclenchement en lui-même est une protection qui fonctionne. Ce qui est "
         "préoccupant, c'est la cause : une surcharge répétée signifie que des conducteurs sont "
         "sollicités au-delà de ce pour quoi ils ont été prévus, et une fuite de courant "
         "récurrente signale un défaut d'isolement qui s'aggrave.</p>"),
        ("Puis-je remettre le courant en attendant l'électricien ?",
         "<p>Oui, si le circuit tient une fois les appareils débranchés et si aucun signe "
         "d'échauffement n'est présent. En revanche, en cas d'odeur de brûlé, de fumée ou de "
         "chaleur anormale, laissez le circuit coupé.</p>"),
    ],
    "related_services": ["disjoncteur", "court-circuit", "recherche-panne", "electricien-depannage"],
})

ARTICLES.append({
    "slug": "que-faire-en-cas-de-panne-electrique",
    "category": "depannage-electrique",
    "date": "2026-03-04",
    "updated": "2026-07-02",
    "title": "Que faire en cas de panne électrique ? La marche à suivre",
    "meta_title": "Que faire en cas de panne électrique ? Marche à suivre | Electricien Richard",
    "desc": ("Panne électrique totale ou partielle : les vérifications à mener dans l'ordre, "
             "les gestes à éviter et le moment où il faut appeler un professionnel."),
    "h1": "Que faire en cas de panne électrique ?",
    "chapo": ("Face à une coupure, quelques vérifications simples permettent souvent de "
              "situer l'origine du problème — et parfois de le résoudre — avant même "
              "d'appeler."),
    "quick": ("<p><strong>Dans l'ordre : vérifiez si vos voisins ont du courant, regardez "
              "quel dispositif a déclenché au tableau, débranchez les appareils du circuit "
              "concerné, puis réarmez une seule fois.</strong></p>"
              "<p>Si la protection déclenche à nouveau immédiatement, sans aucun appareil "
              "branché, n'insistez pas : le défaut est dans l'installation et relève d'un "
              "professionnel.</p>"),
    "body": """
<h2 id="etape-1">Étape 1 : la coupure vient-elle de chez vous ?</h2>

<p>C'est la première question, et elle se règle en quelques secondes. Si les voisins sont
également privés d'électricité, ou si l'éclairage public est éteint, l'origine est sur le
réseau public. Aucune intervention chez vous ne servira à rien : il faut signaler la coupure
au gestionnaire de réseau.</p>

<p>Si vous êtes le seul concerné, le problème se situe dans votre branchement ou votre
installation.</p>

<h2 id="etape-2">Étape 2 : lire le tableau électrique</h2>

<p>Le dispositif qui a déclenché indique la nature du problème.</p>

<div class="table-wrap"><table>
<caption>Ce que signale chaque dispositif</caption>
<thead><tr><th scope="col">Dispositif en position basse</th><th scope="col">Ce que cela signifie</th></tr></thead>
<tbody>
<tr><td>Disjoncteur de branchement (près du compteur)</td><td>Puissance souscrite dépassée, ou défaut affectant l'ensemble de l'installation</td></tr>
<tr><td>Interrupteur différentiel</td><td>Fuite de courant vers la terre sur l'un des circuits qu'il protège</td></tr>
<tr><td>Disjoncteur divisionnaire</td><td>Surcharge ou court-circuit sur ce circuit précis</td></tr>
<tr><td>Rien n'est déclenché</td><td>Défaut d'alimentation en amont, ou coupure interne : ne pas intervenir sur le comptage</td></tr>
</tbody></table></div>

<h2 id="etape-3">Étape 3 : isoler la cause</h2>

<p>La méthode est toujours la même, quel que soit le dispositif concerné.</p>

<ol>
<li>Ouvrir tous les disjoncteurs divisionnaires du tableau.</li>
<li>Réarmer le dispositif qui avait déclenché.</li>
<li>Refermer les circuits un par un, en marquant un temps d'arrêt entre chacun.</li>
<li>Lorsque le déclenchement se reproduit, le dernier circuit refermé est le circuit
fautif.</li>
<li>Sur ce circuit, débrancher tous les appareils, puis les rebrancher un à un.</li>
</ol>

<p>Cette démarche permet de distinguer trois situations : un appareil défectueux, une
surcharge d'usage, ou un défaut de l'installation elle-même.</p>

<h2 id="etape-4">Étape 4 : ce qu'il ne faut pas faire</h2>

<ul>
<li><strong>Réarmer en boucle.</strong> Chaque tentative sur un défaut franc provoque un
nouvel arc au point de contact et aggrave l'échauffement.</li>
<li><strong>Bloquer ou caler une protection.</strong> C'est supprimer la sécurité.</li>
<li><strong>Changer un disjoncteur pour un calibre plus élevé.</strong> Le câble n'est alors
plus protégé.</li>
<li><strong>Ouvrir le tableau et manipuler les conducteurs</strong> sans compétence ni
vérification de l'absence de tension.</li>
<li><strong>Toucher le panneau de comptage.</strong> Il relève du gestionnaire de réseau.</li>
</ul>

<h2 id="urgence">Quand la panne devient une urgence</h2>

<p>Certains signes imposent de couper le disjoncteur général et d'appeler immédiatement :
odeur de brûlé, fumée, noircissement d'une prise ou du tableau, chaleur anormale, crépitement
ou arc visible, sensation de picotement au contact d'un appareil.</p>

<p>En cas de début d'incendie ou si une personne est en contact avec une source électrique,
appelez les secours (18 ou 112) et ne touchez jamais la personne avant d'avoir coupé
l'alimentation. Voir <a href="/electricien-urgence.html">électricien en urgence</a>.</p>

<h2 id="preparer">Préparer l'appel à l'électricien</h2>

<p>Quelques informations font gagner un temps considérable au diagnostic :</p>

<ul>
<li>l'étendue de la panne : tout le logement, une pièce, un seul appareil ;</li>
<li>quel dispositif a déclenché au tableau ;</li>
<li>ce qui s'est passé juste avant : mise en route d'un appareil, orage, travaux, pluie ;</li>
<li>si la panne est permanente ou intermittente ;</li>
<li>ce que vous avez déjà tenté, et le résultat obtenu ;</li>
<li>l'âge approximatif de l'installation et le type de tableau — à fusibles ou à
disjoncteurs.</li>
</ul>
""",
    "faq": [
        ("Comment savoir si la panne vient d'EDF ou de mon installation ?",
         "<p>Si vos voisins sont aussi sans courant, la coupure vient du réseau public et doit "
         "être signalée au gestionnaire de réseau. Si vous êtes seul concerné et qu'un "
         "dispositif est déclenché à votre tableau, le défaut est chez vous.</p>"),
        ("Que faire si le disjoncteur ne se réarme pas du tout ?",
         "<p>Ouvrez d'abord tous les circuits divisionnaires, puis retentez le réarmement. "
         "S'il tient ainsi, le défaut est sur l'un des circuits. S'il refuse toujours de "
         "tenir alors que tous les circuits sont ouverts, le défaut se situe en amont : "
         "n'insistez pas et faites intervenir un professionnel.</p>"),
        ("Mon congélateur est plein, la panne est-elle prioritaire ?",
         "<p>Ce type de situation est traité en priorité. En attendant, laissez l'appareil "
         "fermé : un congélateur plein et non ouvert conserve sa température pendant plusieurs "
         "heures. Vous pouvez aussi tenter de l'alimenter temporairement depuis un circuit "
         "resté fonctionnel avec un cordon adapté.</p>"),
    ],
    "related_services": ["panne-electrique", "electricien-depannage", "electricien-urgence",
                         "disjoncteur"],
})

ARTICLES.append({
    "slug": "reconnaitre-une-installation-electrique-dangereuse",
    "category": "securite-electrique",
    "date": "2026-01-22",
    "updated": "2026-05-14",
    "title": "Comment reconnaître une installation électrique dangereuse",
    "meta_title": "Reconnaître une installation électrique dangereuse | Electricien Richard",
    "desc": ("Les signes qui révèlent une installation électrique dangereuse : tableau, mise "
             "à terre, protections, matériels et montages à risque."),
    "h1": "Comment reconnaître une installation électrique dangereuse",
    "chapo": ("Une installation ancienne n'est pas forcément dangereuse. Une installation "
              "récente peut l'être. Ce qui compte, ce sont des points précis, que l'on peut "
              "pour la plupart observer soi-même."),
    "quick": ("<p><strong>Cinq signes doivent alerter : un tableau à fusibles à broche, "
              "l'absence de dispositif différentiel 30 mA, l'absence de mise à la terre, des "
              "traces d'échauffement, et des montages provisoires devenus permanents.</strong></p>"
              "<p>Un seul de ces éléments justifie un examen de l'installation. L'absence de "
              "terre et l'absence de différentiel sont les deux défauts qui exposent "
              "directement les personnes.</p>"),
    "body": """
<h2 id="tableau">1. Regardez le tableau électrique</h2>

<p>C'est le point de départ, et il ne demande aucune compétence particulière.</p>

<h3>Des fusibles à broche</h3>
<p>Ces petits cylindres de porcelaine que l'on remplace à la main appartiennent à une autre
époque. Ils ne permettent ni protection différentielle adaptée, ni repérage, ni évolution.
Leur présence signale une installation qui n'a pas été reprise depuis longtemps.</p>

<h3>Aucun interrupteur différentiel</h3>
<p>Un différentiel se repère à son bouton de test, généralement marqué « T ». S'il n'y en a
aucun sur le tableau, l'installation ne dispose d'aucune protection contre l'électrisation
par défaut d'isolement. C'est le défaut le plus grave après l'absence de terre.</p>

<h3>Des traces de chaleur</h3>
<p>Noircissement autour d'une borne, plastique jauni ou déformé, odeur au niveau du tableau :
une connexion chauffe. Il s'agit d'une situation à traiter sans attendre.</p>

<h3>Aucun repérage</h3>
<p>Un tableau dont les circuits ne sont pas identifiés rend toute intervention hasardeuse :
impossible de savoir ce que l'on coupe. Le repérage est une exigence de la norme, pas un
confort.</p>

<h2 id="terre">2. Vérifiez la présence d'une mise à la terre</h2>

<p>La mise à la terre permet d'évacuer un courant de défaut. Sans elle, la carcasse
métallique d'un appareil défectueux peut rester sous tension : une personne qui la touche
devient le chemin de passage du courant.</p>

<p>Attention à un piège fréquent : la présence d'une broche de terre sur les prises ne
prouve rien. Cette broche peut n'être reliée à rien du tout, en particulier lorsque des
prises modernes ont été posées sur des circuits anciens. Seule une mesure permet de le
vérifier.</p>

<p>Un indice observable : la présence d'une barrette de terre, généralement près du tableau,
et d'un conducteur vert-jaune qui en part.</p>

<h2 id="materiels">3. Examinez les matériels et les montages</h2>

<ul>
<li><strong>Prises fendues, cassées ou qui bougent</strong> dans leur boîtier, laissant
parfois apparaître des parties sous tension.</li>
<li><strong>Conducteurs apparents non protégés</strong>, agrafés le long d'une plinthe ou
courant dans un placard.</li>
<li><strong>Dominos nus</strong> pendant d'un plafond ou dissimulés derrière un meuble.</li>
<li><strong>Ruban adhésif</strong> utilisé comme isolation.</li>
<li><strong>Rallonges permanentes</strong> traversant une pièce ou passant sous un
tapis.</li>
<li><strong>Multiprises en cascade</strong>, une multiprise branchée sur une autre.</li>
<li><strong>Conducteurs en tissu</strong> ou isolant cassant, typiques des installations
d'avant les années 1960.</li>
</ul>

<h2 id="pieces-eau">4. Contrôlez les pièces d'eau</h2>

<p>La salle de bains est le local le plus exposé. Les points à observer :</p>

<ul>
<li>une prise ou un interrupteur trop proche de la baignoire ou de la douche ;</li>
<li>un luminaire non prévu pour un local humide ;</li>
<li>un appareil de chauffage mobile utilisé dans la pièce ;</li>
<li>l'absence de liaison équipotentielle locale, qui relie entre eux les éléments
conducteurs de la pièce.</li>
</ul>

<h2 id="signaux">5. Écoutez les signaux de fonctionnement</h2>

<p>Certains symptômes traduisent un problème même en l'absence de défaut visible :</p>

<div class="table-wrap"><table>
<caption>Symptômes et ce qu'ils révèlent</caption>
<thead><tr><th scope="col">Symptôme</th><th scope="col">Ce que cela révèle</th></tr></thead>
<tbody>
<tr><td>Prise ou interrupteur tiède</td><td>Connexion desserrée ou circuit surchargé</td></tr>
<tr><td>Éclairage qui vacille</td><td>Faux contact sur le circuit</td></tr>
<tr><td>Crépitement au branchement</td><td>Contacts usés ou amorçage</td></tr>
<tr><td>Picotement au contact d'un appareil</td><td>Défaut d'isolement, masse sous tension</td></tr>
<tr><td>Odeur de plastique chaud</td><td>Échauffement en cours : couper immédiatement</td></tr>
<tr><td>Différentiel qui déclenche par temps humide</td><td>Défaut d'isolement sur un circuit exposé</td></tr>
</tbody></table></div>

<h2 id="test">Le test que tout le monde devrait faire</h2>

<p>Appuyez sur le bouton test de chaque interrupteur différentiel de votre tableau. Le
dispositif doit couper instantanément. S'il ne se passe rien, la protection ne fonctionne
plus : elle est présente, mais elle ne protège personne.</p>

<p>Ce test est à réaliser environ une fois par mois. Il ne prend que quelques secondes et
constitue la vérification la plus utile qu'un occupant puisse faire lui-même.</p>

<h2 id="suite">Que faire si vous constatez plusieurs de ces signes</h2>

<p>Un <a href="/diagnostic-electrique.html">diagnostic de l'installation</a> permet
d'objectiver l'état réel et surtout de hiérarchiser. Tout ne se traite pas en même temps :
la mise à la terre et la protection différentielle passent avant le confort, et le tableau
avant les circuits secondaires. Voir aussi
<a href="/mise-aux-normes-electrique.html">mise aux normes électrique</a>.</p>
""",
    "faq": [
        ("Une installation de 30 ans est-elle dangereuse ?",
         "<p>Pas nécessairement. Une installation des années 1990 dispose généralement d'une "
         "mise à la terre et de conducteurs corrects. Les points à vérifier sont la présence "
         "d'un différentiel 30 mA sur l'ensemble des circuits, l'état du tableau et la "
         "conformité des pièces d'eau.</p>"),
        ("Comment savoir si mes prises sont vraiment reliées à la terre ?",
         "<p>La présence d'une broche de terre ne prouve rien : elle peut ne pas être "
         "raccordée. Seule une mesure de continuité entre la broche de terre de la prise et la "
         "barrette de terre permet de le confirmer. C'est l'un des premiers contrôles réalisés "
         "lors d'un diagnostic.</p>"),
        ("Mon assurance peut-elle refuser d'indemniser un sinistre électrique ?",
         "<p>Un assureur peut opposer des réserves lorsqu'un sinistre résulte d'une "
         "installation manifestement défectueuse ou de travaux réalisés sans respect des "
         "règles. Les modalités dépendent du contrat : conserver les devis, factures et "
         "attestations des travaux réalisés par un professionnel est toujours utile.</p>"),
    ],
    "related_services": ["diagnostic-electrique", "mise-aux-normes-electrique",
                         "tableau-electrique", "renovation-electrique"],
})

ARTICLES.append({
    "slug": "quand-changer-son-tableau-electrique",
    "category": "renovation",
    "date": "2026-04-08",
    "updated": None,
    "title": "Quand faut-il changer son tableau électrique ?",
    "meta_title": "Quand changer son tableau électrique ? | Electricien Richard",
    "desc": ("Les signes indiquant qu'un tableau électrique doit être remplacé, ce que "
             "comprend l'opération et ce qu'elle change réellement pour la sécurité."),
    "h1": "Quand faut-il changer son tableau électrique ?",
    "chapo": ("Le tableau est le point de passage obligé de toute l'installation. Son "
              "remplacement fait partie des travaux au meilleur rapport entre coût et gain de "
              "sécurité — à condition de savoir ce qu'il règle et ce qu'il ne règle pas."),
    "quick": ("<p><strong>Un tableau doit être remplacé s'il comporte des fusibles à broche, "
              "s'il ne dispose pas de dispositif différentiel 30 mA, s'il présente des traces "
              "d'échauffement, ou si son boîtier est détérioré.</strong></p>"
              "<p>Il gagne également à l'être lorsqu'il n'offre plus aucun emplacement libre, "
              "empêchant tout ajout de circuit.</p>"),
    "body": """
<h2 id="obligatoire">Les cas où le remplacement s'impose</h2>

<h3>Un tableau à fusibles à broche</h3>
<p>Ces fusibles ne permettent aucune protection différentielle intégrée, aucun repérage
fiable et aucune évolution. Ils imposent en outre une manipulation manuelle à chaque
incident, avec le risque de remplacer par un calibre inadapté.</p>

<h3>L'absence de protection différentielle 30 mA</h3>
<p>Sans elle, rien ne protège les personnes contre une électrisation due à un défaut
d'isolement. C'est, avec l'absence de mise à la terre, le défaut le plus critique d'une
installation.</p>

<h3>Des traces d'échauffement</h3>
<p>Noircissement, plastique déformé, odeur : une connexion chauffe. Le phénomène s'aggrave
seul, la chaleur dégradant encore la qualité du contact.</p>

<h3>Un boîtier détérioré</h3>
<p>Capot manquant, boîtier fissuré, parties sous tension accessibles : le tableau ne remplit
plus sa fonction de protection contre les contacts directs.</p>

<h3>Un différentiel qui ne réagit pas au test</h3>
<p>Un dispositif qui ne déclenche pas lorsqu'on appuie sur son bouton test est hors service.
Il donne une illusion de protection, ce qui est pire que son absence.</p>

<h2 id="souhaitable">Les cas où c'est fortement recommandé</h2>

<ul>
<li><strong>Plus aucun module libre.</strong> Impossible d'ajouter un circuit pour une
<a href="/borne-recharge.html">borne de recharge</a>, une extension ou un nouvel
équipement.</li>
<li><strong>Trop de circuits derrière un seul différentiel.</strong> Le moindre défaut
plonge la moitié du logement dans le noir, et complique le diagnostic.</li>
<li><strong>Aucun repérage.</strong> On ne sait pas ce que coupe chaque protection.</li>
<li><strong>Ajouts successifs.</strong> Tableau complété au fil des années, avec des
matériels de générations différentes.</li>
<li><strong>Vente ou mise en location.</strong> Le tableau est l'un des premiers points
examinés lors d'un diagnostic.</li>
</ul>

<h2 id="contenu">Ce que comprend un remplacement</h2>

<p>Remplacer un tableau ne consiste pas seulement à changer un coffret. L'opération
comprend :</p>

<ol class="steps">
<li><h3>Le relevé des circuits</h3><p>Identification de chaque départ, de sa section et de son usage réel.</p></li>
<li><h3>Le dimensionnement</h3><p>Nombre de rangées, répartition des différentiels par type, modules libres à prévoir.</p></li>
<li><h3>La dépose et la pose</h3><p>Mise hors tension, dépose de l'ancien matériel, pose du nouveau coffret.</p></li>
<li><h3>Le raccordement</h3><p>Reprise des circuits, du bornier de terre et du bornier de neutre.</p></li>
<li><h3>Le repérage</h3><p>Étiquetage clair de chaque protection.</p></li>
<li><h3>Les essais</h3><p>Test des différentiels, vérification des circuits, contrôle des serrages.</p></li>
</ol>

<h2 id="limites">Ce qu'un tableau neuf ne règle pas</h2>

<p>C'est le point le plus mal compris. Un tableau neuf protège mieux, mais il ne transforme
pas des circuits vétustes en circuits neufs.</p>

<p>Si les conducteurs sont dégradés, si certains circuits sont dépourvus de conducteur de
protection, ou si les sections sont insuffisantes pour les usages actuels, ces problèmes
subsistent après le remplacement. Un tableau moderne les révélera d'ailleurs souvent : les
différentiels, plus sensibles et plus nombreux, déclencheront sur des défauts que l'ancienne
installation laissait passer inaperçus.</p>

<p>C'est pourquoi un relevé de l'état des circuits précède toujours un remplacement : il
permet de savoir si l'opération suffira ou si elle doit s'inscrire dans une
<a href="/renovation-electrique.html">rénovation plus large</a>.</p>

<h2 id="terre">Le lien avec la mise à la terre</h2>

<p>Installer des différentiels sur une installation sans mise à la terre n'apporte qu'une
protection partielle. Le différentiel détecte un courant de fuite ; encore faut-il que ce
courant ait un chemin de retour vers la terre pour être détecté avant qu'une personne ne
serve de conducteur. Lorsque la terre est absente, sa création accompagne donc le
remplacement du tableau.</p>
""",
    "faq": [
        ("Peut-on changer un tableau sans refaire toute l'installation ?",
         "<p>Oui, à condition que les circuits existants soient en état d'être raccordés : "
         "isolement correct, sections cohérentes avec les protections, conducteur de "
         "protection présent. Un relevé préalable permet de le vérifier.</p>"),
        ("Le remplacement d'un tableau nécessite-t-il une déclaration ?",
         "<p>Non pour un simple remplacement dans une installation existante. En revanche, une "
         "installation entièrement rénovée ou une installation neuve doit faire l'objet d'une "
         "attestation de conformité visée par le Consuel avant sa mise en service.</p>"),
        ("Combien de temps dure l'intervention ?",
         "<p>Cela dépend du nombre de circuits et de l'état du câblage existant. L'opération "
         "implique une coupure de courant pendant les travaux, dont la durée estimée est "
         "annoncée avant le début du chantier.</p>"),
    ],
    "related_services": ["tableau-electrique", "renovation-electrique",
                         "mise-aux-normes-electrique", "diagnostic-electrique"],
})

ARTICLES.append({
    "slug": "difference-disjoncteur-differentiel",
    "category": "securite-electrique",
    "date": "2026-05-06",
    "updated": None,
    "title": "Quelle différence entre un disjoncteur et un différentiel ?",
    "meta_title": "Disjoncteur ou différentiel : quelle différence ? | Electricien Richard",
    "desc": ("Disjoncteur, interrupteur différentiel, disjoncteur différentiel : rôles, "
             "différences et complémentarité expliqués simplement."),
    "h1": "Quelle différence entre un disjoncteur et un différentiel ?",
    "chapo": ("Ces deux dispositifs se ressemblent sur un tableau, mais ils ne protègent pas "
              "la même chose. Comprendre cette différence permet d'interpréter correctement "
              "ce qui se passe quand l'un des deux déclenche."),
    "quick": ("<p><strong>Le disjoncteur protège les conducteurs contre les surintensités "
              "— surcharge et court-circuit. Le dispositif différentiel protège les personnes "
              "contre les fuites de courant vers la terre.</strong></p>"
              "<p>Les deux sont nécessaires et ne se remplacent pas l'un l'autre. Un "
              "disjoncteur différentiel réunit les deux fonctions dans un seul appareil.</p>"),
    "body": """
<h2 id="disjoncteur">Le disjoncteur : il protège les câbles</h2>

<p>Un disjoncteur divisionnaire surveille l'intensité qui traverse un circuit. Lorsque cette
intensité dépasse son calibre, il coupe. Il agit dans deux situations :</p>

<ul>
<li><strong>La surcharge</strong> : trop d'appareils fonctionnent simultanément sur le
circuit. La coupure intervient après un délai qui dépend de l'ampleur du dépassement.</li>
<li><strong>Le court-circuit</strong> : contact direct entre conducteurs, intensité très
élevée, coupure instantanée.</li>
</ul>

<p>Son rôle est d'empêcher l'échauffement du conducteur. C'est pour cela que son calibre doit
correspondre à la section du câble : un disjoncteur de 20 A sur un câble de 1,5 mm² laisse
le câble chauffer bien au-delà de ce qu'il supporte.</p>

<p><strong>Ce qu'il ne fait pas :</strong> il ne détecte pas une personne qui touche un
conducteur. Le courant traversant un corps humain est bien trop faible pour le faire
déclencher, tout en étant largement suffisant pour être mortel.</p>

<h2 id="differentiel">Le différentiel : il protège les personnes</h2>

<p>Un dispositif différentiel compare l'intensité qui entre dans le circuit par la phase et
celle qui en ressort par le neutre. En fonctionnement normal, les deux sont égales. Si une
différence apparaît, c'est qu'une partie du courant s'échappe ailleurs : vers la terre, à
travers un défaut d'isolement — ou à travers une personne.</p>

<p>Lorsque cette différence atteint son seuil de sensibilité, il coupe. Pour la protection
des personnes dans les logements, ce seuil est de 30 mA, une valeur choisie pour couper
avant que le courant ne devienne dangereux.</p>

<p><strong>Ce qu'il ne fait pas :</strong> un interrupteur différentiel ne protège pas contre
les surcharges ni les courts-circuits. On peut y raccorder des circuits qui chaufferaient
sans qu'il ne réagisse : c'est le rôle des disjoncteurs placés en aval.</p>

<h2 id="comparaison">Comparaison directe</h2>

<div class="table-wrap"><table>
<caption>Disjoncteur, interrupteur différentiel et disjoncteur différentiel</caption>
<thead><tr><th scope="col"></th><th scope="col">Disjoncteur</th><th scope="col">Interrupteur différentiel</th><th scope="col">Disjoncteur différentiel</th></tr></thead>
<tbody>
<tr><td>Protège</td><td>Les conducteurs</td><td>Les personnes</td><td>Les deux</td></tr>
<tr><td>Détecte</td><td>Surcharge et court-circuit</td><td>Fuite de courant vers la terre</td><td>Les trois</td></tr>
<tr><td>Portée</td><td>Un circuit</td><td>Plusieurs circuits en aval</td><td>Un circuit</td></tr>
<tr><td>Bouton test</td><td>Non</td><td>Oui</td><td>Oui</td></tr>
<tr><td>Position au tableau</td><td>Après le différentiel</td><td>En tête de rangée</td><td>Sur le circuit concerné</td></tr>
</tbody></table></div>

<h2 id="types">Les types de différentiels</h2>

<p>Tous les différentiels ne détectent pas les mêmes formes de courant de défaut.</p>

<ul>
<li><strong>Type AC</strong> : détecte les courants de défaut alternatifs. Convient aux
circuits d'éclairage et de prises classiques.</li>
<li><strong>Type A</strong> : détecte en plus les courants comportant une composante
continue. Il est exigé pour certains circuits, notamment la plaque de cuisson et le
lave-linge, dont l'électronique peut générer ce type de défaut.</li>
<li><strong>Types spécifiques</strong> : d'autres types existent pour des usages
particuliers, notamment les points de recharge de véhicules électriques, où la nature du
défaut possible impose une détection adaptée.</li>
</ul>

<p>C'est pourquoi un tableau correctement conçu comporte plusieurs différentiels de types
différents, et non un seul dispositif en tête d'installation.</p>

<h2 id="pratique">Ce que cela change en pratique</h2>

<p>Quand une protection déclenche, le dispositif concerné indique immédiatement la nature du
problème :</p>

<ul>
<li>un <strong>disjoncteur divisionnaire</strong> a coupé, et lui seul : surcharge ou
court-circuit sur ce circuit ;</li>
<li>un <strong>interrupteur différentiel</strong> a coupé, entraînant plusieurs circuits :
fuite de courant sur l'un d'eux, ou sur un appareil raccordé.</li>
</ul>

<p>Cette lecture oriente directement la recherche. Voir
<a href="/disjoncteur.html">disjoncteur qui saute</a> et
<a href="/recherche-panne.html">recherche de panne</a>.</p>
""",
    "faq": [
        ("Un différentiel remplace-t-il un disjoncteur ?",
         "<p>Non. Un interrupteur différentiel ne protège pas contre les surcharges ni les "
         "courts-circuits : il ne surveille pas l'intensité, mais l'écart entre le courant "
         "entrant et sortant. Les deux dispositifs sont complémentaires et tous deux "
         "nécessaires.</p>"),
        ("Pourquoi faut-il plusieurs différentiels dans un tableau ?",
         "<p>Pour deux raisons. D'abord parce que certains circuits exigent un type "
         "particulier. Ensuite parce que répartir les circuits sur plusieurs différentiels "
         "limite l'étendue d'une coupure : un défaut ne prive alors qu'une partie du logement "
         "d'électricité, ce qui facilite aussi le diagnostic.</p>"),
        ("À quoi sert le bouton test d'un différentiel ?",
         "<p>Il simule un courant de fuite et doit provoquer un déclenchement immédiat. C'est "
         "le seul moyen simple de vérifier que le dispositif fonctionne encore. Un test "
         "mensuel est recommandé : un différentiel resté longtemps sans manœuvre peut se "
         "bloquer mécaniquement.</p>"),
    ],
    "related_services": ["disjoncteur", "tableau-electrique", "mise-aux-normes-electrique",
                         "court-circuit"],
})

ARTICLES.append({
    "slug": "prix-renovation-electrique-maison",
    "category": "prix",
    "date": "2026-06-03",
    "updated": None,
    "title": "Quel prix pour refaire l'installation électrique d'une maison ?",
    "meta_title": "Prix d'une rénovation électrique : ce qui fait varier le devis | Electricien Richard",
    "desc": ("Prix d'une rénovation électrique : les postes qui composent le devis, les "
             "facteurs qui font varier le chiffrage et comment comparer deux offres."),
    "h1": "Quel prix pour refaire l'installation électrique d'une maison ?",
    "chapo": ("Aucun chiffre ne figure dans cet article, et c'est délibéré : un prix annoncé "
              "sans avoir vu l'installation n'engage personne. En revanche, comprendre ce qui "
              "compose un devis permet de comparer sérieusement deux offres."),
    "quick": ("<p><strong>Le prix d'une rénovation électrique dépend de quatre éléments : le "
              "périmètre des travaux, l'état de l'installation existante, l'accessibilité des "
              "cheminements et la gamme du matériel installé.</strong></p>"
              "<p>C'est l'accessibilité qui produit les écarts les plus importants : passer un "
              "câble dans une gaine existante ou dans un mur en pierre de soixante centimètres "
              "ne représente pas le même travail.</p>"),
    "body": """
<h2 id="postes">Les postes qui composent un devis</h2>

<div class="table-wrap"><table>
<caption>Composition d'un devis de rénovation électrique</caption>
<thead><tr><th scope="col">Poste</th><th scope="col">Ce qu'il recouvre</th><th scope="col">Ce qui le fait varier</th></tr></thead>
<tbody>
<tr><td>Main-d'œuvre</td><td>Temps de pose, raccordements, essais</td><td>Accessibilité, nature du bâti, occupation du logement</td></tr>
<tr><td>Tableau et protections</td><td>Coffret, différentiels, disjoncteurs, parafoudre éventuel</td><td>Nombre de circuits, types de différentiels exigés</td></tr>
<tr><td>Câbles et gaines</td><td>Conducteurs, gaines, boîtes de dérivation</td><td>Longueurs, sections, nombre de circuits</td></tr>
<tr><td>Appareillage</td><td>Prises, interrupteurs, points d'éclairage</td><td>Quantité et gamme choisie</td></tr>
<tr><td>Mise à la terre</td><td>Prise de terre, barrette, liaisons équipotentielles</td><td>Existence ou non d'une terre exploitable, nature du terrain</td></tr>
<tr><td>Travaux annexes</td><td>Saignées, rebouchage, reprises de finitions</td><td>Type de murs, ampleur des passages à créer</td></tr>
</tbody></table></div>

<h2 id="facteurs">Les quatre facteurs qui font vraiment varier le prix</h2>

<h3>1. Le périmètre</h3>
<p>Entre une reprise du tableau et de la mise à la terre, et une rénovation complète avec
remplacement de tous les conducteurs, l'écart est considérable. Ces deux opérations portent
pourtant le même nom dans le langage courant. La première question à clarifier est donc
toujours : que comprend exactement le devis ?</p>

<h3>2. L'état de l'existant</h3>
<p>Une installation des années 1990 dotée d'une mise à la terre et de conducteurs corrects
demande beaucoup moins de travail qu'une installation d'avant 1960 sans terre, avec des
conducteurs sous isolant cassant. Le second cas suppose de tout reprendre ; le premier
permet souvent de conserver une partie des circuits.</p>

<h3>3. L'accessibilité</h3>
<p>C'est le facteur le plus sous-estimé. Dans une maison récente, les gaines existantes
permettent de tirer de nouveaux conducteurs sans ouvrir un seul mur. Dans une maison
ancienne en pierre, chaque circuit suppose de créer un cheminement — saignée, plinthe
technique, doublage, combles — avec les reprises de finition correspondantes.</p>

<p>Le bâti local joue directement : murs en pierre du Trégor ou du Centre-Bretagne, tuffeau
angevin, immeubles de la reconstruction à Brest, Lorient ou Saint-Nazaire, maisons de ville
nantaises ou rennaises sur plusieurs niveaux — chacune de ces configurations impose ses
propres méthodes.</p>

<h3>4. La gamme de matériel</h3>
<p>Les écarts sont surtout sensibles sur l'appareillage visible : prises, interrupteurs,
plaques de finition. Sur le matériel de protection, l'écart est plus faible et ce n'est pas
un poste sur lequel il est raisonnable d'économiser.</p>

<h2 id="comparer">Comment comparer deux devis</h2>

<p>Deux devis portant le même intitulé peuvent recouvrir des prestations très différentes.
Les points à vérifier ligne par ligne :</p>

<ul>
<li>le nombre de circuits créés, et non seulement le nombre de points ;</li>
<li>le nombre et le type de dispositifs différentiels ;</li>
<li>la reprise ou non de la mise à la terre ;</li>
<li>le repérage du tableau, souvent absent des devis les moins chers ;</li>
<li>l'inclusion ou non des saignées et des rebouchages ;</li>
<li>l'inclusion ou non des reprises de finitions — peinture, papier peint ;</li>
<li>la gamme d'appareillage prévue, décrite précisément ;</li>
<li>l'évacuation des gravats ;</li>
<li>les assurances de l'entreprise, notamment la décennale.</li>
</ul>

<p>Un devis nettement moins cher que les autres exclut généralement une partie de ces
postes. Ils devront pourtant être réalisés : la question est de savoir par qui, et à quel
moment ils réapparaîtront dans le budget.</p>

<h2 id="etaler">Étaler les travaux dans le temps</h2>

<p>Lorsque le budget ne permet pas une rénovation complète, l'échelonnement est possible à
condition de respecter un ordre logique :</p>

<ol class="steps">
<li><h3>Mise à la terre</h3><p>Elle conditionne l'efficacité de toutes les protections.</p></li>
<li><h3>Tableau</h3><p>Différentiels 30 mA, protection de chaque circuit, repérage.</p></li>
<li><h3>Pièces d'eau et cuisine</h3><p>Les locaux où le risque est le plus élevé.</p></li>
<li><h3>Circuits vétustes</h3><p>Les plus sollicités d'abord.</p></li>
<li><h3>Confort</h3><p>Prises supplémentaires, éclairage, commandes.</p></li>
</ol>

<p>Cet ordre évite de refaire deux fois les mêmes travaux. Poser un appareillage neuf sur des
circuits qui devront être remplacés ensuite est la principale source de dépense inutile.</p>

<h2 id="tva">TVA et aides</h2>

<p>Les travaux réalisés dans un logement achevé depuis plus de deux ans peuvent, selon leur
nature, relever d'un taux réduit de TVA. Concernant les aides, les dispositifs portent
principalement sur la performance énergétique ; l'électricité seule n'y ouvre pas
systématiquement droit. Les conditions évoluant régulièrement, mieux vaut les vérifier
auprès d'un conseiller France Rénov' au moment du projet. Voir aussi la page
<a href="/tarifs.html">tarifs</a>.</p>
""",
    "faq": [
        ("Pourquoi les électriciens refusent-ils de donner un prix par téléphone ?",
         "<p>Parce que les facteurs déterminants ne sont pas observables à distance : état des "
         "conducteurs, présence d'une terre exploitable, accessibilité des cheminements, "
         "nature des murs. Un ordre de grandeur peut être donné à partir de photos et d'une "
         "description précise, mais un prix ferme suppose une visite.</p>"),
        ("Faut-il refaire l'électricité avant ou après les autres travaux ?",
         "<p>Avant les finitions, systématiquement. L'électricité passe après la démolition et "
         "avant les enduits, les cloisons fermées et les revêtements. Refaire l'électricité "
         "après les finitions oblige à choisir entre des cheminements apparents et des "
         "reprises coûteuses.</p>"),
        ("Peut-on fournir soi-même le matériel pour réduire le coût ?",
         "<p>C'est envisageable pour l'appareillage visible et les luminaires. Pour le matériel "
         "de protection, la fourniture par le professionnel est préférable : le choix dépend de "
         "caractéristiques précises, et la responsabilité sur le fonctionnement du matériel "
         "installé est engagée.</p>"),
    ],
    "related_services": ["renovation-electrique", "tarifs", "devis-electricien",
                         "tableau-electrique"],
})

ARTICLES.append({
    "slug": "comment-choisir-un-electricien",
    "category": "conseils",
    "date": "2026-04-25",
    "updated": None,
    "title": "Comment choisir un électricien ? Les points à vérifier",
    "meta_title": "Comment choisir un électricien ? Points à vérifier | Electricien Richard",
    "desc": ("Choisir un électricien : assurances, devis, qualifications, signaux d'alerte et "
             "questions à poser avant de confier des travaux."),
    "h1": "Comment choisir un électricien ?",
    "chapo": ("Les travaux électriques engagent la sécurité du logement sur des décennies. "
              "Quelques vérifications simples permettent d'écarter les situations à risque "
              "avant de signer."),
    "quick": ("<p><strong>Quatre vérifications essentielles : l'existence légale de "
              "l'entreprise (numéro SIRET), ses assurances (responsabilité civile "
              "professionnelle et décennale), un devis écrit et détaillé, et l'absence de "
              "pression commerciale.</strong></p>"
              "<p>Ces éléments peuvent être demandés sans gêne : un professionnel sérieux les "
              "fournit sans difficulté.</p>"),
    "body": """
<h2 id="verifications">Les vérifications à faire avant de signer</h2>

<h3>L'existence légale de l'entreprise</h3>
<p>Un numéro SIRET doit figurer sur le devis. Il permet de vérifier l'immatriculation de
l'entreprise et son activité déclarée. Une entreprise qui n'apparaît nulle part est un
signal d'alerte immédiat.</p>

<h3>Les assurances</h3>
<p>Deux couvertures comptent : la responsabilité civile professionnelle, qui couvre les
dommages causés pendant les travaux, et l'assurance décennale, qui couvre pendant dix ans
les désordres compromettant la solidité ou la destination de l'ouvrage. Les attestations
peuvent être demandées : c'est une démarche normale, et elles doivent être en cours de
validité.</p>

<h3>Le devis</h3>
<p>Il doit être écrit, détaillé et gratuit. Un devis sérieux décrit chaque prestation,
distingue fournitures et main-d'œuvre, précise les caractéristiques du matériel, indique le
taux de TVA appliqué et la durée de validité de l'offre. Un document d'une seule ligne
mentionnant « rénovation électrique » et un montant global n'est pas un devis exploitable.</p>

<h3>Les qualifications</h3>
<p>Certaines qualifications professionnelles attestent d'un savoir-faire dans un domaine
donné, comme l'installation de points de recharge pour véhicules électriques. Elles ne sont
pas exigées pour tous les travaux, mais elles sont pertinentes pour les prestations
concernées.</p>

<h2 id="alertes">Les signaux qui doivent alerter</h2>

<div class="table-wrap"><table>
<caption>Signaux d'alerte et ce qu'ils signifient</caption>
<thead><tr><th scope="col">Signal</th><th scope="col">Pourquoi c'est problématique</th></tr></thead>
<tbody>
<tr><td>Refus de fournir un devis écrit</td><td>Aucun cadre contractuel, aucune référence en cas de litige</td></tr>
<tr><td>Prix annoncé fermement par téléphone, sans visite</td><td>Le chiffrage ne peut pas tenir compte de l'existant</td></tr>
<tr><td>Demande d'un acompte important avant tout début de travaux</td><td>Déséquilibre inhabituel entre versement et prestation</td></tr>
<tr><td>Pression pour signer immédiatement</td><td>Technique commerciale, incompatible avec une décision éclairée</td></tr>
<tr><td>Absence de SIRET ou d'attestation d'assurance</td><td>Aucune garantie en cas de sinistre</td></tr>
<tr><td>Paiement demandé exclusivement en espèces</td><td>Absence de traçabilité et de facture exploitable</td></tr>
<tr><td>Diagnostic alarmiste immédiat sans mesure</td><td>Un constat sérieux repose sur des vérifications, pas sur une impression</td></tr>
</tbody></table></div>

<h2 id="questions">Les questions utiles à poser</h2>

<ul>
<li>Que comprend exactement le devis, et qu'est-ce qui en est explicitement exclu ?</li>
<li>Les saignées, rebouchages et reprises de finitions sont-ils inclus ?</li>
<li>Combien de circuits seront créés, et combien de différentiels sont prévus ?</li>
<li>La mise à la terre sera-t-elle reprise ou créée ?</li>
<li>Le tableau sera-t-il repéré à la fin des travaux ?</li>
<li>Quelle est la durée prévisionnelle et quelles coupures faut-il anticiper ?</li>
<li>Que se passe-t-il si un imprévu apparaît en cours de chantier ?</li>
<li>Une attestation de conformité Consuel est-elle nécessaire, et qui s'en charge ?</li>
</ul>

<h2 id="apres">Après les travaux</h2>

<p>Conservez la facture, le devis signé et, le cas échéant, l'attestation de conformité. Ces
documents servent en cas de sinistre, lors d'une revente, et comme référence si un problème
apparaît sur les travaux réalisés.</p>

<p>Vérifiez également que le tableau est correctement repéré et que les essais ont été
réalisés devant vous — notamment le test des différentiels. Un professionnel prend
normalement le temps d'expliquer ce qui a été fait et ce qui reste éventuellement à
prévoir.</p>

<h2 id="urgence">Le cas particulier de l'urgence</h2>

<p>C'est la situation où le risque de mauvaise décision est le plus élevé : on choisit vite,
sous pression. Quelques réflexes limitent ce risque : demander les conditions tarifaires
avant l'intervention, exiger une facture détaillée, et refuser tout travaux
complémentaires engagés sans devis préalable. Un dépannage urgent peut légitimement coûter
plus cher qu'une intervention planifiée, mais les conditions doivent être annoncées
avant.</p>
""",
    "faq": [
        ("Un électricien doit-il obligatoirement être assuré ?",
         "<p>Oui. Un professionnel du bâtiment doit disposer d'une assurance de responsabilité "
         "civile professionnelle et, pour les travaux relevant de la garantie décennale, d'une "
         "assurance décennale. Les attestations doivent être en cours de validité et couvrir "
         "l'activité concernée.</p>"),
        ("Le devis engage-t-il le client ?",
         "<p>Le devis engage l'entreprise sur le prix et le contenu pendant sa durée de "
         "validité. Il n'engage le client qu'à partir du moment où il le signe. Tant qu'il "
         "n'est pas signé, aucune prestation ne peut être facturée, sauf accord préalable "
         "explicite pour une étude spécifique.</p>"),
        ("Faut-il plusieurs devis ?",
         "<p>C'est utile pour un chantier important, à condition de comparer le contenu et non "
         "seulement le total. Un devis nettement moins cher exclut généralement des postes qui "
         "devront être réalisés de toute façon : mise à la terre, rebouchages, repérage, "
         "nombre de circuits.</p>"),
    ],
    "related_services": ["tarifs", "devis-electricien", "a-propos", "contact"],
})

ARTICLES.append({
    "slug": "preparer-sa-renovation-electrique",
    "category": "renovation",
    "date": "2026-07-15",
    "updated": None,
    "title": "Comment préparer une rénovation électrique",
    "meta_title": "Préparer une rénovation électrique : méthode | Electricien Richard",
    "desc": ("Préparer une rénovation électrique : état des lieux, choix des usages, "
             "coordination avec les autres travaux et points à décider avant le chantier."),
    "h1": "Comment préparer une rénovation électrique",
    "chapo": ("La qualité d'une rénovation électrique se joue en grande partie avant le "
              "premier coup de perceuse. Ce qui n'a pas été prévu se paie ensuite en "
              "cheminements apparents ou en reprises de finitions."),
    "quick": ("<p><strong>Trois étapes préparatoires : établir l'état réel de l'installation "
              "existante, définir les usages pièce par pièce, puis caler le calendrier avec "
              "les autres corps d'état.</strong></p>"
              "<p>L'électricité intervient après la démolition et avant les cloisons fermées, "
              "les enduits et les revêtements de sol.</p>"),
    "body": """
<h2 id="etat-des-lieux">1. Établir l'état de l'existant</h2>

<p>Avant de décider quoi que ce soit, il faut savoir ce dont on part. Les points à établir
sont peu nombreux mais déterminants :</p>

<ul>
<li>la présence et la qualité de la mise à la terre ;</li>
<li>la nature du tableau et le nombre de circuits réellement disponibles ;</li>
<li>l'état d'isolement des conducteurs, mesuré et non supposé ;</li>
<li>la présence d'un conducteur de protection sur chaque circuit ;</li>
<li>la puissance souscrite et le type d'alimentation, monophasé ou triphasé ;</li>
<li>les cheminements existants exploitables : gaines, combles, vides, plinthes.</li>
</ul>

<p>Ce relevé détermine le périmètre réel des travaux et évite les mauvaises surprises en
cours de chantier. Voir <a href="/diagnostic-electrique.html">diagnostic électrique</a>.</p>

<h2 id="usages">2. Définir les usages, pièce par pièce</h2>

<p>C'est l'étape que l'on saute le plus souvent, et celle qui produit le plus de regrets.
Concrètement, il s'agit de se projeter dans l'usage réel de chaque pièce.</p>

<div class="table-wrap"><table>
<caption>Questions à se poser pièce par pièce</caption>
<thead><tr><th scope="col">Pièce</th><th scope="col">Points à décider</th></tr></thead>
<tbody>
<tr><td>Cuisine</td><td>Implantation des appareils, position de la plaque et du four, prises du plan de travail, éclairage fonctionnel sous meubles</td></tr>
<tr><td>Séjour</td><td>Emplacement du téléviseur et de la box, prises près des assises, points d'éclairage et commandes multiples</td></tr>
<tr><td>Chambres</td><td>Prises de part et d'autre du lit, commande de l'éclairage depuis le lit et depuis l'entrée</td></tr>
<tr><td>Salle d'eau</td><td>Éclairage du miroir, prise pour appareils, sèche-serviettes, ventilation</td></tr>
<tr><td>Bureau</td><td>Nombre de prises réel, arrivée réseau, éclairage du plan de travail</td></tr>
<tr><td>Extérieur et garage</td><td>Éclairage d'accès, prises extérieures, alimentation d'un abri, borne de recharge</td></tr>
</tbody></table></div>

<p>Un conseil simple : comptez le nombre de prises que vous utilisez réellement aujourd'hui,
multiprises comprises, et ajoutez une marge. Le sous-dimensionnement est beaucoup plus
fréquent que l'excès.</p>

<h2 id="anticiper">3. Anticiper les évolutions</h2>

<p>Certains équipements ne sont pas prévus aujourd'hui mais le seront peut-être demain :
borne de recharge, pompe à chaleur, climatisation, extension, piscine, atelier. Les
anticiper coûte peu pendant le chantier et très cher après.</p>

<p>Concrètement, cela signifie : prévoir des modules libres au tableau, poser des gaines en
attente vers le garage, les combles et l'extérieur, et vérifier que la puissance souscrite
laisse une marge.</p>

<h2 id="calendrier">4. Caler le calendrier avec les autres travaux</h2>

<p>L'électricité s'insère à un moment précis dans une rénovation.</p>

<ol class="steps">
<li><h3>Démolition et gros œuvre</h3><p>Ouverture des murs, dépose des anciens revêtements.</p></li>
<li><h3>Passage des réseaux</h3><p>Électricité, plomberie, ventilation : saignées, gaines, conducteurs, boîtes.</p></li>
<li><h3>Fermeture</h3><p>Cloisons, doublages, isolation, plafonds : plus rien n'est accessible ensuite.</p></li>
<li><h3>Finitions</h3><p>Enduits, peintures, sols.</p></li>
<li><h3>Appareillage et tableau</h3><p>Pose des prises, interrupteurs, luminaires, raccordement final et essais.</p></li>
</ol>

<p>L'erreur la plus coûteuse consiste à fermer les cloisons avant d'avoir arrêté
l'implantation des prises et des points d'éclairage. Une fois les plaques posées et
enduites, toute modification implique une reprise complète.</p>

<h2 id="decisions">5. Les décisions à prendre avant le chantier</h2>

<ul>
<li>l'emplacement du tableau, accessible et hors des volumes de sécurité des pièces
d'eau ;</li>
<li>l'implantation précise des prises et interrupteurs, si possible marquée au mur ;</li>
<li>le type d'éclairage retenu : plafonniers, spots, appliques, rails ;</li>
<li>la gamme d'appareillage et sa finition ;</li>
<li>la présence ou non de commandes multiples dans les circulations ;</li>
<li>les besoins en réseau informatique, souvent oubliés puis regrettés ;</li>
<li>l'implantation des points extérieurs.</li>
</ul>

<h2 id="pendant">Pendant le chantier</h2>

<p>Une visite avant la fermeture des cloisons est vivement recommandée : c'est le dernier
moment où une modification reste simple. À cette occasion, il est utile de photographier
les murs ouverts, avec les gaines et les boîtes en place. Ces photos serviront plus tard,
lors d'un percement ou d'une intervention ultérieure, pour savoir où passent les
circuits.</p>
""",
    "faq": [
        ("À quel moment intervient l'électricien dans une rénovation ?",
         "<p>Après la démolition et avant la fermeture des cloisons, pour la pose des gaines et "
         "des conducteurs. Il revient ensuite après les finitions pour poser l'appareillage, "
         "raccorder le tableau et procéder aux essais.</p>"),
        ("Peut-on modifier l'implantation en cours de chantier ?",
         "<p>Tant que les cloisons ne sont pas fermées, oui, avec un impact limité. Une fois "
         "les plaques posées et enduites, toute modification suppose de rouvrir et de "
         "reprendre les finitions. C'est pourquoi la visite avant fermeture est un rendez-vous "
         "important.</p>"),
        ("Faut-il prévoir un réseau informatique filaire ?",
         "<p>C'est un choix, mais il est nettement plus simple de poser des gaines pendant les "
         "travaux que d'y revenir ensuite. Même sans câbler immédiatement, laisser des "
         "attentes vers les pièces principales et le point d'arrivée offre une souplesse "
         "appréciable.</p>"),
    ],
    "related_services": ["renovation-electrique", "installation-electrique",
                         "diagnostic-electrique", "tableau-electrique"],
})

ARTICLES.append({
    "slug": "installer-une-borne-de-recharge-ce-qu-il-faut-savoir",
    "category": "bornes-de-recharge",
    "date": "2026-08-05",
    "updated": None,
    "title": "Installer une borne de recharge : ce qu'il faut savoir",
    "meta_title": "Installer une borne de recharge : guide complet | Electricien Richard",
    "desc": ("Installer une borne de recharge pour véhicule électrique : puissance, circuit "
             "dédié, protections, maison individuelle, copropriété et droit à la prise."),
    "h1": "Installer une borne de recharge : ce qu'il faut savoir",
    "chapo": ("Recharger un véhicule électrique est l'usage domestique le plus exigeant pour "
              "une installation : une forte intensité, pendant plusieurs heures, tous les "
              "jours. C'est ce qui explique les règles particulières qui l'encadrent."),
    "quick": ("<p><strong>Une borne de recharge se raccorde sur un circuit dédié depuis le "
              "tableau, avec une protection différentielle adaptée au type de borne.</strong> "
              "La recharge régulière sur une prise domestique ordinaire n'est pas adaptée : "
              "l'intensité soutenue échauffe la prise et son circuit.</p>"
              "<p>Avant tout devis, trois points sont vérifiés : la puissance souscrite, la "
              "place disponible au tableau et la distance entre le tableau et l'emplacement de "
              "la borne.</p>"),
    "body": """
<h2 id="prise-ordinaire">Pourquoi pas une prise ordinaire ?</h2>

<p>Une prise domestique est conçue pour des usages intermittents : quelques minutes à
quelques heures, à intensité modérée. Une recharge sollicite au contraire le circuit à
intensité élevée pendant des heures, chaque nuit.</p>

<p>Cette sollicitation révèle tous les défauts latents : une borne légèrement desserrée, des
contacts un peu usés, un conducteur juste dimensionné. La résistance de contact produit de
la chaleur, la chaleur dégrade encore le contact, et le phénomène s'entretient jusqu'à la
déformation du matériel.</p>

<p>Il existe une solution intermédiaire, la prise renforcée, conçue pour une recharge
prolongée à puissance limitée. Elle exige elle aussi un circuit dédié.</p>

<h2 id="puissance">Quelle puissance choisir ?</h2>

<div class="table-wrap"><table>
<caption>Puissances usuelles en habitation</caption>
<thead><tr><th scope="col">Puissance</th><th scope="col">Type d'alimentation</th><th scope="col">Situation typique</th></tr></thead>
<tbody>
<tr><td>3,7 kW</td><td>Monophasé</td><td>Trajets quotidiens courts, recharge de nuit, installation limitée</td></tr>
<tr><td>7,4 kW</td><td>Monophasé</td><td>Le choix le plus courant en maison individuelle</td></tr>
<tr><td>11 kW</td><td>Triphasé</td><td>Recharge plus rapide, si le raccordement le permet</td></tr>
<tr><td>22 kW</td><td>Triphasé</td><td>Usage intensif ou professionnel</td></tr>
</tbody></table></div>

<p>Deux limites s'imposent au choix. D'abord la puissance souscrite du logement : une borne
de 7,4 kW mobilise une part importante d'un abonnement domestique courant. Ensuite le
chargeur embarqué du véhicule : installer une borne plus puissante que ce que le véhicule
accepte n'apporte aucun gain.</p>

<h2 id="protections">Les protections spécifiques</h2>

<p>C'est le point technique qui distingue une installation correcte d'un montage improvisé.
Un point de recharge exige une protection différentielle adaptée à la nature du courant de
défaut susceptible d'apparaître, qui n'est pas la même que pour un circuit domestique
ordinaire.</p>

<p>Certaines bornes intègrent une partie de cette protection, d'autres non. Le dispositif à
installer au tableau dépend donc du modèle retenu : c'est une raison supplémentaire de
choisir la borne avant de figer l'installation.</p>

<h2 id="gestion">La gestion de charge</h2>

<p>Sans régulation, la borne consomme sa puissance nominale indépendamment du reste du
logement. Si la recharge coïncide avec le fonctionnement du four, du chauffe-eau et du
lave-linge, le disjoncteur de branchement déclenche.</p>

<p>La gestion de charge dynamique mesure la consommation globale et ajuste automatiquement
la puissance de recharge pour rester sous la limite de l'abonnement. Elle permet souvent
d'éviter une augmentation de puissance souscrite, et représente un compromis intéressant
lorsque la marge est faible.</p>

<h2 id="copropriete">En copropriété : le droit à la prise</h2>

<p>Un copropriétaire ou un locataire disposant d'une place de stationnement peut faire
installer un point de recharge à ses frais. La démarche consiste à informer le syndic par
lettre recommandée, en joignant un descriptif détaillé des travaux et un schéma de
raccordement. La question est inscrite à l'ordre du jour de l'assemblée générale à titre
d'information, et l'opposition n'est possible que pour un motif sérieux et légitime.</p>

<p>Deux montages coexistent : le raccordement sur le compteur du logement, simple mais qui
suppose une distance raisonnable, ou la création d'un point de comptage individuel dédié au
stationnement, plus adapté aux grands immeubles.</p>

<h2 id="etapes">Les étapes d'une installation</h2>

<ol class="steps">
<li><h3>Visite technique</h3><p>Relevé du tableau, de la puissance souscrite, de l'emplacement et du cheminement possible.</p></li>
<li><h3>Choix de la borne</h3><p>Puissance, fonctions, gestion de charge, en cohérence avec le véhicule et l'installation.</p></li>
<li><h3>Devis</h3><p>Circuit, protections, cheminement, borne et pose détaillés.</p></li>
<li><h3>Réalisation</h3><p>Création du circuit dédié, pose des protections, cheminement et fixation de la borne.</p></li>
<li><h3>Mise en service</h3><p>Essais, configuration, paramétrage de la gestion de charge et explication du fonctionnement.</p></li>
</ol>

<p>Voir la page dédiée : <a href="/borne-recharge.html">installation de borne de
recharge</a>.</p>
""",
    "faq": [
        ("Faut-il un professionnel qualifié pour installer une borne ?",
         "<p>Au-delà d'une certaine puissance, l'installation doit être réalisée par un "
         "professionnel disposant de la qualification correspondante. Cette exigence conditionne "
         "par ailleurs l'accès à certains dispositifs de soutien financier.</p>"),
        ("Peut-on installer une borne dans un garage collectif ?",
         "<p>Oui, dans le cadre du droit à la prise. La démarche suppose d'informer le syndic "
         "par lettre recommandée avec un descriptif des travaux. L'opposition n'est possible "
         "que pour un motif sérieux et légitime, notamment si l'immeuble dispose déjà d'une "
         "installation répondant au besoin.</p>"),
        ("Combien de temps faut-il pour recharger un véhicule ?",
         "<p>Cela dépend de la capacité de la batterie, de son niveau de charge et de la "
         "puissance délivrée. À puissance donnée, doubler la puissance divise approximativement "
         "le temps par deux, dans la limite de ce que le chargeur embarqué du véhicule "
         "accepte.</p>"),
    ],
    "related_services": ["borne-recharge", "tableau-electrique", "installation-electrique",
                         "electricien-particulier"],
})

ARTICLES.append({
    "slug": "norme-nf-c-15-100-points-essentiels",
    "category": "installation-electrique",
    "date": "2026-03-19",
    "updated": None,
    "title": "La norme NF C 15-100 : les points essentiels à connaître",
    "meta_title": "Norme NF C 15-100 : les points essentiels | Electricien Richard",
    "desc": ("Norme NF C 15-100 : ce qu'elle couvre, circuits obligatoires, protection "
             "différentielle, pièces d'eau et application aux installations existantes."),
    "h1": "La norme NF C 15-100 : les points essentiels",
    "chapo": ("Cette norme est citée partout, souvent de travers. Elle ne rend pas illégale "
              "une installation ancienne, mais elle définit ce qu'est aujourd'hui une "
              "installation correctement conçue."),
    "quick": ("<p><strong>La norme NF C 15-100 fixe les règles de conception et de réalisation "
              "des installations électriques basse tension, dont les logements.</strong> Elle "
              "s'applique aux installations neuves et aux rénovations complètes, pas "
              "rétroactivement aux installations existantes.</p>"
              "<p>Ses exigences les plus structurantes portent sur la protection différentielle "
              "30 mA, la mise à la terre, les circuits spécialisés et les règles applicables "
              "aux pièces d'eau.</p>"),
    "body": """
<h2 id="portee">Ce que couvre la norme — et ce qu'elle ne couvre pas</h2>

<p>La NF C 15-100 s'applique aux installations électriques basse tension : logements, mais
aussi locaux tertiaires et bâtiments recevant du public, avec des dispositions
particulières selon les cas.</p>

<p>Point essentiel, souvent mal compris : <strong>elle n'a pas d'effet rétroactif</strong>.
Une installation réalisée en 1975 selon les règles de l'époque n'est pas « hors la loi »
aujourd'hui. Elle n'est simplement plus conforme aux exigences applicables aux installations
neuves. L'obligation de respecter la norme en vigueur naît des travaux : installation neuve
ou rénovation complète.</p>

<h2 id="protection">La protection des personnes</h2>

<h3>Les dispositifs différentiels 30 mA</h3>
<p>Tous les circuits d'un logement doivent être protégés par un dispositif différentiel de
sensibilité 30 mA. Leur nombre minimal dépend de la surface du logement et du nombre de
circuits, et certains circuits exigent un type particulier — notamment la plaque de cuisson
et le lave-linge.</p>

<h3>La mise à la terre</h3>
<p>L'installation doit comporter une prise de terre, un conducteur principal de protection,
une barrette de coupure permettant sa mesure, et un conducteur de protection accompagnant
les circuits jusqu'aux points d'utilisation qui l'exigent.</p>

<h3>La coupure d'urgence</h3>
<p>Un appareil général de commande et de protection doit permettre de couper l'ensemble de
l'installation, en un point accessible.</p>

<h2 id="circuits">Les circuits</h2>

<p>La norme impose une séparation stricte des usages. Chaque type de circuit dispose de sa
propre protection, dimensionnée en fonction de la section des conducteurs.</p>

<div class="table-wrap"><table>
<caption>Principaux circuits exigés dans un logement</caption>
<thead><tr><th scope="col">Circuit</th><th scope="col">Caractéristique</th></tr></thead>
<tbody>
<tr><td>Éclairage</td><td>Circuits distincts des prises ; nombre de points limité par circuit</td></tr>
<tr><td>Prises de courant</td><td>Nombre de socles limité selon la section et la protection</td></tr>
<tr><td>Plaque de cuisson</td><td>Circuit spécialisé, section renforcée, différentiel de type A</td></tr>
<tr><td>Lave-linge, lave-vaisselle, four</td><td>Un circuit spécialisé par appareil</td></tr>
<tr><td>Chauffe-eau</td><td>Circuit spécialisé</td></tr>
<tr><td>Chauffage électrique</td><td>Circuits dédiés selon la puissance installée</td></tr>
<tr><td>Point de recharge de véhicule</td><td>Circuit dédié avec protection adaptée</td></tr>
</tbody></table></div>

<p>La norme fixe également un nombre minimal de socles de prises et de points d'éclairage par
pièce, variable selon la nature et la surface de celle-ci.</p>

<h2 id="pieces-eau">Les pièces d'eau</h2>

<p>C'est le domaine où les exigences sont les plus strictes, parce que le risque y est le
plus élevé. La norme définit des volumes autour de la baignoire et de la douche, dans
lesquels seuls certains matériels sont admis, selon leur indice de protection et leur
tension d'alimentation.</p>

<p>S'y ajoute l'obligation d'une liaison équipotentielle locale, reliant entre eux les
éléments conducteurs de la pièce — canalisations métalliques, huisseries métalliques,
conducteurs de protection des circuits.</p>

<h2 id="tableau">Le tableau et l'espace technique</h2>

<p>La norme prévoit un emplacement dédié pour le tableau, accessible, hors des volumes de
sécurité des pièces d'eau, regroupant l'arrivée du réseau, la protection et les arrivées de
communication. Elle impose également le repérage des circuits et une réserve de modules
libres pour permettre les évolutions ultérieures.</p>

<h2 id="evolution">Une norme qui évolue</h2>

<p>La NF C 15-100 a fait l'objet de plusieurs révisions successives, qui ont notamment
renforcé les exigences de protection différentielle, revu les règles applicables aux pièces
d'eau et introduit des dispositions relatives aux nouveaux usages, dont la recharge des
véhicules électriques.</p>

<p>C'est pourquoi une installation « aux normes » à sa réalisation ne l'est plus
nécessairement au regard du texte actuel — sans que cela ne la rende dangereuse pour autant.
Voir <a href="/mise-aux-normes-electrique.html">mise aux normes électrique</a> pour la
distinction entre mise en sécurité et mise en conformité.</p>
""",
    "faq": [
        ("Mon installation doit-elle être conforme à la norme actuelle ?",
         "<p>Non, si elle est existante et qu'aucun travaux important n'est réalisé. La norme "
         "s'applique aux installations neuves et aux rénovations complètes. En revanche, une "
         "installation existante ne doit pas présenter de risque manifeste pour la sécurité, en "
         "particulier dans un logement mis en location.</p>"),
        ("Qui contrôle le respect de la norme ?",
         "<p>Pour une installation neuve ou entièrement rénovée, l'attestation de conformité "
         "est visée par le Consuel avant la mise en service par le gestionnaire de réseau. "
         "Pour les installations existantes, le diagnostic obligatoire lors d'une vente ou "
         "d'une location signale les anomalies au regard de points de contrôle liés à la "
         "sécurité.</p>"),
        ("La norme impose-t-elle un nombre de prises par pièce ?",
         "<p>Oui, avec des minimums qui varient selon la nature et la surface de la pièce, et "
         "des exigences renforcées dans le séjour et la cuisine. Ces minimums correspondent "
         "aux usages réels : lorsqu'ils ne sont pas atteints, le recours aux multiprises "
         "devient inévitable.</p>"),
    ],
    "related_services": ["installation-electrique", "mise-aux-normes-electrique",
                         "tableau-electrique", "renovation-electrique"],
})

ARTICLES.append({
    "slug": "electricite-habitat-ancien-bretagne-pays-de-la-loire",
    "category": "guide-local",
    "date": "2026-08-26",
    "updated": None,
    "title": "L'électricité dans l'habitat ancien de Bretagne et des Pays de la Loire",
    "meta_title": "Électricité et habitat ancien : Bretagne et Pays de la Loire | Electricien Richard",
    "desc": ("Les contraintes électriques propres au bâti local : pierre bretonne, tuffeau "
             "angevin, immeubles de la reconstruction, littoral et maisons de ville."),
    "h1": "L'électricité dans l'habitat ancien de Bretagne et des Pays de la Loire",
    "chapo": ("Le bâti local n'est pas un détail de décor : il conditionne directement la "
              "façon de concevoir et de réaliser une installation électrique. Voici ce que "
              "l'on rencontre concrètement dans les six départements couverts."),
    "quick": ("<p><strong>Quatre configurations dominent : le bâti en pierre de l'intérieur "
              "breton, les immeubles de la reconstruction d'après-guerre, le tuffeau du Val de "
              "Loire, et l'habitat littoral exposé aux embruns.</strong></p>"
              "<p>Chacune impose ses propres contraintes de cheminement, de choix de matériels "
              "et de traitement de l'humidité.</p>"),
    "body": """
<h2 id="pierre">Le bâti en pierre de l'intérieur breton</h2>

<p>Longères, maisons de bourg, fermes réhabilitées : ce bâti se retrouve dans tout
l'arrière-pays des <a href="/zones/cotes-d-armor/">Côtes-d'Armor</a>, du
<a href="/zones/finistere/">Finistère</a> et du <a href="/zones/morbihan/">Morbihan</a>,
notamment autour de <a href="/zones/morbihan/electricien-pontivy/">Pontivy</a> et dans le
Centre-Bretagne.</p>

<p>La contrainte principale est le cheminement. Des murs de cinquante à quatre-vingts
centimètres d'épaisseur, des planchers bois, l'absence de gaines techniques : créer un
circuit y suppose de trouver un passage plutôt que de saigner en ligne droite. Les solutions
employées sont le passage par les combles, la reprise lors d'un doublage intérieur, ou les
plinthes techniques.</p>

<p>Le second sujet est la mise à la terre. Beaucoup de ces maisons ont été électrifiées puis
complétées sans reprise d'ensemble, et le conducteur de protection est souvent absent d'une
partie des circuits. C'est le premier point vérifié lors d'un diagnostic.</p>

<h2 id="reconstruction">Les immeubles de la reconstruction</h2>

<p><a href="/zones/finistere/electricien-brest/">Brest</a>,
<a href="/zones/morbihan/electricien-lorient/">Lorient</a> et
<a href="/zones/loire-atlantique/electricien-saint-nazaire/">Saint-Nazaire</a> ont été
largement reconstruites après 1945. Leur parc de logements présente un profil homogène et
des problématiques récurrentes.</p>

<p>Ces logements ont été conçus pour un équipement domestique très léger : éclairage et
quelques prises. Ni la plaque électrique, ni le lave-vaisselle, ni l'informatique, ni la
recharge d'un véhicule n'entraient dans le dimensionnement. On y trouve donc des tableaux
sans circuits spécialisés, des sections limitées, et des prises multipliées par
rallonges.</p>

<p>La difficulté supplémentaire est le passage de nouveaux circuits dans des cloisons et
planchers existants, souvent sans gaines exploitables. Une rénovation y demande une
réflexion préalable sur les cheminements, faute de quoi le résultat se traduit par des
goulottes apparentes.</p>

<h2 id="tuffeau">Le tuffeau du Val de Loire</h2>

<p>En <a href="/zones/maine-et-loire/">Maine-et-Loire</a>, le tuffeau change la donne. Cette
pierre calcaire tendre se perce et se saigne facilement, ce qui a historiquement favorisé
les modifications successives des installations : on ajoutait un circuit sans difficulté, et
sans cohérence d'ensemble.</p>

<p>Sa vraie particularité est son comportement vis-à-vis de l'humidité : il absorbe l'eau et
la restitue lentement. Dans les murs enterrés ou mal ventilés, cette humidité dégrade les
matériels encastrés et finit par créer des défauts d'isolement.</p>

<p>À <a href="/zones/maine-et-loire/electricien-saumur/">Saumur</a> et dans le Saumurois
s'ajoutent les caves et galeries creusées dans le coteau, où l'humidité est permanente
toute l'année. Une installation y exige des matériels dont l'indice de protection correspond
à ces conditions, une protection différentielle et une liaison équipotentielle soignée. Un
matériel d'intérieur ordinaire y tient quelques années au mieux.</p>

<h2 id="littoral">L'habitat littoral</h2>

<p>De la côte de Granit rose au golfe du Morbihan, en passant par la baie de Saint-Brieuc,
la côte d'Émeraude autour de <a href="/zones/ille-et-vilaine/electricien-saint-malo/">Saint-Malo</a>
et le littoral de <a href="/zones/finistere/electricien-concarneau/">Concarneau</a>, une
même contrainte revient : l'air marin.</p>

<p>Le sel se dépose sur les parties métalliques et les contacts. Comme il retient
l'humidité, il entretient l'oxydation. Les matériels extérieurs — coffrets, prises de
terrasse, luminaires de façade, alimentations d'abris — se dégradent nettement plus vite
qu'à l'intérieur des terres, et provoquent des déclenchements différentiels récurrents par
temps humide.</p>

<p>Le second trait du littoral est la part des résidences secondaires. Une installation
inoccupée plusieurs mois voit ses défauts s'aggraver sans que personne ne les constate : les
remises en service de début de saison révèlent régulièrement des différentiels qui ne
tiennent plus.</p>

<h2 id="villes">Les maisons de ville et les copropriétés</h2>

<p><a href="/zones/loire-atlantique/electricien-nantes/">Nantes</a>,
<a href="/zones/ille-et-vilaine/electricien-rennes/">Rennes</a> et
<a href="/zones/maine-et-loire/electricien-angers/">Angers</a> partagent un type de bâti
particulier : la maison de ville en longueur, sur plusieurs niveaux étroits. Les
installations y sont étirées, et le tableau se trouve rarement au bon endroit — souvent
près de l'entrée, loin des usages les plus consommateurs.</p>

<p>Ces trois villes comptent également de nombreux immeubles de rapport anciens, divisés en
appartements, où les circuits ont été repris par morceaux. Enfin, leur importante population
étudiante génère un parc locatif où la mise en sécurité entre deux locataires est une
demande régulière.</p>

<h2 id="conclusion">Ce qu'il faut en retenir</h2>

<p>Deux logements de surface identique, l'un dans un lotissement des années 1990 et l'autre
dans une longère du Centre-Bretagne, ne représentent pas le même travail. C'est la raison
pour laquelle un chiffrage sérieux suppose une visite, et pourquoi la préparation des
cheminements pèse davantage, dans le bâti ancien, que le choix du matériel.</p>
""",
    "faq": [
        ("Faut-il refaire toute l'électricité d'une maison en pierre ?",
         "<p>Pas systématiquement. Tout dépend de l'état d'isolement des conducteurs, de la "
         "présence d'un conducteur de protection et des sections en place. Dans beaucoup de "
         "cas, une reprise du tableau, de la mise à la terre et des circuits sensibles "
         "constitue une première étape suffisante.</p>"),
        ("Comment protéger une installation en bord de mer ?",
         "<p>En choisissant des matériels résistants à la corrosion, avec un indice de "
         "protection adapté à l'exposition réelle, et en soignant les entrées de câble : un "
         "presse-étoupe mal adapté ou mal serré annule l'étanchéité annoncée. Un circuit "
         "extérieur séparé permet en outre d'isoler l'extérieur en cas de défaut.</p>"),
        ("Que vérifier dans une résidence secondaire avant la saison ?",
         "<p>Le fonctionnement des dispositifs différentiels par le bouton test, l'absence "
         "d'humidité dans les boîtiers extérieurs, et l'état des câbles en combles — les "
         "rongeurs sont une cause fréquente de dégradation dans les logements peu occupés. En "
         "cas de déclenchement au réarmement, il faut faire mesurer l'isolement plutôt que "
         "d'insister.</p>"),
    ],
    "related_services": ["renovation-electrique", "diagnostic-electrique",
                         "mise-aux-normes-electrique", "electricien-depannage"],
})


def articles_by_category(slug):
    return [a for a in ARTICLES if a["category"] == slug]


def category_by_slug(slug):
    for c in CATEGORIES:
        if c["slug"] == slug:
            return c
    raise KeyError(slug)


def article_url(article):
    return "/blog/%s/%s.html" % (article["category"], article["slug"])


def category_url(cat):
    return "/blog/%s/" % (cat["slug"] if isinstance(cat, dict) else cat)
