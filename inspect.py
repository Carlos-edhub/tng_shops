import re
lines = open(r"D:\TNGSHOPS\PaginaWeb\src\components\Hero.jsx", "r", encoding="utf-8").readlines()
for i in range(54, 62):
    line = lines[i].rstrip("\n")
    print(f"{i+1}: {repr(line)}")