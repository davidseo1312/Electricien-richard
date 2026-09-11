#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genere les declinaisons rasterisees de la marque a partir des SVG sources.

    python3 tools/make-icons.py

Produit :
    assets/images/apple-touch-icon.png                    180x180
    assets/images/logo/electricien-richard-logo-512.png   512x512 (JSON-LD)
    assets/images/og/electricien-richard-og.png          1200x630 (partage)

A relancer uniquement si la marque change. Necessite Playwright + Chromium
(deja installes dans l'environnement de developpement) ; les PNG produits sont
versionnes, la regeneration n'est donc pas necessaire pour un build courant.
"""
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

OG_HTML = """
<!doctype html><html lang="fr"><head><meta charset="utf-8">
<style>
  @font-face{font-family:X;src:local("Arial")}
  *{margin:0;padding:0;box-sizing:border-box}
  body{width:1200px;height:630px;background:#111827;display:flex;flex-direction:column;
       justify-content:center;gap:34px;padding:0 88px;
       font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;overflow:hidden}
  .bar{position:absolute;top:0;left:0;right:0;height:14px;background:#FACC15}
  .row{display:flex;align-items:center;gap:34px}
  .row .mark{width:156px;flex:none;line-height:0}
  .row .mark svg{width:100%;height:auto;display:block}
  .l1{font-size:60px;font-weight:800;color:#fff;letter-spacing:1px;line-height:1}
  .l2{font-size:82px;font-weight:900;color:#FACC15;letter-spacing:.5px;line-height:1;margin-top:6px}
  .serv{font-size:28px;font-weight:700;color:#E2E8F0;letter-spacing:.2px;white-space:nowrap}
  .serv span{color:#FACC15;margin:0 12px}
  .zones{font-size:22px;font-weight:600;color:#94A3B8;white-space:nowrap}
  .tel{font-size:44px;font-weight:900;color:#fff}
  .tel svg{width:38px;height:38px;fill:#FACC15;vertical-align:-6px;margin-right:12px}
</style></head><body>
  <div class="bar"></div>
  <div class="row">
    <div class="mark">MARQUE</div>
    <div><div class="l1">ÉLECTRICIEN</div><div class="l2">RICHARD</div></div>
  </div>
  <div class="serv">Dépannage <span>•</span> Installation <span>•</span> Rénovation
    <span>•</span> Mise en sécurité</div>
  <div class="zones">Côtes-d'Armor · Finistère · Ille-et-Vilaine · Morbihan · Loire-Atlantique · Maine-et-Loire</div>
  <div class="tel"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M6.6 3h3.1l1.6 4-2 1.4a12.4 12.4 0 0 0 5.3 5.3l1.4-2 4 1.6v3.1c0 1-.8 1.8-1.8 1.6C10.9 17.4 6.6 13.1 5 5.8 4.8 4.8 5.6 3 6.6 3Z"/></svg>02 20 06 00 75</div>
</body></html>
"""


def main():
    from playwright.sync_api import sync_playwright

    # Les URL file:// ne sont pas resolues dans une page set_content :
    # le SVG est donc injecte directement dans le document.
    marque = open(os.path.join(ROOT, "assets/images/logo/"
                                     "electricien-richard-marque.svg"),
                  encoding="utf-8").read()
    favicon = open(os.path.join(ROOT, "favicon.svg"), encoding="utf-8").read()
    sorties = []

    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME)

        def rasterise(svg, taille, dest):
            pg = b.new_page(viewport={"width": taille, "height": taille})
            pg.set_content(
                '<body style="margin:0;width:%dpx;height:%dpx;background:#fff">'
                '<div style="width:%dpx;height:%dpx">%s</div></body>'
                % (taille, taille, taille, taille,
                   svg.replace("<svg", '<svg style="width:100%;height:100%;display:block"',
                               1)))
            pg.wait_for_timeout(250)
            chemin = os.path.join(ROOT, dest)
            os.makedirs(os.path.dirname(chemin), exist_ok=True)
            pg.screenshot(path=chemin, omit_background=False)
            pg.close()
            sorties.append((dest, os.path.getsize(chemin)))

        rasterise(favicon, 180, "assets/images/apple-touch-icon.png")
        rasterise(favicon, 512, "assets/images/logo/electricien-richard-logo-512.png")

        pg = b.new_page(viewport={"width": 1200, "height": 630})
        # Fond sombre : la marque doit passer en version inversee
        pg.set_content(OG_HTML.replace("MARQUE", marque.replace("#111827", "#FFFFFF")))
        pg.wait_for_timeout(400)
        dest = "assets/images/og/electricien-richard-og.png"
        chemin = os.path.join(ROOT, dest)
        os.makedirs(os.path.dirname(chemin), exist_ok=True)
        pg.screenshot(path=chemin)
        sorties.append((dest, os.path.getsize(chemin)))
        b.close()

    for d, poids in sorties:
        print("  %-58s %6.0f Ko" % (d, poids / 1024))


if __name__ == "__main__":
    sys.exit(main())
