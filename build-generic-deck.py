#!/usr/bin/env python3
"""Generate the GENERIC (no agency name) Colleague deck from the current BMF
build (bmf/index.html). No agency is named anywhere in the copy: the pitch
sections speak to "your agency" and the demo sections narrate "the agency"
whose real brain the build was created from. The ALDI creative route, the demo
screenshots, and the closing ALDI film stay fixed by design.

This deck also opens on the AIDEN platform: a live hub screenshot
(assets/aiden-hub-live.png, inlined at build time) plus a refreshed services
roster, before the Colleague story starts.
"""
import base64, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "bmf" / "index.html"
OUT_DIR = HERE / "generic"
HUB_IMG = HERE / "assets" / "aiden-hub-live.png"


def platform_section() -> str:
    hub_b64 = base64.b64encode(HUB_IMG.read_bytes()).decode()
    return (
        '<section id="platform"><div class="wrap rv">\n'
        '  <p class="eyebrow">The platform</p>\n'
        '  <h2>Not a concept.<br>A live&nbsp;platform.</h2>\n'
        '  <p class="lead">AIDEN runs today at www.aiden.services. One login, one token wallet, '
        'and a session that follows you across every service. Everything in this deck '
        'sits on&nbsp;it.</p>\n'
        f'  <figure><img src="data:image/png;base64,{hub_b64}" '
        'alt="The AIDEN hub at www.aiden.services, the live services behind Colleague">\n'
        '  <figcaption>www.aiden.services &middot; the hub &middot; captured live</figcaption></figure>\n'
        '</div></section>\n\n'
    )


REPLACEMENTS = [
    # --- title (unchanged wording, kept explicit for clarity) ---
    ("<title>AIDEN Colleague, The Hunt Is Over</title>",
     "<title>AIDEN Colleague, The Hunt Is Over</title>"),

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

    # --- toolkit refresh: full live roster (Brand Audit live, add Pitch + refrAIm) ---
    ('<div class="tool-name">Brand Audit <span class="soon">Soon</span></div>',
     '<div class="tool-name">Brand Audit</div>'),
    # Pitch slots in after Brief Sharpener (default cold mark, no CSS needed)
    ("""    <div class="tool-card ads">
      <span class="tool-mark"></span>
      <div>
        <div class="tool-name">Ads</div>""",
     """    <div class="tool-card pitch">
      <span class="tool-mark"></span>
      <div>
        <div class="tool-name">Pitch</div>
        <p>Brief to pitch, one workflow. Strategy, territories, the big idea and copy, assembled into a boardroom-ready deck.</p>
      </div>
    </div>
    <div class="tool-card ads">
      <span class="tool-mark"></span>
      <div>
        <div class="tool-name">Ads</div>"""),
    # refrAIm closes the grid after Brand Audit
    ("""        <p>Comprehensive brand analysis for visual identity, messaging consistency and competitive positioning, with clear next moves for where the brand needs to go.</p>
      </div>
    </div>
  </div>""",
     """        <p>Comprehensive brand analysis for visual identity, messaging consistency and competitive positioning, with clear next moves for where the brand needs to go.</p>
      </div>
    </div>
    <div class="tool-card refraim">
      <span class="tool-mark"></span>
      <div>
        <div class="tool-name">refrAIm</div>
        <p>One video, every format. Reframe, resize and adapt finished film for any platform or aspect ratio with AI-driven composition.</p>
      </div>
    </div>
  </div>"""),
    # give refrAIm the red mark alongside chat and ads
    (".tool-card.chat .tool-mark, .tool-card.ads .tool-mark {",
     ".tool-card.chat .tool-mark, .tool-card.ads .tool-mark, .tool-card.refraim .tool-mark {"),
]


def build():
    html = SOURCE.read_text(encoding="utf-8")

    # the platform section opens the deck, right after the cover
    toolkit_anchor = '<section id="tools" class="toolkit">'
    assert toolkit_anchor in html, "toolkit section anchor not found in BMF master"
    html = html.replace(toolkit_anchor, platform_section() + toolkit_anchor)

    missing = []
    for old, new in REPLACEMENTS:
        if old not in html:
            missing.append(old)
        html = html.replace(old, new)
    if missing:
        print(f"  WARNING [generic]: {len(missing)} pattern(s) not found:")
        for m in missing:
            print("   -", m[:80])

    # sanity: no readable BMF should remain (base64 residue is fine)
    readable = [html[max(0, m.start() - 30):m.end() + 30]
                for m in re.finditer("BMF", html)
                if " " in html[max(0, m.start() - 30):m.end() + 30]
                or "<" in html[max(0, m.start() - 30):m.end() + 30]]
    if readable:
        print(f"  NOTE [generic]: {len(readable)} readable 'BMF' left:")
        for r in readable[:8]:
            print("   -", r.strip())

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / "index.html"
    out_path.write_text(html, encoding="utf-8")
    print(f"wrote {out_path} ({out_path.stat().st_size / 1024 / 1024:.2f} MB)")


if __name__ == "__main__":
    build()
