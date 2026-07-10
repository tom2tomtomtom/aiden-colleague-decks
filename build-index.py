#!/usr/bin/env python3
"""Build the landing page listing every agency Colleague deck.
Add an agency to AGENCIES and re-run. Each deck lives at <slug>/index.html."""
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parent
FONTS = pathlib.Path("/Users/tommyhyde/geoff/assets/fonts")

def b64(p, mime):
    return f"data:{mime};base64," + base64.b64encode(pathlib.Path(p).read_bytes()).decode()

anton = b64(FONTS / "Anton-Regular.ttf", "font/ttf")
mono  = b64(FONTS / "SpaceMono-Bold.ttf", "font/ttf")

# slug, name, tagline, status ('live'|'soon'), accent
AGENCIES = [
    ("bmf", "BMF", "Home of the Long Idea. A one-line ALDI brief to a finished film.", "live"),
    ("town-square", "Town Square", "Cultured Creativity, now with memory. Built from Town Square's own brain, a one-line ALDI brief to a finished film.", "live"),
    ("kerfuffle", "Kerfuffle", "Built to command attention. From Kerfuffle's own brain, a one-line ALDI brief to a finished film.", "live"),
    ("uncommon", "Uncommon", "An AI operating system for the agency. A one-line ALDI brief to a finished film.", "live"),
    ("lego", "LEGO", "An AI operating system for the agency. A one-line ALDI brief to a finished film.", "live"),
    ("alt-shift", "Alt/Shift", "An AI operating system for the agency. A one-line ALDI brief to a finished film.", "live"),
    ("alien-baby", "Alien Baby", "An AI operating system for the agency. A one-line ALDI brief to a finished film.", "live"),
]

def card(slug, name, tagline, status):
    if status == "live":
        return f"""<a class="card live" href="{slug}/index.html">
      <div class="ct"><span class="cn">{name}</span><span class="badge live">Live</span></div>
      <p>{tagline}</p>
      <span class="go">Open the deck &rarr;</span>
    </a>"""
    return f"""<div class="card soon">
      <div class="ct"><span class="cn">{name}</span><span class="badge soon">In production</span></div>
      <p>{tagline}</p>
    </div>"""

cards = "\n    ".join(card(*a) for a in AGENCIES)

HTML = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>AIDEN Colleague, agency decks</title>
<style>
@font-face {{ font-family:'Anton'; src:url({anton}) format('truetype'); font-display:swap; }}
@font-face {{ font-family:'Mono'; src:url({mono}) format('truetype'); font-weight:700; font-display:swap; }}
:root {{ --ink:#0C0B0D; --panel:#141215; --paper:#EFEAE2; --muted:#948C81; --warm:#E8912A; --red:#F5442E; --cold:#7FA0BE;
  --line:rgba(239,234,226,0.12); --line-strong:rgba(239,234,226,0.22); }}
* {{ box-sizing:border-box; }}
body {{ margin:0; background:var(--ink); color:var(--paper); -webkit-font-smoothing:antialiased;
  font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif; line-height:1.6; }}
.wrap {{ max-width:960px; margin:0 auto; padding:clamp(3.5rem,10vh,7rem) clamp(1.4rem,5vw,3rem); }}
.mark {{ font-family:'Mono'; font-weight:700; letter-spacing:.02em; font-size:1rem; margin-bottom:2rem; }}
.mark .a {{ color:var(--red); }} .mark .dot {{ color:var(--muted); }}
h1 {{ font-family:'Anton'; font-weight:400; text-transform:uppercase; line-height:.98; letter-spacing:.005em;
  font-size:clamp(2.6rem,7vw,5rem); margin:0 0 1.3rem; text-wrap:balance; }}
.lead {{ font-size:clamp(1.05rem,1.6vw,1.28rem); color:#DDD6CC; max-width:52ch; margin:0 0 3rem; }}
.grid {{ display:grid; grid-template-columns:1fr 1fr; gap:1.2rem; }}
.card {{ display:block; text-decoration:none; color:inherit; background:var(--panel); border:1px solid var(--line-strong);
  border-radius:8px; padding:1.5rem 1.6rem 1.7rem; transition:border-color .2s ease, transform .2s ease; }}
.card.live:hover {{ border-color:var(--warm); transform:translateY(-2px); }}
.card.soon {{ opacity:.55; }}
.ct {{ display:flex; align-items:center; justify-content:space-between; gap:1rem; margin-bottom:.5rem; }}
.cn {{ font-family:'Anton'; text-transform:uppercase; font-size:clamp(1.5rem,3vw,2rem); line-height:1; letter-spacing:.01em; }}
.badge {{ font-family:'Mono'; font-weight:700; font-size:.58rem; letter-spacing:.1em; text-transform:uppercase;
  padding:.22rem .5rem; border-radius:3px; white-space:nowrap; }}
.badge.live {{ background:rgba(232,145,42,.16); color:var(--warm); }}
.badge.soon {{ background:rgba(148,140,129,.16); color:var(--muted); }}
.card p {{ margin:0 0 1.1rem; color:#B9B2A7; font-size:.96rem; max-width:36ch; }}
.card.soon p {{ margin-bottom:0; }}
.go {{ font-family:'Mono'; font-weight:700; font-size:.72rem; letter-spacing:.14em; text-transform:uppercase; color:var(--warm); }}
.foot {{ font-family:'Mono'; font-weight:700; font-size:.68rem; letter-spacing:.16em; text-transform:uppercase;
  color:var(--muted); margin-top:3.5rem; padding-top:1.6rem; border-top:1px solid var(--line); }}
.foot .a {{ color:var(--red); }}
@media (max-width:680px) {{ .grid {{ grid-template-columns:1fr; }} }}
</style>
</head>
<body>
<div class="wrap">
  <div class="mark"><span class="a">AIDEN</span> <span class="dot">&middot;</span> Colleague</div>
  <h1>One operating system.<br>Every agency's own brain.</h1>
  <p class="lead">AIDEN Colleague, built from each agency's beliefs, taking a brief all the way to finished work. A deck per agency, each on its own brain.</p>
  <div class="grid">
    {cards}
  </div>
  <div class="foot"><span class="a">AIDEN</span> &middot; Colleague &nbsp;&middot;&nbsp; colleague.aiden.services</div>
</div>
</body>
</html>
"""

(ROOT / "index.html").write_text(HTML, encoding="utf-8")
print("wrote index.html", f"{(ROOT/'index.html').stat().st_size/1024:.0f} KB")
