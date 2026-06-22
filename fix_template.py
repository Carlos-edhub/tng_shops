import re
with open(r'D:\TNGSHOPS\PaginaWeb\src\components\Hero.jsx', 'r', encoding='utf-8') as f:
    c = f.read()
# Fix broken template literals (were `` - now add ${...} back)
bt = chr(96)
c = "left: " + bt + "${15 + i * 14}" + bt + ",".join(c.rsplit("left: ``,".replace("``", bt + bt), 1))
c = "top: " + bt + "${20 + (i % 3) * 25}" + bt + ",".join(c.rsplit("top: ``,".replace("``", bt + bt), 1))
c = "width: " + bt + "${4 + (i % 3) * 4}" + bt + "px,".join(c.rsplit("width: ``px,".replace("``", bt + bt), 1))
c = "height: " + bt + "${4 + (i % 3) * 4}" + bt + "px,".join(c.rsplit("height: ``px,".replace("``", bt + bt), 1))
c = "animationDelay: " + bt + "${i * 0.8}" + bt + "s,".join(c.rsplit("animationDelay: ``s,".replace("``", bt + bt), 1))
c = "animationDuration: " + bt + "${3 + (i % 3)}" + bt + "s,".join(c.rsplit("animationDuration: ``s,".replace("``", bt + bt), 1))
with open(r'D:\TNGSHOPS\PaginaWeb\src\components\Hero.jsx', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed template literals')