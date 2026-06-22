import re
with open(r"D:\TNGSHOPS\PaginaWeb\src\data\products.js", "r", encoding="utf-8") as f:
    content = f.read()

products = []
pattern = r"id:\s*(\d+).*?name:\s*'([^']*)'.*?brand:\s*'([^']*)'.*?category:\s*'([^']*)'.*?notes:\s*'([^']*)'.*?price:\s*([\d.]+).*?volume:\s*'([^']*)'"
for m in re.finditer(pattern, content, re.DOTALL):
    pid, name, brand, cat, notes, price, vol = m.groups()
    products.append({"id": pid, "name": name, "brand": brand, "category": cat, "notes": notes, "price": price, "volume": vol})

print(f"# CATÁLOGO TNG SHOPS - {len(products)} PERFUMES")
print(f"# ==========================================\n")
for p in products:
    print(f"ID {p['id']:>2} | {p['brand']:>7} | {p['category']:>6} | {p['price']:>5}€ | {p['volume']:>5} | {p['name']}")
    print(f"       Notas: {p['notes']}")
    print(f"       Imagen esperada: /images/productos/{p['brand'].lower()}_{p['name'].lower().replace(' ', '_')}.png")
    print()