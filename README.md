# AIDEN Colleague, agency decks

> **CANONICAL VERSION: 2026-07-21.** Build every new agency deck from the current
> `build-decks.py` pipeline (the generic deck is the reference output). This version
> carries: the three first-person legend phantoms in the career slide (Ogilvy's
> homework, Bernbach's "say that", Mary Wells' planes — real rows in
> `colleague.base_phantoms`), the contradictory-brief pushback in "Same brief.
> Different engine." (real brain reply 2026-07-21, `assets/brain-bad-brief-response.json`,
> 77 of 387 phantoms fired), and the single-card belief slide ("The career is the
> library's. The beliefs are yours."). For a client-facing deck, ALSO do the
> town-square treatment (see below): real tenant captures and examples, no other
> agency's clients or lore anywhere in the deck.

Each deck is a single self-contained HTML file (fonts, screenshots, and video inlined) served from GitHub Pages.

## Structure
- `index.html` — landing page listing every agency deck (built by `build-index.py`)
- `<slug>/index.html` — the deck for that agency

## Live
- **BMF** — `/bmf/` — the source of truth for every generated deck, and kept in its ORIGINAL structure by request (never regenerated). Real BMF tenant screenshots, real data, ending on the finished ALDI film.
- **Generic** and every other agency deck (**Uncommon**, **LEGO**, **Alt/Shift**, **Alien Baby**, **Town Square**, **Kerfuffle**) share the SINGLE-NARRATIVE structure, one style (the Colleague design system), built by `build-decks.py`:
  - **Act I, this is AIDEN**: sameness problem; prefrontal cortex with the live Chat brain screenshot (`assets/phantom-constellation.jpg`); decades-long career shown as three REAL first-person phantoms from `colleague.base_phantoms` (added 2026-07-21); same brief different engine with the brain's actual pushback to the contradictory viral brief (archived at `assets/brain-bad-brief-response.json`).
  - **Act II, live today**: the hub screenshot (`assets/aiden-hub-live.png`), carrying the one-brain-nine-products message.
  - **Act III, the turn**: a brain is nurtured, not installed; the moat; "what if {your company / the agency} had its own phantom brain"; this is Colleague, the ninth product; proof of depth.
  - **Acts IV-VI**: the walk-through, the ALDI creative route and film, the ask with contact.
  - The only per-agency difference is naming ("What if Uncommon had its own phantom brain?", "This is Uncommon's mind", the title, the ask). The generic deck names nobody: "your company" up front, "the agency" in the demo narration.

Same ALDI creative route and demo screenshots throughout by design (one finished example, reused). In the un-treated decks (Uncommon, LEGO, Alt/Shift, Alien Baby, Kerfuffle app shots aside) the screenshots still show the original BMF demo tenant UI — worth knowing before sharing externally. Act I copy was transplanted from the aiden-deck, which lives on unchanged at its own URL for investors.

**Five decks now carry the full tenant treatment** (2026-07-21): Town Square,
Uncommon, LEGO, Alt/Shift and Alien Baby each have a real demo tenant
(`<slug>.deck.demo.<date>@redbaez.com`), so every screenshot and example is
genuinely that agency's — 7 tenant captures plus the cropped pipeline canvas, the
tenant's real Brief Sharpener run instead of HCF, an ALDI-exchange board instead
of LEGO's, real panel persona quotes, and the tenant's own top curated phantom in
the belief slide (invented personal names curated out of displayed stories).
Mechanism: `agency_treatment.py` + `treatment-data/<slug>/` (town-square keeps its
original hand-built `town_square_rework.py`).
Known gap: only Kerfuffle (already presented) and the generic template still carry
the HCF/LEGO examples and BMF tenant screenshots.

## Adding an agency
1. Add `("slug", "Name")` to `DECKS` in `build-decks.py`, run `python3 build-decks.py`. It writes `<slug>/index.html` from the current BMF build.
2. Add the agency to `AGENCIES` in `build-index.py`, set status to `live`, run `python3 build-index.py`.
3. For a client-facing deck, replicate the town-square treatment: create a
   `<name>.deck.demo.<date>@redbaez.com` tenant, onboard it (identity, interview,
   knowledge doc, generate + approve phantoms), run Culture Scan / Synthetic Panel /
   Brief Sharpener on the ALDI examples, capture the 7 shots at 1440x900, and add a
   rework module + screenshot map following `town_square_rework.py`.
4. Commit and push.
