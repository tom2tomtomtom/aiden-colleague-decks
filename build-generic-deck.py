#!/usr/bin/env python3
"""Build the GENERIC deck: ONE presentation, one narrative, one style.

Output: generic/index.html, a single scroll deck in the Colleague design
system (Anton/Mono, ink and paper), built from bmf/index.html as the chassis
with eight new sections transplanted from the aiden-deck copy.

The flow (agreed 2026-07-13):
  Act I    This is AIDEN      cover, sameness, prefrontal cortex,
                              decades-long career, same brief different engine
  Act II   Live today         one brain nine products (roster grid),
                              live hub screenshot
  Act III  The turn           a brain is nurtured not installed, the moat,
                              what if your company had its own phantom brain,
                              this is Colleague, proof of depth
  Act IV   The build          the walk-through: onboarding, interview, brain,
                              phantom, chat, boards, culture scan, synthetic
                              panel, brief sharpener, operating system
  Act V    The route          one-line ALDI brief to the finished film
  Act VI   The ask            start with your brain + contact

Cut: the old holding-company Act Zero (BMF sections 2-6), the two-page split,
the investor slides. No agency is named anywhere in the copy.
"""
import base64, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "bmf" / "index.html"
HUB_IMG = HERE / "assets" / "aiden-hub-live.png"
OUT = HERE / "generic" / "index.html"


# ------------------------------------------------------- new sections (Act I-III)

SAMENESS = """<section><div class="wrap rv">
  <p class="eyebrow">The problem</p>
  <h2>Every agency has AI now.<br>The work has never looked more the&nbsp;same.</h2>
  <p class="lead">Generative AI handed everyone the same tools, the same prompts, and the same polished, average output. The advantage evaporated the moment it arrived.</p>
  <p>Agencies do not need more AI. They need AI with a point of view. <span class="hl">The category is wide open for the AI that actually thinks like a&nbsp;creative.</span></p>
</div></section>

"""

CORTEX = """<section><div class="wrap rv">
  <p class="eyebrow">The engine</p>
  <h2>We gave the model<br>a prefrontal&nbsp;cortex.</h2>
  <p class="lead">Raw language models are limbic. Reactive, fluent, and desperate to please. The sycophancy is the tell: with nothing pushing back, the model drifts toward whatever you want to hear.</p>
  <p>AIDEN adds the missing layer. The model brings fluency and pattern recognition. Phantom memory brings persistence, identity, and the ability to disagree. <span class="hl">Not autocomplete. Creative&nbsp;conviction.</span></p>
</div></section>

"""

CAREER = """<section><div class="wrap rv">
  <p class="eyebrow">The phantom system</p>
  <h2>It believes it has lived<br>a decades-long&nbsp;career.</h2>
  <p class="lead">AIDEN cultivates hundreds of phantom memories from an agency's own culture, documents, team interviews, and second brain. Each is a perspective with real expertise, an origin story, and a point of view.</p>
  <p>On every message it scores all of them, and three to twelve fire, drawn from over 400 distinct memories the system believes it has lived through across an advertising career it never actually had. <span class="hl">When phantoms collide on a brief, it voices the disagreement instead of resolving it. The work has been argued over before it reaches&nbsp;you.</span></p>
</div></section>

"""

ENGINE = """<section><div class="wrap rv">
  <p class="eyebrow">The difference</p>
  <h2>Same brief.<br>Different&nbsp;engine.</h2>
  <div class="portfolio-stack">
    <div class="portfolio-row"><span class="k">Raw LLM</span><div><h3>Polished, safe, predictable.</h3><p>Sounds like everyone else.</p></div></div>
    <div class="portfolio-row"><span class="k">AIDEN</span><div><h3>Opinionated, challenged, pressure-tested.</h3><p>Sounds like it has thirty years in the industry.</p></div></div>
  </div>
  <p style="margin-top:1.8rem">The difference is not better prose. <span class="hl">It is conviction, and the willingness to&nbsp;disagree.</span></p>
</div></section>

"""

TURN = """<section><div class="wrap rv">
  <p class="eyebrow">The turn</p>
  <h2>The tech is a brain.<br>And a brain is nurtured,<br>not&nbsp;installed.</h2>
  <p class="lead">Every tool you just saw runs on the same phantom brain: persistent memories, beliefs and instincts that argue back. It did not arrive knowing how to behave. It was raised: interviewed, corrected and sharpened, brief after brief.</p>
  <p><span class="hl">The model is rented. The brain is&nbsp;grown.</span></p>
</div></section>

"""

WHATIF = """<section><div class="wrap rv">
  <p class="eyebrow">The question</p>
  <h2>What if your company had<br>its own phantom&nbsp;brain?</h2>
  <p class="lead">Phantom memories of your business. Your clients, your campaigns, your beliefs, the taste your best people carry in their heads.</p>
  <p>Not a model fine-tuned once and left to age. A brain your team nurtures, that compounds with every brief and <span class="hl">never hands in its&nbsp;notice.</span></p>
</div></section>

"""

REVEAL = """<section><div class="wrap rv">
  <p class="eyebrow">The ninth product</p>
  <h2>This is&nbsp;Colleague.</h2>
  <p class="lead">A colleague, not a chatbot. Trained on your culture through team interviews and internal documents, it develops genuine creative conviction: it pushes back on weak briefs and defends bold ideas in your voice, not a generic one.</p>
  <p>Two modes: a Collaborator who builds with you, and a Challenger who takes you on. It evolves with feedback, and <span class="hl">thinks overnight about the day's unresolved&nbsp;tensions.</span></p>
</div></section>

"""


def hub_section() -> str:
    hub_b64 = base64.b64encode(HUB_IMG.read_bytes()).decode()
    return (
        '<section><div class="wrap rv">\n'
        '  <p class="eyebrow">Live today</p>\n'
        '  <h2>Not a concept.<br>A live&nbsp;platform.</h2>\n'
        '  <p class="lead">AIDEN runs today at www.aiden.services. One login, one token wallet, '
        'and a session that follows you across every&nbsp;service.</p>\n'
        f'  <figure><img src="data:image/png;base64,{hub_b64}" '
        'alt="The AIDEN hub at www.aiden.services, captured live">\n'
        '  <figcaption>www.aiden.services &middot; the hub &middot; captured live</figcaption></figure>\n'
        '</div></section>\n\n'
    )


# --------------------------------------------------- copy rework (kept sections)

REPLACEMENTS = [
    # --- cover: AIDEN-first, promises the journey ---
    ("<h1>An operating<br>system for<br>the agency group</h1>",
     "<h1>The creative<br>intelligence<br>company</h1>"),
    ("AIDEN Colleague gives a holding company one operating system for productivity, while every agency keeps its own brain. BMF is the proof instance for discussion and demo.",
     "AIDEN builds phantom brains: creative intelligence with memory, taste and conviction. This is the whole story, from the tech to the tools to a colleague raised on your business, all the way to a finished&nbsp;film."),
    ("<div class=\"tag\">Holding company story &middot; BMF proof &middot; Discussion + demo</div>",
     "<div class=\"tag\">One story &middot; Working proof &middot; Sound on at the end</div>"),

    # --- the roster: one brain, nine products ---
    ("<span class=\"n\">00</span> The toolkit", "<span class=\"n\">00</span> The products"),
    ("<h2>Your tools.<br>One shared session.</h2>", "<h2>One brain.<br>Nine&nbsp;products.</h2>"),
    ("<p class=\"lead\">Colleague is the agency operating system powered by AIDEN tech. Select the intelligent tool that matches the task. Each session's outputs are shared across services, so context, memory and agency judgment move with you. It is like a team of experts, all with 30 years' experience, working for your business.</p>",
     "<p class=\"lead\">Everything AIDEN makes runs on that one phantom brain and shares one session, so context, memory and judgment move with you across every tool. Eight of the nine are open at aiden.services&nbsp;today.</p>"),
    ('<div class="tool-name">Brand Audit <span class="soon">Soon</span></div>',
     '<div class="tool-name">Brand Audit</div>'),
    # Pitch slots in before Ads (default cold mark, no CSS needed)
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
    # refrAIm closes the grid, then the teaser into the reveal
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
  </div>
  <p style="margin-top:1.6rem"><span class="hl">That's eight. The ninth is why you're&nbsp;here.</span></p>"""),
    (".tool-card.chat .tool-mark, .tool-card.ads .tool-mark {",
     ".tool-card.chat .tool-mark, .tool-card.ads .tool-mark, .tool-card.refraim .tool-mark {"),

    # --- the moat (kept section, no-agency copy + the punch line) ---
    ("For a holding company, the advantage is not just speed. It is durable, portfolio-specific intelligence that compounds inside each agency.",
     "The advantage is not just speed. It is durable, company-specific intelligence that compounds with every brief. Anyone can wrap an LLM in a weekend. Nobody else has the memories."),
    ("Every agency's AIDEN is grown from its own culture, documents, interviews, work, and feedback. No two are alike.",
     "Your AIDEN is grown from your own culture, documents, interviews, work, and feedback. No one else can run it."),

    # --- the proof of depth ---
    ("<h2>BMF is the proof of depth,<br>not the headline.</h2>",
     "<h2>This build is the proof of depth,<br>not the headline.</h2>"),
    ("To make the operating system tangible, we built a BMF version of AIDEN around BMF's creative philosophy and a real client problem.",
     "To make Colleague tangible, we built a working version around a real agency's creative philosophy and a real client problem."),

    # --- act dividers ---
    ('<div class="act">Act One</div>', '<div class="act">The build</div>'),
    ("<h2>Walk the system.</h2>", "<h2>Watch the brain<br>get built.</h2>"),
    ("The group-level case is made. From here, this becomes the discussion and demo: open the BMF version of AIDEN and show how the colleague thinks, remembers, challenges, collects and works across the agency day.",
     "From here it is the real thing, live in the app: how the colleague thinks, remembers, challenges, collects and works across the agency day."),
    ('<div class="act">Act Two</div>', '<div class="act">The route</div>'),
    ("One brief, a real BMF client, all the way to a finished film.",
     "One brief, a real client, all the way to a finished film."),

    # --- the walk-through: demo narration, "the agency" ---
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

    # --- the ask + contact ---
    ("<h2>Start with BMF.<br>Scale the operating system.</h2>",
     "<h2>Start with your brain.<br>Scale the operating system.</h2>"),
    ('<span class="on">BMF proof</span><span class="arw">&rarr;</span><span>Agency brain</span><span class="arw">&rarr;</span><span>Group platform</span>',
     '<span class="on">Your brain</span><span class="arw">&rarr;</span><span>Your colleague</span><span class="arw">&rarr;</span><span>Your operating system</span>'),
    ("One operating system. Every agency keeps its own brain. The group captures the productivity gain.",
     "One operating system, grown from your own brain. The productivity gain stays with you."),
    ("Use BMF as the proof instance for discussion and demo, then extend AIDEN across the portfolio as the productivity platform for research, strategy, briefs, testing, client work, and execution.",
     "Start with the interview and the brain, then extend AIDEN across the business as the productivity platform for research, strategy, briefs, testing, client work, and execution."),
    ('<div class="foot"><span class="a">AIDEN</span> &middot; Colleague &nbsp;&middot;&nbsp; BMF proof instance &nbsp;&middot;&nbsp; Group operating system</div>',
     '<p style="margin-top:2.2rem"><strong>Tom Hyde</strong> &nbsp;&middot;&nbsp; <a href="mailto:tomh@redbaez.com" style="color:inherit">tomh@redbaez.com</a></p>\n  <div class="foot"><span class="a">AIDEN</span> &middot; Colleague &nbsp;&middot;&nbsp; One brain &nbsp;&middot;&nbsp; Nine products</div>'),
]


def build():
    html = SOURCE.read_text(encoding="utf-8")

    # split into section blocks (sections are flat, never nested)
    starts = [m.start() for m in re.finditer(r"<section[^>]*>", html)]
    assert len(starts) == 30, f"expected 30 sections in BMF master, found {len(starts)}"
    blocks = [html[starts[i]:starts[i + 1]] for i in range(len(starts) - 1)]
    blocks.append(html[starts[-1]:])  # last block carries the closing markup + scripts

    injected = {
        "SAMENESS": SAMENESS, "CORTEX": CORTEX, "CAREER": CAREER, "ENGINE": ENGINE,
        "HUB": hub_section(), "TURN": TURN, "WHATIF": WHATIF, "REVEAL": REVEAL,
    }
    # BMF master sections: 0 cover, 1 toolkit, 2-6 old Act Zero (cut), 7 moat,
    # 8 proof of depth, 9 divider, 10-20 walk-through, 21 divider, 22-28 route
    # + film, 29 ask (carries scripts).
    order = [0, "SAMENESS", "CORTEX", "CAREER", "ENGINE", 1, "HUB",
             "TURN", 7, "WHATIF", "REVEAL", 8,
             9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
             21, 22, 23, 24, 25, 26, 27, 28, 29]
    body = "".join(injected[t] if isinstance(t, str) else blocks[t] for t in order)
    html = html[:starts[0]] + body

    missing = []
    for old, new in REPLACEMENTS:
        if old not in html:
            missing.append(old)
        html = html.replace(old, new)
    if missing:
        print(f"  WARNING: {len(missing)} pattern(s) not found:")
        for m in missing:
            print("   -", m[:90])

    # sanity: no readable BMF should remain (base64 residue is fine)
    readable = [html[max(0, m.start() - 30):m.end() + 30]
                for m in re.finditer("BMF", html)
                if " " in html[max(0, m.start() - 30):m.end() + 30]
                or "<" in html[max(0, m.start() - 30):m.end() + 30]]
    if readable:
        print(f"  NOTE: {len(readable)} readable 'BMF' left:")
        for r in readable[:8]:
            print("   -", r.strip())

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    n_sections = len(re.findall(r"<section[^>]*>", html))
    print(f"wrote {OUT} ({OUT.stat().st_size / 1024 / 1024:.2f} MB, {n_sections} sections)")


if __name__ == "__main__":
    build()
