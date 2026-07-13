#!/usr/bin/env python3
"""Build the GENERIC (no agency name) two-part experience:

  generic/index.html            THE AIDEN STORY - the full aiden-deck slide
                                machine (vendored as aiden-story.html), plus a
                                story-nav, a live hub-screenshot slide after
                                "in production today", and a closing bridge
                                slide into part two.
  generic/colleague/index.html  THE COLLEAGUE STORY - the no-agency-name
                                Colleague deck generated from bmf/index.html.
                                The toolkit section is removed here (the AIDEN
                                story owns the services roster), and the same
                                story-nav is injected.

aiden-story.html is a vendored copy of ~/aiden-deck/index.html. When that deck
changes, re-copy it here and re-run this script.
"""
import base64, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
AIDEN_SOURCE = HERE / "aiden-story.html"
BMF_SOURCE = HERE / "bmf" / "index.html"
HUB_IMG = HERE / "assets" / "aiden-hub-live.png"
OUT_AIDEN = HERE / "generic" / "index.html"
OUT_COLLEAGUE = HERE / "generic" / "colleague" / "index.html"


# ---------------------------------------------------------------- AIDEN story

AIDEN_NAV_CSS = """<style>
.story-nav { position: fixed; top: 22px; right: 40px; z-index: 200; font-size: 12px;
  letter-spacing: .08em; text-transform: uppercase; font-weight: 600; }
.story-nav a { color: var(--text-dim); text-decoration: none; padding: 6px 0; }
.story-nav a:hover { color: var(--text); }
.story-nav a.on { color: var(--accent); }
.story-nav .sep { color: var(--text-dim); margin: 0 10px; }
.hub-shot { display: block; max-width: min(1040px, 82vw); max-height: 56vh;
  margin-top: 36px; border: 1px solid #222; border-radius: 6px;
  box-shadow: 0 30px 80px -30px rgba(0,0,0,.8); }
.hub-caption { margin-top: 14px; font-size: 12px; letter-spacing: .08em;
  text-transform: uppercase; color: var(--text-dim); }
.story-cta { display: inline-block; margin-top: 28px; padding: 14px 28px;
  border: 2px solid var(--accent); color: var(--accent); text-decoration: none;
  font-weight: 700; font-size: 16px; letter-spacing: .04em; }
.story-cta:hover { background: var(--accent); color: #fff; }
</style>
"""

AIDEN_NAV_HTML = """
<nav class="story-nav" onclick="event.stopPropagation()">
  <a class="on" href="./">The AIDEN story</a><span class="sep">/</span><a href="colleague/">The Colleague story</a>
</nav>
"""

HUB_SLIDE_ANCHOR = "<!-- 16b: THE PROOF -->"

BRIDGE_ANCHOR = """tomh@redbaez.com
    </div>
  </div>"""

BRIDGE_SLIDE = """

  <!-- PART TWO BRIDGE -->
  <div class="slide slide-cta">
    <div class="title-accent" style="margin: 0 auto 24px;"></div>
    <h2>Part two. <span class="accent">The Colleague&nbsp;story.</span></h2>
    <p class="cta-detail">One agency's own AIDEN, from a co-created brain to a finished film. The walk-through&nbsp;continues.</p>
    <a class="story-cta" href="colleague/" onclick="event.stopPropagation()">Open the Colleague story &rarr;</a>
  </div>"""


def hub_slide() -> str:
    hub_b64 = base64.b64encode(HUB_IMG.read_bytes()).decode()
    return (
        '<div class="slide">\n'
        '    <div class="accent-line"></div>\n'
        '    <h2>One login. <span class="accent">All of it live at aiden.services.</span></h2>\n'
        f'    <img class="hub-shot" src="data:image/png;base64,{hub_b64}" '
        'alt="The AIDEN hub at www.aiden.services, captured live">\n'
        '    <div class="hub-caption">www.aiden.services &middot; the hub &middot; captured live</div>\n'
        '  </div>\n\n  '
    )


def build_aiden_story():
    html = AIDEN_SOURCE.read_text(encoding="utf-8")
    for anchor in ("</head>", "<body>", HUB_SLIDE_ANCHOR, BRIDGE_ANCHOR):
        assert html.count(anchor) == 1, f"anchor not unique in aiden-story.html: {anchor[:40]!r}"
    html = html.replace("</head>", AIDEN_NAV_CSS + "</head>")
    html = html.replace("<body>", "<body>" + AIDEN_NAV_HTML)
    html = html.replace(HUB_SLIDE_ANCHOR, hub_slide() + HUB_SLIDE_ANCHOR)
    html = html.replace(BRIDGE_ANCHOR, BRIDGE_ANCHOR + BRIDGE_SLIDE)
    OUT_AIDEN.parent.mkdir(parents=True, exist_ok=True)
    OUT_AIDEN.write_text(html, encoding="utf-8")
    print(f"wrote {OUT_AIDEN} ({OUT_AIDEN.stat().st_size / 1024:.0f} KB)")


# ------------------------------------------------------------ Colleague story

COLLEAGUE_NAV_CSS = """<style>
.story-nav { position: fixed; top: 22px; right: clamp(1.4rem,5vw,3rem); z-index: 400;
  font-family: 'Mono'; font-weight: 700; font-size: .62rem; letter-spacing: .14em;
  text-transform: uppercase; }
.story-nav a { color: var(--muted); text-decoration: none; }
.story-nav a:hover { color: var(--paper); }
.story-nav a.on { color: var(--red); }
.story-nav .sep { color: var(--muted); margin: 0 .6rem; }
</style>
"""

COLLEAGUE_NAV_HTML = """
<nav class="story-nav">
  <a href="../">The AIDEN story</a><span class="sep">/</span><a class="on" href="./">The Colleague story</a>
</nav>
"""

REPLACEMENTS = [
    # --- cover: drop the holding-company frame ---
    ("<h1>An operating<br>system for<br>the agency group</h1>",
     "<h1>An operating<br>system for<br>your agency</h1>"),
    ("AIDEN Colleague gives a holding company one operating system for productivity, while every agency keeps its own brain. BMF is the proof instance for discussion and demo.",
     "AIDEN Colleague gives your agency one operating system for productivity, built from your own brain. The build in this deck is a real agency's instance, shown as the proof for discussion and demo."),
    ("<div class=\"tag\">Holding company story &middot; BMF proof &middot; Discussion + demo</div>",
     "<div class=\"tag\">Your own brain &middot; Working proof &middot; Discussion + demo</div>"),

    # --- the productivity opportunity divider ---
    ("<div class=\"act\">Holding company opportunity</div>",
     "<div class=\"act\">The agency opportunity</div>"),

    # --- the strategic choice ---
    ("<h2>AIDEN is how the group captures the productivity gain itself.</h2>",
     "<h2>AIDEN is how your agency captures the productivity gain itself.</h2>"),
    ("Not by replacing people. By making every person in every agency three times better at the job they already do.",
     "Not by replacing people. By making every person in the agency three times better at the job they already do."),
    ("Build a working system that makes the agencies sharper, faster, and more valuable while the gain still belongs to the group.",
     "Build a working system that makes the agency sharper, faster, and more valuable while the gain still belongs to you."),

    # --- one system, built for you ---
    ("<span class=\"n\">00</span> One system, every agency",
     "<span class=\"n\">00</span> One system, built for you"),

    # --- your advantage (was portfolio advantage) ---
    ("<span class=\"n\">00</span> Portfolio advantage",
     "<span class=\"n\">00</span> Your advantage"),
    ("<h2>Base AI makes agencies more similar.<br>AIDEN makes each agency more itself.</h2>",
     "<h2>Base AI makes agencies more similar.<br>AIDEN makes your agency more itself.</h2>"),
    ("If every agency uses the same tools in the same way, the output converges. AIDEN works differently because the group can share infrastructure without flattening the agency brands.",
     "If every agency uses the same tools in the same way, the output converges. AIDEN works differently because it is built from your agency's own brain, not a shared model."),
    ("<h3>Every agency keeps its own brain.</h3><p>BMF thinks like BMF. Hotwire would think like Hotwire. Orchard would think like Orchard.</p>",
     "<h3>You keep your own brain.</h3><p>Your agency thinks like your agency. Base AI thinks like everyone. That difference is the whole point.</p>"),
    ("<h3>The advantage gets harder to copy.</h3><p>The longer each agency uses AIDEN, the more useful its memory becomes, and the more distinctive its version gets.</p>",
     "<h3>The advantage gets harder to copy.</h3><p>The longer your agency uses AIDEN, the more useful its memory becomes, and the more distinctive its thinking gets.</p>"),

    # --- the moat ---
    ("For a holding company, the advantage is not just speed. It is durable, portfolio-specific intelligence that compounds inside each agency.",
     "For your agency, the advantage is not just speed. It is durable, agency-specific intelligence that compounds with every brief."),
    ("Every agency's AIDEN is grown from its own culture, documents, interviews, work, and feedback. No two are alike.",
     "Your agency's AIDEN is grown from its own culture, documents, interviews, work, and feedback. No one else can run it."),

    # --- the proof (no agency named) ---
    ("<h2>BMF is the proof of depth,<br>not the headline.</h2>",
     "<h2>This build is the proof of depth,<br>not the headline.</h2>"),
    ("To make the operating system tangible, we built a BMF version of AIDEN around BMF's creative philosophy and a real client problem.",
     "To make the operating system tangible, we built a working version of AIDEN around a real agency's creative philosophy and a real client problem."),

    # --- act one divider ---
    ("The group-level case is made. From here, this becomes the discussion and demo: open the BMF version of AIDEN and show how the colleague thinks, remembers, challenges, collects and works across the agency day.",
     "The case is made. From here, this becomes the discussion and demo: open the working build of AIDEN and show how the colleague thinks, remembers, challenges, collects and works across the agency day."),

    # --- act one product slides: demo narration, "the agency" ---
    ("feels like BMF.</h2>", "feels like the agency.</h2>"),
    ("it's co-created from BMF's own beliefs.", "it's co-created from the agency's own beliefs."),
    ("It argues like BMF, because it's made of BMF.</span>",
     "It argues like the agency, because it's made of the agency.</span>"),
    ('alt="BMF co-creation onboarding, 100% ready, 80 phantoms"',
     'alt="Co-creation onboarding, 100% ready, 80 phantoms"'),
    ("Co-creation &middot; readiness 100% &middot; 80 BMF-curated phantoms",
     "Co-creation &middot; readiness 100% &middot; 80 agency-curated phantoms"),
    ("This instance is BMF's, not a generic tenant.",
     "This instance is one agency's own, not a generic tenant."),
    ("<h2>This is BMF's mind.</h2>", "<h2>This is the agency's mind.</h2>"),
    ('alt="The BMF brain, 80 curated phantoms"', 'alt="The agency brain, 80 curated phantoms"'),
    ("The brain &middot; 80 BMF-curated phantoms of 564 active",
     "The brain &middot; 80 agency-curated phantoms of 564 active"),
    ("These are three of BMF's own, pulled straight from the brain.",
     "These are three of the agency's own, pulled straight from the brain."),
    ("This is why it argues like BMF.</span>", "This is why it argues like the agency.</span>"),
    ("<h2>It argues like<br>a BMF planner.</h2>",
     "<h2>It argues like<br>the agency's planner.</h2>"),
    ("learning BMF as it goes.", "learning the agency as it goes."),
    ("One brief, a real BMF client, all the way to a finished film.",
     "One brief, a real client, all the way to a finished film."),

    # --- the ask + close ---
    ("<h2>Start with BMF.<br>Scale the operating system.</h2>",
     "<h2>Start with your brain.<br>Scale the operating system.</h2>"),
    ('<span class="on">BMF proof</span><span class="arw">&rarr;</span><span>Agency brain</span><span class="arw">&rarr;</span><span>Group platform</span>',
     '<span class="on">Working proof</span><span class="arw">&rarr;</span><span>Your agency\'s brain</span><span class="arw">&rarr;</span><span>Your operating system</span>'),
    ("One operating system. Every agency keeps its own brain. The group captures the productivity gain.",
     "One operating system, built from your agency's own brain. The productivity gain stays with you."),
    ("Use BMF as the proof instance for discussion and demo, then extend AIDEN across the portfolio as the productivity platform for research, strategy, briefs, testing, client work, and execution.",
     "Use this build as the proof for discussion and demo, then extend AIDEN across your agency as the productivity platform for research, strategy, briefs, testing, client work, and execution."),
    ("&middot; Colleague &nbsp;&middot;&nbsp; BMF proof instance &nbsp;&middot;&nbsp; Group operating system",
     "&middot; Colleague &nbsp;&middot;&nbsp; Working proof instance &nbsp;&middot;&nbsp; Agency operating system"),
]


def build_colleague_story():
    html = BMF_SOURCE.read_text(encoding="utf-8")

    # the AIDEN story owns the services roster; drop the toolkit section here
    html, removed = re.subn(
        r'<section id="tools" class="toolkit">.*?</section>\s*', "", html, count=1, flags=re.S
    )
    assert removed == 1, "toolkit section not found in BMF master"

    missing = []
    for old, new in REPLACEMENTS:
        if old not in html:
            missing.append(old)
        html = html.replace(old, new)
    if missing:
        print(f"  WARNING [colleague]: {len(missing)} pattern(s) not found:")
        for m in missing:
            print("   -", m[:80])

    # story nav
    assert html.count("</head>") == 1 and html.count("<body>") == 1
    html = html.replace("</head>", COLLEAGUE_NAV_CSS + "</head>")
    html = html.replace("<body>", "<body>" + COLLEAGUE_NAV_HTML)

    # sanity: no readable BMF should remain (base64 residue is fine)
    readable = [html[max(0, m.start() - 30):m.end() + 30]
                for m in re.finditer("BMF", html)
                if " " in html[max(0, m.start() - 30):m.end() + 30]
                or "<" in html[max(0, m.start() - 30):m.end() + 30]]
    if readable:
        print(f"  NOTE [colleague]: {len(readable)} readable 'BMF' left:")
        for r in readable[:8]:
            print("   -", r.strip())

    OUT_COLLEAGUE.parent.mkdir(parents=True, exist_ok=True)
    OUT_COLLEAGUE.write_text(html, encoding="utf-8")
    print(f"wrote {OUT_COLLEAGUE} ({OUT_COLLEAGUE.stat().st_size / 1024 / 1024:.2f} MB)")


if __name__ == "__main__":
    build_aiden_story()
    build_colleague_story()
