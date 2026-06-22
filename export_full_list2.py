import re

products = [
    (1, "Fakhar Men Black", "Lattafa", "Hombre", "Cuero, \u00e1mbar, especias", 29.99, "100ml"),
    (2, "Fakhar Men Silver", "Lattafa", "Hombre", "Bergamota, lavanda, almizcle", 26.99, "100ml"),
    (3, "Asad", "Lattafa", "Hombre", "Pimienta negra, tabaco, cuero", 24.99, "100ml"),
    (4, "Ramz Silver", "Lattafa", "Hombre", "Pera, canela, vainilla", 22.99, "100ml"),
    (5, "Qaed Al Fursan", "Lattafa", "Hombre", "Pi\u00f1a, azafr\u00e1n, \u00e1mbar", 27.99, "100ml"),
    (6, "Al Wisam", "Lattafa", "Hombre", "Manzana, cedro, s\u00e1ndalo", 29.99, "100ml"),
    (7, "Raghba Wood Intense", "Lattafa", "Hombre", "Madera de oud, almizcle, \u00e1mbar", 19.99, "100ml"),
    (8, "Shem Al Sheikh", "Lattafa", "Hombre", "Bergamota, oud, s\u00e1ndalo", 18.99, "100ml"),
    (9, "Najdia", "Lattafa", "Hombre", "Toronja, jengibre, almizcle acu\u00e1tico", 21.99, "100ml"),
    (10, "Oud Al Sahraa", "Lattafa", "Hombre", "Oud, rosa, pachul\u00ed", 25.99, "75ml"),
    (11, "Club de Nuit Intense Man", "Armaf", "Hombre", "Bergamota, pimienta rosa, cuero", 36.99, "105ml"),
    (12, "Club de Nuit Iconic", "Armaf", "Hombre", "Bergamota, pimienta, cuero", 36.99, "105ml"),
    (13, "Club de Nuit Sillage", "Armaf", "Hombre", "Lim\u00f3n, jengibre, almizcle", 36.99, "100ml"),
    (14, "Club de Nuit Milestone", "Armaf", "Hombre", "Sal marina, bergamota, almizcle blanco", 38.99, "100ml"),
    (15, "Club de Nuit Urban Man", "Armaf", "Hombre", "Toronja, cardamomo, cedro", 32.99, "100ml"),
    (16, "Hunter Intense", "Armaf", "Hombre", "Lim\u00f3n, lavanda, \u00e1mbar", 28.99, "100ml"),
    (17, "Tag Him", "Armaf", "Hombre", "Toronja, menta, almizcle", 19.99, "100ml"),
    (18, "Voyage Blues", "Armaf", "Hombre", "Mandarina, lavanda, s\u00e1ndalo", 21.99, "100ml"),
    (19, "Odyssey Homme", "Armaf", "Hombre", "Pimienta rosa, cuero, tabaco", 27.99, "100ml"),
    (20, "Shadow Wood", "Armaf", "Hombre", "Madera de cedro, \u00e1mbar, vainilla", 24.99, "75ml"),
    (21, "Khamrah", "Lattafa", "Mujer", "Canela, d\u00e1til, pralin\u00e9", 39.99, "100ml"),
    (22, "Ana Abiyedh Poudr\u00e9e", "Lattafa", "Mujer", "Almendra, vainilla, almizcle", 32.99, "100ml"),
    (23, "Yara", "Lattafa", "Mujer", "Fresa, vainilla, almizcle rosado", 24.99, "100ml"),
    (24, "Ana Abiyedh Rose", "Lattafa", "Mujer", "Rosa turca, pachul\u00ed, s\u00e1ndalo", 28.99, "100ml"),
    (25, "Haya", "Lattafa", "Mujer", "Pera, jazm\u00edn, almizcle", 22.99, "80ml"),
    (26, "Raghba", "Lattafa", "Mujer", "Vainilla, \u00e1mbar, oud suave", 18.99, "100ml"),
    (27, "La Charmante", "Lattafa", "Mujer", "Rosa, jazm\u00edn, s\u00e1ndalo", 29.99, "80ml"),
    (28, "Musk Mood", "Lattafa", "Mujer", "Almizcle blanco, lavanda, iris", 20.99, "100ml"),
    (29, "Oud Mood", "Lattafa", "Mujer", "Oud, rosa, azafr\u00e1n", 23.99, "75ml"),
    (30, "Bade'e Al Oud Amethyst", "Lattafa", "Mujer", "Frutos rojos, oud, vainilla", 31.99, "80ml"),
    (31, "Club de Nuit Woman", "Armaf", "Mujer", "Melocot\u00f3n, rosa, almizcle", 34.99, "100ml"),
    (32, "Club de Nuit Imperial", "Armaf", "Mujer", "Grosella negra, lirio, vainilla", 36.99, "100ml"),
    (33, "Tag Her", "Armaf", "Mujer", "Frambuesa, violeta, almizcle", 19.99, "100ml"),
    (34, "Hunter Woman", "Armaf", "Mujer", "Mandarina, peon\u00eda, s\u00e1ndalo", 24.99, "100ml"),
    (35, "Odyssey Woman", "Armaf", "Mujer", "Pera, jazm\u00edn, almizcle blanco", 26.99, "100ml"),
    (36, "Voyage Bloom", "Armaf", "Mujer", "Loto, peon\u00eda, almizcle", 22.99, "100ml"),
    (37, "Pr\u00e9lude", "Armaf", "Mujer", "Bergamota, jazm\u00edn, s\u00e1ndalo", 28.99, "80ml"),
    (38, "Dareej", "Armaf", "Mujer", "Canela, caramelo, flor de naranjo", 25.99, "100ml"),
    (39, "Sillage Woman", "Armaf", "Mujer", "Lirio, violeta, almizcle", 31.99, "100ml"),
    (40, "Mystique", "Armaf", "Mujer", "Rosa negra, oud, \u00e1mbar", 27.99, "75ml"),
    (41, "Ana Abiyedh White", "Lattafa", "Unisex", "Lavanda, almizcle blanco, pera", 28.99, "100ml"),
    (42, "Opacity", "Armaf", "Unisex", "\u00c1mbar gris, bergamota, pachul\u00ed", 33.99, "90ml"),
    (43, "Bright Peach", "Armaf", "Unisex", "Melocot\u00f3n, caramelo, flores blancas", 31.99, "100ml"),
    (44, "Maahir Black", "Lattafa", "Unisex", "Caf\u00e9, cardamomo, cuero", 26.99, "100ml"),
    (45, "Rave Now", "Lattafa", "Unisex", "Lim\u00f3n, jengibre, menta", 23.99, "100ml"),
    (46, "Fakhar Rose", "Lattafa", "Unisex", "Rosa, azafr\u00e1n, almizcle", 28.99, "100ml"),
]

def safe_filename(name, brand):
    s = f"{brand.lower()}_{name.lower()}"
    s = s.replace("'", "_").replace("\u00e9", "e").replace("\u00e8", "e").replace("\u00ed", "i").replace("\u00fa", "u").replace("\u00f3", "o").replace("\u00e1", "a")
    s = re.sub(r"[^a-z0-9_]", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s

lines = []
lines.append("=" * 100)
lines.append("CATALOGO TNG SHOPS - 46 PERFUMES")
lines.append("=" * 100)
lines.append("")

for p in products:
    pid, name, brand, cat, notes, price, vol = p
    fname = safe_filename(name, brand)
    lines.append(f"ID {pid:>2} | {brand:>7} | {cat:>6} | {price:>5}\u20ac | {vol:>5}")
    lines.append(f"       {name}")
    lines.append(f"       Notas: {notes}")
    lines.append(f"       Imagen: {fname}.png")
    lines.append("")

lines.append("=" * 100)
lines.append("INSTRUCCIONES:")
lines.append("1. Busca cada perfume en Fragrancenet / Fragrantica / Notino / Amazon")
lines.append("2. Descarga la imagen oficial del producto (sin watermark)")
lines.append("3. Renombrala exactamente como indica 'Imagen:' arriba")
lines.append("4. Colocala en public/images/productos/")
lines.append("5. Pasame las imagenes y las reemplazo automaticamente")
lines.append("=" * 100)

path = r"D:\TNGSHOPS\PaginaWeb\CATALOGO_TNG.txt"
with open(path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Written {len(products)} products to CATALOGO_TNG.txt")