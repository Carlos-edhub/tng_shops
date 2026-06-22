import os
import re
import json
from PIL import Image, ImageDraw, ImageFont

# Read products.js
with open(r'D:\TNGSHOPS\PaginaWeb\src\data\products.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract product dicts using regex
products = []
pattern = r'id:\s*(\d+)[^}]+}'
for match in re.finditer(r'\{\s*id:\s*(\d+)(.*?)\}', content, re.DOTALL):
    block = match.group(0)
    p = {}
    for kv in re.finditer(r"(\w+):\s*(?:'([^']*)'|(\d+\.?\d*)|(true|false))", block):
        key = kv.group(1)
        if kv.group(2) is not None:
            p[key] = kv.group(2)
        elif kv.group(3) is not None:
            v = kv.group(3)
            p[key] = float(v) if '.' in v else int(v)
        elif kv.group(4) is not None:
            p[key] = kv.group(4) == 'true'
    if p:
        products.append(p)

print(f"Found {len(products)} products")

output_dir = r'D:\TNGSHOPS\PaginaWeb\public\images\productos'
os.makedirs(output_dir, exist_ok=True)

# Color schemes
BRAND_COLORS = {
    'Lattafa': {
        'Hombre': ('#1a1a2e', '#16213e', '#0f3460'),
        'Mujer': ('#2d1b3d', '#3d1f4e', '#6b2d6b'),
    },
    'Armaf': {
        'Hombre': ('#1c1c2e', '#1a1a3e', '#2d2d5e'),
        'Mujer': ('#2a1a2e', '#3d1f3d', '#5c2d5c'),
    },
}

def safe_filename(name):
    return re.sub(r'[^\w\-]', '_', name.lower().replace(' ', '_')[:40])

def create_image(p, idx):
    name = p.get('name', 'Unknown')
    brand = p.get('brand', 'Lattafa')
    gender = p.get('category', 'Hombre')
    notes = p.get('notes', '')
    price = p.get('price', 0)
    
    # Canvas
    img = Image.new('RGBA', (600, 600), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Colors
    c = BRAND_COLORS.get(brand, BRAND_COLORS['Lattafa']).get(gender if gender != 'Unisex' else 'Hombre', BRAND_COLORS['Lattafa']['Hombre'])
    
    # Background gradient
    for y in range(600):
        r1, g1, b1 = tuple(int(c[0][i:i+2], 16) for i in (1, 3, 5))
        r2, g2, b2 = tuple(int(c[1][i:i+2], 16) for i in (1, 3, 5))
        r3, g3, b3 = tuple(int(c[2][i:i+2], 16) for i in (1, 3, 5))
        
        # Three-stop gradient
        if y < 300:
            t = y / 300
            r = int(r1 + (r2 - r1) * t)
            g = int(g1 + (g2 - g1) * t)
            b = int(b1 + (b2 - b1) * t)
        else:
            t = (y - 300) / 300
            r = int(r2 + (r3 - r2) * t)
            g = int(g2 + (g3 - g2) * t)
            b = int(b2 + (b3 - b2) * t)
        
        draw.line([(0, y), (600, y)], fill=(r, g, b, 255))
    
    # Decorative circle - subtle glow
    glow = Image.new('RGBA', (600, 600), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow)
    accent = (245, 158, 11)  # #f59e0b gold
    for r in range(250, 0, -1):
        alpha = max(0, int(5 * (1 - r/250)))
        gdraw.ellipse([(300-r, 220-r), (300+r, 220+r)], outline=(*accent, alpha), width=1)
    img = Image.alpha_composite(img, glow)
    draw = ImageDraw.Draw(img)
    
    # Glass card
    card_y = 320
    card = Image.new('RGBA', (600, 600), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(card)
    cdraw.rounded_rectangle([(30, card_y), (570, 570)], radius=20, fill=(255, 255, 255, 25), outline=(255, 255, 255, 40), width=1)
    img = Image.alpha_composite(img, card)
    draw = ImageDraw.Draw(img)
    
    # Brand name at top of card
    try:
        font_brand = ImageFont.truetype("arial.ttf", 18)
        font_name = ImageFont.truetype("arial.ttf", 28)
        font_price = ImageFont.truetype("arial.ttf", 22)
        font_notes = ImageFont.truetype("arial.ttf", 14)
    except:
        font_brand = ImageFont.load_default()
        font_name = ImageFont.load_default()
        font_price = ImageFont.load_default()
        font_notes = ImageFont.load_default()
    
    draw.text((300, card_y + 20), brand.upper(), fill=(245, 158, 11, 200), font=font_brand, anchor='mt')
    draw.text((300, card_y + 55), name, fill=(255, 255, 255, 230), font=font_name, anchor='mt')
    draw.text((300, card_y + 95), f"${price:.2f}", fill=(245, 158, 11, 220), font=font_price, anchor='mt')
    draw.text((300, card_y + 130), notes, fill=(255, 255, 255, 140), font=font_notes, anchor='mt')
    
    # Gender badge
    gender_colors = {'Hombre': (100, 149, 237), 'Mujer': (255, 105, 180), 'Unisex': (150, 150, 150)}
    gc = gender_colors.get(gender if gender != 'Mujer' else 'Mujer', (150, 150, 150))
    gc = gender_colors['Hombre'] if gender == 'Hombre' else gender_colors['Mujer']
    gb = Image.new('RGBA', (600, 600), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(gb)
    gdraw.rounded_rectangle([(240, card_y + 155), (360, card_y + 175)], radius=10, fill=(*gc, 60))
    img = Image.alpha_composite(img, gb)
    draw = ImageDraw.Draw(img)
    draw.text((300, card_y + 165), gender, fill=(255, 255, 255, 180), font=font_notes, anchor='mt')
    
    # Decorative bottle shape
    # Simple glass bottle outline
    bx = 300
    by = 160
    bottle = Image.new('RGBA', (600, 600), (0, 0, 0, 0))
    bdraw = ImageDraw.Draw(bottle)
    
    # Bottle body
    bottle_w = 50
    bottle_h = 90
    bottle_x1 = bx - bottle_w//2
    bottle_x2 = bx + bottle_w//2
    bottle_y1 = by - bottle_h//2
    bottle_y2 = by + bottle_h//2
    
    # Neck
    neck_w = 16
    neck_h = 20
    bdraw.rectangle([(bx - neck_w//2, bottle_y1 - neck_h), (bx + neck_w//2, bottle_y1)], fill=(*accent, 100), outline=(*accent, 160), width=2)
    # Body
    bdraw.rounded_rectangle([(bottle_x1, bottle_y1), (bottle_x2, bottle_y2)], radius=10, fill=(255, 255, 255, 30), outline=(*accent, 120), width=2)
    # Cap
    bdraw.rectangle([(bx - 10, bottle_y1 - neck_h - 8), (bx + 10, bottle_y1 - neck_h)], fill=(*accent, 150), outline=(*accent, 200), width=1)
    # Glass shine
    bdraw.rectangle([(bottle_x1 + 8, bottle_y1 + 10), (bottle_x1 + 16, bottle_y2 - 10)], fill=(255, 255, 255, 40))
    
    img = Image.alpha_composite(img, bottle)
    
    # id overlay (tiny, bottom right)
    draw = ImageDraw.Draw(img)
    try:
        font_id = ImageFont.truetype("arial.ttf", 11)
    except:
        font_id = ImageFont.load_default()
    draw.text((570, 585), f"#{p.get('id', idx+1)}", fill=(255, 255, 255, 60), font=font_id, anchor='rs')
    
    return img

for i, p in enumerate(products):
    name = p.get('name', 'unknown')
    brand = p.get('brand', 'Lattafa').lower()
    fname = safe_filename(f"{brand}_{name}")
    img = create_image(p, i)
    path = os.path.join(output_dir, f"{fname}.png")
    img.save(path, 'PNG')
    print(f"  [{i+1}/40] {name} -> {fname}.png")

print("Done! All images generated.")