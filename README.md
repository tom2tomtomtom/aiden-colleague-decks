# AIDEN Colleague, agency decks

Self-contained walk-through decks for AIDEN Colleague, one per agency, each built on that agency's own brain.

Each deck is a single self-contained HTML file (fonts, screenshots, and video inlined) served from GitHub Pages.

## Structure
- `index.html` — landing page listing every agency deck (built by `build-index.py`)
- `<slug>/index.html` — the deck for that agency

## Live
- **BMF** — `/bmf/` — an AI operating system for the agency, ending on a finished ALDI film.

## In production
- Uncommon, LEGO, Alien Baby

## Adding an agency
1. Drop the deck at `<slug>/index.html`.
2. Add the agency to `AGENCIES` in `build-index.py`, set status to `live`.
3. `python3 build-index.py`, commit, push.
