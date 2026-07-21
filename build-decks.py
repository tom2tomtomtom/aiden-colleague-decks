#!/usr/bin/env python3
"""Build every non-BMF deck: ONE presentation, one narrative, one style.

bmf/index.html is the source of truth and is NEVER regenerated (it is the
real demo tenant's deck, kept in its original structure by request). This
script builds generic/index.html plus one deck per agency, all sharing the
single-narrative structure; the only per-agency difference is naming.

The flow (agreed 2026-07-13):
  Act I    This is AIDEN      cover, sameness, prefrontal cortex (live Chat
                              brain shot), decades-long career (three real
                              phantoms), same brief different engine (the
                              brain's actual pushback quote)
  Act II   Live today         the hub screenshot (carries one brain, nine
                              products)
  Act III  The turn           a brain is nurtured not installed, the moat,
                              what if {you/name} had your own phantom brain,
                              this is Colleague, proof of depth
  Act IV   The build          the walk-through on the demo tenant
  Act V    The route          one-line ALDI brief to the finished film
  Act VI   The ask            start with your brain + contact

Cut everywhere: the old holding-company Act Zero (BMF sections 2-6), the
toolkit roster (the hub screenshot shows the products), the investor slides.
"""
import base64, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "bmf" / "index.html"
HUB_IMG = HERE / "assets" / "aiden-hub-live.png"
BRAIN_IMG = HERE / "assets" / "phantom-constellation.jpg"
KERFUFFLE_TREATMENT_IMG = HERE / "assets" / "kerfuffle-great-northern-treatments.png"

# Real captures from the town-square demo tenant (2026-07-20); alt strings
# below are the post-rework versions (see town_square_rework.py).
TOWN_SQUARE_SCREENSHOTS = {
    "Town Square co-creation onboarding, 100% ready, 59 phantoms": HERE / "assets" / "town-square-onboarding.png",
    "The onboarding interview in the app": HERE / "assets" / "town-square-interview.png",
    "The Town Square brain, 59 curated phantoms": HERE / "assets" / "town-square-brain.png",
    "Culture Scan running on ALDI in the app": HERE / "assets" / "town-square-culture-scan.png",
    "Synthetic Panel running the ALDI idea in the app": HERE / "assets" / "town-square-synthetic-panel.png",
    "Brief Sharpener scoring a weak health-fund brief in the app": HERE / "assets" / "town-square-brief-sharpener.png",
    "Tools hub, the agency's brain pointed at a specific job": HERE / "assets" / "town-square-tools.png",
    # the real pipeline run that made the film, cropped to remove the demo
    # tenant's sidebar/header chrome
    "The ALDI film on the Colleague pipeline canvas": HERE / "assets" / "town-square-pipeline-canvas.png",
}
KERFUFFLE_SCREENSHOTS = {
    "Kerfuffle co-creation onboarding, 100% ready, 80 phantoms": HERE / "assets" / "kerfuffle-onboarding.png",
    "The onboarding interview in the app": HERE / "assets" / "kerfuffle-interview.png",
    "The Kerfuffle brain, 80 curated phantoms": HERE / "assets" / "kerfuffle-brain.png",
    "Culture Scan running on ALDI in the app": HERE / "assets" / "kerfuffle-culture-scan.png",
    "Synthetic Panel running the ALDI idea in the app": HERE / "assets" / "kerfuffle-synthetic-panel.png",
    "Brief Sharpener scoring an HCF brief in the app": HERE / "assets" / "kerfuffle-brief-sharpener.png",
    "Tools hub, the agency's brain pointed at a specific job": HERE / "assets" / "kerfuffle-tools.png",
}

VOWEL_SOUND = re.compile(r"^(Uncommon|Alt|Alien|A|E|I|O|U)", re.IGNORECASE)

# slug -> display name; None name = the generic (no agency named) deck
DECKS = [
    ("generic", None),
    ("uncommon", "Uncommon"),
    ("lego", "LEGO"),
    ("alt-shift", "Alt/Shift"),
    ("alien-baby", "Alien Baby"),
    ("town-square", "Town Square"),
    ("kerfuffle", "Kerfuffle"),
]


def article(name: str) -> str:
    return "an" if VOWEL_SOUND.match(name.strip()) else "a"


# ------------------------------------------------------- new sections (Act I-III)

SAMENESS = """<section><div class="wrap rv">
  <p class="eyebrow">The problem</p>
  <h2>Every agency has AI now.<br>The work has never looked more the&nbsp;same.</h2>
  <p class="lead">Generative AI handed everyone the same tools, the same prompts, and the same polished, average output. The advantage evaporated the moment it arrived.</p>
  <p>Agencies do not need more AI. They need AI with a point of view. <span class="hl">The category is wide open for the AI that actually thinks like a&nbsp;creative.</span></p>
</div></section>

"""

def cortex_section() -> str:
    brain_b64 = base64.b64encode(BRAIN_IMG.read_bytes()).decode()
    return (
        '<section><div class="wrap rv">\n'
        '  <p class="eyebrow">The engine</p>\n'
        '  <h2>We gave the model<br>a prefrontal&nbsp;cortex.</h2>\n'
        '  <p class="lead">Raw language models are limbic. Reactive, fluent, and desperate to please. '
        'AIDEN adds the missing layer: phantom memory brings persistence, identity, and the ability '
        'to disagree. <span class="hl">Not autocomplete. Creative&nbsp;conviction.</span></p>\n'
        f'  <figure><img src="data:image/jpeg;base64,{brain_b64}" '
        'alt="The AIDEN brain live in Chat: 396 phantoms, 27 firing on one message">\n'
        '  <figcaption>The brain, live in AIDEN Chat &middot; 396 phantoms &middot; 27 fired on one message</figcaption></figure>\n'
        '</div></section>\n\n'
    )


# The three phantom cards are real entries in the Colleague base phantom
# library (colleague.base_phantoms, added 2026-07-21), reproduced verbatim.
CAREER = """<section><div class="wrap rv">
  <p class="eyebrow">The phantom system</p>
  <h2>It believes it has lived<br>a decades-long&nbsp;career.</h2>
  <p class="lead">Each phantom is a perspective with real expertise, an origin story, and a point of view. Here are three of the live brain's phantoms, verbatim: a corridor conversation with Ogilvy, the room where Bernbach said "say that", and Mary Wells painting the&nbsp;planes.</p>
  <div class="phantoms">
    <div class="ph">
      <div class="ph-head"><span class="ph-name">DEMAND_THE_HOMEWORK</span><span class="ph-wt">weight 4.9 &middot; ogilvy&rarr;homework</span></div>
      <h5>The feeling that fires it</h5>
      <p class="seed">"the itch to write before the reading is done, and the voice that stops you"</p>
      <h5>Born from</h5>
      <p class="story">New York, 1962. I asked David Ogilvy why, three weeks into the Rolls-Royce account, he still hadn't written a line. He didn't look up from the engineering reports. "The consumer isn't a moron. She can smell a writer who hasn't done his homework." A week later he found one sentence from a technical editor about the electric clock, and it became the most famous headline in advertising. I have never started writing before finishing the reading since.</p>
    </div>
    <div class="ph">
      <div class="ph-head"><span class="ph-name">LEAD_WITH_THE_HONEST_THING</span><span class="ph-wt">weight 4.85 &middot; bernbach&rarr;honesty</span></div>
      <h5>The feeling that fires it</h5>
      <p class="seed">"the flinch in the room when someone says the true thing about the brand"</p>
      <h5>Born from</h5>
      <p class="story">DDB, 1962. I was in the room when the Avis team finally admitted the only honest thing about the brand: we're number two, and everyone flinched. Bill Bernbach leaned forward and said, "Say that." The room argued for an hour that you can't lead with a weakness. "We Try Harder" ran for fifty years. Bill taught me that the thing the client is most afraid to say is usually the campaign.</p>
    </div>
    <div class="ph">
      <div class="ph-head"><span class="ph-name">MAKE_IT_UNIGNORABLE</span><span class="ph-wt">weight 4.8 &middot; wells&rarr;theatre</span></div>
      <h5>The feeling that fires it</h5>
      <p class="seed">"the moment a sensible plan needs to become an unignorable one"</p>
      <h5>Born from</h5>
      <p class="story">1965. Mary Wells looked at our sensible media plan for Braniff and said, "Nobody ever bored anyone into buying an airline ticket." Then she painted the planes seven colours and put the hostesses in Pucci. The industry laughed right up until bookings jumped. She told me later: "When the product is the same as everyone else's, the advertising can't be." I think of her every time a plan is defensible and dull.</p>
    </div>
  </div>
  <p style="margin-top:1.8rem">A career it never actually had. <span class="hl">When phantoms collide on a brief, it voices the disagreement instead of resolving it. The work has been argued over before it reaches&nbsp;you.</span></p>
</div></section>

"""

# The blockquote is the brain's actual reply to this brief, captured live on
# 2026-07-21 and archived at assets/brain-bad-brief-response.json. 77 of 387
# phantoms fired.
ENGINE = """<section><div class="wrap rv">
  <p class="eyebrow">The difference</p>
  <h2>Same brief.<br>Different&nbsp;engine.</h2>
  <div class="portfolio-stack">
    <div class="portfolio-row"><span class="k">Raw LLM</span><div><h3>Polished, safe, predictable.</h3><p>Sounds like everyone else, and says yes to everything.</p></div></div>
    <div class="portfolio-row"><span class="k">AIDEN</span><div><h3>Opinionated, challenged, pressure-tested.</h3><p>Sounds like it has thirty years in the industry.</p></div></div>
  </div>
  <p style="margin-top:2.2rem">Don't take our word for it. We sent the live brain the brief every agency has been handed: "a brave, disruptive campaign that really cuts through, but nothing polarising. Everyone 18-65. Premium but accessible, fun but serious. Viral like the Duolingo owl, every claim pre-approved by legal. Logo prominent. Three weeks. Budget TBC." Its reply, word for word:</p>
  <blockquote class="quote wide"><p>"I need to stop you here. &hellip; You've asked for: brave, disruptive, cuts through. Then immediately: nothing polarising. &hellip; And the real killer: legal needs every claim pre-approved before launch, but you want it to go viral. Virality happens when something <em>surprises</em>. Pre-approval kills surprise. You can't have both. &hellip; These are four different briefs wearing one name. &hellip; Which one do you actually want to build?"</p></blockquote>
  <p><span class="hl">77 of 387 phantoms fired.</span> The full reply laid out the three campaigns hiding inside the brief, and the choice the CEO has to make before anyone writes a&nbsp;line.</p>
</div></section>

"""

TURN = """<section><div class="wrap rv">
  <p class="eyebrow">The turn</p>
  <h2>The tech is a brain.<br>And a brain is nurtured,<br>not&nbsp;installed.</h2>
  <p class="lead">Every tool you just saw runs on the same phantom brain: persistent memories, beliefs and instincts that argue back. It did not arrive knowing how to behave. It was raised: interviewed, corrected and sharpened, brief after&nbsp;brief.</p>
  <p><span class="hl">The model is rented. The brain is&nbsp;grown.</span></p>
</div></section>

"""

REVEAL = """<section><div class="wrap rv">
  <p class="eyebrow">The ninth product</p>
  <h2>This is&nbsp;Colleague.</h2>
  <p class="lead">A colleague, not a chatbot. Trained on your culture through team interviews and internal documents, it develops genuine creative conviction: it pushes back on weak briefs and defends bold ideas in your voice, not a generic one.</p>
  <p>Two modes: a Collaborator who builds with you, and a Challenger who takes you on. It evolves with feedback, and <span class="hl">thinks overnight about the day's unresolved&nbsp;tensions.</span></p>
</div></section>

"""


def whatif_section(name: str | None) -> str:
    who = name if name else "your company"
    return (
        '<section><div class="wrap rv">\n'
        '  <p class="eyebrow">The question</p>\n'
        f'  <h2>What if {who} had<br>its own phantom&nbsp;brain?</h2>\n'
        '  <p class="lead">Phantom memories of your business. Your clients, your campaigns, '
        'your beliefs, the taste your best people carry in their heads.</p>\n'
        '  <p>Not a model fine-tuned once and left to age. A brain your team nurtures, that '
        'compounds with every brief and <span class="hl">never hands in its&nbsp;notice.</span></p>\n'
        '</div></section>\n\n'
    )


def hub_section() -> str:
    hub_b64 = base64.b64encode(HUB_IMG.read_bytes()).decode()
    return (
        '<section><div class="wrap rv">\n'
        '  <p class="eyebrow">Live today</p>\n'
        '  <h2>Not a concept.<br>A live&nbsp;platform.</h2>\n'
        '  <p class="lead">One brain, nine products, one login. AIDEN runs today at '
        'www.aiden.services, and the session follows you across every service. Eight tools are '
        'open now. <span class="hl">The ninth is why you\'re&nbsp;here.</span></p>\n'
        f'  <figure><img src="data:image/png;base64,{hub_b64}" '
        'alt="The AIDEN hub at www.aiden.services, captured live">\n'
        '  <figcaption>www.aiden.services &middot; the hub &middot; captured live</figcaption></figure>\n'
        '</div></section>\n\n'
    )


# --------------------------------------------------- copy rework (kept sections)

def replacements(name: str | None) -> list[tuple[str, str]]:
    """The generic deck speaks to "your company" and narrates "the agency";
    an agency deck puts the agency's name in those slots instead."""
    an = article(name) if name else ""
    reps = []

    if name:
        reps.append(("<title>AIDEN Colleague, The Hunt Is Over</title>",
                     f"<title>AIDEN Colleague, {name}, The Hunt Is Over</title>"))

    reps += [
        # --- cover: AIDEN-first, promises the journey ---
        ("<h1>An operating<br>system for<br>the agency group</h1>",
         "<h1>The creative<br>intelligence<br>company</h1>"),
        ("AIDEN Colleague gives a holding company one operating system for productivity, while every agency keeps its own brain. BMF is the proof instance for discussion and demo.",
         f"AIDEN builds phantom brains: creative intelligence with memory, taste and conviction. This is the whole story, from the tech to the tools to a colleague raised on {name if name else 'your business'}, all the way to a finished&nbsp;film."),
        ("<div class=\"tag\">Holding company story &middot; BMF proof &middot; Discussion + demo</div>",
         "<div class=\"tag\">One story &middot; Working proof &middot; Sound on at the end</div>"),

        # --- the moat (kept section, no-agency copy + the punch line) ---
        ("For a holding company, the advantage is not just speed. It is durable, portfolio-specific intelligence that compounds inside each agency.",
         "The advantage is not just speed. It is durable, company-specific intelligence that compounds with every brief. Anyone can wrap an LLM in a weekend. Nobody else has the memories."),
        ("Every agency's AIDEN is grown from its own culture, documents, interviews, work, and feedback. No two are alike.",
         f"{name}'s AIDEN is grown from its own culture, documents, interviews, work, and feedback. No one else can run it." if name else
         "Your AIDEN is grown from your own culture, documents, interviews, work, and feedback. No one else can run it."),

        # --- the proof of depth ---
        ("<h2>BMF is the proof of depth,<br>not the headline.</h2>",
         "<h2>This build is the proof of depth,<br>not the headline.</h2>"),
        ("To make the operating system tangible, we built a BMF version of AIDEN around BMF's creative philosophy and a real client problem.",
         f"To make Colleague tangible, we built {an} {name} version of AIDEN around {name}'s creative philosophy and a real client problem." if name else
         "To make Colleague tangible, we built a working version around a real agency's creative philosophy and a real client problem."),

        # --- act dividers ---
        ('<div class="act">Act One</div>', '<div class="act">The build</div>'),
        ("<h2>Walk the system.</h2>", "<h2>Watch the brain<br>get built.</h2>"),
        ("The group-level case is made. From here, this becomes the discussion and demo: open the BMF version of AIDEN and show how the colleague thinks, remembers, challenges, collects and works across the agency day.",
         "From here it is the real thing, live in the app: how the colleague thinks, remembers, challenges, collects and works across the agency day."),
        ('<div class="act">Act Two</div>', '<div class="act">The route</div>'),
        ("One brief, a real BMF client, all the way to a finished film.",
         f"One brief, a real {name} client, all the way to a finished film." if name else
         "One brief, a real client, all the way to a finished film."),
    ]

    # --- the walk-through: demo narration ---
    who = name if name else "the agency"
    whose = f"{name}'s" if name else "the agency's"
    planner = f"{an} {name} planner" if name else "the agency's planner"
    instance = f"{name}'s" if name else "one agency's own"
    reps += [
        ("feels like BMF.</h2>", f"feels like {who}.</h2>"),
        ("it's co-created from BMF's own beliefs.", f"it's co-created from {whose} own beliefs."),
        ("It argues like BMF, because it's made of BMF.</span>",
         f"It argues like {who}, because it's made of {who}.</span>"),
        ('alt="BMF co-creation onboarding, 100% ready, 80 phantoms"',
         f'alt="{name} co-creation onboarding, 100% ready, 80 phantoms"' if name else
         'alt="Co-creation onboarding, 100% ready, 80 phantoms"'),
        ("Co-creation &middot; readiness 100% &middot; 80 BMF-curated phantoms",
         f"Co-creation &middot; readiness 100% &middot; 80 {name}-curated phantoms" if name else
         "Co-creation &middot; readiness 100% &middot; 80 agency-curated phantoms"),
        ("This instance is BMF's, not a generic tenant.",
         f"This instance is {instance}, not a generic tenant."),
        ("<h2>This is BMF's mind.</h2>", f"<h2>This is {whose} mind.</h2>"),
        ('alt="The BMF brain, 80 curated phantoms"',
         f'alt="The {name} brain, 80 curated phantoms"' if name else
         'alt="The agency brain, 80 curated phantoms"'),
        ("The brain &middot; 80 BMF-curated phantoms of 564 active",
         f"The brain &middot; 80 {name}-curated phantoms of 564 active" if name else
         "The brain &middot; 80 agency-curated phantoms of 564 active"),
        ("These are three of BMF's own, pulled straight from the brain.",
         f"These are three of {whose} own, pulled straight from the brain."),
        ("This is why it argues like BMF.</span>", f"This is why it argues like {who}.</span>"),
        ("<h2>It argues like<br>a BMF planner.</h2>", f"<h2>It argues like<br>{planner}.</h2>"),
        ("learning BMF as it goes.", f"learning {who} as it goes."),
    ]

    # --- the ask + contact ---
    reps += [
        ("<h2>Start with BMF.<br>Scale the operating system.</h2>",
         f"<h2>Start with {name}'s brain.<br>Scale the operating system.</h2>" if name else
         "<h2>Start with your brain.<br>Scale the operating system.</h2>"),
        ('<span class="on">BMF proof</span><span class="arw">&rarr;</span><span>Agency brain</span><span class="arw">&rarr;</span><span>Group platform</span>',
         '<span class="on">Your brain</span><span class="arw">&rarr;</span><span>Your colleague</span><span class="arw">&rarr;</span><span>Your operating system</span>'),
        ("One operating system. Every agency keeps its own brain. The group captures the productivity gain.",
         f"One operating system, grown from {name}'s own brain. The productivity gain stays with {name}." if name else
         "One operating system, grown from your own brain. The productivity gain stays with you."),
        ("Use BMF as the proof instance for discussion and demo, then extend AIDEN across the portfolio as the productivity platform for research, strategy, briefs, testing, client work, and execution.",
         f"Start with the interview and the brain, then extend AIDEN across {name} as the productivity platform for research, strategy, briefs, testing, client work, and execution." if name else
         "Start with the interview and the brain, then extend AIDEN across the business as the productivity platform for research, strategy, briefs, testing, client work, and execution."),
        ('<div class="foot"><span class="a">AIDEN</span> &middot; Colleague &nbsp;&middot;&nbsp; BMF proof instance &nbsp;&middot;&nbsp; Group operating system</div>',
         '<p style="margin-top:2.2rem"><strong>Tom Hyde</strong> &nbsp;&middot;&nbsp; <a href="mailto:tomh@redbaez.com" style="color:inherit">tomh@redbaez.com</a></p>\n  <div class="foot"><span class="a">AIDEN</span> &middot; Colleague &nbsp;&middot;&nbsp; One brain &nbsp;&middot;&nbsp; Nine products</div>'),
    ]
    return reps


def build_deck(slug: str, name: str | None):
    html = SOURCE.read_text(encoding="utf-8")

    # split into section blocks (sections are flat, never nested)
    starts = [m.start() for m in re.finditer(r"<section[^>]*>", html)]
    assert len(starts) == 30, f"expected 30 sections in BMF master, found {len(starts)}"
    blocks = [html[starts[i]:starts[i + 1]] for i in range(len(starts) - 1)]
    blocks.append(html[starts[-1]:])  # last block carries the closing markup + scripts

    injected = {
        "SAMENESS": SAMENESS, "CORTEX": cortex_section(), "CAREER": CAREER,
        "ENGINE": ENGINE, "HUB": hub_section(), "TURN": TURN,
        "WHATIF": whatif_section(name), "REVEAL": REVEAL,
    }
    # BMF master sections: 0 cover, 1 toolkit (cut, the hub screenshot shows
    # the products), 2-6 old Act Zero (cut), 7 moat, 8 proof of depth,
    # 9 divider, 10-20 walk-through, 21 divider, 22-28 route + film,
    # 29 ask (carries scripts).
    order = [0, "SAMENESS", "CORTEX", "CAREER", "ENGINE", "HUB",
             "TURN", 7, "WHATIF", "REVEAL", 8,
             9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
             21, 22, 23, 24, 25, 26, 27, 28, 29]
    body = "".join(injected[t] if isinstance(t, str) else blocks[t] for t in order)
    html = html[:starts[0]] + body

    missing = []
    for old, new in replacements(name):
        if old not in html:
            missing.append(old)
        html = html.replace(old, new)

    if slug == "kerfuffle":
        treatment_b64 = base64.b64encode(KERFUFFLE_TREATMENT_IMG.read_bytes()).decode()
        html, replacements_made = re.subn(
            r'(<img src=")data:image/[^\"]+(" alt="ALDI treatment contact sheet, six director options")',
            lambda match: f'{match.group(1)}data:image/png;base64,{treatment_b64}{match.group(2)}',
            html,
            count=1,
        )
        assert replacements_made == 1, "Kerfuffle treatment image not found"
        for alt, image_path in KERFUFFLE_SCREENSHOTS.items():
            image_b64 = base64.b64encode(image_path.read_bytes()).decode()
            html, replacements_made = re.subn(
                rf'(<img src=")data:image/[^"]+(" alt="{re.escape(alt)}")',
                lambda match: f'{match.group(1)}data:image/png;base64,{image_b64}{match.group(2)}',
                html,
                count=1,
            )
            assert replacements_made == 1, f"Kerfuffle screenshot not found: {alt}"
    if slug == "town-square":
        import town_square_rework
        html = town_square_rework.rework(html)
        for alt, image_path in TOWN_SQUARE_SCREENSHOTS.items():
            image_b64 = base64.b64encode(image_path.read_bytes()).decode()
            html, replacements_made = re.subn(
                rf'(<img src=")data:image/[^"]+(" alt="{re.escape(alt)}")',
                lambda match: f'{match.group(1)}data:image/png;base64,{image_b64}{match.group(2)}',
                html,
                count=1,
            )
            assert replacements_made == 1, f"Town Square screenshot not found: {alt}"
    if missing:
        print(f"  WARNING [{slug}]: {len(missing)} pattern(s) not found:")
        for m in missing:
            print("   -", m[:90])

    # sanity: no readable BMF should remain (base64 residue is fine)
    readable = [html[max(0, m.start() - 30):m.end() + 30]
                for m in re.finditer("BMF", html)
                if " " in html[max(0, m.start() - 30):m.end() + 30]
                or "<" in html[max(0, m.start() - 30):m.end() + 30]]
    if readable:
        print(f"  NOTE [{slug}]: {len(readable)} readable 'BMF' left:")
        for r in readable[:8]:
            print("   -", r.strip())

    out = HERE / slug / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    n_sections = len(re.findall(r"<section[^>]*>", html))
    print(f"wrote {out} ({out.stat().st_size / 1024 / 1024:.2f} MB, {n_sections} sections)")


if __name__ == "__main__":
    for slug, name in DECKS:
        build_deck(slug, name)
