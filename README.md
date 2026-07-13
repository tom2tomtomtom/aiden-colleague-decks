# AIDEN Colleague, agency decks

Self-contained walk-through decks for AIDEN Colleague, one per agency, each built on that agency's own brain.

Each deck is a single self-contained HTML file (fonts, screenshots, and video inlined) served from GitHub Pages.

## Structure
- `index.html` — landing page listing every agency deck (built by `build-index.py`)
- `<slug>/index.html` — the deck for that agency

## Live
- **BMF** — `/bmf/` — the source of truth for every generated deck, and kept in its ORIGINAL structure by request (never regenerated). Real BMF tenant screenshots, real data, ending on the finished ALDI film.
- **Generic** and every other agency deck (**Uncommon**, **LEGO**, **Alt/Shift**, **Alien Baby**, **Town Square**, **Kerfuffle**) share the SINGLE-NARRATIVE structure, one style (the Colleague design system), built by `build-decks.py`:
  - **Act I, this is AIDEN**: sameness problem; prefrontal cortex with the live Chat brain screenshot (`assets/phantom-constellation.jpg`); decades-long career shown as three REAL phantoms from `aiden-chat/backend/phantoms_unified.json`; same brief different engine with the brain's actual pushback quote (archived at `assets/brain-pushback-response.json`).
  - **Act II, live today**: the hub screenshot (`assets/aiden-hub-live.png`), carrying the one-brain-nine-products message.
  - **Act III, the turn**: a brain is nurtured, not installed; the moat; "what if {your company / the agency} had its own phantom brain"; this is Colleague, the ninth product; proof of depth.
  - **Acts IV-VI**: the walk-through, the ALDI creative route and film, the ask with contact.
  - The only per-agency difference is naming ("What if Uncommon had its own phantom brain?", "This is Uncommon's mind", the title, the ask). The generic deck names nobody: "your company" up front, "the agency" in the demo narration.

Same ALDI creative route and demo screenshots throughout by design (one finished example, reused). The app screenshots still show the original BMF demo tenant UI (no real tenant exists yet for these agencies) — worth knowing before sharing externally. Act I copy was transplanted from the aiden-deck, which lives on unchanged at its own URL for investors.

## Adding an agency
1. Add `("slug", "Name")` to `DECKS` in `build-decks.py`, run `python3 build-decks.py`. It writes `<slug>/index.html` from the current BMF build.
2. Add the agency to `AGENCIES` in `build-index.py`, set status to `live`, run `python3 build-index.py`.
3. Commit and push.
