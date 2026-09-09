#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Integration des photos dans le site.

Usage
-----
    python3 tools/photos.py --list      # emplacements et etat de chacun
    python3 tools/photos.py             # traite le contenu de photos-inbox/

Fonctionnement
--------------
1. Deposer les photos dans le dossier `photos-inbox/` a la racine du projet.
   Le nom du fichier doit contenir la CLE de l'emplacement, par exemple :
       hero.jpg
       svc_disjoncteur.png
       svc_eclairage.jpeg
   L'extension et la casse n'ont pas d'importance ; un nom du type
   `photo hero (1).jpg` fonctionne aussi.
2. Lancer `python3 tools/photos.py`. Le script :
   - corrige l'orientation EXIF,
   - supprime les metadonnees (donnees GPS comprises),
   - redimensionne a 1600 px de large maximum,
   - convertit en WebP (qualite 82),
   - genere les variantes responsives 480 / 800 / 1200 / 1600,
   - ecrit le tout au chemin attendu par le manifeste,
   - deplace le fichier source dans photos-inbox/traitees/.
3. Lancer `python3 tools/build.py` pour regenerer le site.

Aucune photo n'est modifiee dans son contenu : seuls le format, la taille et
les metadonnees changent.
"""

import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import images as IMG   # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
INBOX = os.path.join(ROOT, "photos-inbox")
DONE = os.path.join(INBOX, "traitees")
LARGEURS = (480, 800, 1200, 1600)
QUALITE = 82


def slots():
    """Tous les emplacements du manifeste, y compris zones et blog."""
    from content.zones import DEPARTEMENTS
    from content.blog import ARTICLES
    out = dict(IMG.IMAGES)
    for dep in DEPARTEMENTS:
        out["dept_" + dep["slug"]] = IMG.dept_image(dep["slug"], dep["name"])
        for city in dep["cities"]:
            out["ville_" + city["slug"]] = IMG.city_image(city["slug"], city["name"])
    for art in ARTICLES:
        out["blog_" + art["slug"]] = IMG.blog_image(art)
    return out


def lister():
    tous = slots()
    presents = [(k, v) for k, v in tous.items() if os.path.exists(os.path.join(ROOT, v["file"]))]
    manquants = [(k, v) for k, v in tous.items() if not os.path.exists(os.path.join(ROOT, v["file"]))]
    print("PHOTOS EN PLACE (%d)" % len(presents))
    for k, v in sorted(presents):
        print("  %-34s %s" % (k, v["file"]))
    print()
    print("EMPLACEMENTS LIBRES (%d)" % len(manquants))
    for k, v in sorted(manquants):
        sujet = v.get("sujet") or v["alt"]
        print("  %-34s %s" % (k, sujet[:78]))
        print("  %-34s -> %s" % ("", v["file"]))
    print()
    print("Deposer un fichier nomme <cle>.jpg dans photos-inbox/ puis relancer :")
    print("    python3 tools/photos.py")


def cle_depuis_nom(nom, cles):
    """Retrouve la cle d'emplacement contenue dans le nom de fichier."""
    base = os.path.splitext(os.path.basename(nom))[0].lower()
    base = re.sub(r"[^a-z0-9_-]+", "-", base)
    # correspondance exacte d'abord, puis la cle la plus longue contenue
    if base in cles:
        return base
    candidats = [c for c in cles if c.lower() in base]
    return max(candidats, key=len) if candidats else None


def traiter(source, cible):
    from PIL import Image, ImageOps

    img = Image.open(source)
    img = ImageOps.exif_transpose(img)          # orientation depuis l'EXIF
    if img.mode not in ("RGB", "L"):
        img = img.convert("RGB")

    dest = os.path.join(ROOT, cible)
    os.makedirs(os.path.dirname(dest), exist_ok=True)

    largeur_max = min(1600, img.width)
    principal = img if img.width <= largeur_max else img.resize(
        (largeur_max, round(img.height * largeur_max / img.width)), Image.LANCZOS)
    # save() sans exif ni icc : les metadonnees (dont GPS) ne sont pas reprises
    principal.save(dest, "WEBP", quality=QUALITE, method=6)
    ecrits = [(os.path.relpath(dest, ROOT), principal.size, os.path.getsize(dest))]

    base, ext = os.path.splitext(dest)
    for w in LARGEURS:
        if w >= img.width:
            continue
        variante = "%s-%dw%s" % (base, w, ext)
        red = img.resize((w, round(img.height * w / img.width)), Image.LANCZOS)
        red.save(variante, "WEBP", quality=QUALITE, method=6)
        ecrits.append((os.path.relpath(variante, ROOT), red.size, os.path.getsize(variante)))
    return ecrits


def main():
    if "--list" in sys.argv:
        lister()
        return 0

    os.makedirs(INBOX, exist_ok=True)
    fichiers = [f for f in sorted(os.listdir(INBOX))
                if os.path.isfile(os.path.join(INBOX, f)) and not f.startswith(".")]
    if not fichiers:
        print("photos-inbox/ est vide.")
        print("Deposez-y vos photos (nommees d'apres la cle de l'emplacement),")
        print("puis relancez. Pour voir les cles : python3 tools/photos.py --list")
        return 0

    tous = slots()
    traites, ignores = 0, []
    for f in fichiers:
        src = os.path.join(INBOX, f)
        cle = cle_depuis_nom(f, tous)
        if not cle:
            ignores.append(f)
            continue
        print("%s  ->  %s" % (f, cle))
        try:
            for chemin, (w, h), poids in traiter(src, tous[cle]["file"]):
                print("    %-72s %4dx%-4d %6.0f Ko" % (chemin, w, h, poids / 1024))
        except Exception as exc:                       # noqa: BLE001
            print("    ECHEC : %s" % exc)
            continue
        os.makedirs(DONE, exist_ok=True)
        shutil.move(src, os.path.join(DONE, f))
        traites += 1

    print()
    print("%d photo(s) integree(s)." % traites)
    if ignores:
        print("Non reconnues (le nom ne contient aucune cle d'emplacement) :")
        for f in ignores:
            print("   - %s" % f)
        print("   Voir les cles disponibles : python3 tools/photos.py --list")
    if traites:
        print("Verifier le texte alternatif dans tools/content/images.py,")
        print("puis relancer : python3 tools/build.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
