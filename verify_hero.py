lines = open(r"D:\TNGSHOPS\PaginaWeb\src\components\Hero.jsx", "r", encoding="utf-8").readlines()
searches = ["hero-badge", "hero-social", "hero-glow--alt", "hero-image-glass", "btn-hero", "Fragancias originales Lattafa"]
for s in searches:
    found = [i+1 for i, l in enumerate(lines) if s in l]
    if found:
        print(f"  {s}: lines {found}")
    else:
        print(f"  {s}: NOT FOUND")
for i in range(63, 70):
    print(f"Line {i+1}: {lines[i].rstrip()}")