# Photos

Fichier **généré automatiquement** à chaque build (`python3 tools/build.py`).

## Comment ajouter une photo

```bash
# 1. déposer la photo dans photos-inbox/ en la nommant d'après la clé
#    de l'emplacement (extension et casse indifférentes)
cp ma-photo.jpg photos-inbox/svc_eclairage.jpg

# 2. intégration : conversion WebP, variantes responsives, mise en place
python3 tools/photos.py

# 3. régénération du site
python3 tools/build.py
```

`python3 tools/photos.py --list` affiche toutes les clés disponibles.

Le script corrige l'orientation, **supprime les métadonnées EXIF (y compris les coordonnées GPS)**, redimensionne à 1600 px, convertit en WebP et génère les variantes 480 / 800 / 1200 / 1600 px utilisées par `srcset`.

Rien d'autre n'est à modifier : les dimensions affichées sont lues dans le fichier livré, donc le ratio est toujours exact et aucun décalage de mise en page ne se produit.

## 1. Photos transmises — fichiers à déposer (6)

Ces photos ont été analysées et affectées. **Une photo = un seul emplacement**, aucune n'est réutilisée ailleurs sur le site.

| Clé (nom du fichier) | Photo | Emplacement |
|---|---|---|
| `hero` | Cuisine grise, plan de travail bois : pose d'un ruban LED sous les meubles hauts | Accueil — image principale |
| `svc_eclairage` | Chambre : technicien sur escabeau posant un ruban LED en corniche de plafond | eclairage.html |
| `svc_luminaire` | Salon : technicien casqué remplaçant l'ampoule d'une suspension noire | luminaire.html |
| `svc_prise-electrique` | Séjour : technicien à genoux posant une prise, bâche de protection et outils au sol | prise-electrique.html |
| `svc_disjoncteur` | Coffret extérieur : intervention sur le disjoncteur de branchement sous compteur Linky | disjoncteur.html |
| `svc_interrupteur` | Rangée de boîtes d'encastrement ouvertes, raccordement des prises et interrupteurs | interrupteur.html |

## 2. Emplacements encore libres (62)

Les sections concernées restent masquées tant qu'aucune photo n'y figure : le site n'affiche jamais d'emplacement vide au visiteur.

- [ ] `assets/images/blog/comment-choisir-un-electricien.webp`
      → Comment choisir un électricien ?
- [ ] `assets/images/blog/difference-disjoncteur-differentiel.webp`
      → Quelle différence entre un disjoncteur et un différentiel ?
- [ ] `assets/images/blog/electricite-habitat-ancien-bretagne-pays-de-la-loire.webp`
      → L'électricité dans l'habitat ancien de Bretagne et des Pays de la Loire
- [ ] `assets/images/blog/installer-une-borne-de-recharge-ce-qu-il-faut-savoir.webp`
      → Installer une borne de recharge : ce qu'il faut savoir
- [ ] `assets/images/blog/norme-nf-c-15-100-points-essentiels.webp`
      → La norme NF C 15-100 : les points essentiels
- [ ] `assets/images/blog/pourquoi-mon-disjoncteur-saute.webp`
      → Pourquoi mon disjoncteur saute ?
- [ ] `assets/images/blog/preparer-sa-renovation-electrique.webp`
      → Comment préparer une rénovation électrique
- [ ] `assets/images/blog/prix-renovation-electrique-maison.webp`
      → Quel prix pour refaire l'installation électrique d'une maison ?
- [ ] `assets/images/blog/quand-changer-son-tableau-electrique.webp`
      → Quand faut-il changer son tableau électrique ?
- [ ] `assets/images/blog/que-faire-en-cas-de-panne-electrique.webp`
      → Que faire en cas de panne électrique ?
- [ ] `assets/images/blog/reconnaitre-une-installation-electrique-dangereuse.webp`
      → Comment reconnaître une installation électrique dangereuse
- [ ] `assets/images/bornes/borne-recharge-installation-maison.webp`
      → Borne de recharge pour véhicule électrique installée en maison individuelle
- [ ] `assets/images/depannage/court-circuit-connexion-endommagee.webp`
      → Connexion électrique endommagée à l'origine d'un défaut
- [ ] `assets/images/depannage/depannage-electrique-diagnostic-circuit.webp`
      → Contrôle d'un circuit électrique lors d'un dépannage
- [ ] `assets/images/depannage/depannage-electrique-urgence-tableau.webp`
      → Intervention sur un tableau électrique lors d'un dépannage
- [ ] `assets/images/depannage/panne-electrique-verification-tableau.webp`
      → Vérification des protections d'un tableau après une panne
- [ ] `assets/images/depannage/recherche-panne-electrique-mesure.webp`
      → Recherche de panne électrique avec appareil de mesure
- [ ] `assets/images/electricien/electricien-richard-vehicule-intervention.webp`
      → Véhicule d'intervention d'Electricien Richard
- [ ] `assets/images/electricien/electricien-travaux-electriques.webp`
      → Électricien réalisant des travaux électriques dans un logement
- [ ] `assets/images/installation/installation-electrique-neuve-tableau.webp`
      → Installation électrique neuve en cours de raccordement
- [ ] `assets/images/installation/raccordement-electrique-vmc.webp`
      → Raccordement électrique d'un caisson de VMC
- [ ] `assets/images/interventions/devis-travaux-electriques.webp`
      → Établissement d'un devis de travaux électriques
- [ ] `assets/images/interventions/diagnostic-electrique-controle-installation.webp`
      → Contrôle d'une installation électrique lors d'un diagnostic
- [ ] `assets/images/interventions/electricien-intervention-logement.webp`
      → Intervention électrique dans un logement
- [ ] `assets/images/interventions/electricien-local-professionnel.webp`
      → Travaux électriques dans un local professionnel
- [ ] `assets/images/renovation/mise-aux-normes-electrique-tableau.webp`
      → Mise en sécurité d'une installation électrique ancienne
- [ ] `assets/images/renovation/renovation-electrique-passage-circuits.webp`
      → PHOTO ATTENDUE : passage de gaines ou saignées en rénovation
- [ ] `assets/images/tableau-electrique/remplacement-tableau-electrique-chantier.webp`
      → PHOTO ATTENDUE : tableau électrique ouvert pendant l'intervention
- [ ] `assets/images/tableau-electrique/remplacement-tableau-electrique.webp`
      → Remplacement d'un tableau électrique
- [ ] `assets/images/zones/electricien-ancenis-intervention.webp`
      → Intervention électrique à Ancenis-Saint-Géréon
- [ ] `assets/images/zones/electricien-angers-intervention.webp`
      → Intervention électrique à Angers
- [ ] `assets/images/zones/electricien-auray-intervention.webp`
      → Intervention électrique à Auray
- [ ] `assets/images/zones/electricien-brest-intervention.webp`
      → Intervention électrique à Brest
- [ ] `assets/images/zones/electricien-cholet-intervention.webp`
      → Intervention électrique à Cholet
- [ ] `assets/images/zones/electricien-concarneau-intervention.webp`
      → Intervention électrique à Concarneau
- [ ] `assets/images/zones/electricien-cotes-d-armor-intervention.webp`
      → Intervention électrique en Côtes-d'Armor
- [ ] `assets/images/zones/electricien-dinan-intervention.webp`
      → Intervention électrique à Dinan
- [ ] `assets/images/zones/electricien-finistere-intervention.webp`
      → Intervention électrique en Finistère
- [ ] `assets/images/zones/electricien-fougeres-intervention.webp`
      → Intervention électrique à Fougères
- [ ] `assets/images/zones/electricien-guingamp-intervention.webp`
      → Intervention électrique à Guingamp
- [ ] `assets/images/zones/electricien-ille-et-vilaine-intervention.webp`
      → Intervention électrique en Ille-et-Vilaine
- [ ] `assets/images/zones/electricien-lamballe-intervention.webp`
      → Intervention électrique à Lamballe-Armor
- [ ] `assets/images/zones/electricien-lannion-intervention.webp`
      → Intervention électrique à Lannion
- [ ] `assets/images/zones/electricien-loire-atlantique-intervention.webp`
      → Intervention électrique en Loire-Atlantique
- [ ] `assets/images/zones/electricien-lorient-intervention.webp`
      → Intervention électrique à Lorient
- [ ] `assets/images/zones/electricien-maine-et-loire-intervention.webp`
      → Intervention électrique en Maine-et-Loire
- [ ] `assets/images/zones/electricien-morbihan-intervention.webp`
      → Intervention électrique en Morbihan
- [ ] `assets/images/zones/electricien-morlaix-intervention.webp`
      → Intervention électrique à Morlaix
- [ ] `assets/images/zones/electricien-nantes-intervention.webp`
      → Intervention électrique à Nantes
- [ ] `assets/images/zones/electricien-ploermel-intervention.webp`
      → Intervention électrique à Ploërmel
- [ ] `assets/images/zones/electricien-pontivy-intervention.webp`
      → Intervention électrique à Pontivy
- [ ] `assets/images/zones/electricien-quimper-intervention.webp`
      → Intervention électrique à Quimper
- [ ] `assets/images/zones/electricien-redon-intervention.webp`
      → Intervention électrique à Redon
- [ ] `assets/images/zones/electricien-rennes-intervention.webp`
      → Intervention électrique à Rennes
- [ ] `assets/images/zones/electricien-reze-intervention.webp`
      → Intervention électrique à Rezé
- [ ] `assets/images/zones/electricien-saint-brieuc-intervention.webp`
      → Intervention électrique à Saint-Brieuc
- [ ] `assets/images/zones/electricien-saint-herblain-intervention.webp`
      → Intervention électrique à Saint-Herblain
- [ ] `assets/images/zones/electricien-saint-malo-intervention.webp`
      → Intervention électrique à Saint-Malo
- [ ] `assets/images/zones/electricien-saint-nazaire-intervention.webp`
      → Intervention électrique à Saint-Nazaire
- [ ] `assets/images/zones/electricien-saumur-intervention.webp`
      → Intervention électrique à Saumur
- [ ] `assets/images/zones/electricien-vannes-intervention.webp`
      → Intervention électrique à Vannes
- [ ] `assets/images/zones/electricien-vitre-intervention.webp`
      → Intervention électrique à Vitré
