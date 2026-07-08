# AIDEN Colleague, agency decks

Self-contained walk-through decks for AIDEN Colleague, one per agency, each built on that agency's own brain.

Each deck is a single self-contained HTML file (fonts, screenshots, and video inlined) served from GitHub Pages.

## Structure
- `index.html` — landing page listing every agency deck (built by `build-index.py`)
- `<slug>/index.html` — the deck for that agency

## Live
- **BMF** — `/bmf/` — an AI operating system for the agency, ending on a finished ALDI film. Source build (real BMF tenant screenshots, real data).
- **Uncommon** — `/uncommon/`
- **LEGO** — `/lego/`
- **Alt/Shift** — `/alt-shift/`
- **Alien Baby** — `/alien-baby/`

Uncommon, LEGO, Alt/Shift, and Alien Baby are generated from the BMF deck by `build-agency-deck.py`, which swaps the agency name through the narrative copy. Same ALDI creative route throughout by design (one finished example, reused). The app screenshots in these four still show the original BMF demo tenant UI (no real tenant exists yet for these agencies) — worth knowing before sharing externally.

## Adding an agency
1. Drop the deck at `<slug>/index.html` (or generate one via `build-agency-deck.py` from the BMF source).
2. Add the agency to `AGENCIES` in `build-index.py`, set status to `live`.
3. `python3 build-index.py`, commit, push.
