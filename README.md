# AIDEN Colleague, agency decks

Self-contained walk-through decks for AIDEN Colleague, one per agency, each built on that agency's own brain.

Each deck is a single self-contained HTML file (fonts, screenshots, and video inlined) served from GitHub Pages.

## Structure
- `index.html` — landing page listing every agency deck (built by `build-index.py`)
- `<slug>/index.html` — the deck for that agency

## Live
- **BMF** — `/bmf/` — an AI operating system for the agency, ending on a finished ALDI film. Source build (real BMF tenant screenshots, real data). This is the source of truth for every other deck.
- **Generic** — `/generic/` — ONE presentation, one narrative, one style (the Colleague design system), no agency named anywhere. Flow: this is AIDEN (sameness problem; prefrontal cortex with the live Chat brain screenshot `assets/phantom-constellation.jpg`; decades-long career shown as three REAL phantoms from `aiden-chat/backend/phantoms_unified.json`; same brief different engine with the brain's actual pushback quote, archived at `assets/brain-pushback-response.json`) → the live hub screenshot (`assets/aiden-hub-live.png`, carries the nine-products message) → the turn (a brain is nurtured, not installed; the moat; "what if your company had its own phantom brain") → this is Colleague, the ninth product → the walk-through on a real agency's instance → the ALDI creative route and film → the ask with contact. Act I-III copy was transplanted from the aiden-deck (which lives on unchanged at its own URL for investors); the old holding-company Act Zero of the Colleague deck is cut.
- **Town Square** — `/town-square/` — independent framing.
- **Kerfuffle** — `/kerfuffle/` — independent framing.
- **Uncommon** — `/uncommon/`
- **LEGO** — `/lego/`
- **Alt/Shift** — `/alt-shift/`
- **Alien Baby** — `/alien-baby/`

All other decks are generated from `bmf/index.html`. Three builders exist:

- `build-agency-deck.py` — **holding-company / agency-group** framing (Uncommon, LEGO, Alt/Shift, Alien Baby). Swaps the agency name through the narrative copy, keeping the "one operating system for the group, every agency keeps its own brain, BMF is the proof" story.
- `build-independent-deck.py` — **independent-agency** framing (Town Square, Kerfuffle). Reframes Act Zero away from any holding company: you own your brain, the productivity gain stays with you, and it compounds into a moat rivals can't copy. Adds a light positioning touch per agency (Town Square: "Cultured Creativity"; Kerfuffle: "command attention").
- `build-generic-deck.py` — **generic** single-narrative deck. One page built from `bmf/index.html` with eight new Act I-III sections (aiden-deck copy in the Colleague idiom). Run it after any change to the BMF master.

Same ALDI creative route and demo screenshots throughout by design (one finished example, reused). The app screenshots still show the original BMF demo tenant UI (no real tenant exists yet for these agencies) — worth knowing before sharing externally.

## Adding an agency
1. Generate the deck: add it to `AGENCIES` in `build-independent-deck.py` (independent) or the list in `build-agency-deck.py` (group), then run that script. It writes `<slug>/index.html` from the current BMF build.
2. Add the agency to `AGENCIES` in `build-index.py`, set status to `live`, run `python3 build-index.py`.
3. Commit and push.
