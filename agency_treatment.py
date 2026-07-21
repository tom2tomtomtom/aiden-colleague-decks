"""Parameterized per-agency deck treatment (generalises town_square_rework.py).

For each treated agency, `treatment-data/<slug>/` holds the REAL outputs from
that agency's demo tenant (created and captured 2026-07-21):
  counts.json           curated/total phantom counts, tool scores
  phantoms.json         top approved agency_phantoms rows (REST export)
  sharpener-output.txt  full Brief Sharpener innerText for the weak brief run
  panel-output.txt      full Synthetic Panel innerText for the ALDI concept run
Screenshots live at assets/<slug>-*.png and are swapped by build-decks.py.

Everything injected into the deck is parsed from those files, so the deck only
claims what the tenant actually produced.
"""
import html as html_mod
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent

# The ALDI board content is culture-scan-derived and agency-agnostic (one
# route, reused by design, like the film).
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

BENCH_FALLBACK = [
    ("Dumb Ways to Die, Metro Trains.", "Made a category people avoid thinking about culturally unavoidable. Entertaining first, educational second."),
]


def esc(s):
    return html_mod.escape(s, quote=False).replace('"', '"')


def first_sentences(text, limit=230):
    text = ' '.join(text.split())
    if len(text) <= limit:
        return text
    cut = text[:limit]
    for stop in ['. ', '! ', '? ']:
        k = cut.rfind(stop)
        if k > 80:
            return cut[:k + 1].strip()
    return cut.rstrip() + '…'


# ------------------------------------------------------------------ parsers

def parse_sharpener(txt):
    out = {}
    m = re.search(r'Score\n(\d+)/100', txt)
    out['score'] = int(m.group(1))
    dims = []
    dim_block = txt.split('Completeness across the 8 brief dimensions.')[1]
    dim_block = dim_block.split('What the brief actually says')[0]
    lines = [l.strip() for l in dim_block.split('\n') if l.strip()]
    for i in range(0, len(lines) - 2, 3):
        name, score, label = lines[i], lines[i + 1], lines[i + 2]
        if not re.fullmatch(r'\d+/10', score):
            continue
        dims.append((name, score, label))
    out['dims'] = dims[:8]

    personas = []
    pp = txt.split('Phantom perspectives')[1].split('Against the strategic frameworks')[0]
    plines = [l.rstrip() for l in pp.split('\n')]
    i = 0
    while i < len(plines):
        line = plines[i].strip()
        nxt = plines[i + 1].strip() if i + 1 < len(plines) else ''
        if line and re.fullmatch(r'\d+/10', nxt):
            name, score = line, nxt
            j = i + 2
            paras = []
            fix = None
            while j < len(plines):
                cand = plines[j].strip()
                peek = plines[j + 1].strip() if j + 1 < len(plines) else ''
                if cand and re.fullmatch(r'\d+/10', peek):
                    break
                if cand.startswith('Fix:'):
                    fix = cand[4:].strip()
                elif cand:
                    paras.append(cand)
                j += 1
            personas.append({'name': name, 'score': score,
                             'quote': first_sentences(' '.join(paras), 260),
                             'fix': first_sentences(fix, 180) if fix else None})
            i = j
        else:
            i += 1
    out['personas'] = personas[:4]

    fws = []
    fw = txt.split('Against the strategic frameworks')[1].split('Benchmark campaigns')[0]
    fw = fw.split('Graded on')[1] if 'Graded on' in fw else fw
    flines = [l.strip() for l in fw.split('\n') if l.strip()]
    i = 0
    while i + 1 < len(flines):
        name, score = flines[i], flines[i + 1]
        if re.fullmatch(r'\d+/5', score):
            j = i + 2
            body = []
            while j < len(flines) and not (j + 1 < len(flines) and re.fullmatch(r'\d+/5', flines[j + 1])):
                body.append(flines[j])
                j += 1
            advice = next((b[8:].strip() for b in body if b.startswith('Advice:')), ' '.join(body))
            fws.append((score, name, first_sentences(advice, 150)))
            i = j
        else:
            i += 1
    out['frameworks'] = fws[:7]

    bench = []
    if 'Benchmark campaigns' in txt:
        bb = txt.split('Benchmark campaigns')[1].split('Gaps')[0]
        blines = [l.strip() for l in bb.split('\n') if l.strip()]
        blines = [l for l in blines if not l.startswith('Briefs that nailed')]
        i = 0
        while i < len(blines):
            title = blines[i]
            if '·' in title or ',' in title:
                desc = blines[i + 1] if i + 1 < len(blines) else ''
                bench.append((title.replace(' · ', ', ') + '.', first_sentences(desc, 140)))
                i += 2
            else:
                i += 1
    out['bench'] = bench[:3] or BENCH_FALLBACK
    return out


def parse_panel(txt):
    out = {}
    m = re.search(r'Pressure score\n(\d+)/100', txt)
    out['score'] = int(m.group(1)) if m else None
    personas = []
    if 'Panel reactions' in txt:
        pr = txt.split('Panel reactions')[1]
        plines = [l.rstrip() for l in pr.split('\n')]
        i = 0
        while i < len(plines) and len(personas) < 3:
            line = plines[i].strip()
            nxt = plines[i + 1].strip() if i + 1 < len(plines) else ''
            if line and re.fullmatch(r'intent \d+/10', nxt):
                name = line
                intent = nxt
                label = plines[i + 2].strip() if i + 2 < len(plines) else ''
                j = i + 3
                # skip the posture line (first non-empty), take the next paragraph
                paras = [p.strip() for p in plines[j:j + 14] if p.strip()]
                quote = first_sentences(paras[1] if len(paras) > 1 else paras[0], 230)
                personas.append({'name': name, 'intent': intent, 'label': label, 'quote': quote})
                i = j + 2
            else:
                i += 1
    out['personas'] = personas
    return out


def parse_rewrite(txt):
    """Extract up to 4 sections of the tool's sharpened rewrite, keeping the
    run's own section names (formats vary: '## Header' or 'Header:' lines)."""
    if 'Sharpened rewrite' not in txt:
        return None
    rw = txt.split('Sharpened rewrite')[1].split('Recent runs')[0]
    sections = []          # (label, [body lines])
    cur = None
    for raw in rw.split('\n'):
        line = raw.strip()
        if not line:
            continue
        m = (re.match(r'^##\s*(.+)$', line)
             or re.match(r"^([A-Z][^:]{2,48}):$", line)
             or (re.match(r"^([A-Z][A-Za-z'()/ ]{2,48})$", line)
                 if not line.endswith('.') and not line.startswith('-') else None))
        if m:
            cur = [m.group(1).strip(), []]
            sections.append(cur)
        elif cur:
            cur[1].append(line)
        elif len(line) < 80 and not line.endswith('.') and not sections:
            sections.append([ 'The idea', [re.sub(r'^Brief:\s*', '', line)] ])  # standalone title line
    picked = [(h, first_sentences(' '.join(b), 240)) for h, b in sections if b][:4]
    return picked if len(picked) >= 3 else None


def rewrite_block(picked):
    rows = '\n'.join(f'      <h5>{esc(h)}</h5>\n      <p>{esc(t)}</p>' for h, t in picked)
    return f"""<div class="rewrite">
      <div class="rtitle">Then it rewrote the brief</div>
{rows}
    </div>"""


# ------------------------------------------------------------------ builders

def sharpener_card(sh, name):
    cls = lambda s: 'bad' if int(s.split('/')[0]) <= 1 else ('ok' if int(s.split('/')[0]) >= 6 else 'mid')
    dims = '\n'.join(
        f'      <li>{esc(n)} <span class="sc {cls(s)}">{s}</span></li>' for n, s, _ in sh['dims'])
    personas = []
    for p in sh['personas']:
        fix = f'<span class="pfix"><b>Fix</b> {esc(p["fix"])}</span>' if p['fix'] else ''
        personas.append(
            f'    <div class="persona"><span class="pn"><b>{esc(p["name"])}</b> &middot; {p["score"]}</span>'
            f'<q>{esc(p["quote"])}</q>{fix}</div>')
    fws = '\n'.join(
        f'      <li><span class="fwsc{" ok" if int(s.split("/")[0]) >= 2 else ""}">{s}</span>'
        f'<span class="fwn">{esc(n)}</span><span class="fwa">{esc(a)}</span></li>'
        for s, n, a in sh['frameworks'])
    bench = '\n'.join(f'      <li><b>{esc(t)}</b> {esc(d)}</li>' for t, d in sh['bench'])
    return dims, '\n'.join(personas), fws, bench


def phantom_card(ph, name):
    trig = ''.join(f'<span>{esc(t)}</span>' for t in (ph.get('word_triggers') or [])[:6])
    return f'''<div class="phantoms">
    <div class="ph">
      <div class="ph-head"><span class="ph-name">{esc(ph['shorthand'].upper().replace('→', '_').replace(' ', '_'))}</span><span class="ph-wt">weight {ph['weight']} &middot; the highest in the brain</span></div>
      <h5>The feeling that fires it</h5>
      <p class="seed">"{esc(first_sentences(ph['feeling_seed'], 320))}"</p>
      <h5>Born from</h5>
      <p class="story">{esc(first_sentences(ph['phantom_story'], 520))}</p>
      <div class="trig">{trig}</div>
    </div>
  </div>'''


def _swap(html, start_anchor, end_anchor, new_block, search_from=0):
    i = html.index(start_anchor, search_from)
    j = html.index(end_anchor, i) + len(end_anchor)
    return html[:i] + new_block + html[j:]


def rework(html, slug, name):
    data_dir = HERE / 'treatment-data' / slug
    counts = json.loads((data_dir / 'counts.json').read_text())
    phantoms = json.loads((data_dir / 'phantoms.json').read_text())
    sh = parse_sharpener((data_dir / 'sharpener-output.txt').read_text())
    pan = parse_panel((data_dir / 'panel-output.txt').read_text())
    curated, total = counts['curated'], counts['total']

    reps = [
        (', 80 phantoms"', f', {curated} phantoms"'),
        ('80 curated phantoms', f'{curated} curated phantoms'),
        (f'80 {name}-curated phantoms', f'{curated} {name}-curated phantoms'),
        ('of 564 active', f'of {total} active'),
        (f'One brief, a real {name} client, all the way to a finished film.',
         'One brief, a brand every Australian knows, all the way to a finished film.'),
        ('A thin HCF brief comes back a blunt <span class="hl">28 out of 100.</span>',
         f'A deliberately weak health-fund brief comes back a blunt <span class="hl">{sh["score"]} out of 100.</span>'),
        ('alt="Brief Sharpener scoring an HCF brief in the app"',
         'alt="Brief Sharpener scoring a weak health-fund brief in the app"'),
        ('Brief Sharpener &middot; HCF &middot; live in the app',
         'Brief Sharpener &middot; live in the app'),
        ('<span class="tool">Brief Sharpener &middot; HCF</span>',
         '<span class="tool">Brief Sharpener</span>'),
        ('<span class="score bad">30<small>/100</small></span>',
         f'<span class="score bad">{sh["score"]}<small>/100</small></span>'),
        ('This board built itself from the creator-campaign exchange:',
         'This board built itself from the ALDI exchange:'),
    ]
    for old, new in reps:
        assert old in html, f'{slug}: missing anchor: {old[:70]}'
        html = html.replace(old, new)

    dims, personas, fws, bench = sharpener_card(sh, name)
    html = _swap(html, '<ul class="dims">', '</ul>', f'<ul class="dims">\n{dims}\n    </ul>')
    html = _swap(html, '<ul class="fw">', '</ul>', f'<ul class="fw">\n{fws}\n    </ul>')
    html = _swap(html, '<ul class="bench">', '</ul>', f'<ul class="bench">\n{bench}\n    </ul>')
    i = html.index('<div class="persona"><span class="pn"><b>The platform-builder</b>')
    j = html.index('<h4>Against the strategic frameworks</h4>', i)
    html = html[:i] + personas + '\n    ' + html[j:]
    html = _swap(html, '<div class="board">', '</div>\n  <p style="margin-top:1.6rem">',
                 BOARD + '\n  <p style="margin-top:1.6rem">')
    rw = parse_rewrite((data_dir / 'sharpener-output.txt').read_text())
    assert rw, f'{slug}: could not parse sharpened rewrite'
    html = _swap(html, '<div class="rewrite">', '</div>\n  </div>\n</div></section>',
                 rewrite_block(rw) + '\n  </div>\n</div></section>')

    best = next((p for p in phantoms if (p.get('phantom_story') or '').strip()), None)
    assert best, f'{slug}: no phantom with a story'
    k = html.index('already outranking most of the library.')
    html = _swap(html, '<div class="phantoms">', '</div></section>',
                 phantom_card(best, name) + '\n</div></section>', search_from=k)

    for old_name, p in zip(['<b>Priya</b>', '<b>Zoe</b>', '<b>Josh</b>'], pan['personas']):
        new_div = (f'<div class="persona"><span class="pn"><b>{esc(p["name"])}</b> &middot; {p["intent"]}'
                   f' &middot; {esc(p["label"])}</span><q>{esc(p["quote"])}</q></div>')
        pattern = re.compile(r'<div class="persona"><span class="pn">' + re.escape(old_name) + r'.*?</q></div>', re.S)
        html, n = pattern.subn(new_div, html, count=1)
        assert n == 1, f'{slug}: panel persona anchor not found: {old_name}'

    # panel score in copy if it differs from BMF's 42/100
    if pan['score'] and pan['score'] != 42:
        html = html.replace("scored the agency's own idea 42/100",
                            f"scored the agency's own idea {pan['score']}/100")
        html = html.replace(f"scored {name}'s own idea 42/100",
                            f"scored {name}'s own idea {pan['score']}/100")
    return html
