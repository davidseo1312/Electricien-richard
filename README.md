# electricien-richard.fr

Site statique d'Electricien Richard — artisan électricien intervenant dans six
départements de Bretagne et des Pays de la Loire.

Le site est **généré** : le contenu vit dans des fichiers Python (`tools/content/`),
le HTML statique est produit à la racine du dépôt. Aucun framework, aucune
dépendance à installer.

---

## Démarrage

```bash
python3 tools/build.py          # génère l'ensemble du site
python3 -m http.server 8000     # aperçu sur http://localhost:8000
```

Le build échoue si un contrôle ne passe pas : périmètre géographique, titles ou
meta descriptions dupliqués, H1 multiples, liens internes cassés.

---

## À COMPLÉTER AVANT LA MISE EN LIGNE

Ces informations ne peuvent pas être inventées. Tant qu'elles ne sont pas
renseignées, elles ne sont **pas** injectées dans les données structurées, afin de
ne jamais déclarer de fausse information à Google.

Tout se trouve dans **`tools/content/site.py`** :

| Champ | Description |
|---|---|
| `phone_display` / `phone_tel` | ✅ Renseigné : **02 20 06 00 75** (lien `tel:0220060075`, `+33220060075` en JSON-LD). |
| `email` | ⚠️ `contact@electricien-richard.fr` n'existe pas encore : créer la boîte, puis passer `email_is_placeholder` à `False`. |
| `address` | Laissé à `None` **volontairement** — voir « Siège social et SEO local » ci-dessous. |
| `legal` | ✅ Renseigné (ASSOUL BILAL, SIREN, SIRET, RCS, siège). Alimente **uniquement** la page mentions légales. Reste à compléter : TVA intracommunautaire, assurances, hébergeur, médiateur. |
| `geo` | Coordonnées GPS réelles de l'établissement (facultatif). |
| `opening_hours` | Horaires réels. `None` = aucun horaire affiché ni déclaré. |
| `assurance`, `hebergeur` | Mentions légales : assureur + n° de police (RC pro et décennale), et identité de l'hébergeur. |
| `social` | URL des profils réellement existants. |
| `form_action` | Endpoint du formulaire (Formspree, Netlify Forms, script serveur…). Tant qu'il vaut `None`, le formulaire bascule sur un envoi par messagerie afin de rester fonctionnel. |

Après modification : `python3 tools/build.py`.

### Siège social et SEO local — décision technique

Le siège social (1 rue Albert Simonin, 92400 Courbevoie) figure dans les **mentions
légales**, comme la loi l'impose. Il n'est en revanche **pas** déclaré comme adresse du
`LocalBusiness` dans les données structurées, et `address` reste donc à `None`.

Raison : cette adresse se situe dans les Hauts-de-Seine, à plusieurs centaines de
kilomètres des six départements desservis. La déclarer comme adresse de l'établissement
enverrait à Google un signal de localisation en Île-de-France, en contradiction directe
avec le référencement local visé en Bretagne et en Pays de la Loire. Le site déclare donc
uniquement une zone desservie (`areaServed`), ce qui est le schéma prévu pour une
entreprise d'intervention sans point d'accueil du public.

Si un établissement secondaire est un jour ouvert dans l'un des six départements, c'est
**cette** adresse qu'il faudra renseigner dans `address` — et elle devra être strictement
identique à celle de la fiche Google Business Profile.

### Points à faire vérifier par l'exploitant

1. **Code APE 81.29A** — l'activité enregistrée (désinfection, désinsectisation,
   dératisation) ne correspond pas à des travaux d'électricité. Une mise à jour auprès de
   l'INSEE est à demander.
2. **Assurances** — la RC professionnelle et la décennale doivent couvrir explicitement
   l'activité d'électricien. Une police souscrite pour une activité de nettoyage ou de
   désinfection ne couvrirait pas des travaux électriques en cas de sinistre.
3. **Adresse e-mail** — `contact@electricien-richard.fr` doit être créée pour que le
   formulaire soit exploitable.

### Ce qui n'est volontairement pas présent

- **Aucun tarif chiffré.** La page `tarifs.html` explique la composition d'un prix
  sans annoncer de montant, faute de grille réelle.
- **Aucun avis client.** La section « Avis clients » de l'accueil affiche un état
  vide explicite. Aucun témoignage, note ou nom n'a été inventé.
- **Aucun délai d'intervention chiffré.** Aucune promesse de type « en 30 minutes »
  n'est faite, faute de pouvoir la garantir.
- **Aucune ancienneté ni chiffre d'activité.**

Ces éléments peuvent être ajoutés quand ils seront vérifiables.

---

## Ajouter des photos

Les cinq photos déjà transmises ont été analysées et **affectées à leurs pages** (hero,
galerie, éclairage, luminaire, prises, interrupteur, rénovation). Il ne manque que les
fichiers : voir la section 1 de `PHOTOS-A-FOURNIR.md` pour le chemin exact de chacune.

1. Consulter **`PHOTOS-A-FOURNIR.md`** — régénéré à chaque build, il liste les
   emplacements attendus avec leur chemin exact et le sujet de la photo.
2. Déposer le fichier au chemin indiqué.
3. Relancer `python3 tools/build.py`.

La photo remplace automatiquement l'emplacement neutre : aucune modification de
code n'est nécessaire.

**Variantes responsives** (recommandé) : en déposant à côté du fichier principal
`nom-480w.webp`, `nom-800w.webp`, `nom-1200w.webp`, `nom-1600w.webp`, un attribut
`srcset` complet est généré automatiquement.

**Textes alternatifs** : ils sont définis dans `tools/content/images.py`. Vérifier
qu'ils décrivent bien ce que montre la photo réellement fournie. Un `alt` décrit une
image, il ne contient pas une liste de mots-clés.

---

## Architecture

```
/                             pages de prestations (électricien.html, tableau-electrique.html…)
/zones/<département>/         page pilier départementale
/zones/<département>/<ville>/ page ville
/blog/                        index du blog
/blog/<catégorie>/            page catégorie
/blog/<catégorie>/<article>   article
/assets/css | js | images     ressources
/tools/                       générateur (non publié — exclu par robots.txt)
```

### Fichiers du générateur

| Fichier | Rôle |
|---|---|
| `tools/build.py` | Assemblage des pages, sitemap, robots, contrôles de build |
| `tools/render.py` | Layout, composants réutilisables, données structurées JSON-LD |
| `tools/content/site.py` | Configuration : identité, contact, périmètre |
| `tools/content/services.py` | 21 pages de prestations + blocs réutilisables |
| `tools/content/zones.py` | 6 départements et 27 villes, contenu rédigé par ville |
| `tools/content/blog.py` | 8 catégories et 11 articles |
| `tools/content/images.py` | Manifeste des photos (chemin, alt, dimensions, légende) |
| `tools/make_icon.py` | Génère le favicon tactile et l'image Open Graph |
| `tools/vendor-leaflet.sh` | Installe Leaflet en local (supprime la requête CDN) |

---

## Stratégie SEO / SEO local / GEO

**Silo thématique** — une page pilier `electricien.html` distribue vers les pages
spécialisées (dépannage, urgence, installation, rénovation, mise aux normes,
tableau, disjoncteur, court-circuit, prise, interrupteur, éclairage, luminaire,
borne de recharge, VMC, diagnostic, recherche de panne).

**Silo géographique** — hub `zones-d-intervention.html` → 6 pages départementales →
27 pages villes. Chaque page ville dispose d'un contenu propre : contexte bâti,
secteurs, besoins fréquents, FAQ locale. Aucune page n'est dupliquée d'une ville à
l'autre.

**Périmètre strict** — 22, 29, 35, 56, 44, 49. Le build **échoue** si un
département hors périmètre est introduit dans les données.

**GEO (Generative Engine Optimization)** — chaque page importante comporte :
un bloc « réponse rapide » en tête, une fiche d'identité factuelle
(Qui / Quoi / Où / Pour qui / Comment / Contact), des paragraphes courts, des
tableaux comparatifs, une FAQ avec `FAQPage`, et un maillage explicite entre
services et zones.

**Données structurées** — `Electrician`, `WebSite`, `WebPage`, `BreadcrumbList`,
`Service`, `FAQPage`, `Blog`, `BlogPosting`, reliées entre elles par `@id`.

**Performance** — CSS unique d'environ 25 Ko, JavaScript d'environ 4 Ko, aucune
dépendance de rendu. La carte Leaflet n'est chargée qu'à l'approche du viewport
(`IntersectionObserver`), les polices en `media="print"` puis basculées, les images
avec `width`/`height` explicites pour éviter tout décalage de mise en page.

---

## Carte interactive

Leaflet + OpenStreetMap, chargé uniquement lorsque la carte approche du viewport.
Si le chargement échoue, un message de repli s'affiche et le contenu textuel des
zones reste entièrement accessible.

Pour supprimer toute requête vers un CDN tiers :

```bash
bash tools/vendor-leaflet.sh && python3 tools/build.py
```

Le build détecte automatiquement la copie locale et l'utilise à la place du CDN.

---

## Mise en ligne

Le site est constitué de fichiers statiques : n'importe quel hébergement convient
(Netlify, Vercel, GitHub Pages, hébergement mutualisé).

1. Publier la racine du dépôt (hors `tools/`, exclu par `robots.txt`).
2. Activer HTTPS et la redirection `http → https`.
3. Vérifier que `/404.html` est bien servie (un `.htaccess` est fourni pour Apache).
4. Déclarer le site dans Google Search Console et y soumettre
   `https://electricien-richard.fr/sitemap.xml`.
5. Créer la fiche Google Business Profile avec **exactement** les mêmes nom,
   téléphone et adresse que ceux du site (cohérence NAP).

---

## Contrôles exécutés à chaque build

- périmètre géographique strictement limité aux 6 départements ;
- unicité des `<title>` et des meta descriptions ;
- un seul `<h1>` par page ;
- aucun lien interne cassé ;
- liste des photos manquantes régénérée.
