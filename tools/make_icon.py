#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genere assets/images/apple-touch-icon.png (180x180) sans dependance externe.
A relancer uniquement si l'identite visuelle change.
"""
import os, zlib, struct

SIZE = 180
DARK = (17, 24, 39)
YELLOW = (250, 204, 21)
# Contour de l'eclair, exprime dans le repere 40x40 du logo SVG
BOLT = [(22.5, 8), (14, 22), (19.2, 22), (17.5, 32), (27, 17.5), (21.6, 17.5)]
SCALE = SIZE / 40.0
POLY = [(x * SCALE, y * SCALE) for x, y in BOLT]


def inside(px, py, poly):
    hit = False
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        if (y1 > py) != (y2 > py):
            xint = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
            if px < xint:
                hit = not hit
    return hit


def build():
    rows = []
    for y in range(SIZE):
        row = bytearray([0])          # filtre "None"
        for x in range(SIZE):
            # anti-aliasing simple : 2x2 sous-echantillons
            cover = sum(inside(x + dx, y + dy, POLY)
                        for dx in (0.25, 0.75) for dy in (0.25, 0.75)) / 4.0
            r = round(DARK[0] + (YELLOW[0] - DARK[0]) * cover)
            g = round(DARK[1] + (YELLOW[1] - DARK[1]) * cover)
            b = round(DARK[2] + (YELLOW[2] - DARK[2]) * cover)
            row += bytes((r, g, b))
        rows.append(bytes(row))
    raw = b"".join(rows)

    def chunk(tag, data):
        return (struct.pack(">I", len(data)) + tag + data
                + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF))

    png = (b"\x89PNG\r\n\x1a\n"
           + chunk(b"IHDR", struct.pack(">IIBBBBB", SIZE, SIZE, 8, 2, 0, 0, 0))
           + chunk(b"IDAT", zlib.compress(raw, 9))
           + chunk(b"IEND", b""))

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                       "assets", "images", "apple-touch-icon.png")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "wb") as fh:
        fh.write(png)
    print("apple-touch-icon.png genere (%d octets)" % len(png))




# --------------------------------------------------------------------------
# Image Open Graph par defaut (1200x630).
# Visuel de marque neutre, sans texte fictif ni photo simulee.
# A remplacer par un visuel definitif (logo + baseline) lorsqu'il existera.
# --------------------------------------------------------------------------
OG_W, OG_H = 1200, 630


def build_og():
    bolt_scale = 11.0
    ox, oy = 90, 60
    poly = [(x * bolt_scale + ox, y * bolt_scale + oy) for x, y in BOLT]

    rows = []
    for y in range(OG_H):
        row = bytearray([0])
        for x in range(OG_W):
            # fond degrade sombre
            t = (x / OG_W) * 0.5 + (y / OG_H) * 0.5
            r = round(17 + 6 * t)
            g = round(24 + 8 * t)
            b = round(39 + 12 * t)
            # bandes jaunes discretes en bas a droite
            if x > OG_W - 260 and (x + y) % 46 < 10:
                r, g, b = 202, 138, 4
            cover = sum(inside(x + dx, y + dy, poly)
                        for dx in (0.25, 0.75) for dy in (0.25, 0.75)) / 4.0
            if cover:
                r = round(r + (YELLOW[0] - r) * cover)
                g = round(g + (YELLOW[1] - g) * cover)
                b = round(b + (YELLOW[2] - b) * cover)
            row += bytes((r, g, b))
        rows.append(bytes(row))
    raw = b"".join(rows)

    def chunk(tag, data):
        return (struct.pack(">I", len(data)) + tag + data
                + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF))

    png = (b"\x89PNG\r\n\x1a\n"
           + chunk(b"IHDR", struct.pack(">IIBBBBB", OG_W, OG_H, 8, 2, 0, 0, 0))
           + chunk(b"IDAT", zlib.compress(raw, 9))
           + chunk(b"IEND", b""))
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                       "assets", "images", "og", "electricien-richard-og.png")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "wb") as fh:
        fh.write(png)
    print("image Open Graph generee (%d octets)" % len(png))


if __name__ == "__main__":
    build()
    build_og()
