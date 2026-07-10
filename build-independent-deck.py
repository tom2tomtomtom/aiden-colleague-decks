#!/usr/bin/env python3
"""Generate agency-branded Colleague decks for INDEPENDENT agencies from the
current BMF build (bmf/index.html). Unlike build-agency-deck.py, this reframes
Act Zero away from the holding-company / agency-group pitch: for an independent
agency there is no group, so the story becomes "you own your brain, the
productivity gain stays with you, and it compounds into a moat rivals can't
copy." A light positioning touch per agency is woven into the cover and the
proof slide. The ALDI creative route and demo screenshots stay fixed by design.
"""
import pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "bmf" / "index.html"
OUT_ROOT = HERE

VOWEL_SOUND = re.compile(r"^(Uncommon|Alt|Alien|A|E|I|O|U)", re.IGNORECASE)


def article(name: str) -> str:
    return "an" if VOWEL_SOUND.match(name.strip()) else "a"


# Per-agency: slug, display name, cover sub-line, proof-slide philosophy phrase.
AGENCIES = [
    {
        "slug": "town-square",
        "name": "Town Square",
        "cover_sub": ("AIDEN Colleague gives Town Square one operating system for productivity, "
                      "built from Town Square's own brain and its Cultured Creativity. This build "
                      "is the proof instance for discussion and demo."),
        "philosophy": "Town Square's Cultured Creativity",
    },
    {
        "slug": "kerfuffle",
        "name": "Kerfuffle",
        "cover_sub": ("AIDEN Colleague gives Kerfuffle one operating system for productivity, "
                      "built from Kerfuffle's own brain and its instinct to command attention. "
                      "This build is the proof instance for discussion and demo."),
        "philosophy": "Kerfuffle's instinct to command attention",
    },
]


def build_for(agency: dict):
    name = agency["name"]
    slug = agency["slug"]
    an = article(name)
    html = SOURCE.read_text(encoding="utf-8")

    replacements = [
        # --- title ---
        ("<title>AIDEN Colleague, The Hunt Is Over</title>",
         f"<title>AIDEN Colleague, {name}, The Hunt Is Over</title>"),

        # --- cover: drop the holding-company frame ---
        ("<h1>An operating<br>system for<br>the agency group</h1>",
         f"<h1>An operating<br>system for<br>{name}</h1>"),
        ("AIDEN Colleague gives a holding company one operating system for productivity, while every agency keeps its own brain. BMF is the proof instance for discussion and demo.",
         agency["cover_sub"]),
        ("<div class=\"tag\">Holding company story &middot; BMF proof &middot; Discussion + demo</div>",
         f"<div class=\"tag\">{name}'s own brain &middot; Working proof &middot; Discussion + demo</div>"),

        # --- the productivity opportunity divider ---
        ("<div class=\"act\">Holding company opportunity</div>",
         "<div class=\"act\">The independent opportunity</div>"),

        # --- the strategic choice ---
        ("<h2>AIDEN is how the group captures the productivity gain itself.</h2>",
         f"<h2>AIDEN is how {name} captures the productivity gain itself.</h2>"),
        ("Not by replacing people. By making every person in every agency three times better at the job they already do.",
         f"Not by replacing people. By making every person at {name} three times better at the job they already do."),
        ("Build a working system that makes the agencies sharper, faster, and more valuable while the gain still belongs to the group.",
         f"Build a working system that makes {name} sharper, faster, and more valuable while the gain still belongs to you."),

        # --- one system, built for you ---
        ("<span class=\"n\">00</span> One system, every agency",
         "<span class=\"n\">00</span> One system, built for you"),

        # --- your advantage (was portfolio advantage) ---
        ("<span class=\"n\">00</span> Portfolio advantage",
         "<span class=\"n\">00</span> Your advantage"),
        ("<h2>Base AI makes agencies more similar.<br>AIDEN makes each agency more itself.</h2>",
         f"<h2>Base AI makes agencies more similar.<br>AIDEN makes {name} more itself.</h2>"),
        ("If every agency uses the same tools in the same way, the output converges. AIDEN works differently because the group can share infrastructure without flattening the agency brands.",
         f"If every agency uses the same tools in the same way, the output converges. AIDEN works differently because it is built from {name}'s own brain, not a shared model."),
        ("<h3>Every agency keeps its own brain.</h3><p>BMF thinks like BMF. Hotwire would think like Hotwire. Orchard would think like Orchard.</p>",
         f"<h3>You keep your own brain.</h3><p>{name} thinks like {name}. Base AI thinks like everyone. That difference is the whole point.</p>"),
        ("<h3>The advantage gets harder to copy.</h3><p>The longer each agency uses AIDEN, the more useful its memory becomes, and the more distinctive its version gets.</p>",
         f"<h3>The advantage gets harder to copy.</h3><p>The longer {name} uses AIDEN, the more useful its memory becomes, and the more distinctive its thinking gets.</p>"),

        # --- the moat ---
        ("For a holding company, the advantage is not just speed. It is durable, portfolio-specific intelligence that compounds inside each agency.",
         f"For {name}, the advantage is not just speed. It is durable, agency-specific intelligence that compounds with every brief."),
        ("Every agency's AIDEN is grown from its own culture, documents, interviews, work, and feedback. No two are alike.",
         f"{name}'s AIDEN is grown from its own culture, documents, interviews, work, and feedback. No one else can run it."),

        # --- the proof (independent framing + positioning touch) ---
        ("<h2>BMF is the proof of depth,<br>not the headline.</h2>",
         "<h2>This build is the proof of depth,<br>not the headline.</h2>"),
        ("To make the operating system tangible, we built a BMF version of AIDEN around BMF's creative philosophy and a real client problem.",
         f"To make the operating system tangible, we built {an} {name} version of AIDEN around {agency['philosophy']} and a real client problem."),

        # --- act one divider ---
        ("The group-level case is made. From here, this becomes the discussion and demo: open the BMF version of AIDEN and show how the colleague thinks, remembers, challenges, collects and works across the agency day.",
         f"The case is made. From here, this becomes the discussion and demo: open the {name} version of AIDEN and show how the colleague thinks, remembers, challenges, collects and works across the agency day."),

        # --- act one product slides: straight name swaps ---
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
        ("One brief, a real BMF client, all the way to a finished film.",
         f"One brief, a real {name} client, all the way to a finished film."),

        # --- the ask + close (independent framing) ---
        ("<h2>Start with BMF.<br>Scale the operating system.</h2>",
         f"<h2>Start with the proof.<br>Scale across {name}.</h2>"),
        ('<span class="on">BMF proof</span><span class="arw">&rarr;</span><span>Agency brain</span><span class="arw">&rarr;</span><span>Group platform</span>',
         f'<span class="on">Working proof</span><span class="arw">&rarr;</span><span>{name} brain</span><span class="arw">&rarr;</span><span>Agency platform</span>'),
        ("One operating system. Every agency keeps its own brain. The group captures the productivity gain.",
         f"One operating system, built from {name}'s brain. The productivity gain stays with {name}."),
        ("Use BMF as the proof instance for discussion and demo, then extend AIDEN across the portfolio as the productivity platform for research, strategy, briefs, testing, client work, and execution.",
         f"Use this build as the proof for discussion and demo, then extend AIDEN across {name} as the productivity platform for research, strategy, briefs, testing, client work, and execution."),
        ("&middot; Colleague &nbsp;&middot;&nbsp; BMF proof instance &nbsp;&middot;&nbsp; Group operating system",
         f"&middot; Colleague &nbsp;&middot;&nbsp; {name} operating system &nbsp;&middot;&nbsp; Built from {name}'s brain"),
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

    # sanity: no readable BMF should remain (base64 residue is fine)
    readable = [html[max(0, m.start() - 30):m.end() + 30]
                for m in re.finditer("BMF", html)
                if " " in html[max(0, m.start() - 30):m.end() + 30]
                or "<" in html[max(0, m.start() - 30):m.end() + 30]]
    if readable:
        print(f"  NOTE [{slug}]: {len(readable)} readable 'BMF' left:")
        for r in readable[:8]:
            print("   -", r.strip())

    out_dir = OUT_ROOT / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "index.html"
    out_path.write_text(html, encoding="utf-8")
    print(f"wrote {out_path} ({out_path.stat().st_size / 1024 / 1024:.2f} MB)")


if __name__ == "__main__":
    for agency in AGENCIES:
        build_for(agency)
