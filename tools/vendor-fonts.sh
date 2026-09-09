#!/usr/bin/env bash
# Auto-heberge la police Inter : supprime la requete vers Google Fonts,
# ameliore le LCP et simplifie la politique de confidentialite.
# A executer une fois, puis relancer : python3 tools/build.py
set -euo pipefail
DIR="$(cd "$(dirname "$0")/.." && pwd)/assets/fonts"
mkdir -p "$DIR"
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
for W in 400 600 700 800; do
  CSS=$(curl -fsSL -A "$UA" "https://fonts.googleapis.com/css2?family=Inter:wght@${W}&display=swap")
  URL=$(printf '%s' "$CSS" | grep -oE 'https://fonts\.gstatic\.com[^)]+\.woff2' | head -1)
  [ -n "$URL" ] || { echo "URL woff2 introuvable pour la graisse $W" >&2; exit 1; }
  curl -fsSL -o "$DIR/inter-${W}.woff2" "$URL"
  echo "  inter-${W}.woff2 : $(wc -c < "$DIR/inter-${W}.woff2") octets"
done
echo "Police installee dans assets/fonts/ — relancez : python3 tools/build.py"
echo "Pensez a retirer la mention Google Fonts de politique-de-confidentialite."
