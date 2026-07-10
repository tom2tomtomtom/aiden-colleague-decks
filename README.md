# AIDEN Colleague, agency decks

Self-contained walk-through decks for AIDEN Colleague, one per agency, each built on that agency's own brain.

Each deck is a single self-contained HTML file (fonts, screenshots, and video inlined) served from GitHub Pages.

## Structure
- `index.html` — landing page listing every agency deck (built by `build-index.py`)
- `<slug>/index.html` — the deck for that agency

## Live
- **BMF** — `/bmf/` — an AI operating system for the agency, ending on a finished ALDI film. Source build (real BMF tenant screenshots, real data). This is the source of truth for every other deck.
- **Town Square** — `/town-square/` — independent framing.
- **Kerfuffle** — `/kerfuffle/` — independent framing.
- **Uncommon** — `/uncommon/`
- **LEGO** — `/lego/`
- **Alt/Shift** — `/alt-shift/`
- **Alien Baby** — `/alien-baby/`

All other decks are generated from `bmf/index.html`. Two builders exist:

- `build-agency-deck.py` — **holding-company / agency-group** framing (Uncommon, LEGO, Alt/Shift, Alien Baby). Swaps the agency name through the narrative copy, keeping the "one operating system for the group, every agency keeps its own brain, BMF is the proof" story.
- `build-independent-deck.py` — **independent-agency** framing (Town Square, Kerfuffle). Reframes Act Zero away from any holding company: you own your brain, the productivity gain stays with you, and it compounds into a moat rivals can't copy. Adds a light positioning touch per agency (Town Square: "Cultured Creativity"; Kerfuffle: "command attention").

Same ALDI creative route and demo screenshots throughout by design (one finished example, reused). The app screenshots still show the original BMF demo tenant UI (no real tenant exists yet for these agencies) — worth knowing before sharing externally.

## Adding an agency
1. Generate the deck: add it to `AGENCIES` in `build-independent-deck.py` (independent) or the list in `build-agency-deck.py` (group), then run that script. It writes `<slug>/index.html` from the current BMF build.
2. Add the agency to `AGENCIES` in `build-index.py`, set status to `live`, run `python3 build-index.py`.
3. Commit and push.
