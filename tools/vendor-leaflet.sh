#!/usr/bin/env bash
# Telecharge Leaflet en local pour supprimer toute requete vers un CDN tiers.
# A executer une fois, puis relancer : python3 tools/build.py
set -euo pipefail
VERSION="1.9.4"
DIR="$(cd "$(dirname "$0")/.." && pwd)/assets/vendor/leaflet"
mkdir -p "$DIR"
for f in leaflet.js leaflet.css; do
  curl -fSL -o "$DIR/$f" "https://unpkg.com/leaflet@${VERSION}/dist/$f"
  echo "  $f : $(wc -c < "$DIR/$f") octets"
done
echo "Leaflet ${VERSION} installe dans assets/vendor/leaflet/"
echo "Relancez : python3 tools/build.py"
