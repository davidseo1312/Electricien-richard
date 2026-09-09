# Dossier de dépôt des photos

Déposez ici les photos à intégrer au site, en nommant chaque fichier d'après la
**clé** de son emplacement — par exemple `svc_eclairage.jpg`, `hero.png`.

Pour voir toutes les clés disponibles :

```bash
python3 tools/photos.py --list
```

Puis :

```bash
python3 tools/photos.py     # conversion WebP + variantes + mise en place
python3 tools/build.py      # régénération du site
```

Les fichiers traités sont déplacés dans `photos-inbox/traitees/`.
Formats acceptés : JPEG, PNG, WebP, HEIC (selon la machine), TIFF.
