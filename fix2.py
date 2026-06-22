import re
with open(r'D:\TNGSHOPS\PaginaWeb\src\components\Hero.jsx', 'r', encoding='utf-8') as f:
    c = f.read()
bt = chr(96)
d = chr(36)
lb = chr(123)
rb = chr(125)
c = c.replace('left: ' + bt + bt + ',', 'left: ' + bt + d + lb + '15 + i * 14' + rb + '%' + bt + ',')
c = c.replace('top: ' + bt + bt + ',', 'top: ' + bt + d + lb + '20 + (i % 3) * 25' + rb + '%' + bt + ',')
c = c.replace('width: ' + bt + bt + 'px,', 'width: ' + bt + d + lb + '4 + (i % 3) * 4' + rb + 'px' + bt + ',')
c = c.replace('height: ' + bt + bt + 'px,', 'height: ' + bt + d + lb + '4 + (i % 3) * 4' + rb + 'px' + bt + ',')
c = c.replace('animationDelay: ' + bt + bt + 's,', 'animationDelay: ' + bt + d + lb + 'i * 0.8' + rb + 's' + bt + ',')
c = c.replace('animationDuration: ' + bt + bt + 's,', 'animationDuration: ' + bt + d + lb + '3 + (i % 3)' + rb + 's' + bt + ',')
with open(r'D:\TNGSHOPS\PaginaWeb\src\components\Hero.jsx', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed!')