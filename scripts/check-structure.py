#!/usr/bin/env python3
"""Check that every slide deck is named after a chapter in the book.

A deck lives at `<lang>/chapters/<slug>.qmd`, where <slug> is the chapter's
file name in that edition's _quarto.yml in the book repository — the same
path the chapter itself has, so a deck and its chapter are always one rename
apart. The chapter list is read from GitHub.

    python3 scripts/check-structure.py
"""
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOK = "https://raw.githubusercontent.com/bbardakk/uygulamali-dogal-dil-isleme/main/{lang}/_quarto.yml"


def main():
    problems, count = [], 0
    for lang in ("en", "tr"):
        text = urllib.request.urlopen(BOOK.format(lang=lang), timeout=30).read().decode("utf-8")
        slugs = set(re.findall(r"chapters/([0-9]{2}-[a-z0-9-]+)\.qmd", text))
        for deck in sorted((ROOT / lang / "chapters").glob("*.qmd")):
            if deck.stem not in slugs:
                problems.append(f"{lang}/chapters/{deck.name}: no chapter with this slug in the book")
            else:
                count += 1
    if problems:
        print("\n".join(problems))
        sys.exit(1)
    print(f"check-structure: {count} deck(s), every file matches a book chapter")


if __name__ == "__main__":
    main()
