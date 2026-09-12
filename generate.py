# -*- coding: utf-8 -*-
"""Genererar Vapes-sidan: index + 6 kategorisidor."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

CATS = [
    ("80k-fumot-4in1", "80k Fumot 4in1 RandM", "80k-fumot-4in1.png"),
    ("randm-18k", "18k RandM", "randm-18k.png"),
    ("10k-shisha-randm", "10k Shisha RandM", "10k-shisha-randm.png"),
    ("7k-fumot", "7k RandM Fumot", "7k-fumot.png"),
    ("15k-fumot", "15k RandM Fumot", "15k-fumot.png"),
    ("32k-fumot", "32k Fumot RandM", "32k-fumot.png"),
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
  .hjarta { text-align: center; font-size: 170px; line-height: 1; margin-top: 40px;
    animation: hjartslag 1.6s ease-in-out infinite; }
  @keyframes hjartslag { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.12); } }
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
  .product .red-banner { color: #ef4444; font-weight: 700; font-size: 2em;
    letter-spacing: .02em; margin-top: 16px; }
  .product .subtitle { color: var(--accent); font-weight: 600; margin-top: 6px; letter-spacing: .03em; }
  .product .mix { color: var(--muted); margin-top: 10px; font-size: 1rem; letter-spacing: .02em; }
  .product .price { color: var(--ink); font-weight: 700; margin-top: 8px; font-size: 1.1rem; }
  .product .deal { color: #ef4444; font-weight: 700; margin-top: 12px; font-size: 1.4rem; letter-spacing: .02em; }
  .video { max-width: 560px; margin: 0 auto 48px; }
  .video video { display: block; width: 100%; aspect-ratio: 16/9;
    border: 1px solid var(--border); border-radius: var(--radius); background: #000; }
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
SOLD_OUT_80K = set()  # Magic Love var bara ett test – ingen slut längre

# 7k RandM – smaker (siffror i källan ignorerade)
FLAVORS_7K = [
    "Cool Mint",
    "Blueberry On Ice",
    "Mango On Ice",
    "Peach Ice",
    "Cotton Candy",
    "Strawberry Banana",
    "Strawberry Kiwi",
    "Peach Mango",
    "Blackcurrant Ice",
    "Blueberry Raspberry",
]
SOLD_OUT_7K = set()

# 15k RandM Fumot – smaker (siffror i källan ignorerade)
FLAVORS_15K = [
    "Blue Razz Lemonade",
    "Peach Ice",
    "Watermelon Ice",
    "Blueberry On Ice",
    "Strawberry Ice",
    "Cola Ice",
    "Strawberry Watermelon",
    "Peach Mango",
    "Strawberry Kiwi",
    "Blueberry Bubblegum",
    "Bluesour Raspberry",
    "Cherry Cola",
    "Lemon & Lime",
    "Red Energy Ice",
    "Strawberry Banana",
    "Fresh Menthol Mojito",
    "Cactus Kiwi",
]
SOLD_OUT_15K = set()

# 10k Shisha RandM – smaker. Slut-smaker visas överstrukna
FLAVORS_10K = [
    "Double Apple",
    "Strawberry Punch",
    "Gum Flavour",
    "Gum Mint",
    "Blueberry Bubblegum",
    "Peach Ice",
    "Love 66",
    "Watermelone Ice",
]
SOLD_OUT_10K = {
    "Strawberry Punch",
    "Peach Ice",
    "Love 66",
    "Watermelone Ice",
}

# 18k RandM – smaker. Slut-smaker visas överstrukna
FLAVORS_18K = [
    "Cherry Cola",
    "Lemon & Lime",
    "Grape Ice",
    "Fizzy Cherry",
    "Watermelon Ice",
    "Blueberry On Ice",
    "Cola Ice",
    "Peach Mango",
    "Peach Ice",
    "Mango Ice",
    "Cotton Candy",
]
SOLD_OUT_18K = {
    "Watermelon Ice",
    "Blueberry On Ice",
    "Cola Ice",
    "Peach Mango",
    "Peach Ice",
    "Mango Ice",
    "Cotton Candy",
}

# 32k Fumot RandM – blandningar (2 smaker per rad). Slut-blandningar visas överstrukna
FLAVORS_32K = [
    "Fizzy Lemon & Lime · Lemon & Blueberry",
    "Grape Rainbow Drops · Strawberry Rainbow Drops",
    "Blue Razz Ice · Blueberry Raspberry",
    "Cool Mint · Spear Mint",
    "Blackcurrant Lemonade · Cherry Cola",
    "Grape Ice · Strawberry Ice",
    "Blue Razz Lemonade · Pink Lemonade",
    "Strawberry Grapefruit · Strawberry Dragonfruit",
    "Blueberry Hubba Bubba · Watermelon Hubba Bubba",
    "Watermelon Ice · Raspberry Watermelon",
    "Peach Ice · Triple Mango",
    "Lucid Dream · Rainbow Candy",
    "Kiwi Passion Fruit Guava · Pineapple Ice",
    "Dr Blue · Blueberry Sour Raspberry",
    "Fruit Bomb · Strawberry Watermelon",
    "Blueberry Cherry Cranberry · Cherry Ice",
]
SOLD_OUT_32K = {
    "Cool Mint · Spear Mint",
    "Peach Ice · Triple Mango",
}

# Underrubrik (t.ex. nikotinstyrka) per kategori
SUBTITLES = {
    "80k-fumot-4in1": "5% Nikotin",
    "7k-fumot": "5% Nikotin",
    "15k-fumot": "5% Nikotin",
    "10k-shisha-randm": "0.8% Nikotin",
    "randm-18k": "2% Nikotin",
    "32k-fumot": "2% Nikotin",
}

# Pris per kategori
PRICES = {
    "80k-fumot-4in1": "Pris: 1 för 250kr, 2 för 400kr",
    "7k-fumot": "Pris: 200kr",
    "15k-fumot": "Pris: 250 kr",
    "10k-shisha-randm": "Pris: 1 för 200kr, 3 för 500kr",
    "randm-18k": "Pris: 250kr",
    "32k-fumot": "Pris: 300kr",
}

# Ord för antal i smak-rubriken
COUNT_WORD = {
    "80k-fumot-4in1": "blandningar",
    "32k-fumot": "blandningar",
    "7k-fumot": "st",
    "15k-fumot": "st",
    "10k-shisha-randm": "st",
    "randm-18k": "st",
}

# Röd rubrik direkt ovanför priset (erbjudande) per kategori
DEAL_HEADING = {
    "80k-fumot-4in1": "Erbjudande",
}

# Röd text ovanför rubriken (t.ex. "KOMMER SNART") per kategori
RED_BANNER = {
    "32k-fumot": "Dessa monterar vi vid beställning",
}

# Smakinfo-rad mellan rubrik och nikotin (t.ex. "4 smaker in 1")
MIX_LINE = {
    "80k-fumot-4in1": "4 smaker in 1",
    "32k-fumot": "2 smaker i 1",
}

# Lokal video per kategori (filnamn i repot)
VIDEOS = {
    "80k-fumot-4in1": "80k-video.mp4",
    "15k-fumot": "15k-video.mp4",
    "randm-18k": "18k-video.mp4",
    "10k-shisha-randm": "shisha-video.mp4",
    "7k-fumot": "7k-video.mp4",
    "32k-fumot": "32k-video.mp4",
}

def info_block(flavors=None, sold_out=(), count_word="blandningar"):
    if flavors is None:
        return '      <p>Info kommer snart…</p>\n'
    items = "\n".join(
        f'      <li class="soldout"><s>{f}</s> <span class="slut">SLUT</span></li>'
        if f in sold_out else f"      <li>{f}</li>"
        for f in flavors
    )
    return f"""      <p><strong>Smaker ({len(flavors)} {count_word}):</strong></p>
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
index_body = f"""    <div class="hjarta">&#10084;&#65039;</div>
    <header>
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
FLAVORS = {"80k-fumot-4in1": FLAVORS_80K, "7k-fumot": FLAVORS_7K, "15k-fumot": FLAVORS_15K,
           "10k-shisha-randm": FLAVORS_10K, "randm-18k": FLAVORS_18K, "32k-fumot": FLAVORS_32K}
SOLD_OUT = {"80k-fumot-4in1": SOLD_OUT_80K, "7k-fumot": SOLD_OUT_7K, "15k-fumot": SOLD_OUT_15K,
            "10k-shisha-randm": SOLD_OUT_10K, "randm-18k": SOLD_OUT_18K, "32k-fumot": SOLD_OUT_32K}

for slug, name, img in CATS:
    flavors = FLAVORS.get(slug)
    sold_out = SOLD_OUT.get(slug, ())
    subtitle = SUBTITLES.get(slug, "")
    price = PRICES.get(slug, "")
    count_word = COUNT_WORD.get(slug, "blandningar")
    coming = RED_BANNER.get(slug, "")
    deal = DEAL_HEADING.get(slug, "")
    mix = MIX_LINE.get(slug, "")
    video = VIDEOS.get(slug, "")
    body = f"""    <a class="back" href="index.html">&larr; Tillbaka till alla</a>
    <div class="product">
      <img src="{img}" alt="{name}">
      {'<p class="red-banner">' + coming + '</p>' if coming else ''}
      <h1>{name}</h1>
      {'<p class="mix">' + mix + '</p>' if mix else ''}
      {'<p class="subtitle">' + subtitle + '</p>' if subtitle else ''}
      {'<p class="deal">' + deal + '</p>' if deal else ''}
      {'<p class="price">' + price + '</p>' if price else ''}
    </div>
    {'<div class="video"><video controls preload="metadata" playsinline src="' + video + '"></video></div>' if video else ''}
    <div class="info">
      <h2>Info & smaker</h2>
{info_block(flavors, sold_out, count_word)}    </div>
"""
    with open(os.path.join(BASE, slug + ".html"), "w", encoding="utf-8") as f:
        f.write(page_template(name + " – Vapes", body))

print("Skapade:", ", ".join(["index.html"] + [c[0] + ".html" for c in CATS]))
