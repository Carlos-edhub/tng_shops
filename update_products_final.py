import os, re

products = [
    # HOMBRE (20)
    (1, "Fakhar Men Black", "Lattafa", "Hombre", "Misterioso e intenso. Noche con car\u00e1cter.", "Cuero, \u00e1mbar, especias", 29.99, "100ml", False, 3, 39.99),
    (2, "Fakhar Men Silver", "Lattafa", "Hombre", "Fresco y moderno. Para el d\u00eda a d\u00eda.", "Bergamota, lavanda, almizcle", 26.99, "100ml", True, None, None),
    (3, "Asad", "Lattafa", "Hombre", "Audaz y especiado. Presencia magn\u00e9tica.", "Pimienta negra, tabaco, cuero", 24.99, "100ml", False, 5, None),
    (4, "Ramz Silver", "Lattafa", "Hombre", "Dulce y envolvente. Perfume de impacto.", "Pera, canela, vainilla", 22.99, "100ml", True, None, 29.99),
    (5, "Qaed Al Fursan", "Lattafa", "Hombre", "Ex\u00f3tico y c\u00e1lido. Aventura en botella.", "Pi\u00f1a, azafr\u00e1n, \u00e1mbar", 27.99, "100ml", False, None, None),
    (6, "Al Wisam", "Lattafa", "Hombre", "Vers\u00e1til y fresco. Ideal diario.", "Manzana, cedro, s\u00e1ndalo", 29.99, "100ml", False, None, 35.99),
    (7, "Raghba Wood Intense", "Lattafa", "Hombre", "Amaderado y sensual. Deja huella.", "Madera de oud, almizcle, \u00e1mbar", 19.99, "100ml", False, 4, None),
    (8, "Shem Al Sheikh", "Lattafa", "Hombre", "Cl\u00e1sico \u00e1rabe. Elegancia tradicional.", "Bergamota, oud, s\u00e1ndalo", 18.99, "100ml", False, None, None),
    (9, "Najdia", "Lattafa", "Hombre", "Marino y en\u00e9rgico. Frescura activa.", "Toronja, jengibre, almizcle acu\u00e1tico", 21.99, "100ml", True, None, None),
    (10, "Oud Al Sahraa", "Lattafa", "Hombre", "Oud intenso. Noches \u00e1rabes.", "Oud, rosa, pachul\u00ed", 25.99, "75ml", False, 2, 32.99),
    (11, "Club de Nuit Intense Man", "Armaf", "Hombre", "Icono indiscutido. Poderoso y elegante.", "Bergamota, pimienta rosa, cuero", 36.99, "105ml", False, 5, 46.99),
    (12, "Club de Nuit Iconic", "Armaf", "Hombre", "Audaz y moderno. Presencia segura.", "Bergamota, pimienta, cuero", 36.99, "105ml", True, None, None),
    (13, "Club de Nuit Sillage", "Armaf", "Hombre", "Elegancia fresca y magn\u00e9tica.", "Lim\u00f3n, jengibre, almizcle", 36.99, "100ml", False, None, None),
    (14, "Club de Nuit Milestone", "Armaf", "Hombre", "Frescura \u00fanica. Estilo inconfundible.", "Sal marina, bergamota, almizcle blanco", 38.99, "100ml", True, None, None),
    (15, "Club de Nuit Urban Man", "Armaf", "Hombre", "Energ\u00eda urbana. Para el d\u00eda.", "Toronja, cardamomo, cedro", 32.99, "100ml", False, None, None),
    (16, "Hunter Intense", "Armaf", "Hombre", "Din\u00e1mico y cautivador. Atr\u00e9vete.", "Lim\u00f3n, lavanda, \u00e1mbar", 28.99, "100ml", False, 3, 35.99),
    (17, "Tag Him", "Armaf", "Hombre", "Deportivo y limpio. Para el gym.", "Toronja, menta, almizcle", 19.99, "100ml", False, None, None),
    (18, "Voyage Blues", "Armaf", "Hombre", "Aventura acu\u00e1tica. Frescura total.", "Mandarina, lavanda, s\u00e1ndalo", 21.99, "100ml", False, None, None),
    (19, "Odyssey Homme", "Armaf", "Hombre", "\u00c9pico y misterioso. Viaje olfativo.", "Pimienta rosa, cuero, tabaco", 27.99, "100ml", False, 4, None),
    (20, "Shadow Wood", "Armaf", "Hombre", "Amaderado \u00edntimo. Elegancia nocturna.", "Madera de cedro, \u00e1mbar, vainilla", 24.99, "75ml", False, None, 29.99),
    # MUJER (20)
    (21, "Khamrah", "Lattafa", "Mujer", "C\u00e1lido y dulce. Perfecto oto\u00f1o.", "Canela, d\u00e1til, pralin\u00e9", 39.99, "100ml", False, 1, 49.99),
    (22, "Ana Abiyedh Poudr\u00e9e", "Lattafa", "Mujer", "Suave empolvado. Sofisticado.", "Almendra, vainilla, almizcle", 32.99, "100ml", True, None, None),
    (23, "Yara", "Lattafa", "Mujer", "Femenino y floral. Dulce y moderno.", "Fresa, vainilla, almizcle rosado", 24.99, "100ml", True, None, None),
    (24, "Ana Abiyedh Rose", "Lattafa", "Mujer", "Rosa delicada. Elegancia pura.", "Rosa turca, pachul\u00ed, s\u00e1ndalo", 28.99, "100ml", False, None, None),
    (25, "Haya", "Lattafa", "Mujer", "Alegre y juvenil. Flores y fruta.", "Pera, jazm\u00edn, almizcle", 22.99, "80ml", False, 4, None),
    (26, "Raghba", "Lattafa", "Mujer", "C\u00e1lido y acogedor. Vainilla \u00e1rabe.", "Vainilla, \u00e1mbar, oud suave", 18.99, "100ml", False, None, None),
    (27, "La Charmante", "Lattafa", "Mujer", "Refinada y lujosa. Ocasiones especiales.", "Rosa, jazm\u00edn, s\u00e1ndalo", 29.99, "80ml", False, 2, None),
    (28, "Musk Mood", "Lattafa", "Mujer", "Almizcle limpio. Frescura \u00edntima.", "Almizcle blanco, lavanda, iris", 20.99, "100ml", False, None, None),
    (29, "Oud Mood", "Lattafa", "Mujer", "Oud floral. Misterio femenino.", "Oud, rosa, azafr\u00e1n", 23.99, "75ml", False, None, 28.99),
    (30, "Bade'e Al Oud Amethyst", "Lattafa", "Mujer", "Oud y frutos rojos. Seducci\u00f3n.", "Frutos rojos, oud, vainilla", 31.99, "80ml", True, None, None),
    (31, "Club de Nuit Woman", "Armaf", "Mujer", "Floral afrutado. Femenino poderoso.", "Melocot\u00f3n, rosa, almizcle", 34.99, "100ml", False, None, None),
    (32, "Club de Nuit Imperial", "Armaf", "Mujer", "Imperial y cautivador. Deja huella.", "Grosella negra, lirio, vainilla", 36.99, "100ml", False, 3, 44.99),
    (33, "Tag Her", "Armaf", "Mujer", "Dulce y coqueto. Para el d\u00eda.", "Frambuesa, violeta, almizcle", 19.99, "100ml", False, None, None),
    (34, "Hunter Woman", "Armaf", "Mujer", "Cautivador y vibrante. Elegancia.", "Mandarina, peon\u00eda, s\u00e1ndalo", 24.99, "100ml", True, None, None),
    (35, "Odyssey Woman", "Armaf", "Mujer", "Aventura floral. Viaje sensorial.", "Pera, jazm\u00edn, almizcle blanco", 26.99, "100ml", False, 5, None),
    (36, "Voyage Bloom", "Armaf", "Mujer", "Floral acu\u00e1tico. Brisa primaveral.", "Loto, peon\u00eda, almizcle", 22.99, "100ml", False, None, None),
    (37, "Pr\u00e9lude", "Armaf", "Mujer", "Apertura floral. Romance en botella.", "Bergamota, jazm\u00edn, s\u00e1ndalo", 28.99, "80ml", True, None, 34.99),
    (38, "Dareej", "Armaf", "Mujer", "Osado y dulce. Personalidad \u00fanica.", "Canela, caramelo, flor de naranjo", 25.99, "100ml", False, None, None),
    (39, "Sillage Woman", "Armaf", "Mujer", "Estela floral. Sofisticaci\u00f3n pura.", "Lirio, violeta, almizcle", 31.99, "100ml", False, None, None),
    (40, "Mystique", "Armaf", "Mujer", "Misteriosa y envolvente. Noche m\u00e1gica.", "Rosa negra, oud, \u00e1mbar", 27.99, "75ml", False, 2, None),
    # UNISEX (6)
    (41, "Ana Abiyedh White", "Lattafa", "Unisex", "Limpio y fresco. Para cualquier momento.", "Lavanda, almizcle blanco, pera", 28.99, "100ml", False, None, None),
    (42, "Opacity", "Armaf", "Unisex", "Moderno y envolvente. Magn\u00e9tico.", "\u00c1mbar gris, bergamota, pachul\u00ed", 33.99, "90ml", False, None, None),
    (43, "Bright Peach", "Armaf", "Unisex", "Dulce y jugoso. Vibrante y juvenil.", "Melocot\u00f3n, caramelo, flores blancas", 31.99, "100ml", True, None, None),
    (44, "Maahir Black", "Lattafa", "Unisex", "Intenso y seductor. Noche m\u00e1gica.", "Caf\u00e9, cardamomo, cuero", 26.99, "100ml", False, None, None),
    (45, "Rave Now", "Lattafa", "Unisex", "Energ\u00eda pura. Frescura \u00e9pica.", "Lim\u00f3n, jengibre, menta", 23.99, "100ml", True, None, None),
    (46, "Fakhar Rose", "Lattafa", "Unisex", "Rosa \u00e1rabe. Elegancia compartida.", "Rosa, azafr\u00e1n, almizcle", 28.99, "100ml", False, None, None),
]

def esc(val):
    if val is None: return None
    return str(val).replace("\\", "\\\\").replace("'", "\\'")

lines = ["const products = ["]
for p in products:
    pid, name, brand, cat, desc, notes, price, vol, isNew, stock, origPrice = p
    fname = f"{brand.lower()}_{name.lower()}".replace("'", "_")
    fname = re.sub(r"[^a-z0-9_\u00e0-\u00ff]", "_", fname).replace("__", "_").strip("_")
    image_path = f"/images/productos/{fname}.png"
    
    lines.append("  {")
    lines.append(f"    id: {pid},")
    lines.append(f"    name: '{esc(name)}',")
    lines.append(f"    description: '{esc(desc)}',")
    lines.append(f"    price: {price},")
    if origPrice is not None:
        lines.append(f"    originalPrice: {origPrice},")
    lines.append(f"    image: '{image_path}',")
    lines.append(f"    category: '{cat}',")
    lines.append(f"    brand: '{brand}',")
    lines.append(f"    notes: '{esc(notes)}',")
    lines.append(f"    volume: '{vol}',")
    if isNew:
        lines.append("    isNew: true,")
    if stock is not None:
        lines.append(f"    stock: {stock},")
    lines.append("  },")
lines.append("];")
lines.append("")
lines.append("export default products;")

with open(r'D:\TNGSHOPS\PaginaWeb\src\data\products.js', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f"Written {len(products)} products")