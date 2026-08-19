# -*- coding: utf-8 -*-
"""Genererar Vapes-sidan: index + 6 kategorisidor."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

CATS = [
    ("80k-fumot-4in1", "80k Fumot 4in1 RandM", "80k-fumot-4in1.png"),
    ("randm-18k", "Randm 18k", "randm-18k.png"),
    ("10k-shisha-randm", "10k Shisha Randm", "10k-shisha-randm.png"),
    ("7k-fumot", "7k Fumot", "7k-fumot.png"),
    ("15k-fumot", "15k Fumot", "15k-fumot.png"),
    ("32k-fumot", "32k Fumot", "32k-fumot.png"),
]

CSS = """
  :root {
    --bg: #101318; --surface: #1a1e26; --ink: #e8e6e1; --muted: #9aa0ab;
    --accent: #fbbf24; --border: #2a2f3a; --radius: 14px;
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { background: var(--bg); color: var(--ink);
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
    line-height: 1.6; -webkit-font-smoothing: antialiased; }
  .wrap { max-width: 1000px; margin: 0 auto; padding: 0 20px; }
  header { padding: 56px 0 32px; text-align: center; }
  header h1 { font-size: 2.2rem; letter-spacing: -0.02em; }
  header p { color: var(--muted); margin-top: 8px; }
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 16px; padding-bottom: 48px; }
  .card { display: block; background: var(--surface); border: 1px solid var(--border);
    border-radius: var(--radius); overflow: hidden; text-decoration: none; color: var(--ink);
    transition: transform .15s ease, border-color .15s ease; }
  .card:hover { transform: translateY(-4px); border-color: var(--accent); }
  .card img { display: block; width: 100%; height: 200px; object-fit: contain; background: #fff; padding: 12px; }
  .card .name { padding: 14px; text-align: center; font-weight: 600; }
  .card:hover .name { color: var(--accent); }
  .back { display: inline-block; margin: 24px 0; color: var(--accent); text-decoration: none; font-weight: 600; }
  .back:hover { text-decoration: underline; }
  .product { text-align: center; padding-bottom: 40px; }
  .product img { max-width: 100%; max-height: 420px; object-fit: contain; background: #fff;
    border-radius: var(--radius); padding: 16px; border: 1px solid var(--border); }
  .product h1 { margin-top: 20px; }
  .info { text-align: left; background: var(--surface); border: 1px solid var(--border);
    border-radius: var(--radius); padding: 24px; margin-bottom: 48px; }
  .info h2 { font-size: 1.15rem; margin-bottom: 12px; padding-left: 12px; border-left: 3px solid var(--accent); }
  .info p { color: var(--muted); margin-bottom: 10px; }
  .info p:last-child { margin-bottom: 0; }
  .info ul { list-style: none; margin: 0; padding: 0; }
  .info li { color: var(--muted); padding: 8px 12px; margin-bottom: 6px;
    background: var(--bg); border: 1px solid var(--border); border-radius: 10px; }
  .info li.soldout { border-color: #b91c1c; background: #1f1113; }
  .info li.soldout s { color: #ef4444; text-decoration: line-through; text-decoration-color: #ef4444; }
  .info li .slut { color: #ef4444; font-weight: 700; font-size: .75rem;
    letter-spacing: .05em; text-transform: uppercase; }
  .age { color: var(--accent); font-weight: 600; }
  footer { border-top: 1px solid var(--border); padding: 28px 0 40px; text-align: center; color: var(--muted); font-size: .9rem; }
  @media (max-width: 480px) { header h1 { font-size: 1.7rem; } }
"""

FLAVORS_80K = [
    "Magic Love · Kiwi Passion Fruit Guava · Dragonfruit Raspberry · Lemon Lime",
    "Peach Ice · Mixed Berries · Lemon Peach Passionfruit · Black Ice Dragonfruit Strawberry",
    "Strawberry Banana · Strawberry Kiwi · Strawberry Watermelon · Strawberry Ice",
    "Fresh Menthol Mojito · Pink Lemonade · Cool Mint · Mint Watermelon",
    "Grape Burst · Blueberry Sour Raspberry · Strawberry Raspberry Cherry Ice · Cherry Ice",
    "Watermelon Ice · Peach Mango · Lady Killer · Strawberry Red Bull",
    "Blueberry On Ice · Pineapple Lemonade · Peach Mango Watermelon · Blue Razz Cherry",
    "Grape Gummy Bear · Blueberry Hubba Bubba · Watermelon Bubblegum · Skittles",
    "Peach Berry · Lemon Peach · Passionfruit Grapefruit Orange · Blueberry Cherry Cranberry",
    "Cola Lime · Cherry Cola · Dr Blue · Strawberry Grape",
]

# Smaker som är SLUT (slutsålda) – visas överstrukna med rött
SOLD_OUT_80K = {
    "Magic Love · Kiwi Passion Fruit Guava · Dragonfruit Raspberry · Lemon Lime",
}

def info_block(flavors=None, sold_out=()):
    if flavors is None:
        return '      <p>Info kommer snart…</p>\n'
    items = "\n".join(
        f'      <li class="soldout"><s>{f}</s> <span class="slut">SLUT</span></li>'
        if f in sold_out else f"      <li>{f}</li>"
        for f in flavors
    )
    return f"""      <p><strong>Smaker ({len(flavors)} blandningar):</strong></p>
      <ul>
{items}
      </ul>
"""

def page_template(title, body):
    return f"""<!DOCTYPE html>
<html lang="sv">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>{CSS}</style>
</head>
<body>
  <div class="wrap">
{body}
  </div>
</body>
</html>
"""

# --- Startsida ---
cards = "\n".join(
    f'    <a class="card" href="{slug}.html">\n'
    f'      <img src="{img}" alt="{name}">\n'
    f'      <div class="name">{name}</div>\n'
    f'    </a>'
    for slug, name, img in CATS
)
index_body = f"""    <header>
      <h1>Vapes</h1>
      <p>Välj en vape för info & smaker</p>
    </header>
    <div class="grid">
{cards}
    </div>
    <footer>
      <p><span class="age">18+</span> · Endast för vuxna</p>
    </footer>
"""
with open(os.path.join(BASE, "index.html"), "w", encoding="utf-8") as f:
    f.write(page_template("Vapes – Smaker & Info", index_body))

# --- Kategorisidor ---
for slug, name, img in CATS:
    flavors = FLAVORS_80K if slug == "80k-fumot-4in1" else None
    sold_out = SOLD_OUT_80K if slug == "80k-fumot-4in1" else ()
    body = f"""    <a class="back" href="index.html">&larr; Tillbaka till alla</a>
    <div class="product">
      <img src="{img}" alt="{name}">
      <h1>{name}</h1>
    </div>
    <div class="info">
      <h2>Info & smaker</h2>
{info_block(flavors, sold_out)}    </div>
"""
    with open(os.path.join(BASE, slug + ".html"), "w", encoding="utf-8") as f:
        f.write(page_template(name + " – Vapes", body))

print("Skapade:", ", ".join(["index.html"] + [c[0] + ".html" for c in CATS]))
