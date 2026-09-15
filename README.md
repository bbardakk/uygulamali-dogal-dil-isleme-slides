# Uygulamalı Doğal Dil İşleme — Slides

Lecture slides for **Applied Natural Language Processing — From Tokens to Agents**
(*Uygulamalı Doğal Dil İşleme — Token'lardan Ajanlara*): one [Quarto](https://quarto.org)
reveal.js deck per chapter, in English and in Turkish.

- Published slides: <https://bbardakk.github.io/uygulamali-dogal-dil-isleme-slides/>
- Book: <https://bbardakk.github.io/uygulamali-dogal-dil-isleme/> · source: [bbardakk/uygulamali-dogal-dil-isleme](https://github.com/bbardakk/uygulamali-dogal-dil-isleme)
- Notebooks: [bbardakk/uygulamali-dogal-dil-isleme-notebooks](https://github.com/bbardakk/uygulamali-dogal-dil-isleme-notebooks)

## Layout

Decks mirror the book's own paths, so a deck and its chapter are always one rename apart:

| book | deck |
|:--|:--|
| `en/chapters/01-why-nlp-now.qmd` | `en/chapters/01-why-nlp-now.qmd` |
| `tr/chapters/01-neden-nlp.qmd` | `tr/chapters/01-neden-nlp.qmd` |

```text
_quarto.yml                 website project; shared reveal.js options (1280×720, footer, slide numbers)
index.qmd                   landing page listing the decks per language
theme/slides.scss           the book's palette and fonts, sized for a lecture hall
en/chapters/<slug>.qmd      English decks
tr/chapters/<slug>.qmd      Turkish decks, the same slides in the same order
scripts/check-structure.py  checks every deck name against the book's chapter list
```

Every number, date and claim on a slide comes from the chapter it belongs to; explanation lives
in the speaker notes (press **S** in a deck). `python3 scripts/check-structure.py` reads the
chapter list from the book repository on GitHub and fails if a deck has no matching chapter.

| chapter | English | Türkçe |
|:--|:--|:--|
| 01 Why NLP, Why Now | [deck](en/chapters/01-why-nlp-now.qmd) | [sunum](tr/chapters/01-neden-nlp.qmd) |

## Rendering

The site is rendered by GitHub Actions with Quarto 1.10.18 on every push to `main`
(`.github/workflows/publish.yml`) and published to GitHub Pages. Locally:

```bash
quarto render                                   # the whole site, into _site/
quarto preview en/chapters/01-why-nlp-now.qmd   # one deck, live-reloading
```

## License

Slide content (text, figures, speaker notes) is [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/);
the build configuration, theme and scripts are MIT — the same split as the book. See [LICENSE](LICENSE).
