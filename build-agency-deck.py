#!/usr/bin/env python3
"""Generate an agency-branded copy of the Colleague deck from the BMF source
build. Same ALDI creative-route example throughout (by design); only the
agency name in Act One's narrative copy changes. Screenshots still show the
original BMF demo tenant UI (no real tenant exists for these agencies) -
intentional, flagged in the repo README.
"""
import pathlib, re, sys

SOURCE = pathlib.Path("/Users/tommyhyde/aiden-colleague/demo/presentation/aldi-deck.html")
OUT_ROOT = pathlib.Path("/Users/tommyhyde/aiden-colleague-decks")

VOWEL_SOUND = re.compile(r"^(Uncommon|Alt|Alien|A|E|I|O|U)", re.IGNORECASE)

def article(name: str) -> str:
    return "an" if VOWEL_SOUND.match(name.strip()) else "a"

def build_for(name: str, slug: str):
    html = SOURCE.read_text(encoding="utf-8")
    an = article(name)
    replacements = [
        ("AIDEN Colleague for BMF, an AI operating system built from the agency's own brain.",
         f"AIDEN Colleague for {name}, an AI operating system built from the agency's own brain."),
        ("it's built from BMF's own beliefs.", f"it's built from {name}'s own beliefs."),
        ("It argues like BMF, because it's made of BMF.</span>",
         f"It argues like {name}, because it's made of {name}.</span>"),
        ('alt="BMF co-creation onboarding, 100% ready, 80 phantoms"',
         f'alt="{name} co-creation onboarding, 100% ready, 80 phantoms"'),
        ("Co-creation &middot; readiness 100% &middot; 80 BMF-curated phantoms",
         f"Co-creation &middot; readiness 100% &middot; 80 {name}-curated phantoms"),
        ("This instance is BMF's, not a generic tenant.",
         f"This instance is {name}'s, not a generic tenant."),
        ("<h2>This is BMF's mind.</h2>", f"<h2>This is {name}'s mind.</h2>"),
        ('alt="The BMF brain, 80 curated phantoms"', f'alt="The {name} brain, 80 curated phantoms"'),
        ("The brain &middot; 80 BMF-curated phantoms of 564 active",
         f"The brain &middot; 80 {name}-curated phantoms of 564 active"),
        ("These are three of BMF's own, pulled straight from the brain.",
         f"These are three of {name}'s own, pulled straight from the brain."),
        ("This is why it argues like BMF.</span>", f"This is why it argues like {name}.</span>"),
        ("<h2>It argues like<br>a BMF planner.</h2>",
         f"<h2>It argues like<br>{an} {name} planner.</h2>"),
        ("learning BMF as it goes.", f"learning {name} as it goes."),
        ("One brief, a real BMF client, all the way to a finished film.",
         f"One brief, a real {name} client, all the way to a finished film."),
        ("built from BMF's brain, carrying an idea", f"built from {name}'s brain, carrying an idea"),
        ("BMF &nbsp;&middot;&nbsp; The Hunt Is Over", f"{name} &nbsp;&middot;&nbsp; The Hunt Is Over"),
    ]
    missing = []
    for old, new in replacements:
        if old not in html:
            missing.append(old)
        html = html.replace(old, new)
    if missing:
        print(f"  WARNING [{slug}]: {len(missing)} pattern(s) not found:")
        for m in missing:
            print("   -", m[:80])
    if "BMF" in html.replace("BMF-Australia", ""):
        # any straggler BMF mentions (shouldn't be any given the list above)
        leftover = len(re.findall(r"BMF", html))
        print(f"  NOTE [{slug}]: {leftover} residual 'BMF' occurrence(s) remain (expected 0 in copy; screenshots retain BMF UI by design).")

    wrapped = (
        "<!doctype html>\n<html lang=\"en\">\n<head>\n"
        "<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        "<meta name=\"robots\" content=\"noindex, nofollow\">\n"
        f"<title>AIDEN Colleague, {name}, The Hunt Is Over</title>\n"
        "<style>html,body{margin:0;background:#0C0B0D}</style>\n</head>\n<body>\n"
        + html +
        "\n</body>\n</html>\n"
    )
    out_dir = OUT_ROOT / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "index.html"
    out_path.write_text(wrapped, encoding="utf-8")
    print(f"wrote {out_path} ({out_path.stat().st_size/1024/1024:.2f} MB)")

if __name__ == "__main__":
    for name, slug in [("LEGO", "lego"), ("Uncommon", "uncommon"), ("Alt/Shift", "alt-shift"), ("Alien Baby", "alien-baby")]:
        build_for(name, slug)
