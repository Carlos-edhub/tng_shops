import os, re
from PIL import Image, ImageDraw, ImageFont

output_dir = r'D:\TNGSHOPS\PaginaWeb\public\images\productos'
os.makedirs(output_dir, exist_ok=True)

# Only the 6 new Unisex products
products = [
    (41, "Ana Abiyedh White", "Lattafa", "Unisex", "Lavanda, almizcle blanco, pera", 28.99, "100ml"),
    (42, "Opacity", "Armaf", "Unisex", "\u00c1mbar gris, bergamota, pachul\u00ed", 33.99, "90ml"),
    (43, "Bright Peach", "Armaf", "Unisex", "Melocot\u00f3n, caramelo, flores blancas", 31.99, "100ml"),
    (44, "Maahir Black", "Lattafa", "Unisex", "Caf\u00e9, cardamomo, cuero", 26.99, "100ml"),
    (45, "Rave Now", "Lattafa", "Unisex", "Lim\u00f3n, jengibre, menta", 23.99, "100ml"),
    (46, "Fakhar Rose", "Lattafa", "Unisex", "Rosa, azafr\u00e1n, almizcle", 28.99, "100ml"),
]

accent = (245, 158, 11)

def safe_filename(name, brand):
    s = f"{brand.lower()}_{name.lower()}".replace("'", "_")
    s = re.sub(r"[^a-z0-9_\u00e0-\u00ff]", "_", s).replace("__", "_").strip("_")
    return s

def create_image(p):
    pid, name, brand, gender, notes, price, volume = p
    
    img = Image.new('RGBA', (600, 600), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    c = ("#1e1e2e", "#2a1a2e", "#3d2d3d")
    rgb = [tuple(int(x[i:i+2], 16) for i in (1, 3, 5)) for x in c]
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
    
    # Glow
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
    
    # Card
    card = Image.new('RGBA', (600, 600), (0, 0, 0, 0))
    cd = ImageDraw.Draw(card)
    cd.rounded_rectangle([(30, 320), (570, 580)], radius=24, fill=(255, 255, 255, 22), outline=(255, 255, 255, 35), width=1)
    cd.rounded_rectangle([(30, 320), (570, 380)], radius=24, fill=(255, 255, 255, 8))
    img = Image.alpha_composite(img, card)
    draw = ImageDraw.Draw(img)
    
    try:
        fb = ImageFont.truetype("arial.ttf", 18)
        fn = ImageFont.truetype("arial.ttf", 26)
        fp = ImageFont.truetype("arial.ttf", 22)
        fnt = ImageFont.truetype("arial.ttf", 13)
        fid = ImageFont.truetype("arial.ttf", 11)
    except:
        fb = fn = fp = fnt = fid = ImageFont.load_default()
    
    draw.text((300, 340), brand.upper(), fill=(*accent, 200), font=fb, anchor="mt")
    draw.text((300, 375), name, fill=(255, 255, 255, 235), font=fn, anchor="mt")
    draw.text((300, 420), f"${price:.2f}", fill=(*accent, 230), font=fp, anchor="mt")
    draw.text((300, 455), volume, fill=(255, 255, 255, 130), font=fnt, anchor="mt")
    draw.text((300, 480), notes, fill=(255, 255, 255, 110), font=fnt, anchor="mt")
    
    # Gender badge
    gc = (150, 100, 200)
    gb = Image.new('RGBA', (600, 600), (0, 0, 0, 0))
    gd2 = ImageDraw.Draw(gb)
    gd2.rounded_rectangle([(265, 505), (335, 525)], radius=10, fill=(*gc, 50))
    img = Image.alpha_composite(img, gb)
    draw = ImageDraw.Draw(img)
    draw.text((300, 515), gender, fill=(*gc, 200), font=fnt, anchor="mt")
    
    # Bottle
    bx, by = 300, 165
    bottle = Image.new('RGBA', (600, 600), (0, 0, 0, 0))
    bd = ImageDraw.Draw(bottle)
    bw, bh = 50, 85
    bx1, bx2 = bx - bw//2, bx + bw//2
    by1, by2 = by - bh//2, by + bh//2
    nw = 16; nh = 18
    bd.rectangle([(bx - nw//2, by1 - nh), (bx + nw//2, by1)], fill=(*accent, 80), outline=(*accent, 150), width=2)
    bd.rounded_rectangle([(bx1, by1), (bx2, by2)], radius=12, fill=(255, 255, 255, 25), outline=(*accent, 100), width=2)
    bd.rectangle([(bx - 10, by1 - nh - 8), (bx + 10, by1 - nh)], fill=(*accent, 130), outline=(*accent, 180), width=1)
    bd.rectangle([(bx1 + 8, by1 + 12), (bx1 + 16, by2 - 12)], fill=(255, 255, 255, 35))
    img = Image.alpha_composite(img, bottle)
    draw = ImageDraw.Draw(img)
    draw.text((570, 588), f"#{pid}", fill=(255, 255, 255, 50), font=fid, anchor="rs")
    
    return img

for i, p in enumerate(products):
    pid, name = p[0], p[1]
    fname = safe_filename(name, p[2])
    img = create_image(p)
    path = os.path.join(output_dir, f"{fname}.png")
    img.save(path, "PNG")
    print(f"  [{pid}] {name} -> {fname}.png")

print("Done - 6 Unisex images")