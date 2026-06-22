lines = open(r"D:\TNGSHOPS\PaginaWeb\src\components\Hero.jsx.bak", "r", encoding="utf-8").readlines()
for i in range(55, 62):
    line = lines[i].rstrip("\n")
    print(f"{i+1}: {repr(line)}")