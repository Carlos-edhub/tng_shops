import os, re
from PIL import Image, ImageDraw, ImageFont

output_dir = r'D:\TNGSHOPS\PaginaWeb\public\images\productos'
os.makedirs(output_dir, exist_ok=True)

products = [
    # (id, name, brand, gender, notes, price, volume, isNew, stock, originalPrice)
    # HOMBRE
    (1, "Fakhar Men Black", "Lattafa", "Hombre", "Cuero, Ámbar, Especias", 29.99, "100ml", False, 3, 39.99),
    (2, "Fakhar Men Silver", "Lattafa", "Hombre", "Bergamota, Lavanda, Almizcle", 26.99, "100ml", True, None, None),
    (3, "Asad", "Lattafa", "Hombre", "Pimienta Negra, Tabaco, Cuero", 24.99, "100ml", False, 5, None),
    (4, "Ramz Silver", "Lattafa", "Hombre", "Pera, Canela, Vainilla", 22.99, "100ml", True, None, 29.99),
    (5, "Qaed Al Fursan", "Lattafa", "Hombre", "Piña, Azafrán, Ámbar", 27.99, "100ml", False, None, None),
    (6, "Al Wisam", "Lattafa", "Hombre", "Manzana, Cedro, Sándalo", 29.99, "100ml", False, None, 35.99),
    (7, "Raghba Wood Intense", "Lattafa", "Hombre", "Madera de Oud, Almizcle, Ámbar", 19.99, "100ml", False, 4, None),
    (8, "Shem Al Sheikh", "Lattafa", "Hombre", "Bergamota, Oud, Sándalo", 18.99, "100ml", False, None, None),
    (9, "Najdia", "Lattafa", "Hombre", "Toronja, Jengibre, Almizcle Acuático", 21.99, "100ml", True, None, None),
    (10, "Oud Al Sahraa", "Lattafa", "Hombre", "Oud, Rosa, Pachulí", 25.99, "75ml", False, 2, 32.99),
    (11, "Club de Nuit Intense Man", "Armaf", "Hombre", "Bergamota, Pimienta Rosa, Cuero", 36.99, "105ml", False, 5, 46.99),
    (12, "Club de Nuit Iconic", "Armaf", "Hombre", "Bergamota, Pimienta, Cuero", 36.99, "105ml", True, None, None),
    (13, "Club de Nuit Sillage", "Armaf", "Hombre", "Limón, Jengibre, Almizcle", 36.99, "100ml", False, None, None),
    (14, "Club de Nuit Milestone", "Armaf", "Hombre", "Sal Marina, Bergamota, Almizcle Blanco", 38.99, "100ml", True, None, None),
    (15, "Club de Nuit Urban Man", "Armaf", "Hombre", "Toronja, Cardamomo, Cedro", 32.99, "100ml", False, None, None),
    (16, "Hunter Intense", "Armaf", "Hombre", "Limón, Lavanda, Ámbar", 28.99, "100ml", False, 3, 35.99),
    (17, "Tag Him", "Armaf", "Hombre", "Toronja, Menta, Almizcle", 19.99, "100ml", False, None, None),
    (18, "Voyage Blues", "Armaf", "Hombre", "Mandarina, Lavanda, Sándalo", 21.99, "100ml", False, None, None),
    (19, "Odyssey Homme", "Armaf", "Hombre", "Pimienta Rosa, Cuero, Tabaco", 27.99, "100ml", False, 4, None),
    (20, "Shadow Wood", "Armaf", "Hombre", "Cedro, Ámbar, Vainilla", 24.99, "75ml", False, None, 29.99),
    # MUJER
    (21, "Khamrah", "Lattafa", "Mujer", "Canela, Dátil, Praliné", 39.99, "100ml", False, 1, 49.99),
    (22, "Ana Abiyedh Poudree", "Lattafa", "Mujer", "Almendra, Vainilla, Almizcle", 32.99, "100ml", True, None, None),
    (23, "Yara", "Lattafa", "Mujer", "Fresa, Vainilla, Almizcle Rosado", 24.99, "100ml", True, None, None),
    (24, "Ana Abiyedh Rose", "Lattafa", "Mujer", "Rosa Turca, Pachulí, Sándalo", 28.99, "100ml", False, None, None),
    (25, "Haya", "Lattafa", "Mujer", "Pera, Jazmín, Almizcle", 22.99, "80ml", False, 4, None),
    (26, "Raghba", "Lattafa", "Mujer", "Vainilla, Ámbar, Oud Suave", 18.99, "100ml", False, None, None),
    (27, "La Charmante", "Lattafa", "Mujer", "Rosa, Jazmín, Sándalo", 29.99, "80ml", False, 2, None),
    (28, "Musk Mood", "Lattafa", "Mujer", "Almizcle Blanco, Lavanda, Iris", 20.99, "100ml", False, None, None),
    (29, "Oud Mood", "Lattafa", "Mujer", "Oud, Rosa, Azafrán", 23.99, "75ml", False, None, 28.99),
    (30, "Bade e Al Oud Amethyst", "Lattafa", "Mujer", "Frutos Rojos, Oud, Vainilla", 31.99, "80ml", True, None, None),
    (31, "Club de Nuit Woman", "Armaf", "Mujer", "Melocotón, Rosa, Almizcle", 34.99, "100ml", False, None, None),
    (32, "Club de Nuit Imperial", "Armaf", "Mujer", "Grosella Negra, Lirio, Vainilla", 36.99, "100ml", False, 3, 44.99),
    (33, "Tag Her", "Armaf", "Mujer", "Frambuesa, Violeta, Almizcle", 19.99, "100ml", False, None, None),
    (34, "Hunter Woman", "Armaf", "Mujer", "Mandarina, Peonía, Sándalo", 24.99, "100ml", True, None, None),
    (35, "Odyssey Woman", "Armaf", "Mujer", "Pera, Jazmín, Almizcle Blanco", 26.99, "100ml", False, 5, None),
    (36, "Voyage Bloom", "Armaf", "Mujer", "Loto, Peonía, Almizcle", 22.99, "100ml", False, None, None),
    (37, "Prelude", "Armaf", "Mujer", "Bergamota, Jazmín, Sándalo", 28.99, "80ml", True, None, 34.99),
    (38, "Dareej", "Armaf", "Mujer", "Canela, Caramelo, Flor de Naranjo", 25.99, "100ml", False, None, None),
    (39, "Sillage Woman", "Armaf", "Mujer", "Lirio, Violeta, Almizcle", 31.99, "100ml", False, None, None),
    (40, "Mystique", "Armaf", "Mujer", "Rosa Negra, Oud, Ámbar", 27.99, "75ml", False, 2, None),
]

def safe_filename(name, brand):
    s = f"{brand.lower()}_{name.lower()}"
    s = re.sub(r"[^a-z0-9_\-\u00e0-\u00ff]", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s[:50]

def create_image(p, idx):
    prod_id, name, brand, gender, notes, price, volume, isNew, stock, orig_price = p
    
    img = Image.new('RGBA', (600, 600), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    accent = (245, 158, 11)
    
    # Colors per brand+gender
    if brand == "Lattafa":
        c1, c2, c3 = ("#1a1a2e", "#16213e", "#0f3460") if gender == "Hombre" else ("#2d1b3d", "#3d1f4e", "#6b2d6b")
    else:
        c1, c2, c3 = ("#1c1c2e", "#1a1a3e", "#2d2d5e") if gender == "Hombre" else ("#2a1a2e", "#3d1f3d", "#5c2d5c")
    
    # Background
    rgb = [tuple(int(x[i:i+2], 16) for i in (1, 3, 5)) for x in (c1, c2, c3)]
    for y in range(600):
        if y < 300:
            t = y / 300
            r = int(rgb[0][0] + (rgb[1][0] - rgb[0][0]) * t)
            g = int(rgb[0][1] + (rgb[1][1] - rgb[0][1]) * t)
            b = int(rgb[0][2] + (rgb[1][2] - rgb[0][2]) * t)
        else:
            t = (y - 300) / 300
            r = int(rgb[1][0] + (rgb[2][0] - rgb[1][0]) * t)
            g = int(rgb[1][1] + (rgb[2][1] - rgb[1][1]) * t)
            b = int(rgb[1][2] + (rgb[2][2] - rgb[1][2]) * t)
        draw.line([(0, y), (600, y)], fill=(r, g, b, 255))
    
    # Glow rings
    glow = Image.new('RGBA', (600, 600), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    for r2 in range(180, 0, -5):
        a = max(0, int(3 * (1 - r2/180)))
        gd.ellipse([(300-r2, 180-r2), (300+r2, 180+r2)], outline=(*accent, a), width=1)
    for r2 in range(140, 0, -3):
        a = max(0, int(2 * (1 - r2/140)))
        gd.ellipse([(300-r2, 210-r2), (300+r2, 210+r2)], outline=(255, 255, 255, a), width=1)
    img = Image.alpha_composite(img, glow)
    draw = ImageDraw.Draw(img)
    
    # Glass card
    card = Image.new('RGBA', (600, 600), (0, 0, 0, 0))
    cd = ImageDraw.Draw(card)
    cd.rounded_rectangle([(30, 320), (570, 580)], radius=24, fill=(255, 255, 255, 22), outline=(255, 255, 255, 35), width=1)
    # Subtle shine on card
    cd.rounded_rectangle([(30, 320), (570, 380)], radius=24, fill=(255, 255, 255, 8))
    img = Image.alpha_composite(img, card)
    draw = ImageDraw.Draw(img)
    
    # Fonts
    try:
        fb = ImageFont.truetype("arial.ttf", 18)
        fn = ImageFont.truetype("arial.ttf", 26)
        fp = ImageFont.truetype("arial.ttf", 22)
        fnt = ImageFont.truetype("arial.ttf", 13)
        fid = ImageFont.truetype("arial.ttf", 11)
    except:
        fb = fn = fp = fnt = fid = ImageFont.load_default()
    
    # Brand
    draw.text((300, 340), brand.upper(), fill=(*accent, 200), font=fb, anchor="mt")
    # Name
    draw.text((300, 375), name, fill=(255, 255, 255, 235), font=fn, anchor="mt")
    # Price
    if orig_price:
        draw.text((260, 420), f"${orig_price:.2f}", fill=(255, 255, 255, 80), font=fp, anchor="rt")
        draw.line([(230, 425), (290, 425)], fill=(255, 80, 80, 150), width=2)
    draw.text((300 if not orig_price else 300 + 15, 420), f"${price:.2f}", fill=(*accent, 230), font=fp, anchor="mt")
    # Volume
    draw.text((300, 455), volume, fill=(255, 255, 255, 130), font=fnt, anchor="mt")
    # Notes
    draw.text((300, 480), notes, fill=(255, 255, 255, 110), font=fnt, anchor="mt")
    # Gender
    gc = (100, 149, 237) if gender == "Hombre" else (255, 105, 180)
    gb = Image.new('RGBA', (600, 600), (0, 0, 0, 0))
    gd2 = ImageDraw.Draw(gb)
    tw = 50
    gd2.rounded_rectangle([(300 - tw//2, 505), (300 + tw//2, 525)], radius=10, fill=(*gc, 50))
    img = Image.alpha_composite(img, gb)
    draw = ImageDraw.Draw(img)
    draw.text((300, 515), gender, fill=(*gc, 200), font=fnt, anchor="mt")
    
    # Perfume bottle icon
    bx, by = 300, 165
    bottle = Image.new('RGBA', (600, 600), (0, 0, 0, 0))
    bd = ImageDraw.Draw(bottle)
    
    bw, bh = 50, 85
    bx1, bx2 = bx - bw//2, bx + bw//2
    by1, by2 = by - bh//2, by + bh//2
    
    # Neck
    nw = 16
    nh = 18
    bd.rectangle([(bx - nw//2, by1 - nh), (bx + nw//2, by1)], fill=(*accent, 80), outline=(*accent, 150), width=2)
    # Body
    bd.rounded_rectangle([(bx1, by1), (bx2, by2)], radius=12, fill=(255, 255, 255, 25), outline=(*accent, 100), width=2)
    # Cap
    bd.rectangle([(bx - 10, by1 - nh - 8), (bx + 10, by1 - nh)], fill=(*accent, 130), outline=(*accent, 180), width=1)
    # Shine
    bd.rectangle([(bx1 + 8, by1 + 12), (bx1 + 16, by2 - 12)], fill=(255, 255, 255, 35))
    
    img = Image.alpha_composite(img, bottle)
    
    # Badges
    badge_y = 305
    if isNew:
        b = Image.new('RGBA', (600, 600), (0, 0, 0, 0))
        bd2 = ImageDraw.Draw(b)
        bd2.rounded_rectangle([(180, badge_y - 11), (230, badge_y + 11)], radius=10, fill=(0, 200, 100, 180))
        img = Image.alpha_composite(img, b)
        draw = ImageDraw.Draw(img)
        draw.text((205, badge_y), "NUEVO", fill=(255, 255, 255, 230), font=fnt, anchor="mt")
    
    if orig_price:
        b = Image.new('RGBA', (600, 600), (0, 0, 0, 0))
        bd2 = ImageDraw.Draw(b)
        pct = int((1 - price/orig_price) * 100)
        bd2.rounded_rectangle([(370, badge_y - 11), (430, badge_y + 11)], radius=10, fill=(255, 50, 50, 180))
        img = Image.alpha_composite(img, b)
        draw = ImageDraw.Draw(img)
        draw.text((400, badge_y), f"-{pct}%", fill=(255, 255, 255, 230), font=fnt, anchor="mt")
    
    if stock and stock <= 3:
        b = Image.new('RGBA', (600, 600), (0, 0, 0, 0))
        bd2 = ImageDraw.Draw(b)
        bd2.rounded_rectangle([(505, badge_y - 11), (560, badge_y + 11)], radius=10, fill=(255, 150, 0, 180))
        img = Image.alpha_composite(img, b)
        draw = ImageDraw.Draw(img)
        draw.text((532, badge_y), f"Quedan {stock}", fill=(255, 255, 255, 230), font=fnt, anchor="mt")
    
    # ID
    draw = ImageDraw.Draw(img)
    draw.text((570, 588), f"#{prod_id}", fill=(255, 255, 255, 50), font=fid, anchor="rs")
    
    return img

# Generate
for i, p in enumerate(products):
    prod_id, name, brand, gender, notes, price, volume, isNew, stock, orig_price = p
    fname = safe_filename(name, brand)
    # Handle special names
    fname = fname.replace("e_e", "e")
    img = create_image(p, i)
    path = os.path.join(output_dir, f"{fname}.png")
    img.save(path, "PNG")
    print(f"  [{prod_id:>2}/40] {name} -> {fname}.png")

print("Done!")