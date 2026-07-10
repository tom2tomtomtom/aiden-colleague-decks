#!/usr/bin/env python3
"""Generate agency-branded copies of the Colleague deck from the current BMF
build in this repo (bmf/index.html is the source of truth - the version last
presented). Only the proof-instance name changes: everywhere the copy names
"BMF" as the proof agency, the agency name is substituted. The holding-company /
agency-group framing stays generic, and the ALDI creative-route example plus the
demo screenshots are retained across every deck by design (no real tenant exists
for these agencies - flagged in the README).
"""
import pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "bmf" / "index.html"
OUT_ROOT = HERE

VOWEL_SOUND = re.compile(r"^(Uncommon|Alt|Alien|A|E|I|O|U)", re.IGNORECASE)


def article(name: str) -> str:
    return "an" if VOWEL_SOUND.match(name.strip()) else "a"


def build_for(name: str, slug: str):
    html = SOURCE.read_text(encoding="utf-8")
    an = article(name)
    replacements = [
        # cover + holding-company framing
        ("<title>AIDEN Colleague, The Hunt Is Over</title>",
         f"<title>AIDEN Colleague, {name}, The Hunt Is Over</title>"),
        ("keeps its own brain. BMF is the proof instance for discussion and demo.",
         f"keeps its own brain. {name} is the proof instance for discussion and demo."),
        ("Holding company story &middot; BMF proof &middot; Discussion + demo",
         f"Holding company story &middot; {name} proof &middot; Discussion + demo"),
        ("BMF thinks like BMF. Hotwire", f"{name} thinks like {name}. Hotwire"),
        # the proof section
        ("<h2>BMF is the proof of depth,<br>not the headline.</h2>",
         f"<h2>{name} is the proof of depth,<br>not the headline.</h2>"),
        ("we built a BMF version of AIDEN around BMF's creative philosophy",
         f"we built {an} {name} version of AIDEN around {name}'s creative philosophy"),
        ("open the BMF version of AIDEN and show how",
         f"open the {name} version of AIDEN and show how"),
        # act one - onboarding + brain
        ("feels like BMF.</h2>", f"feels like {name}.</h2>"),
        ("it's co-created from BMF's own beliefs.", f"it's co-created from {name}'s own beliefs."),
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
        # act two + the ask + close
        ("One brief, a real BMF client, all the way to a finished film.",
         f"One brief, a real {name} client, all the way to a finished film."),
        ("<h2>Start with BMF.<br>Scale the operating system.</h2>",
         f"<h2>Start with {name}.<br>Scale the operating system.</h2>"),
        ('<span class="on">BMF proof</span>', f'<span class="on">{name} proof</span>'),
        ("Use BMF as the proof instance for discussion and demo",
         f"Use {name} as the proof instance for discussion and demo"),
        ("&middot;&nbsp; BMF proof instance &nbsp;&middot;&nbsp; Group operating system",
         f"&middot;&nbsp; {name} proof instance &nbsp;&middot;&nbsp; Group operating system"),
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

    out_dir = OUT_ROOT / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "index.html"
    out_path.write_text(html, encoding="utf-8")
    print(f"wrote {out_path} ({out_path.stat().st_size / 1024 / 1024:.2f} MB)")


if __name__ == "__main__":
    for name, slug in [("LEGO", "lego"), ("Uncommon", "uncommon"), ("Alt/Shift", "alt-shift"), ("Alien Baby", "alien-baby")]:
        build_for(name, slug)
