# -*- coding: utf-8 -*-
"""
Silo thematique : pages de services.
Chaque page repond a une intention de recherche distincte.
Aucun tarif, delai ou garantie n'est invente : seuls les elements
techniques verifiables et le fonctionnement reel du metier sont decrits.
"""

SERVICES = []

SERVICES.append({
    "slug": "electricien",
    "path": "electricien.html",
    "pillar": True,
    "icon": "bolt",
    "category": "Prestation principale",
    "nav_label": "Électricien",
    "card_desc": ("La page de référence : rôle de l'électricien, prestations, déroulement "
                  "d'une intervention et sécurité électrique."),
    "title": "Électricien — Dépannage, installation et rénovation | Electricien Richard",
    "desc": ("Électricien professionnel : dépannage, recherche de panne, installation, "
             "rénovation et mise aux normes. Interventions dans les Côtes-d'Armor, le "
             "Finistère, l'Ille-et-Vilaine, le Morbihan, la Loire-Atlantique et le "
             "Maine-et-Loire."),
    "h1": "Électricien : dépannage, installation et rénovation électrique",
    "intro": ("Electricien Richard intervient chez les particuliers, dans les commerces et "
              "auprès des professionnels pour l'ensemble des travaux électriques : dépannage "
              "d'une panne, remplacement d'un tableau, rénovation complète d'une installation "
              "ou mise en sécurité d'un logement."),
    "service_type": "Travaux d'électricité générale",
    "quick": {
        "title": "L'essentiel en quelques lignes",
        "answer": (
            "<p><strong>Un électricien conçoit, installe, dépanne et met en sécurité les "
            "installations électriques</strong> des logements, des commerces et des locaux "
            "professionnels. Son travail couvre trois domaines : le dépannage (retrouver et "
            "corriger l'origine d'une panne), les travaux (installer ou rénover une "
            "installation) et la mise en sécurité (rendre une installation existante conforme "
            "aux exigences de sécurité en vigueur).</p>"
            "<p>En France, les installations électriques des logements relèvent de la norme "
            "<strong>NF C 15-100</strong>, qui fixe les règles de conception et de réalisation "
            "des installations basse tension.</p>"),
        "facts": [
            ("Interventions", "Dépannage, recherche de panne, installation, rénovation, mise aux normes"),
            ("Pour qui", "Particuliers, commerces, professionnels"),
            ("Zone", "Côtes-d'Armor, Finistère, Ille-et-Vilaine, Morbihan, Loire-Atlantique, Maine-et-Loire"),
            ("Référence technique", "Norme NF C 15-100 pour les installations basse tension"),
            ("Devis", "Établi après examen de l'installation, avant tout démarrage des travaux"),
        ],
    },
    "body": """
<h2 id="metier">Que fait un électricien ?</h2>

<p>Le métier recouvre des situations très différentes, du dépannage d'une prise qui ne
fonctionne plus à la conception complète de l'installation d'une maison. Dans la pratique,
les interventions se répartissent en quatre grandes familles.</p>

<h3>Le dépannage et la recherche de panne</h3>
<p>Il s'agit d'identifier l'origine d'un dysfonctionnement, puis de le corriger. Un
disjoncteur qui déclenche, une pièce sans courant, une prise qui chauffe ou un différentiel
impossible à réarmer relèvent de cette catégorie. La difficulté n'est pas la réparation
elle-même, mais le <a href="/recherche-panne.html">diagnostic</a> : une même
manifestation peut avoir plusieurs causes très différentes.</p>

<h3>L'installation électrique</h3>
<p>Créer une installation neuve, dans une construction ou une extension, suppose de
dimensionner les circuits, de définir les protections, d'implanter le tableau et de réaliser
la mise à la terre. Le travail commence par un calcul des besoins, pas par la pose de
câbles. Voir la page <a href="/installation-electrique.html">installation
électrique</a>.</p>

<h3>La rénovation et la mise aux normes</h3>
<p>La <a href="/renovation-electrique.html">rénovation électrique</a> consiste à reprendre
tout ou partie d'une installation existante. La <a href="/mise-aux-normes-electrique.html">mise
aux normes</a>, elle, vise à supprimer les défauts de sécurité d'une installation ancienne :
absence de mise à la terre, protection différentielle inadaptée, matériel vétuste.</p>

<h3>Les équipements spécifiques</h3>
<p>Éclairage, <a href="/borne-recharge.html">bornes de recharge pour véhicule
électrique</a>, VMC, circuits pour appareils particuliers : ces travaux supposent presque
toujours de vérifier au préalable la capacité de l'installation existante à les accueillir.</p>

<h2 id="prestations">Nos prestations en détail</h2>
<p>Chaque prestation dispose de sa page dédiée, avec le détail du déroulement, des points de
vigilance et des questions fréquentes.</p>
{{SERVICES_GRID}}

<h2 id="securite">Les points de sécurité qui comptent vraiment</h2>

<p>Dans une installation, quelques éléments assurent l'essentiel de la sécurité des
personnes. Ce sont eux qui sont examinés en priorité lors d'un diagnostic.</p>

<h3>La mise à la terre</h3>
<p>Elle permet d'évacuer un courant de défaut vers le sol. Sans elle, la carcasse métallique
d'un appareil défectueux peut se retrouver sous tension sans qu'aucune protection ne
réagisse. C'est le défaut le plus grave que l'on rencontre dans les installations anciennes.</p>

<h3>Les dispositifs différentiels 30 mA</h3>
<p>Un dispositif différentiel compare le courant qui entre et celui qui sort d'un circuit.
Si une différence apparaît — c'est-à-dire si du courant s'échappe, éventuellement à travers
une personne — il coupe l'alimentation. La sensibilité de 30 mA est celle exigée pour la
protection des personnes dans les logements.</p>

<h3>La protection contre les surintensités</h3>
<p>Disjoncteurs et fusibles protègent les conducteurs contre l'échauffement en cas de
surcharge ou de <a href="/court-circuit.html">court-circuit</a>. Leur calibre doit
correspondre à la section du câble qu'ils protègent : un calibre trop élevé laisse le câble
chauffer sans déclencher.</p>

<h3>La cohérence de l'ensemble</h3>
<p>Un tableau neuf sur des circuits vétustes n'apporte qu'une partie de la sécurité
attendue. Inversement, des circuits corrects mal protégés restent dangereux. C'est la
cohérence de l'ensemble qui compte.</p>

<h2 id="deroulement">Comment se déroule une intervention</h2>
{{PROCESS_STEPS}}

<h2 id="quand-appeler">Quand faut-il appeler un électricien ?</h2>

<p>Certaines situations relèvent d'un simple réflexe et peuvent être vérifiées soi-même :
une lampe grillée, un appareil défectueux à débrancher, un disjoncteur déclenché après le
branchement simultané de plusieurs appareils puissants.</p>

<p>D'autres imposent l'intervention d'un professionnel, sans tentative de réparation
personnelle :</p>

<ul>
<li>odeur de brûlé, noircissement ou déformation au niveau d'une prise ou du tableau ;</li>
<li>prise, interrupteur ou câble anormalement chaud ;</li>
<li>disjoncteur ou différentiel qui déclenche immédiatement après chaque réarmement ;</li>
<li>ressenti de picotement au contact d'un appareil ou d'un robinet ;</li>
<li>arc électrique, crépitement ou étincelle visible ;</li>
<li>installation sans mise à la terre ou équipée de fusibles à broche ;</li>
<li>coupure totale sans cause identifiable.</li>
</ul>

<p>Dans ces cas, la règle est simple : couper l'alimentation concernée et faire intervenir un
professionnel plutôt que de forcer le réarmement.</p>

<h2 id="professionnels">Particuliers, commerces et professionnels</h2>

<p>Les besoins diffèrent selon le contexte. Chez un
<a href="/electricien-particulier.html">particulier</a>, le sujet dominant est la sécurité
du logement et son adaptation aux usages actuels. Pour un
<a href="/electricien-entreprise.html">commerce ou une entreprise</a>, s'y ajoutent la
continuité d'activité, les contraintes propres aux locaux recevant du public et les
exigences liées aux équipements professionnels.</p>

<h2 id="zones">Où intervenons-nous ?</h2>
{{ZONES_STRIP}}
""",
    "faq": [
        ("Quelle est la différence entre un électricien et un dépanneur ?",
         "<p>Il n'existe pas de distinction réglementaire. Dans les faits, un électricien "
         "installateur réalise des travaux planifiés — installation, rénovation, mise aux "
         "normes — tandis que le dépannage consiste à intervenir sur un dysfonctionnement "
         "constaté. Un même professionnel exerce généralement les deux activités.</p>"),
        ("Un électricien doit-il être assuré ?",
         "<p>Oui. Un professionnel du bâtiment doit disposer d'une assurance de responsabilité "
         "civile professionnelle et, pour les travaux relevant de la garantie décennale, d'une "
         "assurance décennale. Ces attestations peuvent être demandées avant le début des "
         "travaux : c'est une vérification légitime et courante.</p>"),
        ("Puis-je réaliser moi-même mon installation électrique ?",
         "<p>La réglementation n'interdit pas à un particulier de travailler sur sa propre "
         "installation. En revanche, celle-ci doit respecter la norme NF C 15-100, et une "
         "installation neuve ou entièrement rénovée doit faire l'objet d'une attestation de "
         "conformité visée par le Consuel avant sa mise en service par le gestionnaire de "
         "réseau. Par ailleurs, les travaux réalisés par le propriétaire ne bénéficient "
         "d'aucune garantie professionnelle, ce qui peut poser problème en cas de sinistre.</p>"),
        ("Qu'est-ce que la norme NF C 15-100 ?",
         "<p>C'est la norme française qui définit les règles de conception, de réalisation et "
         "de vérification des installations électriques basse tension, dont les logements. "
         "Elle traite notamment de la protection des personnes, du nombre et de la nature des "
         "circuits, des sections de conducteurs, de la mise à la terre et des règles "
         "particulières aux pièces d'eau. Elle a été révisée à plusieurs reprises : une "
         "installation ancienne n'est pas nécessairement dangereuse, mais elle ne répond plus "
         "aux exigences actuelles.</p>"),
        ("Faut-il refaire son installation électrique lors d'un achat immobilier ?",
         "<p>Ce n'est pas une obligation légale. Le vendeur doit fournir un diagnostic "
         "lorsque l'installation a plus de quinze ans, mais il n'est pas tenu de réaliser les "
         "travaux. En pratique, les anomalies relevées permettent de hiérarchiser les "
         "priorités : la mise à la terre et la protection différentielle passent avant le "
         "confort.</p>"),
        ("Combien de temps dure une intervention électrique ?",
         "<p>Cela dépend entièrement de la nature du travail. Un remplacement de prise ou "
         "d'interrupteur se traite rapidement ; une recherche de panne dépend de la "
         "complexité du défaut ; un remplacement de tableau ou une rénovation se planifient. "
         "La durée estimée est indiquée au moment du devis.</p>"),
    ],
    "related": ["electricien-depannage", "installation-electrique", "renovation-electrique",
                "mise-aux-normes-electrique", "tableau-electrique", "panne-electrique"],
})

SERVICES.append({
    "slug": "electricien-urgence",
    "path": "electricien-urgence.html",
    "icon": "clock",
    "category": "Dépannage",
    "nav_label": "Urgence",
    "card_desc": ("Coupure totale, odeur de brûlé, échauffement au tableau : les situations "
                  "qui imposent une intervention sans attendre."),
    "title": "Électricien en urgence — Intervention rapide | Electricien Richard",
    "desc": ("Électricien en urgence : coupure totale, disjoncteur qui saute, odeur de brûlé, "
             "échauffement au tableau. Que faire immédiatement et quand appeler un "
             "professionnel."),
    "h1": "Électricien en urgence : réagir face à un problème électrique",
    "intro": ("Toutes les pannes électriques ne constituent pas une urgence, mais certaines "
              "situations imposent de couper l'alimentation et de faire intervenir un "
              "professionnel sans attendre. Cette page explique comment les reconnaître et "
              "quels gestes adopter."),
    "service_type": "Dépannage électrique en urgence",
    "quick": {
        "title": "Que faire en cas d'urgence électrique",
        "answer": (
            "<p><strong>Trois réflexes immédiats :</strong></p>"
            "<ol><li>Couper l'alimentation au disjoncteur général si vous constatez une odeur "
            "de brûlé, de la fumée, un échauffement ou un arc électrique.</li>"
            "<li>Ne pas toucher un appareil, une prise ou un câble suspect, et éloigner les "
            "personnes de la zone concernée.</li>"
            "<li>Appeler un électricien en décrivant précisément ce que vous constatez.</li></ol>"
            "<p>En cas de début d'incendie ou d'électrisation d'une personne, appelez d'abord "
            "les secours : <strong>18</strong> ou <strong>112</strong>.</p>"),
        "facts": [
            ("Urgence réelle", "Odeur de brûlé, fumée, échauffement, arc électrique, électrisation"),
            ("Urgence relative", "Coupure totale sans signe de danger, disjoncteur qui ne se réarme pas"),
            ("Non urgent", "Prise ou interrupteur défectueux isolé, point lumineux hors service"),
            ("Geste à éviter", "Réarmer en boucle un disjoncteur qui déclenche immédiatement"),
            ("Secours", "18 ou 112 en cas d'incendie ou d'accident corporel"),
        ],
    },
    "body": """
<h2 id="vraies-urgences">Qu'est-ce qu'une vraie urgence électrique ?</h2>

<p>Une urgence électrique se définit par la présence d'un risque immédiat pour les personnes
ou les biens : risque d'incendie, risque d'électrisation, ou impossibilité de rétablir
l'alimentation d'un équipement vital.</p>

<h3>Les signes qui imposent une coupure immédiate</h3>

<ul>
<li><strong>Odeur de brûlé ou de plastique chaud</strong> près d'une prise, d'un
interrupteur ou du tableau : un échauffement est en cours.</li>
<li><strong>Fumée, noircissement ou déformation</strong> d'un appareillage : le matériel a
déjà subi une élévation de température anormale.</li>
<li><strong>Crépitement, arc ou étincelle</strong> lors d'un branchement ou d'un
actionnement : mauvais contact ou amorçage.</li>
<li><strong>Chaleur anormale</strong> au toucher sur une prise, un interrupteur, un câble
ou la façade du tableau.</li>
<li><strong>Sensation de picotement</strong> au contact d'un appareil, d'une carcasse
métallique ou d'un robinet : défaut d'isolement avec mise sous tension d'une masse.</li>
<li><strong>Contact d'eau avec une installation sous tension</strong> : fuite au-dessus
d'un tableau, inondation d'un local électrifié.</li>
</ul>

<p>Dans tous ces cas, la conduite à tenir est la même : couper le disjoncteur général,
n'utiliser aucun appareil du circuit concerné, et appeler un professionnel.</p>

<h3>Les situations urgentes sans danger immédiat</h3>

<p>D'autres situations justifient une intervention rapide sans présenter de risque
immédiat : coupure totale d'un logement occupé, différentiel impossible à réarmer, absence
de chauffage en période froide, panne affectant un congélateur plein ou un équipement
médical. Elles sont traitées en priorité, mais n'appellent pas les mêmes gestes de mise en
sécurité.</p>

<h2 id="gestes">Les gestes à adopter — et ceux à éviter</h2>

<h3>Ce qu'il faut faire</h3>
<ul>
<li>Localiser le disjoncteur général et savoir le manœuvrer.</li>
<li>Vérifier si la coupure touche tout le logement ou un seul circuit.</li>
<li>Débrancher les appareils du circuit concerné avant tout essai de réarmement.</li>
<li>Vérifier auprès des voisins si la coupure vient du réseau public.</li>
<li>Noter ce que vous avez constaté : bruit, odeur, moment du déclenchement, appareil en
service. Ces éléments accélèrent le diagnostic.</li>
</ul>

<h3>Ce qu'il ne faut pas faire</h3>
<ul>
<li>Réarmer plusieurs fois de suite un disjoncteur qui déclenche immédiatement : la
protection signale un défaut réel, et l'insistance aggrave l'échauffement.</li>
<li>Bloquer, caler ou shunter une protection.</li>
<li>Remplacer un disjoncteur par un calibre supérieur pour « qu'il ne saute plus » : le
câble n'est alors plus protégé.</li>
<li>Intervenir sur un tableau sous tension.</li>
<li>Utiliser de l'eau sur un départ de feu d'origine électrique avant d'avoir coupé
l'alimentation.</li>
</ul>

<h2 id="panne-generale">Coupure générale : d'où vient le problème ?</h2>

<p>Avant d'appeler, une vérification simple permet souvent de situer l'origine de la
coupure.</p>
{{TABLE_COUPURE}}

<h2 id="notre-intervention">Comment se passe une intervention en urgence</h2>

<p>L'appel téléphonique sert d'abord à qualifier la situation : nature du problème, présence
d'un risque, adresse et accès. Certaines situations trouvent une réponse immédiate par
téléphone — un différentiel déclenché par un appareil défectueux, par exemple.</p>

<p>Sur place, l'intervention commence par la mise en sécurité : coupure de l'alimentation
concernée, vérification de l'absence de tension, examen du tableau et des points chauds.
Vient ensuite l'identification du défaut, puis la réparation ou, si celle-ci ne peut être
menée immédiatement, une mise en sécurité provisoire permettant de rétablir le reste de
l'installation.</p>

<p>Toute intervention fait l'objet d'une explication de ce qui a été constaté et de ce qui a
été fait, ainsi que des travaux complémentaires éventuellement nécessaires.</p>
""",
    "faq": [
        ("Mon disjoncteur saute et ne se réarme plus, que faire ?",
         "<p>Débranchez tous les appareils du circuit concerné, puis tentez un réarmement. "
         "S'il tient, rebranchez les appareils un par un pour identifier celui qui provoque le "
         "défaut. S'il déclenche immédiatement même sans appareil branché, le défaut se situe "
         "dans l'installation elle-même : n'insistez pas et faites intervenir un "
         "professionnel.</p>"),
        ("Je sens une odeur de brûlé près d'une prise, est-ce grave ?",
         "<p>Oui. Une odeur de brûlé signale un échauffement, généralement dû à une connexion "
         "desserrée ou à une surcharge. C'est l'une des causes fréquentes de départ de feu "
         "d'origine électrique. Coupez le circuit concerné, n'utilisez plus cette prise et "
         "faites intervenir un électricien.</p>"),
        ("La coupure vient-elle de chez moi ou du réseau ?",
         "<p>Si vos voisins sont également privés d'électricité, l'origine est probablement sur "
         "le réseau public : il faut alors contacter le gestionnaire de réseau. Si vous êtes "
         "seul concerné et que le disjoncteur de branchement ou un dispositif du tableau est "
         "en position déclenchée, le défaut se situe dans votre installation.</p>"),
        ("Que faire si quelqu'un est en contact avec une source électrique ?",
         "<p>Ne touchez pas la personne. Coupez immédiatement l'alimentation au disjoncteur "
         "général. Si la coupure est impossible, écartez la personne du contact à l'aide d'un "
         "objet isolant et sec, sans jamais la toucher directement. Appelez ensuite les "
         "secours (15, 18 ou 112), même si la personne semble aller bien : une électrisation "
         "peut avoir des effets différés.</p>"),
        ("Un dépannage en urgence coûte-t-il plus cher ?",
         "<p>Une intervention réalisée en dehors des horaires habituels fait généralement "
         "l'objet d'une tarification spécifique, comme dans l'ensemble du secteur. Le principe "
         "reste le même : les conditions tarifaires sont communiquées avant l'intervention, "
         "et un devis est établi pour les travaux qui dépassent le simple dépannage.</p>"),
    ],
    "related": ["electricien-depannage", "panne-electrique", "disjoncteur", "court-circuit",
                "recherche-panne"],
})

SERVICES.append({
    "slug": "electricien-depannage",
    "path": "electricien-depannage.html",
    "icon": "tools",
    "category": "Dépannage",
    "nav_label": "Dépannage",
    "card_desc": ("Identifier l'origine d'un dysfonctionnement électrique et le corriger "
                  "durablement, sans se contenter de rétablir le courant."),
    "title": "Dépannage électrique — Diagnostic et réparation | Electricien Richard",
    "desc": ("Dépannage électrique : disjoncteur qui saute, prise hors service, panne "
             "partielle ou totale. Diagnostic méthodique et réparation durable dans les six "
             "départements couverts."),
    "h1": "Dépannage électrique : diagnostic et réparation",
    "intro": ("Un dépannage réussi ne consiste pas à rétablir le courant, mais à comprendre "
              "pourquoi il a été coupé. Tant que la cause n'est pas identifiée, le problème "
              "réapparaît."),
    "service_type": "Dépannage électrique",
    "quick": {
        "title": "Le dépannage électrique en résumé",
        "answer": (
            "<p><strong>Le dépannage électrique consiste à identifier l'origine d'un "
            "dysfonctionnement, puis à le corriger.</strong> Il se distingue du simple "
            "rétablissement du courant : réarmer un disjoncteur sans chercher pourquoi il a "
            "déclenché revient à ignorer un signal d'alarme.</p>"
            "<p>La démarche est méthodique : constater le symptôme, isoler le circuit "
            "concerné, mesurer, identifier le défaut, puis réparer.</p>"),
        "facts": [
            ("Symptômes traités", "Disjoncteur qui saute, coupure partielle ou totale, prise ou "
                                  "éclairage hors service, échauffement, faux contact"),
            ("Méthode", "Isolement des circuits, mesures d'isolement et de continuité, "
                        "contrôle des connexions"),
            ("Résultat attendu", "Cause identifiée et corrigée, pas seulement courant rétabli"),
            ("Suite possible", "Devis pour les travaux complémentaires si l'installation le justifie"),
        ],
    },
    "body": """
<h2 id="symptomes">Les pannes les plus fréquentes</h2>

<p>La plupart des demandes de dépannage relèvent d'un nombre limité de symptômes, dont
chacun oriente vers des causes précises.</p>

<h3>Un disjoncteur ou un différentiel qui déclenche</h3>
<p>C'est le motif le plus courant. Un <a href="/disjoncteur.html">disjoncteur divisionnaire</a>
déclenche en cas de surcharge ou de <a href="/court-circuit.html">court-circuit</a> ; un
dispositif différentiel déclenche en cas de fuite de courant vers la terre. Ces deux
comportements n'ont pas la même origine et n'appellent pas le même traitement.</p>

<h3>Une pièce ou un circuit sans courant</h3>
<p>Lorsque la coupure est limitée à une zone, le défaut se situe généralement sur le circuit
correspondant : protection déclenchée, conducteur coupé, connexion desserrée dans une boîte
de dérivation. Une <a href="/recherche-panne.html">recherche de panne</a> structurée permet
de localiser le point exact.</p>

<h3>Une prise ou un interrupteur qui ne fonctionne plus</h3>
<p>Souvent lié à une borne desserrée, à un appareillage usé ou à un conducteur sectionné.
Ce type de défaut est fréquemment accompagné de traces d'échauffement, qu'il faut examiner
avec attention.</p>

<h3>Des variations d'éclairage ou des faux contacts</h3>
<p>Lumières qui vacillent, appareils qui se coupent par intermittence : ces symptômes
signalent presque toujours une connexion défectueuse. Ils sont à traiter sans attendre, car
un mauvais contact chauffe.</p>

<h3>Un échauffement anormal</h3>
<p>Prise tiède, façade de tableau chaude, odeur de plastique : il s'agit d'une situation à
traiter en <a href="/electricien-urgence.html">urgence</a>, la connexion en cause pouvant
provoquer un départ de feu.</p>

<h2 id="methode">Comment se déroule un dépannage</h2>
{{PROCESS_DEPANNAGE}}

<h2 id="causes">Pourquoi une panne se répète-t-elle ?</h2>

<p>Une panne qui revient signale toujours une cause non traitée. Les configurations les plus
courantes sont les suivantes.</p>

<h3>Un défaut d'isolement latent</h3>
<p>Un circuit dont l'isolement s'est dégradé — humidité, câble blessé, matériel extérieur
corrodé — laisse fuir un courant faible. Le différentiel déclenche lorsque ce courant
atteint son seuil, ce qui explique des coupures apparemment aléatoires, souvent liées à la
météo ou à l'utilisation d'un appareil précis.</p>

<h3>Une surcharge structurelle</h3>
<p>Lorsque plusieurs appareils puissants partagent un circuit non prévu pour eux, le
disjoncteur déclenche dès qu'ils fonctionnent simultanément. Le remède n'est pas d'augmenter
le calibre de la protection, mais de créer un circuit adapté.</p>

<h3>Une connexion desserrée</h3>
<p>Une borne mal serrée augmente la résistance de contact, donc l'échauffement. Le phénomène
s'aggrave avec le temps, produisant d'abord des faux contacts, puis un noircissement, puis
un risque d'incendie.</p>

<h3>Un appareil défectueux</h3>
<p>Un appareil dont l'isolement est dégradé — ballon d'eau chaude, lave-linge, plaque de
cuisson — provoque des déclenchements du différentiel. La méthode d'identification consiste
à débrancher les appareils un à un.</p>

<h2 id="limites">Ce qu'un dépannage ne remplace pas</h2>

<p>Un dépannage traite un défaut ponctuel. Lorsque l'installation présente des faiblesses
de fond — absence de mise à la terre, tableau vétuste, absence de protection différentielle
adaptée — la réparation ponctuelle ne fait pas disparaître le risque. Dans ce cas, un
<a href="/diagnostic-electrique.html">diagnostic de l'installation</a> permet d'établir
l'ordre des travaux à envisager, qui relèvent alors de la
<a href="/mise-aux-normes-electrique.html">mise aux normes</a> ou de la
<a href="/renovation-electrique.html">rénovation</a>.</p>
""",
    "faq": [
        ("Combien coûte un dépannage électrique ?",
         "<p>Le coût dépend de la nature du défaut, du temps de recherche nécessaire et des "
         "fournitures à remplacer. Une intervention en horaires habituels et une intervention "
         "en soirée ou un jour férié ne relèvent pas des mêmes conditions. Les modalités "
         "tarifaires sont communiquées avant l'intervention, et un devis est établi dès que "
         "les travaux dépassent le dépannage lui-même.</p>"),
        ("Faut-il couper le courant avant l'arrivée de l'électricien ?",
         "<p>Oui si vous constatez un signe de danger — odeur de brûlé, échauffement, fumée, "
         "arc. Dans les autres cas, il est utile de laisser l'installation en l'état afin que "
         "le symptôme reste observable, ce qui facilite le diagnostic.</p>"),
        ("Puis-je remplacer moi-même une prise défectueuse ?",
         "<p>Techniquement, l'opération est simple. Les précautions, elles, ne le sont pas : "
         "il faut couper le circuit au tableau, vérifier l'absence de tension avec un "
         "appareil adapté, et respecter le raccordement du conducteur de protection. Si la "
         "prise présentait des traces d'échauffement, le remplacement seul ne suffit pas : "
         "l'origine de l'échauffement doit être identifiée.</p>"),
        ("Le dépannage règle-t-il définitivement le problème ?",
         "<p>Oui lorsque la cause est identifiée et traitée. En revanche, si le défaut révèle "
         "une faiblesse générale de l'installation, la réparation ponctuelle ne fait que "
         "traiter le symptôme le plus visible. Le constat est alors expliqué et les travaux "
         "utiles proposés, sans obligation.</p>"),
        ("Que faire si la panne concerne un appareil et non l'installation ?",
         "<p>Le dépannage électrique porte sur l'installation, pas sur la réparation des "
         "appareils électroménagers. Si le diagnostic établit qu'un appareil est en cause, il "
         "est mis hors circuit et l'information vous est communiquée afin que vous puissiez "
         "vous adresser à un réparateur spécialisé.</p>"),
    ],
    "related": ["panne-electrique", "recherche-panne", "disjoncteur", "court-circuit",
                "electricien-urgence"],
})

SERVICES.append({
    "slug": "panne-electrique",
    "path": "panne-electrique.html",
    "icon": "bolt",
    "category": "Dépannage",
    "card_desc": ("Comprendre une panne électrique : origines possibles, vérifications à "
                  "mener et solutions."),
    "title": "Panne électrique — Causes, vérifications et solutions | Electricien Richard",
    "desc": ("Panne électrique totale ou partielle : origines possibles, vérifications à "
             "effectuer soi-même, quand appeler un électricien et comment le défaut est "
             "identifié."),
    "h1": "Panne électrique : comprendre, vérifier, résoudre",
    "intro": ("Une panne électrique n'a pas toujours la même signification. Selon qu'elle "
              "touche tout le logement, une seule pièce ou un seul appareil, l'origine et la "
              "démarche à suivre diffèrent."),
    "service_type": "Dépannage de panne électrique",
    "quick": {
        "title": "Qu'est-ce qu'une panne électrique ?",
        "answer": (
            "<p><strong>Une panne électrique est une interruption totale ou partielle de "
            "l'alimentation en électricité.</strong> Elle peut provenir du réseau public, du "
            "branchement du logement, de l'installation intérieure ou d'un appareil "
            "défectueux.</p>"
            "<p>La première question à trancher est celle de l'étendue : tout le logement, "
            "une partie seulement, ou un seul appareil. Cette distinction oriente "
            "immédiatement vers la cause.</p>"),
        "facts": [
            ("Panne totale", "Réseau public, disjoncteur de branchement, ou défaut affectant "
                             "l'ensemble de l'installation"),
            ("Panne partielle", "Protection déclenchée sur un circuit, conducteur coupé, "
                                "connexion défectueuse"),
            ("Panne d'un appareil", "Appareil défectueux ou prise hors service"),
            ("Premier réflexe", "Regarder le tableau : quelle protection est en position basse ?"),
            ("À éviter", "Réarmer en boucle une protection qui déclenche immédiatement"),
        ],
    },
    "body": """
<h2 id="types">Panne totale, partielle ou isolée ?</h2>

<h3>La panne totale</h3>
<p>Aucun appareil ne fonctionne, aucun éclairage ne s'allume. Trois origines sont possibles :
une coupure du réseau public, un déclenchement du disjoncteur de branchement, ou un défaut
généralisé de l'installation. La vérification auprès des voisins permet de trancher
immédiatement entre la première hypothèse et les deux autres.</p>

<h3>La panne partielle</h3>
<p>Une pièce, un étage ou un type d'usage — l'éclairage, les prises — ne fonctionne plus.
Le défaut se situe alors sur un circuit identifié. Le tableau indique généralement lequel :
la protection correspondante est en position déclenchée.</p>

<h3>La panne isolée</h3>
<p>Un seul point ne fonctionne plus : une prise, un luminaire, un appareil. Le défaut est
local — appareillage usé, conducteur desserré, lampe ou appareil défectueux.</p>

<h2 id="causes">Les causes les plus fréquentes</h2>
{{TABLE_CAUSES_PANNE}}

<h2 id="verifications">Les vérifications à faire avant d'appeler</h2>

<p>Quelques contrôles simples, sans aucun démontage, permettent souvent d'identifier
l'origine du problème — ou au minimum de fournir des éléments utiles au dépanneur.</p>

<ol>
<li><strong>Vos voisins ont-ils du courant ?</strong> Si non, la coupure vient du réseau
public et il faut contacter le gestionnaire de réseau.</li>
<li><strong>Quelle protection est déclenchée ?</strong> Ouvrez le tableau et repérez le
dispositif en position basse : disjoncteur de branchement, interrupteur différentiel, ou
disjoncteur divisionnaire.</li>
<li><strong>Que s'est-il passé juste avant ?</strong> Mise en route d'un appareil, orage,
travaux, forte pluie, branchement d'une rallonge : ces éléments orientent le diagnostic.</li>
<li><strong>Le défaut est-il permanent ou intermittent ?</strong> Une panne qui revient à
heure fixe évoque souvent un appareil programmé, comme un chauffe-eau.</li>
<li><strong>Après avoir débranché les appareils du circuit, la protection tient-elle ?</strong>
Si oui, un appareil est en cause. Si non, le défaut est dans l'installation.</li>
</ol>

<h2 id="terminologie">Comprendre ce que dit le tableau</h2>

<p>Le dispositif qui a déclenché indique la nature du problème.</p>
{{TABLE_TABLEAU_SIGNAUX}}

<h2 id="intervention">Comment la panne est identifiée</h2>

<p>La recherche suit une logique d'élimination : on sépare l'installation en parties, on
teste chaque partie, et on réduit progressivement le périmètre du défaut. Les mesures
d'isolement, réalisées circuit par circuit hors tension, permettent de distinguer un défaut
franc d'une dégradation progressive. Le détail de cette démarche est présenté sur la page
<a href="/recherche-panne.html">recherche de panne</a>.</p>
""",
    "faq": [
        ("Pourquoi ai-je une panne électrique alors que mes voisins ont du courant ?",
         "<p>Parce que le problème vient de votre branchement ou de votre installation "
         "intérieure. Vérifiez la position du disjoncteur de branchement — celui placé près du "
         "compteur — puis celle des dispositifs du tableau. Un différentiel déclenché indique "
         "une fuite de courant, un disjoncteur déclenché une surcharge ou un court-circuit.</p>"),
        ("Ma panne revient toujours à la même heure, pourquoi ?",
         "<p>C'est souvent le signe qu'un appareil programmé est en cause. Le chauffe-eau, qui "
         "se déclenche en heures creuses, est le suspect le plus fréquent : lorsque sa "
         "résistance présente un défaut d'isolement, le différentiel coupe au moment précis de "
         "sa mise en route.</p>"),
        ("Que faire si le disjoncteur de branchement a sauté ?",
         "<p>Coupez d'abord tous les disjoncteurs du tableau, puis réarmez le disjoncteur de "
         "branchement. Remettez ensuite les circuits en service un par un : celui qui provoque "
         "un nouveau déclenchement est en cause. Si le disjoncteur de branchement ne tient pas "
         "même avec tous les circuits coupés, ne forcez pas.</p>"),
        ("Une panne électrique peut-elle endommager mes appareils ?",
         "<p>Une coupure simple est sans conséquence pour la plupart des appareils. En "
         "revanche, une surtension — foudre, défaut sur le réseau — peut endommager les "
         "équipements électroniques. Un parafoudre, obligatoire dans certaines zones et "
         "configurations d'installation, limite ce risque.</p>"),
        ("Combien de temps faut-il pour trouver une panne ?",
         "<p>Cela varie fortement. Un défaut franc — court-circuit, appareil clairement en "
         "cause — se localise rapidement. Un défaut intermittent ou lié à l'humidité demande "
         "davantage de temps, car il faut parfois recréer les conditions dans lesquelles il "
         "apparaît.</p>"),
    ],
    "related": ["recherche-panne", "electricien-depannage", "disjoncteur", "court-circuit",
                "electricien-urgence"],
})

SERVICES.append({
    "slug": "recherche-panne",
    "path": "recherche-panne.html",
    "icon": "search",
    "category": "Dépannage",
    "card_desc": ("La méthode de localisation d'un défaut électrique : isolement des "
                  "circuits, mesures et interprétation."),
    "title": "Recherche de panne électrique — Méthode et diagnostic | Electricien Richard",
    "desc": ("Recherche de panne électrique : méthode d'isolement des circuits, mesures "
             "d'isolement et de continuité, localisation des défauts intermittents."),
    "h1": "Recherche de panne électrique",
    "intro": ("Localiser un défaut électrique est un travail de méthode. Il ne s'agit pas de "
              "deviner, mais de réduire progressivement le périmètre dans lequel le défaut "
              "peut se trouver."),
    "service_type": "Recherche de panne électrique",
    "quick": {
        "title": "Comment trouve-t-on une panne électrique ?",
        "answer": (
            "<p><strong>La recherche de panne procède par élimination.</strong> L'installation "
            "est divisée en parties, chaque partie est testée séparément, et le périmètre du "
            "défaut se réduit à chaque étape jusqu'à isoler le point exact.</p>"
            "<p>Les mesures utilisées sont principalement la mesure d'isolement (entre "
            "conducteurs et entre conducteur et terre), la mesure de continuité et le contrôle "
            "des connexions.</p>"),
        "facts": [
            ("Principe", "Diviser l'installation, tester chaque partie, réduire le périmètre"),
            ("Mesures", "Isolement, continuité, tension, contrôle des serrages"),
            ("Défauts francs", "Court-circuit, conducteur coupé : localisation généralement rapide"),
            ("Défauts intermittents", "Humidité, faux contact, dilatation : recherche plus longue"),
            ("Sans destruction", "L'objectif est de localiser avant d'ouvrir ou de démonter"),
        ],
    },
    "body": """
<h2 id="pourquoi">Pourquoi une recherche de panne est-elle parfois longue ?</h2>

<p>Un défaut électrique n'est pas toujours visible. Un conducteur peut être blessé à
l'intérieur d'une gaine, une connexion peut se desserrer progressivement dans une boîte
encastrée, l'isolement d'un câble enterré peut se dégrader lentement sous l'effet de
l'humidité. Rien de tout cela ne se voit à l'œil nu.</p>

<p>À cela s'ajoutent les défauts intermittents, qui n'apparaissent que dans certaines
conditions : après une pluie, lors du fonctionnement d'un appareil précis, à une certaine
température. Ces défauts imposent parfois de recréer les conditions dans lesquelles ils se
manifestent.</p>

<h2 id="methode">La méthode de recherche, étape par étape</h2>
{{STEPS_RECHERCHE}}

<h2 id="mesures">Les mesures utilisées</h2>

<h3>La mesure d'isolement</h3>
<p>Réalisée hors tension avec un contrôleur d'isolement, elle évalue la qualité de
l'isolation entre les conducteurs actifs et la terre. Une valeur faible révèle un chemin de
fuite : humidité, câble détérioré, matériel dégradé. C'est la mesure de référence pour
expliquer les déclenchements d'un différentiel.</p>

<h3>La mesure de continuité</h3>
<p>Elle vérifie qu'un conducteur assure bien la liaison entre deux points. Elle sert
notamment à contrôler la continuité du conducteur de protection, c'est-à-dire l'efficacité
réelle de la mise à la terre.</p>

<h3>Le contrôle des connexions</h3>
<p>Une part importante des défauts se trouve aux points de raccordement : bornes du tableau,
boîtes de dérivation, appareillages. Le contrôle porte sur le serrage, l'état des
conducteurs et les traces éventuelles d'échauffement.</p>

<h3>Les mesures de tension et de courant</h3>
<p>Elles permettent de vérifier la présence et le niveau de la tension en différents points,
et de contrôler la charge réelle d'un circuit lorsqu'une surcharge est suspectée.</p>

<h2 id="defauts">Les défauts les plus souvent trouvés</h2>
{{TABLE_DEFAUTS}}

<h2 id="apres">Après la localisation</h2>

<p>Une fois le défaut localisé, la réparation dépend de sa nature : remplacement d'un
appareillage, reprise d'une connexion, remplacement d'une portion de circuit, ou
remplacement d'un matériel de protection. Lorsque le défaut résulte d'une faiblesse
générale de l'installation, la réparation est expliquée comme telle : elle rétablit le
fonctionnement, mais un traitement de fond peut rester nécessaire.</p>
""",
    "faq": [
        ("Faut-il casser les murs pour trouver une panne électrique ?",
         "<p>Dans la grande majorité des cas, non. La localisation se fait par mesures et par "
         "élimination, ce qui permet de cibler précisément la zone à ouvrir. Lorsqu'une "
         "ouverture est nécessaire, elle est limitée au point identifié et vous est présentée "
         "avant d'être réalisée.</p>"),
        ("Pourquoi mon différentiel déclenche-t-il seulement quand il pleut ?",
         "<p>Parce qu'un circuit présente un défaut d'isolement qui s'aggrave avec l'humidité. "
         "L'eau crée un chemin de fuite vers la terre, et le différentiel coupe lorsque le "
         "courant de fuite atteint son seuil. Les circuits extérieurs et les matériels de "
         "jardin sont les premiers concernés.</p>"),
        ("Une panne intermittente peut-elle être trouvée ?",
         "<p>Oui, mais la recherche demande plus de temps. La démarche consiste à identifier "
         "les conditions d'apparition — appareil, météo, moment de la journée — puis à mesurer "
         "l'installation dans ces conditions. Les mesures d'isolement révèlent souvent une "
         "dégradation avant même que le défaut ne devienne permanent.</p>"),
        ("Un électricien peut-il localiser un câble dans un mur ?",
         "<p>Oui, à l'aide d'un détecteur de câbles ou d'un traceur, avec une précision qui "
         "dépend de la nature du mur et de la profondeur d'encastrement. Cette recherche est "
         "utile avant un percement, pour éviter d'endommager un circuit existant.</p>"),
        ("Quelle différence entre recherche de panne et diagnostic ?",
         "<p>La recherche de panne vise un défaut précis qui empêche le fonctionnement. Le "
         "<a href=\"/diagnostic-electrique.html\">diagnostic</a> évalue l'état général de "
         "l'installation, même en l'absence de panne : sécurité, conformité, capacité à "
         "supporter les usages actuels.</p>"),
    ],
    "related": ["panne-electrique", "electricien-depannage", "diagnostic-electrique",
                "court-circuit", "disjoncteur"],
})

# =========================================================================
# Blocs reutilisables injectes dans les corps de page via des jetons {{NOM}}
# =========================================================================
BLOCKS = {}

BLOCKS["TABLE_COUPURE"] = """
<div class="table-wrap"><table>
<caption>Localiser l'origine d'une coupure générale</caption>
<thead><tr><th scope="col">Constat</th><th scope="col">Origine probable</th><th scope="col">Conduite à tenir</th></tr></thead>
<tbody>
<tr><td>Les voisins sont aussi sans courant</td><td>Coupure du réseau public</td><td>Contacter le gestionnaire de réseau ; aucune intervention chez vous n'est utile</td></tr>
<tr><td>Le disjoncteur de branchement est déclenché</td><td>Surcharge globale ou défaut affectant toute l'installation</td><td>Couper tous les circuits, réarmer, puis remettre les circuits un par un</td></tr>
<tr><td>Un interrupteur différentiel est déclenché</td><td>Fuite de courant vers la terre sur l'un des circuits qu'il protège</td><td>Ouvrir les disjoncteurs concernés, réarmer le différentiel, refermer un à un</td></tr>
<tr><td>Un disjoncteur divisionnaire est déclenché</td><td>Surcharge ou court-circuit sur ce circuit précis</td><td>Débrancher les appareils du circuit avant de réarmer une seule fois</td></tr>
<tr><td>Rien n'est déclenché mais il n'y a pas de courant</td><td>Défaut d'alimentation en amont ou coupure interne</td><td>Ne pas intervenir sur le panneau de comptage : faire appel à un professionnel</td></tr>
</tbody></table></div>
"""

BLOCKS["TABLE_CAUSES_PANNE"] = """
<div class="table-wrap"><table>
<caption>Symptômes et causes fréquentes d'une panne électrique</caption>
<thead><tr><th scope="col">Symptôme</th><th scope="col">Causes les plus fréquentes</th></tr></thead>
<tbody>
<tr><td>Coupure totale du logement</td><td>Coupure réseau, déclenchement du disjoncteur de branchement, dépassement de la puissance souscrite</td></tr>
<tr><td>Une pièce entière sans courant</td><td>Disjoncteur divisionnaire déclenché, conducteur coupé, connexion desserrée en boîte de dérivation</td></tr>
<tr><td>Les prises fonctionnent mais pas l'éclairage</td><td>Circuit d'éclairage protégé séparément : protection déclenchée ou défaut sur ce circuit</td></tr>
<tr><td>Déclenchement du différentiel</td><td>Défaut d'isolement d'un appareil ou d'un circuit, humidité, matériel extérieur dégradé</td></tr>
<tr><td>Déclenchement répété d'un disjoncteur</td><td>Surcharge du circuit, court-circuit, calibre inadapté à l'usage réel</td></tr>
<tr><td>Une seule prise hors service</td><td>Appareillage usé, borne desserrée, conducteur sectionné</td></tr>
<tr><td>Éclairage qui vacille</td><td>Faux contact, connexion desserrée, source lumineuse ou variateur inadapté</td></tr>
</tbody></table></div>
"""

BLOCKS["TABLE_TABLEAU_SIGNAUX"] = """
<div class="table-wrap"><table>
<caption>Ce que signale chaque dispositif du tableau</caption>
<thead><tr><th scope="col">Dispositif</th><th scope="col">Rôle</th><th scope="col">Signification d'un déclenchement</th></tr></thead>
<tbody>
<tr><td>Disjoncteur de branchement</td><td>Protège l'installation dans son ensemble et limite la puissance appelée</td><td>Dépassement de la puissance souscrite ou défaut généralisé</td></tr>
<tr><td>Interrupteur différentiel 30 mA</td><td>Protège les personnes contre les fuites de courant vers la terre</td><td>Défaut d'isolement sur l'un des circuits protégés ou sur un appareil</td></tr>
<tr><td>Disjoncteur divisionnaire</td><td>Protège un circuit contre les surcharges et les courts-circuits</td><td>Trop d'appareils sur le circuit, ou court-circuit</td></tr>
<tr><td>Disjoncteur différentiel</td><td>Cumule les deux fonctions sur un même circuit</td><td>Surcharge, court-circuit ou fuite de courant sur ce circuit</td></tr>
<tr><td>Parafoudre</td><td>Limite les surtensions d'origine atmosphérique</td><td>Voyant de fin de vie : cartouche à remplacer</td></tr>
</tbody></table></div>
"""

BLOCKS["TABLE_DEFAUTS"] = """
<div class="table-wrap"><table>
<caption>Défauts les plus fréquemment localisés lors d'une recherche de panne</caption>
<thead><tr><th scope="col">Défaut</th><th scope="col">Où on le trouve</th><th scope="col">Comment il se manifeste</th></tr></thead>
<tbody>
<tr><td>Connexion desserrée</td><td>Bornes du tableau, boîtes de dérivation, appareillages</td><td>Faux contact, échauffement, noircissement, coupure intermittente</td></tr>
<tr><td>Défaut d'isolement</td><td>Circuits extérieurs, salles d'eau, câbles enterrés, appareils de chauffage de l'eau</td><td>Déclenchement du différentiel, souvent lié à l'humidité ou à un appareil</td></tr>
<tr><td>Conducteur blessé</td><td>Passage de gaine, percement, fixation, zone de travaux antérieurs</td><td>Court-circuit franc ou dégradation progressive de l'isolement</td></tr>
<tr><td>Appareillage usé</td><td>Prises fortement sollicitées, interrupteurs anciens</td><td>Contact intermittent, chaleur, jeu mécanique</td></tr>
<tr><td>Surcharge de circuit</td><td>Cuisines, bureaux, ateliers</td><td>Déclenchement du disjoncteur à chaque usage simultané</td></tr>
<tr><td>Dégradation par les rongeurs</td><td>Combles, vides sanitaires, dépendances</td><td>Coupure brutale ou défaut d'isolement dans une zone peu visitée</td></tr>
</tbody></table></div>
"""

BLOCKS["PROCESS_DEPANNAGE"] = """
<ol class="steps">
<li><h3>Description du symptôme</h3><p>Nature de la panne, moment d'apparition, circuits concernés, événements précédant le déclenchement.</p></li>
<li><h3>Mise en sécurité</h3><p>Coupure de l'alimentation concernée et vérification de l'absence de tension avant toute intervention.</p></li>
<li><h3>Examen du tableau</h3><p>Position des protections, état des connexions, traces d'échauffement, repérage des circuits.</p></li>
<li><h3>Isolement et mesures</h3><p>Séparation des circuits, mesures d'isolement et de continuité pour localiser le défaut.</p></li>
<li><h3>Réparation</h3><p>Reprise de la connexion, remplacement du matériel défectueux ou de la portion de circuit en cause.</p></li>
<li><h3>Contrôle et explication</h3><p>Vérification du bon fonctionnement, essai des protections, explication du défaut constaté et des suites éventuelles.</p></li>
</ol>
"""

BLOCKS["STEPS_RECHERCHE"] = """
<ol class="steps">
<li><h3>Reproduire le symptôme</h3><p>Identifier les conditions exactes dans lesquelles le défaut apparaît : appareil en service, météo, moment de la journée.</p></li>
<li><h3>Délimiter le périmètre</h3><p>Déterminer quels circuits sont concernés en ouvrant les protections une à une.</p></li>
<li><h3>Isoler et mesurer</h3><p>Hors tension, mesurer l'isolement et la continuité de chaque circuit suspect pour distinguer le défaut réel des circuits sains.</p></li>
<li><h3>Réduire la zone</h3><p>Sectionner le circuit en portions — boîtes de dérivation, points d'utilisation — et refaire les mesures sur chaque portion.</p></li>
<li><h3>Localiser le point exact</h3><p>Identifier la connexion, le matériel ou la longueur de câble en cause, avec le minimum d'ouverture.</p></li>
<li><h3>Réparer et vérifier</h3><p>Corriger le défaut, puis contrôler par une nouvelle mesure que l'installation retrouve des valeurs correctes.</p></li>
</ol>
"""

BLOCKS["PROCESS_STEPS"] = """
<ol class="steps">
<li><h3>Prise de contact</h3><p>Description du besoin par téléphone ou via le formulaire. Les situations urgentes sont qualifiées immédiatement par téléphone.</p></li>
<li><h3>Examen sur place</h3><p>État de l'installation existante, contraintes du bâtiment, faisabilité et points de sécurité à traiter en priorité.</p></li>
<li><h3>Devis détaillé</h3><p>Description des travaux, fournitures, délais et prix. Aucun travaux n'est engagé avant votre accord.</p></li>
<li><h3>Réalisation</h3><p>Intervention planifiée, coupures annoncées à l'avance, protection des lieux et nettoyage en fin de chantier.</p></li>
<li><h3>Contrôle et remise</h3><p>Essais des protections, vérification du fonctionnement, repérage du tableau et explications sur l'installation.</p></li>
</ol>
"""

def register_blocks(extra):
    BLOCKS.update(extra)

SERVICES.append({
    "slug": "installation-electrique",
    "path": "installation-electrique.html",
    "icon": "home",
    "category": "Travaux",
    "nav_label": "Installation",
    "card_desc": ("Concevoir et réaliser une installation électrique neuve : circuits, "
                  "protections, tableau et mise à la terre."),
    "title": "Installation électrique — Conception et réalisation | Electricien Richard",
    "desc": ("Installation électrique complète : dimensionnement des circuits, tableau, mise "
             "à la terre, conformité NF C 15-100. Logements, commerces et locaux "
             "professionnels."),
    "h1": "Installation électrique : conception et réalisation",
    "intro": ("Une installation électrique se conçoit avant de se poser. Le nombre de "
              "circuits, la section des conducteurs, la nature des protections et "
              "l'implantation du tableau découlent d'une analyse des usages, pas d'un "
              "catalogue standard."),
    "service_type": "Installation électrique",
    "quick": {
        "title": "Ce que comprend une installation électrique",
        "answer": (
            "<p><strong>Une installation électrique complète comprend l'arrivée et le comptage, "
            "le tableau de répartition, les circuits, les points d'utilisation et la mise à la "
            "terre.</strong> Sa conception est encadrée par la norme NF C 15-100, qui fixe "
            "notamment le nombre minimal de circuits, les sections de conducteurs et les "
            "protections obligatoires.</p>"
            "<p>Une installation neuve ou entièrement rénovée doit faire l'objet d'une "
            "attestation de conformité visée par le Consuel avant sa mise en service par le "
            "gestionnaire de réseau.</p>"),
        "facts": [
            ("Concerne", "Construction neuve, extension, rénovation lourde, changement d'usage d'un local"),
            ("Référence", "Norme NF C 15-100"),
            ("Éléments clés", "Tableau, circuits spécialisés, différentiels 30 mA, mise à la terre"),
            ("Formalité", "Attestation de conformité visée par le Consuel pour une installation neuve"),
            ("Préalable", "Étude des besoins et des puissances avant tout chiffrage"),
        ],
    },
    "body": """
<h2 id="etapes">Les composantes d'une installation</h2>

<h3>Le point de livraison et le tableau</h3>
<p>L'installation commence au disjoncteur de branchement, qui protège l'ensemble et limite
la puissance appelée. En aval, le <a href="/tableau-electrique.html">tableau de
répartition</a> distribue et protège chaque circuit. Son emplacement n'est pas libre : la
norme prévoit un espace technique dédié, accessible, hors des volumes de sécurité des
pièces d'eau.</p>

<h3>Les circuits</h3>
<p>Une installation moderne repose sur une séparation stricte des usages. L'éclairage, les
prises, et chaque gros appareil disposent de circuits distincts. Cette séparation limite
l'étendue d'une coupure et permet de dimensionner correctement chaque protection.</p>

<div class="table-wrap"><table>
<caption>Principaux circuits d'un logement et leurs caractéristiques usuelles</caption>
<thead><tr><th scope="col">Circuit</th><th scope="col">Section usuelle</th><th scope="col">Protection usuelle</th><th scope="col">Remarque</th></tr></thead>
<tbody>
<tr><td>Éclairage</td><td>1,5 mm²</td><td>16 A maximum</td><td>Nombre de points lumineux limité par circuit</td></tr>
<tr><td>Prises de courant 16 A</td><td>1,5 mm² ou 2,5 mm²</td><td>16 A ou 20 A selon la section</td><td>Le nombre de socles admis dépend de la section</td></tr>
<tr><td>Plaque de cuisson</td><td>6 mm²</td><td>32 A</td><td>Circuit spécialisé, protection différentielle de type A</td></tr>
<tr><td>Lave-linge, lave-vaisselle, four</td><td>2,5 mm²</td><td>20 A</td><td>Un circuit spécialisé par appareil</td></tr>
<tr><td>Chauffe-eau</td><td>2,5 mm²</td><td>20 A</td><td>Circuit spécialisé, souvent commandé en heures creuses</td></tr>
<tr><td>Borne de recharge</td><td>Selon puissance et longueur</td><td>Dédiée et adaptée</td><td>Protection différentielle spécifique — voir <a href="/borne-recharge.html">borne de recharge</a></td></tr>
</tbody></table>
</div>
<p class="form-note">Les valeurs ci-dessus correspondent aux configurations les plus
courantes. Le dimensionnement réel dépend de la longueur des circuits, du mode de pose et
des puissances effectivement installées : il est établi lors de l'étude.</p>

<h3>Les protections</h3>
<p>Chaque circuit est protégé contre les surintensités par un disjoncteur dont le calibre
correspond à la section du conducteur. L'ensemble des circuits doit par ailleurs être
protégé par des dispositifs différentiels de sensibilité 30 mA, dont le nombre et le type
dépendent de la surface du logement et de la nature des circuits — certains, comme la
plaque de cuisson ou le lave-linge, exigent un différentiel de type A.</p>

<h3>La mise à la terre</h3>
<p>Prise de terre, conducteur principal, barrette de coupure, liaisons équipotentielles :
c'est l'ossature de la sécurité. Un conducteur de protection doit accompagner chaque
circuit jusqu'aux points d'utilisation qui l'exigent.</p>

<h2 id="etude">L'étude préalable : ce qui est examiné</h2>

<p>Avant tout chiffrage, plusieurs éléments sont déterminés :</p>

<ul>
<li>l'usage réel de chaque pièce et les équipements prévus, y compris à moyen terme ;</li>
<li>la puissance nécessaire et, le cas échéant, la puissance à souscrire ;</li>
<li>le type d'alimentation disponible, monophasée ou triphasée ;</li>
<li>les longueurs de circuits, qui influencent la section des conducteurs ;</li>
<li>les contraintes du bâtiment : nature des murs, présence de gaines, combles, sous-sol ;</li>
<li>les pièces particulières : salle d'eau, cuisine, extérieur, local technique, cave.</li>
</ul>

<p>C'est cette étude qui détermine le nombre de circuits et la taille du tableau, et non
l'inverse. Un tableau prévu trop juste condamne toute évolution ultérieure.</p>

<h2 id="cas">Installation neuve, extension ou changement d'usage</h2>

<h3>Construction neuve</h3>
<p>L'installation est conçue avec le projet. Les cheminements sont intégrés au gros œuvre,
ce qui permet une réalisation propre et une évolution facilitée par la mise en place de
gaines en attente.</p>

<h3>Extension ou surélévation</h3>
<p>La question centrale est la capacité de l'installation existante à absorber la nouvelle
partie : place disponible au tableau, puissance souscrite, état des protections. Une
extension raccordée sur un tableau déjà saturé produit inévitablement des déclenchements.</p>

<h3>Changement d'usage d'un local</h3>
<p>Transformer un garage en pièce de vie, un atelier en logement ou un local d'habitation
en local professionnel modifie les exigences applicables. L'installation d'origine est
rarement transposable telle quelle.</p>

<h2 id="conformite">Conformité et mise en service</h2>

<p>Pour une installation neuve ou entièrement rénovée, une attestation de conformité doit
être établie et visée par le Consuel. C'est ce document qui permet au gestionnaire de
réseau de procéder à la mise en service. Il s'agit d'une étape administrative obligatoire,
distincte de la vérification technique réalisée en fin de chantier.</p>
""",
    "faq": [
        ("Combien de circuits faut-il dans une maison ?",
         "<p>Il n'existe pas de chiffre unique : le nombre dépend de la surface, du nombre de "
         "pièces et des équipements. La norme impose des circuits spécialisés pour la plaque "
         "de cuisson et les gros appareils, ainsi que des circuits distincts pour l'éclairage "
         "et les prises, avec un nombre maximal de points par circuit. En pratique, une maison "
         "correctement équipée dispose de nettement plus de circuits qu'une installation "
         "ancienne de surface équivalente.</p>"),
        ("Faut-il du triphasé ou du monophasé ?",
         "<p>Le monophasé suffit à la grande majorité des logements. Le triphasé se justifie "
         "lorsque des équipements l'exigent — certaines machines, une borne de recharge de "
         "forte puissance, un local professionnel — ou lorsque la puissance nécessaire dépasse "
         "ce qu'un branchement monophasé peut fournir. Le changement relève d'une demande "
         "auprès du gestionnaire de réseau.</p>"),
        ("Qu'est-ce que le Consuel et quand est-il obligatoire ?",
         "<p>Le Consuel est l'organisme qui vise les attestations de conformité des "
         "installations électriques. Son visa est requis pour la mise en service d'une "
         "installation neuve, d'une installation entièrement rénovée, ou lors d'un changement "
         "de nature du raccordement. Sans lui, le gestionnaire de réseau ne procède pas à la "
         "mise sous tension.</p>"),
        ("Peut-on prévoir une installation évolutive ?",
         "<p>Oui, et c'est fortement recommandé. Cela passe par un tableau comportant des "
         "modules libres, des gaines en attente vers les zones susceptibles d'évoluer — "
         "garage, combles, extérieur — et une puissance souscrite cohérente avec les projets "
         "envisagés. Le surcoût à la construction est sans commune mesure avec celui d'une "
         "reprise ultérieure.</p>"),
        ("Combien de temps dure la réalisation d'une installation complète ?",
         "<p>La durée dépend de la surface, du nombre de circuits et de la nature du bâti. "
         "Elle se décompose généralement en deux phases : la pose des gaines et des "
         "conducteurs avant les finitions, puis l'appareillage et le raccordement du tableau "
         "après. Le planning est établi avec les autres corps d'état.</p>"),
    ],
    "related": ["tableau-electrique", "renovation-electrique", "mise-aux-normes-electrique",
                "prise-electrique", "eclairage", "borne-recharge"],
})

SERVICES.append({
    "slug": "renovation-electrique",
    "path": "renovation-electrique.html",
    "icon": "tools",
    "category": "Travaux",
    "nav_label": "Rénovation",
    "card_desc": ("Reprendre tout ou partie d'une installation existante, par étapes ou en "
                  "une seule fois."),
    "title": "Rénovation électrique — Reprise d'installation | Electricien Richard",
    "desc": ("Rénovation électrique d'un logement : diagnostic préalable, ordre des travaux, "
             "rénovation partielle ou complète, conformité et sécurité."),
    "h1": "Rénovation électrique d'un logement",
    "intro": ("Rénover une installation électrique, ce n'est pas nécessairement tout refaire. "
              "L'enjeu est de déterminer ce qui doit être repris, dans quel ordre, et ce qui "
              "peut être conservé sans compromettre la sécurité."),
    "service_type": "Rénovation électrique",
    "quick": {
        "title": "Rénovation électrique : l'essentiel",
        "answer": (
            "<p><strong>La rénovation électrique consiste à reprendre tout ou partie d'une "
            "installation existante pour la remettre en sécurité et l'adapter aux usages "
            "actuels.</strong> Elle peut être partielle — tableau, circuits sensibles — ou "
            "complète, avec remplacement de l'ensemble des conducteurs.</p>"
            "<p>L'ordre des travaux compte autant que leur nature : la mise à la terre et le "
            "tableau conditionnent la sécurité de tout le reste, ils sont donc traités en "
            "premier.</p>"),
        "facts": [
            ("Rénovation partielle", "Tableau, mise à la terre, circuits de cuisine et de salle d'eau"),
            ("Rénovation complète", "Reprise de l'ensemble des circuits et des points d'utilisation"),
            ("Signes déclencheurs", "Fusibles à broche, absence de terre, tableau saturé, traces d'échauffement"),
            ("Étalement possible", "Oui, à condition de respecter l'ordre de priorité"),
            ("Préalable", "Diagnostic de l'installation existante"),
        ],
    },
    "body": """
<h2 id="quand">Quand faut-il rénover une installation ?</h2>

<p>Plusieurs constats justifient une rénovation, du plus urgent au plus confortable.</p>

<h3>Les signes qui imposent une reprise</h3>
<ul>
<li>Installation dépourvue de mise à la terre, ou terre non raccordée à l'ensemble des
circuits.</li>
<li>Tableau équipé de fusibles à broche, ou sans dispositif différentiel 30 mA.</li>
<li>Conducteurs sous isolant dégradé, cassant ou en tissu.</li>
<li>Traces d'échauffement : noircissement, déformation, odeur.</li>
<li>Matériel vétuste dans les pièces d'eau ou en extérieur.</li>
</ul>

<h3>Les signes qui invitent à envisager des travaux</h3>
<ul>
<li>Tableau sans emplacement libre, empêchant tout ajout de circuit.</li>
<li>Déclenchements répétés lors d'usages simultanés normaux.</li>
<li>Recours permanent aux multiprises et aux rallonges.</li>
<li>Absence de circuits spécialisés pour l'électroménager.</li>
<li>Projet d'installer une <a href="/borne-recharge.html">borne de recharge</a>, une pompe
à chaleur ou une climatisation.</li>
</ul>

<h2 id="ordre">Dans quel ordre mener les travaux</h2>

<ol class="steps">
<li><h3>La mise à la terre</h3><p>Sans elle, aucune protection ne peut fonctionner correctement. Elle conditionne tout le reste.</p></li>
<li><h3>Le tableau</h3><p>Protection différentielle 30 mA, protection de chaque circuit, repérage clair et modules disponibles pour l'avenir.</p></li>
<li><h3>Les pièces d'eau et la cuisine</h3><p>Ce sont les locaux où le risque est le plus élevé et où les défauts de conformité sont les plus fréquents.</p></li>
<li><h3>Les circuits vétustes</h3><p>Remplacement des conducteurs dont l'isolement est dégradé, en commençant par les plus sollicités.</p></li>
<li><h3>Le confort et les usages</h3><p>Ajout de prises, points d'éclairage, circuits dédiés, commandes et équipements complémentaires.</p></li>
</ol>

<h2 id="partielle-complete">Rénovation partielle ou complète ?</h2>

<div class="table-wrap"><table>
<caption>Comparaison des deux approches</caption>
<thead><tr><th scope="col">Critère</th><th scope="col">Rénovation partielle</th><th scope="col">Rénovation complète</th></tr></thead>
<tbody>
<tr><td>Périmètre</td><td>Tableau, mise à la terre, circuits prioritaires</td><td>Ensemble des conducteurs et des points d'utilisation</td></tr>
<tr><td>Conditions</td><td>Conducteurs existants en bon état, terre présente ou créable</td><td>Isolement dégradé, absence de terre généralisée, bâti à reprendre</td></tr>
<tr><td>Impact sur le logement</td><td>Limité, réalisable en site occupé</td><td>Important : saignées, reprises de finitions</td></tr>
<tr><td>Conformité</td><td>Améliore la sécurité sans rendre l'ensemble conforme au neuf</td><td>Permet une conformité d'ensemble à la norme en vigueur</td></tr>
<tr><td>Évolutivité</td><td>Dépend de la capacité du tableau retenu</td><td>Installation dimensionnée pour les usages futurs</td></tr>
</tbody></table></div>

<h2 id="deroulement">Comment se déroule une rénovation</h2>

<p>Une rénovation électrique commence toujours par un
<a href="/diagnostic-electrique.html">examen de l'existant</a> : état du tableau, présence
et qualité de la terre, nature et isolement des conducteurs, repérage des circuits. Ce
constat détermine le périmètre réel des travaux.</p>

<p>Vient ensuite l'étude des cheminements, étape décisive dans le bâti ancien. Murs en
pierre, planchers bois, combles, plinthes et doublages existants offrent des passages qui
évitent des saignées inutiles. C'est ce travail préparatoire qui fait la différence entre
un chantier maîtrisé et un chantier destructeur.</p>

<p>La réalisation est ensuite planifiée en tenant compte de l'occupation du logement. Les
coupures sont annoncées, et la remise en service se fait circuit par circuit, avec essai
des protections.</p>

<h2 id="coordination">Rénovation électrique et travaux du logement</h2>

<p>Une rénovation électrique gagne à être coordonnée avec les autres travaux. Une isolation
intérieure, un remplacement de sol, une réfection de plafond ou une reprise de cuisine
créent autant d'occasions de faire passer des circuits sans reprise de finitions. À
l'inverse, refaire l'électricité après les finitions oblige à choisir entre des
cheminements apparents et des reprises coûteuses.</p>
""",
    "faq": [
        ("Combien coûte la rénovation électrique d'un logement ?",
         "<p>Le coût dépend de la surface, du nombre de circuits à créer, de la nature du bâti "
         "et du périmètre retenu — partiel ou complet. Une reprise de tableau et une "
         "rénovation complète avec remplacement de tous les conducteurs ne relèvent pas du "
         "même ordre de grandeur. Un chiffrage sérieux suppose une visite : il n'est pas "
         "possible d'annoncer un prix fiable sans avoir vu l'installation.</p>"),
        ("Peut-on vivre dans le logement pendant les travaux ?",
         "<p>Oui pour une rénovation partielle, avec des coupures limitées et planifiées. Une "
         "rénovation complète avec saignées est nettement plus contraignante : elle génère "
         "poussière et coupures prolongées, et se réalise plus confortablement dans un "
         "logement vide.</p>"),
        ("Faut-il tout refaire quand il n'y a pas de terre ?",
         "<p>Pas nécessairement. Si les conducteurs existants sont en bon état et que leur "
         "cheminement le permet, il est parfois possible de créer une prise de terre et de "
         "tirer un conducteur de protection vers les circuits concernés. Lorsque les "
         "conducteurs sont d'origine et sans conducteur de protection dans les gaines, le "
         "remplacement devient la seule solution.</p>"),
        ("La rénovation électrique est-elle obligatoire pour vendre ?",
         "<p>Non. Le vendeur doit fournir un diagnostic pour toute installation de plus de "
         "quinze ans, mais aucune obligation de travaux ne lui est imposée. Les anomalies "
         "relevées sont portées à la connaissance de l'acquéreur, qui en tient généralement "
         "compte dans sa décision.</p>"),
        ("Existe-t-il des aides pour la rénovation électrique ?",
         "<p>Les dispositifs d'aide à la rénovation portent principalement sur la performance "
         "énergétique, et l'électricité seule n'ouvre pas systématiquement droit à une aide. "
         "Certaines situations — rénovation globale, travaux d'adaptation du logement, "
         "opérations locales — peuvent en revanche être concernées. Les conditions évoluant "
         "régulièrement, il est conseillé de se renseigner auprès d'un conseiller France Rénov' "
         "avant d'engager les travaux.</p>"),
    ],
    "related": ["mise-aux-normes-electrique", "tableau-electrique", "diagnostic-electrique",
                "installation-electrique", "electricien-particulier"],
})

SERVICES.append({
    "slug": "mise-aux-normes-electrique",
    "path": "mise-aux-normes-electrique.html",
    "icon": "shield",
    "category": "Sécurité",
    "card_desc": ("Supprimer les défauts de sécurité d'une installation ancienne et la "
                  "rendre conforme aux exigences actuelles."),
    "title": "Mise aux normes électrique — NF C 15-100 | Electricien Richard",
    "desc": ("Mise aux normes d'une installation électrique : points de sécurité obligatoires, "
             "différence entre mise en sécurité et conformité, obligations lors d'une vente "
             "ou d'une location."),
    "h1": "Mise aux normes d'une installation électrique",
    "intro": ("Une installation ancienne n'est pas nécessairement dangereuse, mais elle ne "
              "répond plus aux exigences actuelles. La mise aux normes consiste à supprimer "
              "les défauts qui font réellement courir un risque."),
    "service_type": "Mise aux normes électrique",
    "quick": {
        "title": "Mise en sécurité ou mise en conformité ?",
        "answer": (
            "<p><strong>La mise en sécurité supprime les dangers d'une installation existante. "
            "La mise en conformité rend l'installation conforme à la norme NF C 15-100 en "
            "vigueur.</strong> Les deux notions sont souvent confondues.</p>"
            "<p>Une installation ancienne n'a pas à être conforme à la norme actuelle : celle-ci "
            "s'applique aux installations neuves et aux rénovations complètes. En revanche, "
            "elle ne doit pas présenter de risque pour les personnes.</p>"),
        "facts": [
            ("Obligatoire ?", "Aucune obligation générale de mise aux normes d'une installation existante"),
            ("Vente", "Diagnostic obligatoire si l'installation a plus de 15 ans ; travaux non imposés"),
            ("Location", "Le logement doit être décent : installation en bon état, sans risque manifeste"),
            ("Rénovation totale", "La norme en vigueur s'applique, avec attestation de conformité"),
            ("Priorités", "Mise à la terre, différentiels 30 mA, protection des circuits, pièces d'eau"),
        ],
    },
    "body": """
<h2 id="six-points">Les six points de sécurité examinés</h2>

<p>Le diagnostic électrique obligatoire s'appuie sur des points de contrôle qui constituent
également la base de toute mise en sécurité.</p>

<div class="table-wrap"><table>
<caption>Points de sécurité fondamentaux d'une installation</caption>
<thead><tr><th scope="col">Point</th><th scope="col">Ce qui est vérifié</th><th scope="col">Risque en cas de défaut</th></tr></thead>
<tbody>
<tr><td>Appareil général de commande et de protection</td><td>Présence d'un organe de coupure accessible pour l'ensemble de l'installation</td><td>Impossibilité de couper rapidement en cas d'incident</td></tr>
<tr><td>Protection différentielle</td><td>Présence et fonctionnement d'un dispositif différentiel adapté</td><td>Absence de protection contre l'électrisation par défaut d'isolement</td></tr>
<tr><td>Protection contre les surintensités</td><td>Adéquation entre le calibre des protections et la section des conducteurs</td><td>Échauffement des câbles, risque d'incendie</td></tr>
<tr><td>Mise à la terre</td><td>Existence de la prise de terre et continuité du conducteur de protection</td><td>Masse métallique pouvant rester sous tension</td></tr>
<tr><td>Pièces d'eau</td><td>Respect des volumes de sécurité et liaison équipotentielle locale</td><td>Risque majeur d'électrisation en milieu humide</td></tr>
<tr><td>Matériels et conducteurs</td><td>Absence de matériel vétuste, de conducteur non protégé mécaniquement ou d'isolant dégradé</td><td>Contacts directs, courts-circuits, incendie</td></tr>
</tbody></table></div>

<h2 id="obligations">Quelles sont les obligations réelles ?</h2>

<h3>Pour un propriétaire occupant</h3>
<p>Il n'existe aucune obligation générale de mettre aux normes une installation existante.
L'obligation naît des travaux : une rénovation complète ou une installation neuve doit
respecter la norme en vigueur.</p>

<h3>Pour une vente</h3>
<p>Un diagnostic de l'installation intérieure d'électricité doit être fourni lorsque
celle-ci a plus de quinze ans. Il informe l'acquéreur, mais n'impose pas de travaux au
vendeur.</p>

<h3>Pour une location</h3>
<p>Le logement doit répondre aux critères de décence, ce qui suppose une installation en bon
état d'usage et de fonctionnement, ne présentant pas de risques manifestes pour la sécurité
des occupants. Un diagnostic est également requis dans le dossier de location pour les
installations de plus de quinze ans.</p>

<h3>Pour un local professionnel</h3>
<p>Les exigences sont plus étendues, notamment pour les établissements recevant du public,
avec des obligations de vérification périodique par un organisme agréé. Voir la page
<a href="/electricien-entreprise.html">électricien pour entreprises et commerces</a>.</p>

<h2 id="travaux">Les travaux les plus fréquents</h2>

<h3>Créer ou reprendre la mise à la terre</h3>
<p>C'est le travail le plus structurant. Il comprend la réalisation d'une prise de terre —
piquet ou boucle à fond de fouille selon la configuration —, la pose d'une barrette de
coupure, et la distribution du conducteur de protection vers les circuits.</p>

<h3>Remplacer le tableau</h3>
<p>Le remplacement d'un tableau à fusibles par un tableau à disjoncteurs et différentiels
30 mA constitue, avec la terre, l'amélioration la plus efficace. Voir
<a href="/tableau-electrique.html">tableau électrique</a>.</p>

<h3>Reprendre les pièces d'eau</h3>
<p>Respect des volumes autour de la douche et de la baignoire, mise en place de la liaison
équipotentielle locale, remplacement des matériels inadaptés.</p>

<h3>Supprimer les montages provisoires</h3>
<p>Rallonges permanentes, dominos apparents, prises en cascade, conducteurs non protégés :
ces montages sont à l'origine d'un grand nombre d'incidents.</p>

<h2 id="limites">Ce que la mise aux normes ne fait pas</h2>

<p>Une mise en sécurité ne transforme pas une installation ancienne en installation neuve.
Elle supprime les risques identifiés, mais ne crée pas les circuits spécialisés ni le
nombre de prises qu'exigerait une installation actuelle. Lorsque ces éléments sont
souhaités, on entre dans le champ de la
<a href="/renovation-electrique.html">rénovation électrique</a>.</p>
""",
    "faq": [
        ("La mise aux normes électrique est-elle obligatoire ?",
         "<p>Non, il n'existe pas d'obligation générale de mettre aux normes une installation "
         "existante. L'obligation apparaît lors de travaux importants — installation neuve ou "
         "rénovation complète — qui doivent respecter la norme en vigueur. En location, le "
         "logement doit par ailleurs être décent, ce qui implique une installation sans risque "
         "manifeste.</p>"),
        ("Quelle est la différence entre mise en sécurité et mise en conformité ?",
         "<p>La mise en sécurité supprime les dangers d'une installation existante : absence de "
         "terre, défaut de protection différentielle, matériel vétuste. La mise en conformité "
         "va plus loin : elle rend l'installation conforme à l'ensemble des exigences de la "
         "norme actuelle, y compris le nombre de circuits et de points d'utilisation.</p>"),
        ("Mon installation date de 1970, est-elle dangereuse ?",
         "<p>Pas automatiquement. Une installation des années 1970 dispose souvent d'une mise "
         "à la terre et de conducteurs corrects. Les points à vérifier sont la présence d'une "
         "protection différentielle 30 mA, l'état du tableau, la conformité des pièces d'eau "
         "et l'absence de montages ajoutés sans protection.</p>"),
        ("Combien de temps est valable un diagnostic électrique ?",
         "<p>Trois ans dans le cadre d'une vente, six ans dans le cadre d'une location. Passé "
         "ce délai, un nouveau diagnostic doit être réalisé si l'opération se renouvelle.</p>"),
        ("Le diagnostic signale des anomalies, dois-je tout faire ?",
         "<p>Non, mais elles n'ont pas toutes le même poids. L'absence de mise à la terre ou de "
         "protection différentielle relève de la sécurité des personnes et doit être traitée "
         "en priorité. D'autres anomalies, comme un matériel inadapté à un local, peuvent être "
         "planifiées. Une lecture commentée du rapport permet de hiérarchiser.</p>"),
    ],
    "related": ["diagnostic-electrique", "renovation-electrique", "tableau-electrique",
                "electricien-particulier", "installation-electrique"],
})

SERVICES.append({
    "slug": "diagnostic-electrique",
    "path": "diagnostic-electrique.html",
    "icon": "doc",
    "category": "Sécurité",
    "card_desc": ("Évaluer l'état réel d'une installation : sécurité, conformité et capacité "
                  "à supporter les usages actuels."),
    "title": "Diagnostic électrique — État de l'installation | Electricien Richard",
    "desc": ("Diagnostic électrique : points contrôlés, différence avec le diagnostic "
             "obligatoire de vente ou de location, lecture des anomalies et hiérarchisation "
             "des travaux."),
    "h1": "Diagnostic électrique d'une installation",
    "intro": ("Un diagnostic permet de savoir où en est réellement une installation : ce qui "
              "présente un risque, ce qui n'est plus adapté aux usages, et ce qui peut être "
              "conservé."),
    "service_type": "Diagnostic électrique",
    "quick": {
        "title": "À quoi sert un diagnostic électrique ?",
        "answer": (
            "<p><strong>Un diagnostic électrique évalue l'état d'une installation : sécurité "
            "des personnes, état des matériels et adéquation aux usages.</strong> Il permet de "
            "hiérarchiser les travaux plutôt que de subir les pannes.</p>"
            "<p>Il ne doit pas être confondu avec le diagnostic immobilier obligatoire, réalisé "
            "par un diagnostiqueur certifié dans le cadre d'une vente ou d'une location, qui "
            "constate sans réparer ni chiffrer.</p>"),
        "facts": [
            ("Diagnostic obligatoire", "Réalisé par un diagnostiqueur certifié ; constat sans travaux"),
            ("Examen technique", "Réalisé par l'électricien pour préparer et hiérarchiser les travaux"),
            ("Points contrôlés", "Terre, différentiels, protections, pièces d'eau, matériels, tableau"),
            ("Quand", "Avant achat, avant travaux, avant location, après incident"),
            ("Résultat", "État des lieux commenté et ordre de priorité des interventions"),
        ],
    },
    "body": """
<h2 id="deux-diagnostics">Deux diagnostics à ne pas confondre</h2>

<div class="table-wrap"><table>
<caption>Diagnostic immobilier obligatoire et examen technique de l'installation</caption>
<thead><tr><th scope="col"></th><th scope="col">Diagnostic obligatoire</th><th scope="col">Examen technique par l'électricien</th></tr></thead>
<tbody>
<tr><td>Cadre</td><td>Vente ou location d'un logement de plus de 15 ans d'installation</td><td>Libre, à la demande du propriétaire</td></tr>
<tr><td>Réalisé par</td><td>Diagnostiqueur certifié</td><td>Électricien</td></tr>
<tr><td>Objet</td><td>Constater les anomalies au regard de points de contrôle définis</td><td>Comprendre l'état réel et préparer les travaux</td></tr>
<tr><td>Contenu</td><td>Rapport normalisé listant les anomalies</td><td>Constat commenté, priorités, solutions envisageables</td></tr>
<tr><td>Travaux</td><td>Non chiffrés, non réalisés</td><td>Chiffrage possible sous forme de devis</td></tr>
<tr><td>Validité</td><td>3 ans (vente), 6 ans (location)</td><td>Sans durée réglementaire</td></tr>
</tbody></table></div>

<h2 id="points">Ce qui est examiné</h2>

<h3>La mise à la terre</h3>
<p>Présence d'une prise de terre, d'une barrette de coupure, et surtout continuité effective
du conducteur de protection jusqu'aux points d'utilisation. Une prise avec broche de terre
n'est pas la preuve d'une terre raccordée : seule la mesure le confirme.</p>

<h3>Les dispositifs différentiels</h3>
<p>Présence, sensibilité, type et bon fonctionnement. Un différentiel qui ne déclenche pas
au test ne protège plus.</p>

<h3>La protection des circuits</h3>
<p>Cohérence entre le calibre des protections et la section des conducteurs. Un disjoncteur
surcalibré est un défaut fréquent et rarement visible sans examen.</p>

<h3>Le tableau</h3>
<p>État général, repérage des circuits, serrage des connexions, traces d'échauffement, place
disponible, présence de matériels obsolètes.</p>

<h3>Les pièces d'eau et les locaux particuliers</h3>
<p>Respect des volumes de sécurité, liaison équipotentielle locale, indices de protection
des matériels installés en extérieur, en cave ou en local humide.</p>

<h3>Les matériels et les montages</h3>
<p>Appareillages cassés ou vétustes, conducteurs non protégés mécaniquement, rallonges
permanentes, dominos apparents, prises en cascade.</p>

<h2 id="quand">Quand faire réaliser un diagnostic ?</h2>

<ul>
<li><strong>Avant un achat immobilier</strong>, pour évaluer le budget électrique réel du
projet, au-delà du rapport obligatoire.</li>
<li><strong>Avant des travaux</strong>, afin de définir le périmètre de la rénovation et
d'éviter de découvrir un problème une fois les finitions posées.</li>
<li><strong>Avant une mise en location</strong>, pour s'assurer que le logement ne présente
pas de risque manifeste.</li>
<li><strong>Après un incident</strong> — déclenchement répété, échauffement, dégât des eaux,
foudre — pour vérifier l'intégrité de l'installation.</li>
<li><strong>Avant d'ajouter un équipement</strong> important : borne de recharge, pompe à
chaleur, climatisation, équipement professionnel.</li>
</ul>

<h2 id="resultat">Ce que vous obtenez</h2>

<p>Le diagnostic aboutit à un constat commenté : ce qui présente un risque immédiat, ce qui
doit être repris à moyen terme, ce qui est simplement daté mais sans danger. Cette
hiérarchisation est la partie utile du travail : elle permet de décider en connaissance de
cause, et d'échelonner les travaux si nécessaire.</p>
""",
    "faq": [
        ("Le diagnostic électrique est-il payant ?",
         "<p>Un diagnostic immobilier obligatoire est une prestation facturée par un "
         "diagnostiqueur certifié. Un examen technique réalisé par un électricien peut être "
         "intégré à l'établissement d'un devis ou facturé selon son étendue. Les conditions "
         "sont indiquées avant l'intervention.</p>"),
        ("Combien de points comporte le diagnostic obligatoire ?",
         "<p>Le diagnostic de l'installation intérieure d'électricité s'appuie sur des points "
         "de contrôle portant notamment sur l'appareil général de commande et de protection, la "
         "protection différentielle, la protection contre les surintensités, la mise à la "
         "terre, les matériels présentant des risques, et les installations particulières des "
         "pièces d'eau.</p>"),
        ("Une installation ancienne peut-elle être jugée conforme ?",
         "<p>Le diagnostic ne juge pas de la conformité à la norme actuelle, mais de l'absence "
         "d'anomalies au regard des points de contrôle relatifs à la sécurité. Une installation "
         "ancienne bien entretenue peut donc ne présenter aucune anomalie, sans pour autant "
         "répondre aux exigences applicables aux installations neuves.</p>"),
        ("Que faire si le diagnostic révèle beaucoup d'anomalies ?",
         "<p>Les hiérarchiser. L'absence de terre, l'absence de différentiel 30 mA et les "
         "défauts des pièces d'eau touchent directement à la sécurité des personnes et passent "
         "en premier. Les autres points peuvent être traités par étapes, dans un ordre "
         "cohérent qui évite de refaire deux fois les mêmes travaux.</p>"),
        ("Un diagnostic peut-il être réalisé sans couper le courant ?",
         "<p>Une partie de l'examen se fait sous tension — vérifications visuelles, essais des "
         "différentiels, mesures de tension. Les mesures d'isolement et le contrôle des "
         "serrages exigent en revanche une coupure, de courte durée et annoncée à l'avance.</p>"),
    ],
    "related": ["mise-aux-normes-electrique", "renovation-electrique", "tableau-electrique",
                "recherche-panne", "electricien-particulier"],
})

SERVICES.append({
    "slug": "tableau-electrique",
    "path": "tableau-electrique.html",
    "icon": "building",
    "category": "Équipements",
    "card_desc": ("Le cœur de l'installation : rôle, composition, signes d'usure et "
                  "remplacement."),
    "title": "Tableau électrique — Remplacement et mise à niveau | Electricien Richard",
    "desc": ("Tableau électrique : rôle, composition, signes indiquant un remplacement "
             "nécessaire, déroulement des travaux et conformité NF C 15-100."),
    "h1": "Tableau électrique : rôle, remplacement et mise à niveau",
    "intro": ("Le tableau électrique est le point de distribution et de protection de toute "
              "l'installation. Son état conditionne directement la sécurité du logement."),
    "service_type": "Installation et remplacement de tableau électrique",
    "quick": {
        "title": "À quoi sert un tableau électrique ?",
        "answer": (
            "<p><strong>Le tableau électrique répartit l'électricité entre les différents "
            "circuits du logement et protège chacun d'eux.</strong> Il regroupe les dispositifs "
            "différentiels, qui protègent les personnes, et les disjoncteurs divisionnaires, "
            "qui protègent les conducteurs.</p>"
            "<p>C'est également le point de coupure utilisé pour intervenir en sécurité sur "
            "n'importe quelle partie de l'installation, ce qui suppose un repérage clair de "
            "chaque circuit.</p>"),
        "facts": [
            ("Fonctions", "Répartition, protection des circuits, protection des personnes, coupure"),
            ("Composants", "Différentiels 30 mA, disjoncteurs divisionnaires, parfois parafoudre et contacteur"),
            ("Emplacement", "Espace technique dédié, accessible, hors volumes des pièces d'eau"),
            ("À remplacer si", "Fusibles à broche, absence de différentiel, traces d'échauffement, saturation"),
            ("Évolutivité", "Modules libres à prévoir pour les usages futurs"),
        ],
    },
    "body": """
<h2 id="composition">De quoi se compose un tableau</h2>

<div class="table-wrap"><table>
<caption>Composants d'un tableau électrique et leur rôle</caption>
<thead><tr><th scope="col">Composant</th><th scope="col">Rôle</th><th scope="col">Ce qu'il protège</th></tr></thead>
<tbody>
<tr><td>Interrupteur différentiel 30 mA</td><td>Détecte les fuites de courant vers la terre</td><td>Les personnes</td></tr>
<tr><td>Disjoncteur divisionnaire</td><td>Coupe en cas de surcharge ou de court-circuit</td><td>Les conducteurs du circuit</td></tr>
<tr><td>Disjoncteur différentiel</td><td>Cumule les deux fonctions sur un circuit unique</td><td>Personnes et conducteurs</td></tr>
<tr><td>Parafoudre</td><td>Écoule les surtensions d'origine atmosphérique</td><td>Les équipements sensibles</td></tr>
<tr><td>Contacteur jour/nuit</td><td>Commande un circuit selon le tarif ou un ordre extérieur</td><td>Généralement le chauffe-eau</td></tr>
<tr><td>Borniers de terre et de neutre</td><td>Assurent le raccordement commun des conducteurs</td><td>La continuité de l'installation</td></tr>
</tbody></table></div>

<h3>Le type de différentiel a son importance</h3>
<p>Tous les différentiels ne se valent pas. Le type AC couvre les défauts classiques ; le
type A est exigé pour certains circuits dont les appareils peuvent générer des composantes
continues, notamment la plaque de cuisson et le lave-linge. Un tableau correctement conçu
comporte donc plusieurs différentiels de types différents, répartis de façon à limiter
l'étendue d'une coupure.</p>

<h2 id="quand-remplacer">Quand faut-il remplacer un tableau ?</h2>

<h3>Les situations qui l'imposent</h3>
<ul>
<li>Présence de fusibles à broche : ni protection différentielle adaptée, ni repérage, ni
possibilité d'évolution.</li>
<li>Absence de dispositif différentiel 30 mA sur tout ou partie des circuits.</li>
<li>Traces d'échauffement : noircissement, plastique déformé, odeur, borne oxydée.</li>
<li>Boîtier détérioré, capot manquant, pièces sous tension accessibles.</li>
<li>Différentiel qui ne déclenche pas lors du test.</li>
</ul>

<h3>Les situations qui le justifient</h3>
<ul>
<li>Aucun module libre pour ajouter un circuit — cas fréquent lors d'un projet de
<a href="/borne-recharge.html">borne de recharge</a> ou d'extension.</li>
<li>Circuits non repérés, rendant toute intervention hasardeuse.</li>
<li>Trop de circuits regroupés derrière un même différentiel : la moindre fuite coupe une
grande partie du logement.</li>
<li>Installation ayant fait l'objet d'ajouts successifs sans reprise d'ensemble.</li>
</ul>

<h2 id="remplacement">Comment se déroule un remplacement</h2>

<ol class="steps">
<li><h3>Relevé de l'existant</h3><p>Identification des circuits, de leur section, de leur usage et de la puissance souscrite.</p></li>
<li><h3>Définition du nouveau tableau</h3><p>Nombre de rangées, répartition des différentiels par type, modules libres à prévoir.</p></li>
<li><h3>Coupure et dépose</h3><p>Mise hors tension, vérification de l'absence de tension, dépose de l'ancien matériel.</p></li>
<li><h3>Pose et raccordement</h3><p>Installation du coffret, câblage, reprise du bornier de terre et raccordement des circuits.</p></li>
<li><h3>Repérage</h3><p>Étiquetage clair de chaque protection : c'est ce qui permettra plus tard d'intervenir sans risque.</p></li>
<li><h3>Essais</h3><p>Test des différentiels, vérification des circuits, contrôle du serrage des connexions.</p></li>
</ol>

<h2 id="emplacement">Où doit se trouver le tableau ?</h2>

<p>Le tableau doit être accessible sans outil et sans avoir à déplacer de meuble, situé hors
des volumes de sécurité des pièces d'eau, à l'abri de l'humidité et à une hauteur permettant
la manœuvre. La norme prévoit un espace technique dédié dans les logements neufs,
regroupant l'arrivée, le tableau et les arrivées de communication.</p>

<p>Un tableau placé dans un placard encombré, dans une salle de bains ou derrière un
appareil est un défaut fréquent dans les installations anciennes : en cas d'incident, on
doit pouvoir couper immédiatement.</p>
""",
    "faq": [
        ("Combien de temps dure le remplacement d'un tableau électrique ?",
         "<p>Cela dépend du nombre de circuits, de l'état du câblage existant et de la "
         "nécessité de reprendre la mise à la terre. L'intervention implique une coupure de "
         "courant pendant les travaux, dont la durée estimée est annoncée avant le début du "
         "chantier.</p>"),
        ("Peut-on remplacer un tableau sans refaire l'installation ?",
         "<p>Oui, et c'est même l'un des travaux les plus utiles sur une installation ancienne. "
         "Il faut toutefois que les circuits existants soient en état d'être raccordés : "
         "isolement correct, sections cohérentes, conducteur de protection présent. Sinon, "
         "le nouveau tableau protégerait des circuits qui restent défaillants.</p>"),
        ("Combien de différentiels faut-il dans un tableau ?",
         "<p>Au minimum deux dans un logement, leur nombre augmentant avec la surface et le "
         "nombre de circuits. Certains circuits exigent un différentiel de type A. Au-delà de "
         "l'exigence normative, répartir les circuits sur plusieurs différentiels limite "
         "l'étendue d'une coupure en cas de défaut.</p>"),
        ("Mon tableau est plein, que faire ?",
         "<p>Deux solutions : ajouter une rangée si le coffret le permet et si son alimentation "
         "l'autorise, ou remplacer le tableau par un modèle plus capacitaire. Le choix dépend "
         "de l'état de l'existant, de la répartition des différentiels et du nombre de circuits "
         "à créer.</p>"),
        ("Faut-il un parafoudre ?",
         "<p>Il est obligatoire dans certaines configurations, en fonction notamment du niveau "
         "de risque foudre de la zone et du type d'alimentation. Au-delà de l'obligation, il "
         "constitue une protection utile pour les équipements électroniques dans les secteurs "
         "exposés. Son voyant doit être surveillé : une cartouche en fin de vie ne protège "
         "plus.</p>"),
    ],
    "related": ["disjoncteur", "installation-electrique", "mise-aux-normes-electrique",
                "renovation-electrique", "diagnostic-electrique"],
})

SERVICES.append({
    "slug": "disjoncteur",
    "path": "disjoncteur.html",
    "icon": "shield",
    "category": "Équipements",
    "card_desc": ("Comprendre un disjoncteur qui saute : surcharge, court-circuit, fuite de "
                  "courant, et que faire."),
    "title": "Disjoncteur qui saute — Causes et solutions | Electricien Richard",
    "desc": ("Disjoncteur qui saute : différence entre surcharge, court-circuit et "
             "déclenchement différentiel, méthode d'identification et solutions durables."),
    "h1": "Disjoncteur : pourquoi il saute et que faire",
    "intro": ("Un disjoncteur qui déclenche fait son travail : il signale un problème. La "
              "question n'est jamais « comment l'empêcher de sauter », mais « pourquoi "
              "saute-t-il »."),
    "service_type": "Dépannage de disjoncteur",
    "quick": {
        "title": "Pourquoi un disjoncteur saute-t-il ?",
        "answer": (
            "<p><strong>Trois causes principales :</strong> une surcharge (trop d'appareils sur "
            "le circuit), un court-circuit (contact direct entre conducteurs), ou une fuite de "
            "courant vers la terre détectée par un dispositif différentiel.</p>"
            "<p>Identifier lequel des trois est en cause est la première étape : le dispositif "
            "qui a déclenché indique déjà la nature du problème.</p>"),
        "facts": [
            ("Surcharge", "Le disjoncteur déclenche après quelques minutes d'usage simultané"),
            ("Court-circuit", "Déclenchement instantané, souvent accompagné d'un bruit sec"),
            ("Fuite de courant", "C'est le différentiel qui coupe, parfois plusieurs circuits d'un coup"),
            ("Méthode", "Débrancher, réarmer, rebrancher un appareil à la fois"),
            ("À ne pas faire", "Augmenter le calibre ou réarmer en boucle"),
        ],
    },
    "body": """
<h2 id="types">Disjoncteur, différentiel : qui fait quoi</h2>

<p>Le mot « disjoncteur » recouvre plusieurs dispositifs qui n'ont pas la même fonction.</p>

<h3>Le disjoncteur de branchement</h3>
<p>Placé en amont, près du compteur, il protège l'installation dans son ensemble et limite
la puissance appelée. Lorsqu'il déclenche, c'est généralement que la puissance souscrite est
dépassée, ou qu'un défaut majeur affecte l'installation.</p>

<h3>Le disjoncteur divisionnaire</h3>
<p>Placé au tableau, il protège un circuit contre les surcharges et les courts-circuits. Son
calibre — 10 A, 16 A, 20 A, 32 A — doit correspondre à la section du conducteur qu'il
protège.</p>

<h3>L'interrupteur différentiel</h3>
<p>Il ne protège pas contre les surcharges : il détecte les fuites de courant vers la terre
et protège les personnes. Il couvre plusieurs circuits à la fois, ce qui explique qu'un
défaut sur un seul circuit puisse couper une partie importante du logement.</p>

<h3>Le disjoncteur différentiel</h3>
<p>Il combine les deux fonctions sur un circuit unique, ce qui permet d'isoler précisément
le circuit concerné en cas de défaut.</p>

<h2 id="diagnostic">Identifier la cause : la méthode</h2>

<div class="table-wrap"><table>
<caption>Interpréter un déclenchement</caption>
<thead><tr><th scope="col">Constat</th><th scope="col">Cause probable</th><th scope="col">Que faire</th></tr></thead>
<tbody>
<tr><td>Déclenchement après quelques minutes d'usage intense</td><td>Surcharge du circuit</td><td>Répartir les appareils ; envisager un circuit dédié</td></tr>
<tr><td>Déclenchement instantané au réarmement</td><td>Court-circuit ou défaut franc</td><td>Ne pas insister ; faire rechercher le défaut</td></tr>
<tr><td>Déclenchement à la mise en route d'un appareil précis</td><td>Appareil défectueux ou circuit inadapté</td><td>Tester l'appareil sur un autre circuit</td></tr>
<tr><td>Le différentiel coupe, pas le disjoncteur</td><td>Fuite de courant vers la terre</td><td>Isoler les circuits un à un pour identifier l'origine</td></tr>
<tr><td>Déclenchement par temps humide</td><td>Défaut d'isolement sur un circuit extérieur</td><td>Faire mesurer l'isolement des circuits concernés</td></tr>
<tr><td>Déclenchement toujours à la même heure</td><td>Appareil programmé, souvent le chauffe-eau</td><td>Faire contrôler la résistance et son isolement</td></tr>
</tbody></table></div>

<h3>La procédure d'isolement</h3>
<ol>
<li>Ouvrir tous les disjoncteurs divisionnaires.</li>
<li>Réarmer le différentiel ou le disjoncteur de branchement.</li>
<li>Refermer les circuits un par un, en observant lequel provoque le déclenchement.</li>
<li>Sur le circuit fautif, débrancher tous les appareils, puis les rebrancher un à un.</li>
</ol>
<p>Si le déclenchement persiste avec tous les appareils débranchés, le défaut se situe dans
l'installation : il relève d'une <a href="/recherche-panne.html">recherche de panne</a>.</p>

<h2 id="erreurs">Les erreurs à ne pas commettre</h2>

<ul>
<li><strong>Augmenter le calibre du disjoncteur.</strong> Le conducteur n'est alors plus
protégé : il peut chauffer sans que la protection ne réagisse. C'est l'une des causes
d'incendie d'origine électrique les plus évitables.</li>
<li><strong>Réarmer en boucle.</strong> Chaque réarmement sur défaut sollicite l'installation
et aggrave l'échauffement au point de défaut.</li>
<li><strong>Supprimer ou ponter un différentiel.</strong> C'est supprimer la protection des
personnes.</li>
<li><strong>Ignorer un déclenchement isolé.</strong> Un différentiel qui coupe une fois par
mois signale un défaut naissant, pas un caprice.</li>
</ul>

<h2 id="solutions">Les solutions durables</h2>

<p>Selon la cause identifiée, la solution consiste à créer un circuit dédié pour un appareil
qui surcharge un circuit partagé, à remplacer un matériel dégradé, à reprendre une connexion
défectueuse, ou à remplacer un dispositif de protection en fin de vie. Lorsque les
déclenchements sont multiples et dispersés, c'est généralement l'installation dans son
ensemble qui arrive en limite : un
<a href="/diagnostic-electrique.html">diagnostic</a> permet alors de trancher.</p>
""",
    "faq": [
        ("Mon disjoncteur saute quand j'allume le four et le lave-linge en même temps",
         "<p>C'est une surcharge caractéristique : deux appareils puissants sur un circuit qui "
         "n'est pas prévu pour les alimenter simultanément. La solution n'est pas d'augmenter "
         "le calibre, mais de créer un circuit spécialisé pour chacun de ces appareils, comme "
         "l'exige la norme pour les installations actuelles.</p>"),
        ("Pourquoi mon différentiel saute-t-il sans raison apparente ?",
         "<p>Il y a toujours une raison : un courant de fuite a atteint son seuil de "
         "déclenchement. Les origines les plus fréquentes sont un appareil dont l'isolement se "
         "dégrade — chauffe-eau, lave-linge, plaque — ou un circuit exposé à l'humidité. Un "
         "différentiel vieillissant peut aussi devenir trop sensible.</p>"),
        ("Un disjoncteur peut-il être défectueux ?",
         "<p>Oui. Un disjoncteur peut se déclencher intempestivement ou, plus grave, ne plus "
         "déclencher du tout. Pour les différentiels, le bouton test permet de vérifier le "
         "fonctionnement : s'il ne déclenche pas au test, le dispositif doit être remplacé "
         "sans délai.</p>"),
        ("Que signifie le calibre d'un disjoncteur ?",
         "<p>C'est l'intensité au-delà de laquelle il coupe le circuit. Ce calibre doit "
         "correspondre à la section du conducteur : un circuit en 1,5 mm² est protégé par un "
         "disjoncteur de calibre plus faible qu'un circuit en 2,5 mm². Le calibre découle donc "
         "du câble, jamais de l'appareil que l'on souhaite y brancher.</p>"),
        ("Combien de temps dure un disjoncteur ?",
         "<p>Il n'existe pas de durée de vie réglementaire, mais ces matériels vieillissent. "
         "Les dispositifs différentiels sont les plus concernés : un test mensuel avec le "
         "bouton prévu à cet effet permet de vérifier qu'ils fonctionnent encore. Un "
         "différentiel resté longtemps sans manœuvre peut se bloquer.</p>"),
    ],
    "related": ["court-circuit", "panne-electrique", "tableau-electrique", "recherche-panne",
                "electricien-depannage"],
})

SERVICES.append({
    "slug": "court-circuit",
    "path": "court-circuit.html",
    "icon": "bolt",
    "category": "Dépannage",
    "card_desc": ("Ce qu'est réellement un court-circuit, ses causes, ses conséquences et la "
                  "conduite à tenir."),
    "title": "Court-circuit — Causes, risques et solutions | Electricien Richard",
    "desc": ("Court-circuit électrique : définition, causes fréquentes, différence avec une "
             "surcharge, risques et conduite à tenir avant l'intervention d'un électricien."),
    "h1": "Court-circuit : causes, risques et conduite à tenir",
    "intro": ("Le court-circuit est l'un des défauts électriques les plus brutaux. Il est "
              "aussi l'un des plus mal nommés dans le langage courant, où il désigne souvent "
              "n'importe quelle panne."),
    "service_type": "Dépannage de court-circuit",
    "quick": {
        "title": "Qu'est-ce qu'un court-circuit ?",
        "answer": (
            "<p><strong>Un court-circuit est un contact direct entre deux conducteurs de "
            "potentiels différents — généralement la phase et le neutre — sans passer par un "
            "récepteur.</strong> Le courant, qui n'est plus limité par la charge, atteint une "
            "intensité très élevée en une fraction de seconde.</p>"
            "<p>La protection réagit alors instantanément. C'est précisément son rôle : sans "
            "elle, le conducteur fondrait et provoquerait un incendie.</p>"),
        "facts": [
            ("Manifestation", "Déclenchement instantané, parfois bruit sec, éclair ou odeur"),
            ("Différence avec la surcharge", "La surcharge est progressive, le court-circuit est immédiat"),
            ("Causes fréquentes", "Câble blessé, appareil défectueux, connexion touchant une masse, humidité"),
            ("Risque principal", "Échauffement extrême et départ de feu si la protection ne coupe pas"),
            ("Conduite à tenir", "Ne pas réarmer plusieurs fois ; faire localiser le défaut"),
        ],
    },
    "body": """
<h2 id="mecanisme">Ce qui se passe lors d'un court-circuit</h2>

<p>Dans une installation qui fonctionne normalement, le courant traverse un récepteur —
lampe, moteur, résistance — qui limite son intensité. Lors d'un court-circuit, ce récepteur
est court-circuité : le courant emprunte un chemin direct entre phase et neutre.</p>

<p>L'intensité devient alors très supérieure à celle du fonctionnement normal, ce qui
produit une élévation de température quasi instantanée dans le conducteur et au point de
défaut. C'est pourquoi la protection doit couper en quelques millisecondes.</p>

<h2 id="causes">Les causes les plus fréquentes</h2>

<div class="table-wrap"><table>
<caption>Origines habituelles d'un court-circuit</caption>
<thead><tr><th scope="col">Origine</th><th scope="col">Contexte typique</th></tr></thead>
<tbody>
<tr><td>Conducteur blessé</td><td>Percement d'un mur, vis traversant une gaine, câble pincé lors de travaux</td></tr>
<tr><td>Appareil défectueux</td><td>Enroulement de moteur en défaut, résistance percée, cordon détérioré</td></tr>
<tr><td>Connexion mal réalisée</td><td>Brin de conducteur dépassant d'une borne et touchant un autre conducteur</td></tr>
<tr><td>Appareillage écrasé</td><td>Prise ou interrupteur trop enfoncé dans sa boîte, conducteurs comprimés</td></tr>
<tr><td>Humidité et infiltration</td><td>Boîtier extérieur non étanche, dégât des eaux, cave inondée</td></tr>
<tr><td>Rongeurs</td><td>Câbles rongés en combles, en vide sanitaire ou en dépendance</td></tr>
<tr><td>Vieillissement de l'isolant</td><td>Conducteurs anciens dont l'isolant devient cassant</td></tr>
</tbody></table></div>

<h2 id="difference">Court-circuit ou surcharge ?</h2>

<p>Les deux provoquent le déclenchement d'un disjoncteur, mais leur signature diffère.</p>

<ul>
<li><strong>La surcharge</strong> est progressive : le circuit supporte une intensité
supérieure à celle prévue, et la protection coupe après un délai qui dépend du dépassement.
Elle survient typiquement lorsque plusieurs appareils puissants fonctionnent ensemble.</li>
<li><strong>Le court-circuit</strong> est instantané. Le déclenchement se produit
immédiatement, souvent au moment précis d'un branchement, d'un actionnement ou d'un
mouvement de câble.</li>
</ul>

<p>Cette distinction est utile : une surcharge se règle en répartissant les usages ou en
créant un circuit dédié, tandis qu'un court-circuit impose de trouver le point de défaut.</p>

<h2 id="conduite">Que faire face à un court-circuit</h2>

<ol>
<li>Ne pas réarmer plusieurs fois de suite. Chaque tentative sur défaut franc provoque un
nouvel arc au point de contact.</li>
<li>Débrancher tous les appareils du circuit concerné.</li>
<li>Tenter un seul réarmement. S'il tient, rebrancher les appareils un à un pour identifier
celui qui est en cause.</li>
<li>S'il déclenche à nouveau immédiatement sans aucun appareil branché, le défaut est dans
l'installation : couper le circuit et faire intervenir un professionnel.</li>
<li>En présence d'une odeur de brûlé, de fumée ou d'un noircissement, couper le disjoncteur
général et ne rien remettre en service.</li>
</ol>

<h2 id="risques">Les risques réels</h2>

<p>Lorsque la protection fonctionne correctement, un court-circuit se solde par une coupure
sans dommage. Les situations dangereuses apparaissent quand cette protection est absente,
inadaptée ou surcalibrée : le conducteur subit alors l'échauffement sans coupure, ce qui
peut enflammer les matériaux environnants.</p>

<p>C'est la raison pour laquelle le calibre d'un disjoncteur doit toujours correspondre à la
section du câble qu'il protège, et pourquoi remplacer une protection par un calibre
supérieur constitue une manipulation dangereuse.</p>
""",
    "faq": [
        ("Un court-circuit peut-il provoquer un incendie ?",
         "<p>Oui, lorsque la protection ne coupe pas ou coupe trop tard : protection absente, "
         "surcalibrée, ou remplacée par un dispositif inadapté. Avec une protection correcte, "
         "la coupure intervient en quelques millisecondes et le risque est maîtrisé.</p>"),
        ("Comment savoir si c'est un court-circuit ou une surcharge ?",
         "<p>Par le délai. Un court-circuit fait déclencher instantanément, souvent au moment "
         "d'un geste précis. Une surcharge provoque un déclenchement après quelques minutes "
         "d'usage simultané de plusieurs appareils. Si le circuit tient sans aucun appareil "
         "branché mais coupe dès qu'on en branche plusieurs, il s'agit d'une surcharge.</p>"),
        ("Un court-circuit peut-il endommager mes appareils ?",
         "<p>L'appareil à l'origine du défaut est généralement hors d'usage. Les autres "
         "appareils du circuit ne subissent normalement pas de dommage, la coupure étant "
         "quasi immédiate. Une surtension, en revanche, peut affecter plusieurs équipements "
         "électroniques.</p>"),
        ("Peut-on réparer soi-même un court-circuit ?",
         "<p>Identifier un appareil défectueux et le débrancher est à la portée de chacun. "
         "En revanche, un court-circuit situé dans l'installation — dans une gaine, une boîte "
         "encastrée ou un câble enterré — exige des mesures et un savoir-faire spécifiques. "
         "Toute intervention doit se faire hors tension, après vérification de l'absence de "
         "tension.</p>"),
        ("Pourquoi mon court-circuit n'a-t-il fait sauter que le différentiel ?",
         "<p>Cela arrive lorsque le contact se fait entre la phase et la terre plutôt qu'entre "
         "phase et neutre. Le courant part alors vers la terre et le dispositif différentiel "
         "réagit avant le disjoncteur. Le défaut n'en est pas moins réel et doit être "
         "localisé.</p>"),
    ],
    "related": ["disjoncteur", "panne-electrique", "recherche-panne", "electricien-urgence",
                "electricien-depannage"],
})

SERVICES.append({
    "slug": "prise-electrique",
    "path": "prise-electrique.html",
    "icon": "plug",
    "category": "Équipements",
    "card_desc": ("Ajout, remplacement et sécurité des prises de courant : règles et points "
                  "de vigilance."),
    "title": "Prise électrique — Ajout, remplacement, sécurité | Electricien Richard",
    "desc": ("Prise électrique : ajout de prises, remplacement d'une prise défectueuse, "
             "nombre de socles par circuit, prises extérieures et règles de sécurité."),
    "h1": "Prise électrique : ajout, remplacement et sécurité",
    "intro": ("Manquer de prises est le symptôme le plus visible d'une installation qui n'a "
              "pas suivi l'évolution des usages. La réponse n'est pas la multiprise, mais "
              "l'ajout de points d'utilisation correctement alimentés."),
    "service_type": "Installation de prises électriques",
    "quick": {
        "title": "Ajouter une prise : ce qu'il faut savoir",
        "answer": (
            "<p><strong>Une prise s'ajoute soit sur un circuit existant, dans la limite du "
            "nombre de socles admis, soit sur un nouveau circuit créé depuis le tableau.</strong> "
            "Ce nombre dépend de la section du conducteur et du calibre de la protection.</p>"
            "<p>Toute prise doit être reliée au conducteur de protection et protégée par un "
            "dispositif différentiel 30 mA.</p>"),
        "facts": [
            ("Circuit 1,5 mm²", "Protection 16 A, nombre de socles limité"),
            ("Circuit 2,5 mm²", "Protection 20 A, nombre de socles plus élevé"),
            ("Obligatoire", "Conducteur de protection et différentiel 30 mA"),
            ("Extérieur", "Matériel adapté, indice de protection suffisant, câble prévu pour l'extérieur"),
            ("À éviter", "Multiprises en cascade et rallonges permanentes"),
        ],
    },
    "body": """
<h2 id="regles">Les règles qui encadrent les prises</h2>

<h3>Nombre de socles par circuit</h3>
<p>Un circuit de prises ne peut alimenter qu'un nombre limité de socles, déterminé par la
section du conducteur et le calibre de la protection. Dépasser cette limite revient à
augmenter la charge possible du circuit au-delà de ce que le câble supporte. C'est un défaut
courant dans les installations complétées au fil du temps.</p>

<h3>Nombre minimal par pièce</h3>
<p>La norme fixe un nombre minimal de socles par pièce, variable selon sa nature et sa
surface, avec des exigences renforcées dans le séjour et la cuisine. Ces minimums
correspondent aux usages réels : lorsqu'ils ne sont pas atteints, les occupants recourent
inévitablement aux multiprises.</p>

<h3>Hauteur et implantation</h3>
<p>Les prises doivent être installées à une hauteur permettant un usage normal et éviter
certaines zones : au-dessus d'un évier ou d'une plaque de cuisson, ou à l'intérieur des
volumes de sécurité d'une salle d'eau.</p>

<h2 id="cuisine">Le cas particulier de la cuisine</h2>

<p>C'est la pièce la plus exigeante. La norme y impose un nombre minimal de socles répartis
au-dessus du plan de travail, ainsi que des circuits spécialisés pour la plaque de cuisson
et pour chaque gros appareil : four, lave-vaisselle, lave-linge lorsqu'il s'y trouve.</p>

<p>Dans les logements anciens, la cuisine est presque toujours le point faible : quelques
prises sur un unique circuit partagé avec l'éclairage, alimentant aujourd'hui plusieurs
appareils puissants. C'est aussi là que se produisent le plus souvent les échauffements.</p>

<h2 id="exterieur">Prises extérieures</h2>

<p>Une prise installée dehors subit la pluie, l'humidité, le gel et, sur le littoral, les
embruns. Elle exige :</p>

<ul>
<li>un matériel prévu pour l'extérieur, avec couvercle et joint, présentant un indice de
protection adapté à son exposition ;</li>
<li>une alimentation par un câble prévu pour la pose extérieure ou enterrée sous
fourreau ;</li>
<li>une fixation évitant les infiltrations par l'arrière du boîtier ;</li>
<li>une protection différentielle 30 mA, comme tout circuit.</li>
</ul>

<p>Détourner un matériel d'intérieur vers un usage extérieur est l'une des causes les plus
fréquentes de déclenchements récurrents par temps humide.</p>

<h2 id="signes">Quand une prise doit être remplacée</h2>

<ul>
<li>Traces de noircissement, plastique déformé ou fondu.</li>
<li>Chaleur perceptible au toucher.</li>
<li>Fiche qui tient mal, contacts desserrés, jeu mécanique.</li>
<li>Crépitement ou étincelle lors du branchement.</li>
<li>Prise cassée laissant apparaître des parties sous tension.</li>
<li>Prise sans conducteur de protection alors que l'usage l'exige.</li>
</ul>

<p>Une prise qui a chauffé ne doit pas être simplement remplacée : il faut comprendre
pourquoi elle a chauffé. Dans la plupart des cas, la cause est une connexion desserrée ou
une surcharge du circuit, et le remplacement seul ne règle rien.</p>

<h2 id="multiprises">Le problème des multiprises</h2>

<p>Une multiprise ne crée pas de puissance supplémentaire : elle répartit celle du circuit.
Brancher plusieurs appareils puissants sur une même multiprise fait circuler l'ensemble du
courant dans un unique cordon et une unique prise murale, qui n'ont pas été prévus pour
cela. Les multiprises en cascade aggravent encore le phénomène.</p>

<p>Lorsque leur usage devient permanent, c'est le nombre de points d'utilisation qu'il faut
revoir, pas le nombre de multiprises.</p>
""",
    "faq": [
        ("Combien de prises peut-on mettre sur un circuit ?",
         "<p>Le nombre dépend de la section du conducteur et du calibre de la protection : un "
         "circuit en 2,5 mm² protégé en 20 A admet davantage de socles qu'un circuit en "
         "1,5 mm² protégé en 16 A. Au-delà de cette limite, il faut créer un nouveau circuit "
         "depuis le tableau.</p>"),
        ("Peut-on ajouter une prise sans refaire le circuit ?",
         "<p>Oui, si le circuit existant n'a pas atteint sa limite de socles, si sa section "
         "est correcte et s'il dispose d'un conducteur de protection. Le raccordement se fait "
         "alors depuis une boîte de dérivation ou une prise existante, jamais par un montage "
         "provisoire.</p>"),
        ("Une prise sans terre est-elle dangereuse ?",
         "<p>Elle l'est pour tout appareil dont la classe d'isolation impose une mise à la "
         "terre : en cas de défaut, la carcasse peut rester sous tension. Certains appareils, "
         "à double isolation, n'en ont pas besoin. Dans un logement, l'absence généralisée de "
         "terre constitue un défaut de sécurité majeur.</p>"),
        ("Pourquoi ma prise chauffe-t-elle ?",
         "<p>Presque toujours à cause d'une résistance de contact anormale : borne desserrée, "
         "contacts usés, ou courant supérieur à ce que la prise peut supporter. Le phénomène "
         "s'auto-entretient, la chaleur dégradant encore le contact. C'est une situation à "
         "traiter sans attendre.</p>"),
        ("Peut-on installer une prise dans une salle de bains ?",
         "<p>Oui, mais hors des volumes de sécurité définis autour de la baignoire et de la "
         "douche, et sous protection différentielle 30 mA. La liaison équipotentielle locale "
         "de la pièce doit par ailleurs être réalisée. Ces règles sont parmi les plus "
         "fréquemment enfreintes dans les installations anciennes.</p>"),
    ],
    "related": ["interrupteur", "installation-electrique", "renovation-electrique",
                "tableau-electrique", "mise-aux-normes-electrique"],
})

SERVICES.append({
    "slug": "interrupteur",
    "path": "interrupteur.html",
    "icon": "plug",
    "category": "Équipements",
    "card_desc": ("Remplacement et installation d'interrupteurs, va-et-vient, variateurs et "
                  "commandes."),
    "title": "Interrupteur — Remplacement et installation | Electricien Richard",
    "desc": ("Interrupteur électrique : remplacement, va-et-vient, télérupteur, variateur, "
             "détecteur de présence. Pannes fréquentes et solutions."),
    "h1": "Interrupteur : remplacement, va-et-vient et commandes",
    "intro": ("Un interrupteur défaillant est rarement grave, mais il révèle parfois un "
              "problème de connexion qui, lui, mérite attention."),
    "service_type": "Installation d'interrupteurs et de commandes d'éclairage",
    "quick": {
        "title": "Les types de commandes d'éclairage",
        "answer": (
            "<p><strong>Un interrupteur simple commande un point lumineux depuis un seul "
            "endroit. Le va-et-vient permet de le commander depuis deux endroits. Au-delà de "
            "deux points de commande, on utilise un bouton-poussoir associé à un "
            "télérupteur.</strong></p>"
            "<p>S'y ajoutent les variateurs, les détecteurs de présence et les commandes "
            "connectées, dont la compatibilité avec les sources lumineuses doit être vérifiée.</p>"),
        "facts": [
            ("Interrupteur simple", "Un point de commande"),
            ("Va-et-vient", "Deux points de commande"),
            ("Télérupteur ou minuterie", "Trois points de commande ou plus, couloirs et escaliers"),
            ("Variateur", "Compatibilité à vérifier avec les sources LED"),
            ("Détecteur", "Circulations, extérieur, locaux à passage occasionnel"),
        ],
    },
    "body": """
<h2 id="types">Choisir la commande adaptée</h2>

<div class="table-wrap"><table>
<caption>Types de commandes et usages</caption>
<thead><tr><th scope="col">Dispositif</th><th scope="col">Usage</th><th scope="col">Remarque</th></tr></thead>
<tbody>
<tr><td>Interrupteur simple</td><td>Pièce avec une seule entrée</td><td>Le plus courant</td></tr>
<tr><td>Va-et-vient</td><td>Couloir, chambre, pièce à deux accès</td><td>Deux points de commande</td></tr>
<tr><td>Bouton-poussoir et télérupteur</td><td>Escalier, long couloir, grande pièce</td><td>Nombre de points de commande non limité</td></tr>
<tr><td>Minuterie</td><td>Parties communes, circulations</td><td>Extinction automatique après un délai</td></tr>
<tr><td>Variateur</td><td>Séjour, chambre</td><td>Exige des sources compatibles avec la variation</td></tr>
<tr><td>Détecteur de mouvement</td><td>Extérieur, garage, cave, dégagement</td><td>Réglages de sensibilité et de temporisation</td></tr>
</tbody></table></div>

<h2 id="pannes">Pannes fréquentes et ce qu'elles signifient</h2>

<h3>L'interrupteur ne répond plus</h3>
<p>Le mécanisme peut être usé, mais dans bien des cas la cause se trouve à la connexion :
borne desserrée, conducteur mal serti. Un interrupteur qui « ne fonctionne plus » alors
qu'il fonctionnait par intermittence auparavant relève presque toujours de cette
catégorie.</p>

<h3>Il crépite ou chauffe</h3>
<p>Signe d'un mauvais contact. À traiter rapidement, car l'échauffement se poursuit tant que
la connexion reste défectueuse.</p>

<h3>Un seul des deux points de va-et-vient fonctionne</h3>
<p>Généralement un conducteur navette coupé ou déconnecté, ou un raccordement incorrect
après un remplacement.</p>

<h3>L'éclairage clignote ou reste faiblement allumé</h3>
<p>Fréquent avec des sources LED associées à des interrupteurs lumineux ou à des variateurs
inadaptés : un courant résiduel très faible suffit à faire luire une LED. La solution passe
par un matériel compatible ou par un dispositif adapté.</p>

<h3>Le variateur chauffe ou grésille</h3>
<p>Souvent une incompatibilité entre le variateur et les sources installées, ou un
dépassement de la puissance admissible du variateur.</p>

<h2 id="remplacement">Remplacer un interrupteur</h2>

<p>L'opération suppose de couper le circuit au tableau, de vérifier l'absence de tension,
puis de repérer les conducteurs avant démontage. Le remplacement est aussi l'occasion de
contrôler l'état de la boîte d'encastrement, le serrage des conducteurs et la présence
éventuelle de traces d'échauffement.</p>

<p>Un point souvent négligé : dans les installations anciennes, la commande d'éclairage
coupe parfois le neutre au lieu de la phase. Cette configuration laisse le point lumineux
sous tension même interrupteur ouvert, ce qui est dangereux lors du remplacement d'une
lampe. Elle est systématiquement corrigée lors d'une reprise.</p>
""",
    "faq": [
        ("Peut-on remplacer un interrupteur soi-même ?",
         "<p>L'opération est simple à condition de couper le circuit au tableau et de vérifier "
         "l'absence de tension avec un appareil adapté. Deux précautions comptent : repérer "
         "les conducteurs avant de les débrancher, et vérifier que c'est bien la phase qui est "
         "coupée par la commande, et non le neutre.</p>"),
        ("Pourquoi mes LED restent-elles faiblement allumées ?",
         "<p>Parce qu'un très faible courant continue de circuler : voyant lumineux de "
         "l'interrupteur, variateur inadapté, ou capacité parasite de l'installation. Les LED "
         "consommant très peu, ce courant résiduel suffit à les faire luire. La solution "
         "consiste à utiliser un matériel compatible ou à installer un dispositif "
         "d'absorption.</p>"),
        ("Comment commander une lampe depuis trois endroits ?",
         "<p>Avec des boutons-poussoirs et un télérupteur placé au tableau. Le nombre de points "
         "de commande n'est alors pas limité, contrairement au va-et-vient qui n'en autorise "
         "que deux.</p>"),
        ("Un interrupteur peut-il faire sauter le disjoncteur ?",
         "<p>Oui, si un conducteur mal serré vient en contact avec un autre à l'intérieur du "
         "boîtier, ou si le mécanisme est détérioré. Le déclenchement se produit alors "
         "typiquement au moment de l'actionnement.</p>"),
        ("Peut-on installer un variateur sur n'importe quel éclairage ?",
         "<p>Non. Les sources LED ne sont pas toutes compatibles avec la variation, et le "
         "variateur doit être adapté au type de charge. Une association inadaptée provoque "
         "scintillements, bourdonnements, plage de réglage réduite ou usure prématurée.</p>"),
    ],
    "related": ["eclairage", "prise-electrique", "luminaire", "installation-electrique",
                "renovation-electrique"],
})

SERVICES.append({
    "slug": "eclairage",
    "path": "eclairage.html",
    "icon": "bulb",
    "category": "Équipements",
    "card_desc": ("Concevoir et installer un éclairage intérieur et extérieur cohérent et "
                  "économe."),
    "title": "Installation d'éclairage intérieur et extérieur | Electricien Richard",
    "desc": ("Installation d'éclairage : conception des circuits, éclairage intérieur, "
             "extérieur, commandes, détecteurs et choix des sources lumineuses."),
    "h1": "Installation d'éclairage intérieur et extérieur",
    "intro": ("Un bon éclairage ne se résume pas au nombre de points lumineux. Il combine des "
              "niveaux d'éclairement adaptés à chaque usage, des commandes bien placées et "
              "des sources de qualité cohérente."),
    "service_type": "Installation d'éclairage",
    "quick": {
        "title": "Concevoir un éclairage : les principes",
        "answer": (
            "<p><strong>Un éclairage réussi superpose trois couches : un éclairage général "
            "pour circuler, un éclairage fonctionnel là où l'on travaille, et un éclairage "
            "d'ambiance pour le confort.</strong></p>"
            "<p>Les circuits d'éclairage sont distincts des circuits de prises et protégés "
            "séparément, ce qui évite de se retrouver dans le noir lors du déclenchement d'un "
            "circuit de prises.</p>"),
        "facts": [
            ("Éclairage général", "Circulation et perception globale de la pièce"),
            ("Éclairage fonctionnel", "Plan de travail, bureau, miroir, lecture"),
            ("Éclairage d'ambiance", "Confort visuel, mise en valeur"),
            ("Extérieur", "Matériel à indice de protection adapté et commande automatique"),
            ("Salle d'eau", "Matériels conformes aux volumes de sécurité"),
        ],
    },
    "body": """
<h2 id="pieces">Éclairer chaque pièce selon son usage</h2>

<h3>Cuisine</h3>
<p>La cuisine demande un éclairement soutenu et surtout non gênant : la principale erreur
consiste à n'installer qu'un point central, qui place l'utilisateur dans son propre ombre au
plan de travail. Un éclairage dédié sous meubles ou en applique corrige ce défaut.</p>

<h3>Salle d'eau</h3>
<p>Deux besoins distincts : un éclairage général et un éclairage du miroir, idéalement
latéral pour éviter les ombres portées sur le visage. Les matériels doivent respecter les
volumes de sécurité définis autour de la douche et de la baignoire.</p>

<h3>Séjour</h3>
<p>C'est la pièce où la superposition des couches prend tout son sens : un éclairage général
discret, des points fonctionnels pour la lecture, et des sources d'ambiance. Les commandes
multiples et la variation y trouvent leur utilité.</p>

<h3>Chambre</h3>
<p>Éclairage général doux, points de lecture indépendants et, si possible, commande depuis
l'entrée et depuis le lit — un va-et-vient simple à prévoir lors d'une rénovation.</p>

<h3>Circulations et escaliers</h3>
<p>Ce sont les zones où les commandes multiples sont indispensables. Un escalier doit
pouvoir s'allumer depuis chaque niveau ; un long couloir gagne à recevoir un détecteur ou
une minuterie.</p>

<h2 id="exterieur">Éclairage extérieur</h2>

<p>L'éclairage extérieur répond à trois besoins : la sécurité des accès, le confort d'usage
et la mise en valeur. Il impose des contraintes techniques précises.</p>

<ul>
<li><strong>Matériel adapté</strong> : indice de protection en rapport avec l'exposition
réelle, et résistance à la corrosion, particulièrement en bord de mer.</li>
<li><strong>Alimentation</strong> : câble prévu pour la pose extérieure ou enterrée sous
fourreau, à une profondeur suffisante et avec un grillage avertisseur.</li>
<li><strong>Commande</strong> : détecteur de mouvement pour les accès, horloge ou cellule
photoélectrique pour les zones à éclairage régulier.</li>
<li><strong>Protection</strong> : circuit dédié protégé par un différentiel 30 mA.</li>
</ul>

<p>Un point souvent sous-estimé : la nuisance lumineuse. Un éclairage mal orienté éclaire
le voisinage et le ciel plus que l'espace utile. L'orientation des luminaires vers le bas et
le choix d'une température de couleur modérée limitent cet effet.</p>

<h2 id="sources">Choisir les sources lumineuses</h2>

<p>Trois critères comptent davantage que la puissance affichée.</p>

<ul>
<li><strong>Le flux lumineux</strong>, exprimé en lumens, indique la quantité de lumière
réellement émise. C'est lui qui remplace l'ancienne référence en watts.</li>
<li><strong>La température de couleur</strong>, en kelvins, détermine l'ambiance : les
valeurs basses donnent une lumière chaude adaptée aux pièces de vie, les valeurs élevées une
lumière froide plus adaptée aux locaux techniques.</li>
<li><strong>L'indice de rendu des couleurs</strong> traduit la fidélité des couleurs sous
la lumière. Un indice faible donne des teintes ternes, particulièrement gênant dans une
cuisine ou une salle d'eau.</li>
</ul>

<p>Un dernier point de cohérence : mélanger des températures de couleur différentes dans une
même pièce produit un résultat désagréable, même avec des sources de bonne qualité.</p>

<h2 id="renovation">Éclairage et rénovation</h2>

<p>Ajouter des points lumineux dans un logement existant suppose de vérifier la capacité du
circuit d'éclairage concerné et le nombre de points déjà raccordés. Dans le bâti ancien, la
difficulté est plus souvent le cheminement que la puissance : plafonds en plâtre sur lattis,
poutres apparentes et combles non accessibles imposent des solutions adaptées, parfois en
applique plutôt qu'au plafond. Voir aussi <a href="/luminaire.html">installation de
luminaires</a> et <a href="/interrupteur.html">commandes d'éclairage</a>.</p>
""",
    "faq": [
        ("Combien de points lumineux peut-on mettre sur un circuit ?",
         "<p>Le nombre est limité par la norme en fonction de la section du conducteur et du "
         "calibre de protection. Au-delà, un second circuit d'éclairage doit être créé. Cette "
         "limite explique qu'on ne puisse pas ajouter indéfiniment des spots sur un circuit "
         "existant.</p>"),
        ("Quelle température de couleur choisir ?",
         "<p>Une lumière chaude convient aux pièces de vie et aux chambres, une lumière plus "
         "neutre à la cuisine et à la salle d'eau, une lumière froide aux garages et locaux "
         "techniques. L'essentiel est la cohérence : une même pièce doit être éclairée par des "
         "sources de température identique.</p>"),
        ("Peut-on installer des spots dans une salle de bains ?",
         "<p>Oui, à condition de respecter les volumes de sécurité et d'utiliser des matériels "
         "dont l'indice de protection correspond au volume concerné. Au-dessus d'une douche, "
         "les exigences sont plus strictes qu'au-dessus d'un lavabo.</p>"),
        ("Comment éclairer une allée ou un accès ?",
         "<p>Par des points bas orientés vers le sol plutôt que par un projecteur unique, avec "
         "une alimentation enterrée sous fourreau et une commande par détecteur ou par "
         "horloge. Cette approche éclaire mieux le cheminement tout en limitant l'éblouissement "
         "et les nuisances pour le voisinage.</p>"),
        ("Faut-il un circuit séparé pour l'éclairage extérieur ?",
         "<p>C'est vivement recommandé. Un circuit dédié permet d'isoler l'extérieur en cas de "
         "défaut — situation fréquente, l'humidité affectant d'abord ces circuits — sans priver "
         "le logement d'éclairage intérieur.</p>"),
    ],
    "related": ["luminaire", "interrupteur", "installation-electrique", "prise-electrique",
                "renovation-electrique"],
})

SERVICES.append({
    "slug": "luminaire",
    "path": "luminaire.html",
    "icon": "bulb",
    "category": "Équipements",
    "card_desc": ("Pose et raccordement de luminaires : suspensions, spots, appliques, rails "
                  "et supports."),
    "title": "Installation de luminaire — Pose et raccordement | Electricien Richard",
    "desc": ("Installation de luminaires : suspensions, spots encastrés, appliques, "
             "raccordement DCL, supports et points de vigilance dans le bâti ancien."),
    "h1": "Installation et raccordement de luminaires",
    "intro": ("Poser un luminaire est une opération courante, mais le raccordement et la "
              "fixation réservent des surprises, en particulier dans les logements anciens."),
    "service_type": "Installation de luminaires",
    "quick": {
        "title": "Poser un luminaire : les points clés",
        "answer": (
            "<p><strong>Trois éléments déterminent la faisabilité : le point d'alimentation "
            "existant, la nature du support, et le poids du luminaire.</strong></p>"
            "<p>Dans les logements récents, les points d'éclairage sont équipés d'un "
            "dispositif de connexion pour luminaire (DCL) qui normalise le raccordement. "
            "Dans le bâti ancien, le raccordement est souvent direct et le support "
            "incertain.</p>"),
        "facts": [
            ("Raccordement", "DCL dans le neuf, raccordement direct à reprendre dans l'ancien"),
            ("Support", "Plafond plâtre, béton, lattis, poutre : fixation adaptée à chaque cas"),
            ("Poids", "Au-delà de quelques kilogrammes, fixation mécanique indépendante"),
            ("Salle d'eau", "Matériel conforme au volume de sécurité concerné"),
            ("Extérieur", "Indice de protection adapté et étanchéité du raccordement"),
        ],
    },
    "body": """
<h2 id="types">Les principaux types de luminaires</h2>

<h3>Suspensions et plafonniers</h3>
<p>Le point de vigilance est la fixation. Un plafond en plaque de plâtre ne supporte pas un
luminaire lourd sans renfort ou sans fixation reprise sur la structure. Dans les plafonds
anciens en plâtre sur lattis, la tenue est souvent aléatoire et impose une reprise.</p>

<h3>Spots encastrés</h3>
<p>Ils exigent un vide suffisant au-dessus du plafond et une attention particulière lorsque
celui-ci est isolé : certains modèles ne peuvent pas être recouverts d'isolant sans risque
d'échauffement. Dans un plafond isolé, il faut choisir des spots prévus pour ce cas ou
prévoir des dispositifs de protection.</p>

<h3>Appliques murales</h3>
<p>Souvent la meilleure solution dans le bâti ancien, lorsque le passage en plafond est
impossible. Elles permettent également d'éclairer un miroir ou une tête de lit sans travaux
lourds.</p>

<h3>Rails et systèmes orientables</h3>
<p>Utiles dans les grandes pièces et les espaces à usages multiples, ils offrent une
souplesse d'orientation à partir d'un seul point d'alimentation.</p>

<h2 id="raccordement">Le raccordement</h2>

<p>Dans les installations récentes, chaque point d'éclairage est équipé d'un dispositif de
connexion pour luminaire, avec socle et fiche. Ce système permet de changer un luminaire
sans manipuler les conducteurs, et garantit qu'une boîte non équipée reste protégée.</p>

<p>Dans les installations anciennes, le raccordement se fait souvent par un domino nu, voire
par une simple torsade isolée de ruban adhésif. Ces montages doivent être repris : ils ne
garantissent ni la tenue mécanique, ni l'isolement. Un point fréquent : l'absence de
conducteur de protection au point d'éclairage, qui interdit l'installation d'un luminaire
métallique nécessitant une mise à la terre.</p>

<h2 id="salle-eau">Salle d'eau et extérieur</h2>

<p>Ce sont les deux situations où le choix du matériel prime sur l'esthétique. Dans une salle
d'eau, l'indice de protection exigé dépend du volume dans lequel le luminaire est installé.
En extérieur, il faut tenir compte de la pluie, mais aussi de la condensation : un luminaire
mal ventilé accumule l'humidité intérieure, ce qui finit par provoquer un défaut
d'isolement.</p>

<h2 id="ancien">Le cas du bâti ancien</h2>

<p>Dans une maison ancienne, poser un luminaire au plafond suppose parfois de créer le point
d'alimentation. Trois solutions sont couramment employées : le passage par les combles
lorsqu'ils sont accessibles, la reprise depuis un point existant, ou l'installation
d'appliques alimentées depuis les circuits périphériques. Le choix dépend de la
configuration et de l'acceptation ou non de cheminements apparents.</p>
""",
    "faq": [
        ("Qu'est-ce qu'un DCL ?",
         "<p>Le dispositif de connexion pour luminaire est un socle normalisé installé au point "
         "d'éclairage. Il permet de raccorder un luminaire par une fiche, sans intervenir sur "
         "les conducteurs. Il est exigé aux points d'éclairage des installations neuves.</p>"),
        ("Peut-on fixer un lustre lourd sur un plafond en plaque de plâtre ?",
         "<p>Pas directement. Au-delà de quelques kilogrammes, la fixation doit être reprise "
         "sur la structure du plafond ou sur un renfort prévu à cet effet. Les chevilles pour "
         "plaque de plâtre ont une capacité limitée, et la chute d'un luminaire lourd est un "
         "risque réel.</p>"),
        ("Peut-on installer des spots dans un plafond isolé ?",
         "<p>Oui, à condition d'utiliser des modèles prévus pour être recouverts d'isolant, ou "
         "de mettre en place des dispositifs maintenant un espace autour du spot. Un spot "
         "ordinaire noyé dans l'isolant accumule la chaleur, ce qui réduit sa durée de vie et "
         "peut présenter un risque.</p>"),
        ("Mon point de plafond n'a pas de fil de terre, est-ce un problème ?",
         "<p>Cela dépend du luminaire. Un luminaire à double isolation n'en a pas besoin. En "
         "revanche, un luminaire dont des parties métalliques sont accessibles doit être relié "
         "au conducteur de protection : en son absence, il faut soit choisir un autre "
         "luminaire, soit reprendre l'alimentation du point.</p>"),
        ("Qui doit installer les luminaires lors d'une rénovation ?",
         "<p>L'électricien met en place les points d'alimentation et les dispositifs de "
         "raccordement. La pose des luminaires eux-mêmes peut être réalisée ensuite, selon ce "
         "qui a été convenu au devis. Il est utile de connaître les luminaires envisagés dès "
         "la conception : leur poids et leur type conditionnent la préparation des supports.</p>"),
    ],
    "related": ["eclairage", "interrupteur", "installation-electrique", "renovation-electrique",
                "prise-electrique"],
})

SERVICES.append({
    "slug": "borne-recharge",
    "path": "borne-recharge.html",
    "icon": "car",
    "category": "Équipements",
    "card_desc": ("Installer un point de recharge pour véhicule électrique en maison ou en "
                  "copropriété."),
    "title": "Borne de recharge véhicule électrique — Installation | Electricien Richard",
    "desc": ("Installation de borne de recharge pour véhicule électrique : puissances, "
             "circuit dédié, protections, maison individuelle et copropriété, droit à la "
             "prise."),
    "h1": "Installation d'une borne de recharge pour véhicule électrique",
    "intro": ("Recharger un véhicule électrique sollicite l'installation plus longtemps et "
              "plus intensément que n'importe quel autre usage domestique. C'est ce qui "
              "impose un circuit dédié et des protections spécifiques."),
    "service_type": "Installation de borne de recharge pour véhicule électrique",
    "quick": {
        "title": "Ce qu'il faut savoir avant d'installer une borne",
        "answer": (
            "<p><strong>Une borne de recharge se raccorde sur un circuit dédié, protégé "
            "spécifiquement, dimensionné selon la puissance retenue et la distance au "
            "tableau.</strong> La recharge sur une prise domestique ordinaire n'est pas adaptée "
            "à un usage régulier : la durée et l'intensité soutenue échauffent la prise et son "
            "circuit.</p>"
            "<p>Au-delà d'une certaine puissance, l'installation doit être réalisée par un "
            "professionnel disposant de la qualification correspondante.</p>"),
        "facts": [
            ("Puissances courantes", "3,7 kW et 7,4 kW en monophasé ; jusqu'à 22 kW en triphasé"),
            ("Circuit", "Dédié, sans autre appareil raccordé"),
            ("Protection", "Disjoncteur adapté et protection différentielle spécifique au point de recharge"),
            ("Préalable", "Vérification de la puissance souscrite et de la place au tableau"),
            ("Copropriété", "Droit à la prise : installation possible à ses frais, après information du syndic"),
        ],
    },
    "body": """
<h2 id="pourquoi">Pourquoi une prise ordinaire ne suffit pas</h2>

<p>Une prise domestique classique est conçue pour des usages intermittents. Recharger un
véhicule impose au contraire un courant élevé pendant plusieurs heures d'affilée. Cette
sollicitation continue met en évidence tous les défauts d'un circuit : connexion légèrement
desserrée, prise usée, conducteur juste dimensionné.</p>

<p>Le résultat est un échauffement progressif de la prise et du câble, parfois jusqu'à la
déformation du matériel. C'est la raison pour laquelle un point de recharge se raccorde sur
un circuit dédié, dimensionné pour cet usage précis.</p>

<h2 id="puissances">Choisir la puissance</h2>

<div class="table-wrap"><table>
<caption>Puissances usuelles de recharge en habitation</caption>
<thead><tr><th scope="col">Puissance</th><th scope="col">Alimentation</th><th scope="col">Usage typique</th></tr></thead>
<tbody>
<tr><td>3,7 kW</td><td>Monophasé</td><td>Petits trajets quotidiens, recharge de nuit, installation existante limitée</td></tr>
<tr><td>7,4 kW</td><td>Monophasé</td><td>Configuration la plus courante en maison individuelle</td></tr>
<tr><td>11 kW</td><td>Triphasé</td><td>Recharge plus rapide, sous réserve d'un raccordement triphasé</td></tr>
<tr><td>22 kW</td><td>Triphasé</td><td>Usage intensif ou professionnel ; le véhicule doit pouvoir l'accepter</td></tr>
</tbody></table></div>

<p>Deux limites conditionnent le choix : la puissance souscrite du logement et la capacité
du chargeur embarqué du véhicule. Installer une borne plus puissante que ce que le véhicule
accepte n'apporte aucun gain.</p>

<h2 id="etude">L'étude préalable</h2>

<p>Avant toute installation, plusieurs points sont vérifiés :</p>

<ul>
<li><strong>La puissance souscrite</strong> et la marge disponible aux heures d'usage
simultané. Une augmentation d'abonnement est parfois nécessaire.</li>
<li><strong>La place au tableau</strong> pour ajouter le circuit et ses protections.</li>
<li><strong>La distance entre le tableau et l'emplacement de la borne</strong>, qui
détermine la section du câble.</li>
<li><strong>Le cheminement</strong> : traversée de mur, passage enterré, gaine existante.</li>
<li><strong>L'état de l'installation existante</strong>, notamment la mise à la terre, qui
doit être effective.</li>
</ul>

<h2 id="protections">Les protections spécifiques</h2>

<p>Un point de recharge exige une protection différentielle adaptée à la nature du courant
de défaut susceptible d'apparaître. Certains équipements intègrent eux-mêmes une partie de
cette protection, d'autres non : le dispositif à installer au tableau dépend donc du modèle
de borne retenu. Ce point est déterminant et constitue l'une des différences majeures entre
une installation réalisée dans les règles et un montage improvisé.</p>

<p>S'y ajoute la gestion de charge, qui permet d'adapter automatiquement la puissance de
recharge à la consommation du logement, évitant le déclenchement du disjoncteur de
branchement lors des pointes.</p>

<h2 id="copropriete">En copropriété : le droit à la prise</h2>

<p>Un copropriétaire ou un locataire disposant d'une place de stationnement peut faire
installer un point de recharge à ses frais. La démarche consiste à informer le syndic par
lettre recommandée en joignant un descriptif des travaux et un schéma de raccordement. Le
syndic inscrit la question à l'ordre du jour de l'assemblée générale à titre d'information,
et l'opposition n'est possible que pour un motif sérieux et légitime.</p>

<p>Techniquement, deux solutions coexistent : le raccordement sur le compteur du logement,
ou la création d'un point de comptage individuel dédié. Le choix dépend de la configuration
de l'immeuble et de la distance entre le logement et le stationnement.</p>

<h2 id="aides">Aides et dispositifs</h2>

<p>Des dispositifs de soutien à l'installation de points de recharge existent, avec des
conditions qui évoluent régulièrement — nature du logement, type d'installation, statut du
demandeur. Il est recommandé de vérifier les conditions en vigueur au moment du projet
plutôt que de se fier à des informations datées. Aucun montant n'est annoncé ici pour cette
raison.</p>
""",
    "faq": [
        ("Peut-on recharger un véhicule électrique sur une prise normale ?",
         "<p>C'est possible en dépannage, avec le câble fourni par le constructeur et sur une "
         "prise en bon état, mais ce n'est pas adapté à un usage quotidien. La durée et "
         "l'intensité soutenue échauffent la prise et son circuit. Pour un usage régulier, un "
         "point de recharge sur circuit dédié est nécessaire.</p>"),
        ("Faut-il augmenter sa puissance souscrite ?",
         "<p>Souvent, oui. Une borne de 7,4 kW représente à elle seule une puissance "
         "importante, qui s'ajoute aux autres usages. Sans marge suffisante, le disjoncteur de "
         "branchement déclenche lors des pointes. Une gestion de charge dynamique permet dans "
         "certains cas d'éviter l'augmentation d'abonnement.</p>"),
        ("Combien de temps dure l'installation d'une borne ?",
         "<p>Cela dépend surtout du cheminement du câble entre le tableau et l'emplacement de "
         "la borne. Un raccordement dans un garage attenant est rapide ; un passage enterré "
         "vers un stationnement éloigné demande davantage de travaux. La durée est précisée au "
         "devis, après visite.</p>"),
        ("Mon syndic peut-il refuser l'installation d'une borne ?",
         "<p>Dans le cadre du droit à la prise, l'opposition n'est possible que pour un motif "
         "sérieux et légitime, par exemple lorsque l'immeuble dispose déjà d'une installation "
         "permettant de répondre à la demande. La procédure suppose d'informer le syndic par "
         "lettre recommandée avec un descriptif des travaux.</p>"),
        ("Quelle différence entre une borne et une prise renforcée ?",
         "<p>Une prise renforcée est conçue pour supporter une recharge prolongée à puissance "
         "limitée, généralement autour de 3,2 kW. Une borne murale permet des puissances plus "
         "élevées, intègre des fonctions de sécurité et de communication avec le véhicule, et "
         "autorise la gestion de charge. Dans les deux cas, un circuit dédié est "
         "nécessaire.</p>"),
    ],
    "related": ["installation-electrique", "tableau-electrique", "electricien-particulier",
                "renovation-electrique", "electricien-entreprise"],
})

SERVICES.append({
    "slug": "vmc",
    "path": "vmc.html",
    "icon": "home",
    "category": "Équipements",
    "card_desc": ("Installation et raccordement électrique d'une VMC : circuit, commande et "
                  "entretien."),
    "title": "VMC — Installation et raccordement électrique | Electricien Richard",
    "desc": ("Installation et raccordement électrique d'une VMC simple ou double flux : "
             "circuit dédié, protection, commande, pannes fréquentes et entretien."),
    "h1": "VMC : installation et raccordement électrique",
    "intro": ("La ventilation mécanique contrôlée fonctionne en continu. Son alimentation "
              "électrique répond à des règles précises, souvent négligées lors des "
              "installations réalisées après coup."),
    "service_type": "Installation électrique de VMC",
    "quick": {
        "title": "L'essentiel sur le raccordement d'une VMC",
        "answer": (
            "<p><strong>Une VMC est alimentée par un circuit dédié, protégé au tableau, et "
            "ne doit pas pouvoir être arrêtée par un interrupteur accessible sans "
            "précaution.</strong> Elle fonctionne en permanence : son arrêt prolongé favorise "
            "l'humidité et les moisissures.</p>"
            "<p>Le dispositif de coupure existe néanmoins, mais il est réservé à l'entretien "
            "et repéré comme tel.</p>"),
        "facts": [
            ("Circuit", "Dédié, protégé au tableau"),
            ("Fonctionnement", "Continu ; l'arrêt prolongé dégrade la qualité de l'air"),
            ("Coupure", "Prévue pour l'entretien, repérée, non accessible par erreur"),
            ("Types", "Simple flux autoréglable ou hygroréglable, double flux"),
            ("Entretien", "Nettoyage des bouches et vérification du caisson"),
        ],
    },
    "body": """
<h2 id="types">Les types de VMC</h2>

<h3>Simple flux autoréglable</h3>
<p>Le débit d'extraction est constant. C'est le système le plus simple et le plus répandu
dans les logements anciens équipés après coup.</p>

<h3>Simple flux hygroréglable</h3>
<p>Le débit varie selon le taux d'humidité, ce qui limite les déperditions de chaleur
lorsque l'air est sec. Les bouches sont spécifiques et ne se remplacent pas par des modèles
autoréglables.</p>

<h3>Double flux</h3>
<p>L'air extrait et l'air entrant se croisent dans un échangeur, ce qui permet de récupérer
une partie de la chaleur. Le système est plus complexe : réseau de gaines double, caisson
volumineux, filtres à entretenir, et raccordement électrique plus élaboré, parfois avec
régulation et sondes.</p>

<h2 id="raccordement">Le raccordement électrique</h2>

<p>Le caisson de VMC est alimenté depuis le tableau par un circuit qui lui est propre. Ce
choix n'est pas de confort : il évite qu'un défaut sur un autre usage n'arrête la
ventilation, et permet d'identifier immédiatement le circuit lors d'un entretien.</p>

<p>Le caisson étant généralement installé en combles ou dans un local technique, plusieurs
points méritent attention :</p>

<ul>
<li>l'accessibilité du caisson pour l'entretien et le remplacement ;</li>
<li>la présence d'un dispositif de coupure à proximité, repéré, pour intervenir en
sécurité ;</li>
<li>la protection du câble sur son cheminement dans les combles ;</li>
<li>la fixation du caisson, dont les vibrations peuvent se transmettre à la structure ;</li>
<li>le raccordement du conducteur de protection lorsque le matériel l'exige.</li>
</ul>

<h2 id="pannes">Pannes fréquentes</h2>

<div class="table-wrap"><table>
<caption>Symptômes et causes possibles sur une VMC</caption>
<thead><tr><th scope="col">Symptôme</th><th scope="col">Causes possibles</th></tr></thead>
<tbody>
<tr><td>La VMC ne tourne plus</td><td>Protection déclenchée au tableau, moteur hors service, condensateur défaillant, câble sectionné en combles</td></tr>
<tr><td>Bruit anormal ou vibrations</td><td>Fixation desserrée, roue encrassée, roulement usé</td></tr>
<tr><td>Débit insuffisant</td><td>Bouches encrassées, gaine écrasée ou percée, entrées d'air obstruées</td></tr>
<tr><td>Condensation et moisissures persistantes</td><td>VMC arrêtée, entrées d'air bouchées, débit inadapté au logement</td></tr>
<tr><td>Déclenchement du différentiel</td><td>Défaut d'isolement du moteur, souvent lié à l'humidité en combles</td></tr>
</tbody></table></div>

<h2 id="entretien">Entretien</h2>

<p>L'entretien courant relève de l'occupant : nettoyage régulier des bouches d'extraction et
des entrées d'air situées sur les menuiseries. Ces éléments s'encrassent et réduisent
progressivement le débit, souvent sans que l'on s'en aperçoive.</p>

<p>Le caisson lui-même demande un contrôle plus espacé : état de la roue, fixation, bruit,
et pour une double flux, remplacement des filtres selon la périodicité indiquée par le
fabricant. Un filtre saturé réduit le débit et augmente la consommation du moteur.</p>
""",
    "faq": [
        ("Peut-on arrêter sa VMC la nuit ou en hiver ?",
         "<p>Ce n'est pas recommandé. La ventilation évacue l'humidité produite par "
         "l'occupation — cuisine, salle d'eau, respiration. Un arrêt prolongé favorise la "
         "condensation et les moisissures, en particulier en hiver, période où l'on aère le "
         "moins.</p>"),
        ("Faut-il un circuit dédié pour la VMC ?",
         "<p>Oui, la VMC doit être alimentée par un circuit qui lui est propre, protégé au "
         "tableau. Cela évite qu'un défaut sur un autre usage n'interrompe la ventilation et "
         "permet d'identifier clairement le circuit lors d'une intervention.</p>"),
        ("Ma VMC fait du bruit, est-ce grave ?",
         "<p>Pas nécessairement, mais cela signale un problème mécanique : fixation desserrée, "
         "roue encrassée ou roulement en fin de vie. Un déséquilibre non traité use "
         "prématurément le moteur. Un contrôle permet de déterminer s'il s'agit d'un simple "
         "nettoyage ou d'un remplacement.</p>"),
        ("Peut-on installer une VMC dans un logement ancien ?",
         "<p>Oui, et c'est souvent utile, notamment après le remplacement de menuiseries qui "
         "a rendu le logement plus étanche. La contrainte principale est le passage des gaines "
         "et l'implantation du caisson, qui exige un volume accessible — combles ou local "
         "technique.</p>"),
        ("Qui installe une VMC : l'électricien ou le plombier-chauffagiste ?",
         "<p>Les deux corps de métier interviennent selon la nature du projet. Le réseau "
         "aéraulique relève du domaine de la ventilation, tandis que l'alimentation, la "
         "protection et la commande relèvent de l'électricité. Sur une installation simple "
         "flux, l'ensemble est fréquemment réalisé par un même intervenant.</p>"),
    ],
    "related": ["installation-electrique", "renovation-electrique", "eclairage",
                "tableau-electrique", "electricien-particulier"],
})

SERVICES.append({
    "slug": "electricien-particulier",
    "path": "electricien-particulier.html",
    "icon": "home",
    "category": "Pour qui",
    "card_desc": ("Interventions chez les particuliers : maison, appartement, copropriété, "
                  "location."),
    "title": "Électricien pour particuliers — Maison et appartement | Electricien Richard",
    "desc": ("Électricien pour particuliers : dépannage, rénovation, mise en sécurité en "
             "maison, appartement, copropriété ou logement mis en location."),
    "h1": "Électricien pour les particuliers",
    "intro": ("Chez un particulier, l'électricité pose presque toujours les mêmes trois "
              "questions : est-ce sûr, est-ce suffisant pour mes usages, et par quoi "
              "faut-il commencer ?"),
    "service_type": "Travaux d'électricité pour particuliers",
    "quick": {
        "title": "Ce que nous réalisons chez les particuliers",
        "answer": (
            "<p><strong>Dépannage, recherche de panne, remplacement de tableau, création ou "
            "reprise de circuits, mise en sécurité, éclairage, bornes de recharge et "
            "rénovation complète.</strong></p>"
            "<p>Les interventions concernent les maisons comme les appartements, en propriété "
            "occupée comme en logement destiné à la location.</p>"),
        "facts": [
            ("Maison individuelle", "Rénovation, extension, dépendances, extérieur, borne de recharge"),
            ("Appartement", "Tableau privatif, circuits, cuisine et salle d'eau"),
            ("Copropriété", "Partie privative ; les parties communes relèvent du syndic"),
            ("Location", "Mise en sécurité entre deux locataires, logement décent"),
            ("Achat", "Examen de l'installation et hiérarchisation des travaux"),
        ],
    },
    "body": """
<h2 id="situations">Les situations les plus fréquentes</h2>

<h3>J'achète un logement</h3>
<p>Le diagnostic remis à la vente signale les anomalies mais ne dit ni ce qui est urgent, ni
ce que coûtera la reprise. Un <a href="/diagnostic-electrique.html">examen de
l'installation</a> permet d'établir un ordre de priorité et d'intégrer le budget électrique
au projet global.</p>

<h3>Je rénove mon logement</h3>
<p>C'est le moment le plus favorable pour reprendre l'électricité : les cheminements sont
accessibles et les finitions ne sont pas encore posées. Coordonner l'électricité avec les
autres corps d'état évite des reprises coûteuses. Voir
<a href="/renovation-electrique.html">rénovation électrique</a>.</p>

<h3>Je loue un logement</h3>
<p>Le logement doit être décent, ce qui suppose une installation en bon état d'usage, sans
risque manifeste pour la sécurité des occupants. Entre deux locataires, une vérification
permet de traiter les points sensibles : protection différentielle, mise à la terre,
suppression des montages provisoires.</p>

<h3>Mon installation ne suit plus</h3>
<p>Déclenchements répétés, multiprises partout, impossibilité d'ajouter un appareil :
l'installation est en limite de capacité. Le sujet est alors le
<a href="/tableau-electrique.html">tableau</a> et le nombre de circuits, pas la puissance
souscrite seule.</p>

<h3>J'ajoute un équipement</h3>
<p>Borne de recharge, pompe à chaleur, climatisation, plaque à induction, spa : chacun de
ces équipements suppose une vérification préalable de la puissance disponible et de la
capacité du tableau.</p>

<h2 id="maison-appartement">Maison ou appartement : ce qui change</h2>

<div class="table-wrap"><table>
<caption>Différences pratiques entre maison et appartement</caption>
<thead><tr><th scope="col">Aspect</th><th scope="col">Maison individuelle</th><th scope="col">Appartement</th></tr></thead>
<tbody>
<tr><td>Périmètre d'intervention</td><td>Ensemble de l'installation, terre comprise</td><td>Partie privative ; colonne montante et communs relèvent de la copropriété</td></tr>
<tr><td>Mise à la terre</td><td>Prise de terre propre au logement, créable ou à reprendre</td><td>Terre généralement issue de l'immeuble</td></tr>
<tr><td>Cheminements</td><td>Combles, vide sanitaire, extérieur, dépendances</td><td>Plinthes, doublages, gaines existantes ; percements limités</td></tr>
<tr><td>Extérieur</td><td>Jardin, garage, portail, éclairage d'accès</td><td>Balcon ou terrasse, avec règles de copropriété</td></tr>
<tr><td>Borne de recharge</td><td>Circuit dédié depuis le tableau</td><td>Droit à la prise, information du syndic</td></tr>
</tbody></table></div>

<h2 id="engagements">Comment nous travaillons</h2>

<ul>
<li>Un devis écrit et détaillé avant tout démarrage, sans engagement.</li>
<li>Des coupures annoncées et limitées, planifiées avec vous.</li>
<li>La protection des lieux pendant les travaux et le nettoyage en fin de chantier.</li>
<li>Le repérage du tableau, pour que vous sachiez ce que protège chaque disjoncteur.</li>
<li>L'explication de ce qui a été fait, et de ce qui reste éventuellement à prévoir.</li>
</ul>
""",
    "faq": [
        ("Intervenez-vous en appartement et en copropriété ?",
         "<p>Oui, sur la partie privative du logement : tableau, circuits, appareillages. Les "
         "colonnes montantes et les installations des parties communes relèvent de la "
         "copropriété et de son syndic.</p>"),
        ("Faut-il vider le logement pendant les travaux ?",
         "<p>Non pour un remplacement de tableau ou une intervention ciblée. Pour une "
         "rénovation complète avec saignées, un logement libéré permet de travailler plus vite "
         "et de limiter la gêne, mais une réalisation en site occupé reste possible, par "
         "étapes.</p>"),
        ("Puis-je fournir moi-même le matériel ?",
         "<p>C'est possible pour l'appareillage visible et les luminaires. Pour le matériel de "
         "protection — disjoncteurs, différentiels, tableau — la fourniture par le "
         "professionnel est préférable : le choix dépend de caractéristiques techniques "
         "précises, et la responsabilité sur le fonctionnement du matériel installé est "
         "engagée.</p>"),
        ("Travaillez-vous avec les assurances en cas de sinistre ?",
         "<p>À la suite d'un dégât des eaux, d'un incendie ou d'un épisode de surtension, un "
         "constat de l'état de l'installation peut être établi et transmis à votre assureur. "
         "La prise en charge relève ensuite de votre contrat.</p>"),
        ("Proposez-vous des interventions en soirée ou le week-end ?",
         "<p>Les situations urgentes sont traitées en priorité. Les interventions réalisées en "
         "dehors des horaires habituels font l'objet de conditions tarifaires spécifiques, "
         "communiquées avant l'intervention.</p>"),
    ],
    "related": ["renovation-electrique", "mise-aux-normes-electrique", "diagnostic-electrique",
                "electricien-depannage", "borne-recharge"],
})

SERVICES.append({
    "slug": "electricien-entreprise",
    "path": "electricien-entreprise.html",
    "icon": "building",
    "category": "Pour qui",
    "card_desc": ("Commerces, bureaux, locaux d'activité : installations, maintenance et "
                  "obligations spécifiques."),
    "title": "Électricien pour entreprises et commerces | Electricien Richard",
    "desc": ("Électricien pour entreprises, commerces et locaux professionnels : "
             "installation, éclairage, tableaux divisionnaires, obligations des "
             "établissements recevant du public."),
    "h1": "Électricien pour entreprises, commerces et professionnels",
    "intro": ("En local professionnel, l'électricité ne se limite pas à la sécurité des "
              "personnes : la continuité de l'activité et les obligations réglementaires "
              "propres aux locaux de travail s'y ajoutent."),
    "service_type": "Travaux d'électricité pour professionnels",
    "quick": {
        "title": "Nos interventions en local professionnel",
        "answer": (
            "<p><strong>Installation et rénovation électrique de commerces, bureaux et locaux "
            "d'activité, éclairage, tableaux divisionnaires, alimentation d'équipements "
            "professionnels et remise en état lors d'un changement d'occupant.</strong></p>"
            "<p>Les établissements recevant du public sont soumis à des obligations "
            "complémentaires, notamment en matière d'éclairage de sécurité et de vérifications "
            "périodiques.</p>"),
        "facts": [
            ("Types de locaux", "Commerces, bureaux, ateliers, locaux techniques, cabinets"),
            ("Prestations", "Installation, rénovation, éclairage, tableaux divisionnaires, dépannage"),
            ("ERP", "Éclairage de sécurité et vérifications périodiques par organisme agréé"),
            ("Contrainte", "Limiter l'interruption d'activité : travaux planifiés ou hors horaires"),
            ("Locaux de travail", "Obligations de vérification à la charge de l'employeur"),
        ],
    },
    "body": """
<h2 id="besoins">Les besoins spécifiques des locaux professionnels</h2>

<h3>La continuité d'activité</h3>
<p>Une coupure a un coût direct. Les travaux sont donc planifiés en tenant compte des
horaires d'ouverture, avec des interventions possibles en dehors des périodes d'activité et
un séquencement qui limite les arrêts.</p>

<h3>Des puissances et des usages différents</h3>
<p>Équipements de production, froid commercial, informatique, éclairage de surface de vente :
les charges sont plus élevées et souvent permanentes. Le dimensionnement des circuits et la
répartition des protections en tiennent compte, de même que la nécessité d'isoler certains
équipements sensibles.</p>

<h3>L'éclairage</h3>
<p>En local de travail, l'éclairage répond à des exigences de niveau et d'uniformité liées à
l'activité exercée. En commerce s'y ajoute la dimension commerciale : mise en valeur des
produits, rendu des couleurs, confort du client.</p>

<h3>La reprise d'un local</h3>
<p>Lors d'un changement d'occupant, l'installation existante correspond rarement au nouvel
usage. Un examen préalable permet d'identifier ce qui est réutilisable et ce qui doit être
repris avant l'ouverture.</p>

<h2 id="obligations">Les obligations réglementaires</h2>

<h3>Établissements recevant du public</h3>
<p>Les ERP sont soumis à des règles de sécurité renforcées. Elles concernent notamment
l'éclairage de sécurité, permettant l'évacuation en cas de défaillance de l'éclairage
normal, les dispositifs de coupure d'urgence, et des vérifications périodiques réalisées par
un organisme agréé. Les exigences précises dépendent de la catégorie et du type de
l'établissement.</p>

<h3>Locaux de travail</h3>
<p>L'employeur est tenu de faire procéder à des vérifications périodiques des installations
électriques par une personne compétente, et de conserver les rapports correspondants. Ces
vérifications donnent lieu à des observations dont la levée relève de sa responsabilité.</p>

<h3>Ce que cela implique en pratique</h3>
<p>Les travaux réalisés doivent être documentés : schémas, repérage des tableaux, nature des
matériels installés. Ces éléments sont demandés lors des vérifications périodiques, et leur
absence complique considérablement les contrôles.</p>

<h2 id="prestations">Nos prestations pour les professionnels</h2>

<ul>
<li>Installation électrique complète de locaux neufs ou réaménagés.</li>
<li>Tableaux divisionnaires et reprise de la distribution.</li>
<li>Éclairage intérieur, éclairage de vitrine et éclairage extérieur.</li>
<li>Alimentation d'équipements professionnels sur circuits dédiés.</li>
<li>Prises de courant et alimentation de postes de travail.</li>
<li>Dépannage et recherche de panne en local d'activité.</li>
<li>Levée d'observations à la suite d'une vérification périodique.</li>
<li>Points de recharge pour flottes et parkings de personnel.</li>
</ul>

<h2 id="humides">Locaux particuliers</h2>

<p>Certains environnements professionnels imposent des matériels spécifiques : locaux
humides, chambres froides, ateliers poussiéreux, cuisines professionnelles, caves et chais.
L'indice de protection, la résistance mécanique et la nature des protections y sont
déterminants. Une installation réalisée avec du matériel d'intérieur ordinaire s'y dégrade
en quelques années.</p>
""",
    "faq": [
        ("Quelles sont les obligations électriques d'un commerce ?",
         "<p>Elles dépendent du classement de l'établissement. Un commerce recevant du public "
         "est soumis à des exigences relatives à l'éclairage de sécurité, aux dispositifs de "
         "coupure et à des vérifications périodiques par un organisme agréé. Par ailleurs, en "
         "tant que lieu de travail, il relève des obligations de vérification incombant à "
         "l'employeur.</p>"),
        ("Pouvez-vous intervenir en dehors des heures d'ouverture ?",
         "<p>Oui. Les travaux impliquant une coupure sont généralement planifiés en dehors des "
         "périodes d'activité afin de limiter la gêne. Les conditions applicables à ces "
         "interventions sont précisées au devis.</p>"),
        ("Que faire après une vérification périodique signalant des observations ?",
         "<p>Les observations doivent être levées, ce qui suppose de comprendre précisément ce "
         "qui est visé. Le rapport est examiné, les travaux nécessaires sont chiffrés, puis "
         "réalisés et documentés afin que la levée puisse être constatée lors du contrôle "
         "suivant.</p>"),
        ("Faut-il un tableau divisionnaire dans un local d'activité ?",
         "<p>C'est souvent la solution la plus rationnelle lorsque les zones à alimenter sont "
         "éloignées du tableau principal ou lorsque des équipements spécifiques nécessitent "
         "des protections dédiées. Cela limite les longueurs de câbles et facilite les "
         "interventions ultérieures.</p>"),
        ("Réalisez-vous la maintenance des installations ?",
         "<p>Des interventions de contrôle et d'entretien peuvent être organisées : "
         "vérification des serrages, contrôle des protections, état des tableaux, examen des "
         "points sensibles. Les modalités sont définies selon la nature du local et de "
         "l'activité.</p>"),
    ],
    "related": ["installation-electrique", "eclairage", "tableau-electrique",
                "electricien-depannage", "borne-recharge"],
})

SERVICES.append({
    "slug": "tarifs",
    "path": "tarifs.html",
    "icon": "euro",
    "category": "Informations",
    "nav_label": "Tarifs",
    "card_desc": ("Comment se construit le prix d'une intervention électrique et ce qui le "
                  "fait varier."),
    "title": "Tarifs électricien — Comment se construit un prix | Electricien Richard",
    "desc": ("Tarifs d'un électricien : composition d'un prix, facteurs de variation, "
             "différence entre devis et estimation, et ce que doit contenir un devis "
             "sérieux."),
    "h1": "Tarifs d'un électricien : comment se construit un prix",
    "intro": ("Cette page n'affiche pas de grille tarifaire, et c'est volontaire : un prix "
              "annoncé sans avoir vu l'installation n'engage personne et induit en erreur. "
              "Elle explique en revanche précisément ce qui compose un prix et ce qui le "
              "fait varier."),
    "service_type": "Devis et tarification de travaux électriques",
    "quick": {
        "title": "Comment est calculé le prix d'une intervention",
        "answer": (
            "<p><strong>Un prix se compose de la main-d'œuvre, des fournitures, du "
            "déplacement et, le cas échéant, des sujétions particulières du chantier.</strong> "
            "Sa part variable dépend surtout de l'état de l'existant et de l'accessibilité.</p>"
            "<p>Aucun tarif n'est affiché ici tant qu'il ne peut pas être garanti : un chiffrage "
            "fiable suppose d'avoir vu l'installation. Le devis, lui, est gratuit et sans "
            "engagement.</p>"),
        "facts": [
            ("Composantes", "Main-d'œuvre, fournitures, déplacement, sujétions du chantier"),
            ("Facteurs de variation", "État de l'existant, accessibilité, nature du bâti, urgence"),
            ("Devis", "Écrit, détaillé, gratuit et sans engagement"),
            ("Horaires particuliers", "Conditions spécifiques annoncées avant l'intervention"),
            ("TVA", "Taux réduit possible sur certains travaux dans les logements de plus de deux ans"),
        ],
    },
    "body": """
<h2 id="composantes">Ce qui compose le prix</h2>

<h3>La main-d'œuvre</h3>
<p>C'est la part la plus importante sur la plupart des chantiers. Elle dépend du temps réel
nécessaire, lequel est fortement influencé par l'accessibilité : passer un câble dans une
gaine existante et le passer dans un mur en pierre de soixante centimètres ne représentent
pas le même travail.</p>

<h3>Les fournitures</h3>
<p>Tableau, protections, câbles, appareillage, luminaires. Les écarts de prix entre gammes
sont réels, en particulier sur l'appareillage visible. Le devis distingue les fournitures de
la pose, ce qui permet d'arbitrer sur ce poste sans remettre en cause la prestation.</p>

<h3>Le déplacement</h3>
<p>Il dépend de la distance et du type d'intervention. Sur un chantier planifié, il est
généralement intégré au devis global.</p>

<h3>Les sujétions du chantier</h3>
<p>Travail en hauteur, local occupé, contraintes horaires, évacuation de gravats, reprise de
finitions, coordination avec d'autres corps d'état : ces éléments s'ajoutent au temps de
pose proprement dit.</p>

<h2 id="variation">Pourquoi deux devis peuvent être très différents</h2>

<p>Pour un même intitulé — « remplacement du tableau », par exemple — deux devis peuvent
recouvrir des prestations très inégales. Les écarts proviennent le plus souvent des points
suivants :</p>

<ul>
<li>le nombre et le type de dispositifs différentiels prévus ;</li>
<li>la reprise ou non de la mise à la terre ;</li>
<li>la présence ou non du repérage des circuits ;</li>
<li>la reprise des connexions existantes ou leur simple raccordement en l'état ;</li>
<li>la gamme du matériel installé ;</li>
<li>l'inclusion ou non des reprises de finitions.</li>
</ul>

<p>Comparer deux devis suppose donc de comparer leur contenu, pas seulement leur total.</p>

<h2 id="devis">Ce que doit contenir un devis sérieux</h2>

<ul>
<li>L'identification complète de l'entreprise et ses assurances.</li>
<li>Le détail des prestations, ligne par ligne, avec les quantités.</li>
<li>La distinction entre fournitures et main-d'œuvre.</li>
<li>Les caractéristiques du matériel prévu, et non une simple mention générique.</li>
<li>Le prix hors taxes, le taux de TVA appliqué et le prix toutes taxes comprises.</li>
<li>La durée de validité de l'offre et les modalités de règlement.</li>
<li>Le délai d'exécution envisagé.</li>
</ul>

<h2 id="tva">TVA applicable</h2>

<p>Les travaux réalisés dans un logement achevé depuis plus de deux ans peuvent, selon leur
nature, relever d'un taux réduit de TVA. Les travaux dans un logement neuf ou assimilé
relèvent du taux normal. Le taux applicable dépend de la nature exacte des travaux et de la
situation du logement : il est indiqué sur le devis, avec l'attestation à compléter lorsque
le taux réduit s'applique.</p>

<h2 id="urgence">Interventions en horaires particuliers</h2>

<p>Une intervention réalisée en soirée, la nuit, un week-end ou un jour férié fait l'objet de
conditions tarifaires spécifiques, comme dans l'ensemble du secteur. Ces conditions sont
communiquées avant l'intervention, afin qu'aucune surprise n'apparaisse sur la facture.</p>

<div class="callout callout--safe"><strong>Un principe simple</strong><p>Aucun travaux n'est
engagé sans accord préalable. Si une intervention de dépannage révèle des travaux
complémentaires, ceux-ci font l'objet d'un devis distinct que vous êtes libre d'accepter ou
non.</p></div>
""",
    "faq": [
        ("Le devis est-il payant ?",
         "<p>Non, l'établissement d'un devis est gratuit et sans engagement. Lorsqu'une étude "
         "technique approfondie est nécessaire — recherche de panne complexe, examen détaillé "
         "d'une installation existante — les conditions sont annoncées avant l'intervention.</p>"),
        ("Pourquoi n'affichez-vous pas de grille de tarifs ?",
         "<p>Parce qu'un prix annoncé sans avoir vu l'installation n'a pas de valeur. Deux "
         "remplacements de tableau peuvent varier du simple au double selon l'état des "
         "circuits, la nécessité de reprendre la terre et l'accessibilité. Afficher un prix "
         "d'appel qui ne serait pas tenu ne rendrait service à personne.</p>"),
        ("Comment obtenir une estimation rapidement ?",
         "<p>En décrivant précisément la situation lors de la prise de contact : type de "
         "logement, âge de l'installation, nature du tableau, travaux envisagés. Des photos du "
         "tableau et de la zone concernée permettent souvent de donner un premier ordre de "
         "grandeur avant la visite.</p>"),
        ("Faut-il verser un acompte ?",
         "<p>Un acompte peut être demandé pour les chantiers impliquant une commande "
         "importante de fournitures. Son montant et ses modalités figurent alors sur le devis, "
         "et il est encaissé après signature.</p>"),
        ("Quel taux de TVA s'applique à des travaux électriques ?",
         "<p>Dans un logement achevé depuis plus de deux ans, certains travaux d'amélioration "
         "peuvent bénéficier d'un taux réduit. Dans un logement neuf, le taux normal "
         "s'applique. Le taux retenu est indiqué sur le devis, et une attestation est à "
         "compléter par le client lorsque le taux réduit est applicable.</p>"),
    ],
    "related": ["devis-electricien", "renovation-electrique", "tableau-electrique",
                "electricien-depannage", "contact"],
})
