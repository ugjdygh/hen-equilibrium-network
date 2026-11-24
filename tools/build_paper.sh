#!/usr/bin/env bash
# Build the metzdowd-style paper PDF: two columns, abstract, numbered sections.
# Requires pandoc + xelatex + Noto Serif + Noto Sans CJK SC.
set -euo pipefail
SRC="docs/whitepaper/review-edition/paper.md"
OUT="${1:-/tmp/hen.pdf}"
HDR="$(mktemp)"
echo '\usepackage{array}' > "$HDR"
pandoc "$SRC" -o /tmp/hen.tex --to=latex --number-sections \
  -V classoption=twocolumn -V fontsize=10pt -V geometry:margin=0.8in -V papersize=a4 -H "$HDR"
( cd /tmp && xelatex -interaction=nonstopmode hen.tex >/dev/null \
  && xelatex -interaction=nonstopmode hen.tex >/dev/null )
cp /tmp/hen.pdf "$OUT"
pdfinfo "$OUT" | grep -i pages
echo "written: $OUT"
