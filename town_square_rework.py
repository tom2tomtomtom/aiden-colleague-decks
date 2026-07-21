"""Town Square deck rework: every example and screenshot comes from the real
town-square demo tenant (townsquare.deck.demo.20260720@redbaez.com, captured
2026-07-20), not from BMF's tenant or another agency's clients.

Replaces: the three phantom cards (were BMF lore: Good Different 2008,
Tourism Tasmania, the Penrith laugh test), the HCF Brief Sharpener example
(HCF is a BMF client; now the tenant's real 18/100 run on a generic weak
health-fund brief), the LEGO World Cup board (now built from the tenant's
real ALDI Culture Scan), the synthetic-panel persona quotes (now the
tenant's real panel run), the curated-phantom counts (59/543, not 80/564),
and the false "a real Town Square client" claim about ALDI.
"""
import re

# ---------------------------------------------------------------- simple text
TEXT_REPLACEMENTS = [
    # counts: the real tenant has 59 curated phantoms of 543 active
    (', 80 phantoms"', ', 59 phantoms"'),
    ('80 curated phantoms', '59 curated phantoms'),
    ('80 Town Square-curated phantoms', '59 Town Square-curated phantoms'),
    ('of 564 active', 'of 543 active'),
    # ALDI is not a Town Square client; don't claim it is
    ('One brief, a real Town Square client, all the way to a finished film.',
     'One brief, a brand every Australian knows, all the way to a finished film.'),
    # Brief Sharpener: HCF out, the tenant's real run in
    ('A thin HCF brief comes back a blunt <span class="hl">28 out of 100.</span>',
     'A deliberately weak health-fund brief comes back a blunt <span class="hl">18 out of 100.</span>'),
    ('alt="Brief Sharpener scoring an HCF brief in the app"',
     'alt="Brief Sharpener scoring a weak health-fund brief in the app"'),
    ('Brief Sharpener &middot; HCF &middot; live in the app',
     'Brief Sharpener &middot; live in the app'),
    ('<span class="tool">Brief Sharpener &middot; HCF</span>',
     '<span class="tool">Brief Sharpener</span>'),
    ('<span class="score bad">30<small>/100</small></span>',
     '<span class="score bad">18<small>/100</small></span>'),
    # board intro: the board came from the ALDI exchange, not a LEGO one
    ('This board built itself from the creator-campaign exchange:',
     'This board built itself from the ALDI exchange:'),
]

# ------------------------------------------------------- sharpener card guts
DIMS = '''<ul class="dims">
      <li>Clear objective <span class="sc bad">2/10</span></li>
      <li>Audience definition <span class="sc bad">1/10</span></li>
      <li>Brand context <span class="sc bad">0/10</span></li>
      <li>Specific deliverables <span class="sc ok">6/10</span></li>
      <li>Tone of voice <span class="sc mid">3/10</span></li>
      <li>Budget and constraints <span class="sc bad">0/10</span></li>
      <li>Timeline <span class="sc bad">0/10</span></li>
      <li>Success metrics <span class="sc bad">0/10</span></li>
    </ul>'''

SHARPENER_PERSONAS = '''<div class="persona"><span class="pn"><b>The strategist who interrogates the ask</b> &middot; 2/10</span><q>They've told you what they want, TikTok content that goes viral, but not what they need. Gen Z actively avoids thinking about health insurance because it represents adult responsibility they're not ready for. This brief solves the wrong problem.</q><span class="pfix"><b>Fix</b> Spend a week not answering this brief. Interview the audience. Come back with the real problem, not the symptom.</span></div>
    <div class="persona"><span class="pn"><b>The founder who filters for meaningful positive change</b> &middot; 3/10</span><q>'Feel good and be part of the conversation' is code for getting attention without taking a position. The category is rife with real problems, cost, access, confusion. This brief ignores all of it in favour of being likeable.</q><span class="pfix"><b>Fix</b> Ask what meaningful positive change this creates for the audience. If the answer is 'awareness', walk away.</span></div>
    <div class="persona"><span class="pn"><b>The creative director who spots inauthenticity instantly</b> &middot; 1/10</span><q>'Viral and shareable' is what clients say when they want the magic without understanding why it worked. Trend-chasing dressed up as strategy. Gen Z will smell it from the first frame.</q></div>
    <div class="persona"><span class="pn"><b>The strategist who pushes back in meeting one</b> &middot; 2/10</span><q>Everyone's nodding at 'warm and trustworthy' like it's a strategy. Every health brand wants that. No tension, no edge, no reason for Gen Z to choose this over doing nothing, which is what most of them are doing.</q></div>'''

FRAMEWORKS = '''<ul class="fw">
      <li><span class="fwsc">0/5</span><span class="fwn">Research-Led Proposition</span><span class="fwa">There is no proposition here, provable or otherwise. Build a single promise from actual research.</span></li>
      <li><span class="fwsc">1/5</span><span class="fwn">Human Truth</span><span class="fwa">'Gen Z wants insurance to feel relevant' is a client assumption, not an insight. Start with what it represents: fear of adulthood, financial burden.</span></li>
      <li><span class="fwsc">0/5</span><span class="fwn">Creative Tension</span><span class="fwa">Name it: they know they need it but avoid it, because it forces them to confront mortality and financial precarity.</span></li>
      <li><span class="fwsc">1/5</span><span class="fwn">Impact First</span><span class="fwa">'Viral and shareable' is not an impact strategy. It's a distribution hope.</span></li>
      <li><span class="fwsc">1/5</span><span class="fwn">Cultural Ambition</span><span class="fwa">'Part of the conversation' without naming the conversation, or what the brand contributes to it.</span></li>
      <li><span class="fwsc">0/5</span><span class="fwn">USP Clarity</span><span class="fwa">No mention of what this brand offers that competitors don't. Without it, this is generic category advertising.</span></li>
      <li><span class="fwsc">0/5</span><span class="fwn">Audience Empathy</span><span class="fwa">'18-30 year olds' is a demographic, not an understanding. Quote real Gen Z in the brief. Prove someone listened.</span></li>
    </ul>'''

BENCHMARKS = '''<ul class="bench">
      <li><b>Dumb Ways to Die, Metro Trains.</b> Made a category people avoid thinking about culturally unavoidable. Entertaining first, educational second.</li>
      <li><b>The Truth, Truth Initiative.</b> Respected young people's intelligence and gave them agency. A youth movement, not an ad campaign.</li>
      <li><b>Like a Girl, Always.</b> Turned an embarrassing category into a cultural conversation about confidence and identity.</li>
    </ul>'''

REWRITE = '''<div class="rewrite">
      <div class="rtitle">Then it rewrote the brief</div>
      <h5>The idea</h5>
      <p>Make getting health insurance feel like self-care, not surrender.</p>
      <h5>The barrier</h5>
      <p>Gen Z knows they need it and actively avoids it. It means admitting you're mortal, broke, and alone, so they do nothing until a crisis forces their hand.</p>
      <h5>The truth</h5>
      <p>They don't need reassuring. They need the absurdity acknowledged and the hard thing made easier, honest bordering on blunt, the friend who says the thing because they actually care.</p>
      <h5>The tension</h5>
      <p>From "something I'll deal with when I have to" to "a small act of taking care of myself."</p>
    </div>'''

# -------------------------------------------------------------- board cards
BOARD = '''<div class="board">
    <div class="bcard insight"><span class="bt">Insight</span><div class="bh">Budget Mastery Is Aspirational Now</div><p>Financial competence is aspirational and thrift is strategic, not shameful. Shoppers want systems that make them feel smart, not stretched.</p></div>
    <div class="bcard insight"><span class="bt">Insight</span><div class="bh">The $5 Ice Cubes Test</div><p>The meme is a live test of whether the brand can handle being policed by its own fans. A value contract so strong customers publicly shame deviations is brand equity, not a crisis.</p></div>
    <div class="bcard insight"><span class="bt">Insight</span><div class="bh">Haul Content Is Survival Math</div><p>People aren't filming grocery trips for fun. They're documenting survival math, and ALDI is cheap enough to be the hero and legible as smart rather than struggling.</p></div>
    <div class="bcard idea"><span class="bt">Idea</span><div class="bh">Own Household Intelligence</div><p>Stop defending on price comparisons. Make ALDI the protagonist of household intelligence, not the cheap alternative.</p></div>
    <div class="bcard idea"><span class="bt">Idea</span><div class="bh">Amplify The Haul Creators</div><p>Product seeding and zero-strings partnerships with the budget-haul creators already making ALDI the hero of comparison content.</p></div>
    <div class="bcard idea"><span class="bt">Idea</span><div class="bh">Answer The Meme In 72 Hours</div><p>Meet the $5 ice cubes moment with self-aware humour in owned channels while the meme is still warm. Silence reads as tone-deaf.</p></div>
    <div class="bcard copy"><span class="bt">Copy</span><div class="bh">The Route Line</div><p>"The Hunt Is Over."</p></div>
    <div class="bcard copy"><span class="bt">Copy</span><div class="bh">The Promise</div><p>"No need to check twice."</p></div>
    <div class="bcard copy"><span class="bt">Copy</span><div class="bh">The Endline</div><p>"Good Different."</p></div>
  </div>'''

# ----------------------------------------------------- phantom trio (tenant)
PHANTOMS = '''<div class="phantoms">
    <div class="ph">
      <div class="ph-head"><span class="ph-name">NO_GENERIC_WORK</span><span class="ph-wt">weight 5.0 &middot; the highest in the brain</span></div>
      <h5>The feeling that fires it</h5>
      <p class="seed">"You're reviewing the work and it's good. Polished. On-strategy. And it could run for any of their competitors with a logo swap. Your chest tightens. Because good isn't the bar. Distinctive is."</p>
      <h5>Born from</h5>
      <p class="story">Marcus, founding partner, 2004. A packaged goods client, first major pitch. The team presented work that tested well and hit all the beats. Marcus asked one question: "Could we run this for their biggest competitor?" Silence. "Then it's not finished." They missed the pitch deadline, and won the business three months later with work that could only belong to that brand. The question became the filter.</p>
      <div class="trig"><span>distinctive</span><span>generic</span><span>category</span><span>competitors</span><span>unique</span><span>brand</span></div>
    </div>
  </div>'''

# ------------------------------------------- synthetic panel persona quotes
PANEL_PERSONAS = [
    ("<b>Priya</b>",
     '<div class="persona"><span class="pn"><b>Emma Chen</b> &middot; intent 3/10 &middot; skeptical</span><q>Not another \'we\'re the calm in the storm\' ad. ALDI built its reputation on being scrappy and no-nonsense, not a zen shopping sanctuary.</q></div>'),
    ("<b>Zoe</b>",
     '<div class="persona"><span class="pn"><b>Zara Ahmed</b> &middot; intent 6/10 &middot; skeptical</span><q>I get the vibe, but I like hunting for deals when I have time, and when I don\'t I\'m not in a supermarket anyway, I\'m on Deliveroo. \'Good Different\' feels a bit 2019, like it\'s trying to be Apple but for beans.</q></div>'),
    ("<b>Josh</b>",
     '<div class="persona"><span class="pn"><b>Marcus Foster</b> &middot; intent 3/10 &middot; dismissive</span><q>I\'ve been to ALDI. It\'s not calm, it\'s frantic chaos at the tills. And the \'stressed shopper\' thing is patronising, like we\'re idiots who can\'t handle a promotion.</q></div>'),
]


def _swap_block(html, start_anchor, end_anchor, new_block, label, search_from=0):
    i = html.index(start_anchor, search_from)
    j = html.index(end_anchor, i) + len(end_anchor)
    return html[:i] + new_block + html[j:]


def rework(html):
    for old, new in TEXT_REPLACEMENTS:
        assert old in html, f"town-square rework: missing text anchor: {old[:70]}"
        html = html.replace(old, new)

    html = _swap_block(html, '<ul class="dims">', '</ul>', DIMS, 'dims')
    html = _swap_block(html, '<ul class="fw">', '</ul>', FRAMEWORKS, 'frameworks')
    html = _swap_block(html, '<ul class="bench">', '</ul>', BENCHMARKS, 'benchmarks')
    html = _swap_block(html, '<div class="rewrite">', '</div>\n  </div>\n</div></section>', REWRITE + '\n  </div>\n</div></section>', 'rewrite')
    html = _swap_block(html, '<div class="board">', '</div>\n  <p style="margin-top:1.6rem">', BOARD + '\n  <p style="margin-top:1.6rem">', 'board')

    # sharpener personas: the four HCF phantom voices, replaced as one run
    i = html.index('<div class="persona"><span class="pn"><b>The platform-builder</b>')
    j = html.index('<h4>Against the strategic frameworks</h4>', i)
    html = html[:i] + SHARPENER_PERSONAS + '\n    ' + html[j:]

    # phantom trio: the container that follows "pulled straight from the brain"
    k = html.index('already outranking most of the library.')
    html = _swap_block(html, '<div class="phantoms">', '</div></section>',
                       PHANTOMS + '\n</div></section>', 'phantoms', search_from=k)

    # panel persona quotes
    for name_anchor, new_div in PANEL_PERSONAS:
        pattern = re.compile(r'<div class="persona"><span class="pn">' + re.escape(name_anchor) + r'.*?</q></div>', re.S)
        html, n = pattern.subn(new_div, html, count=1)
        assert n == 1, f"town-square rework: panel persona not found: {name_anchor}"
    return html
