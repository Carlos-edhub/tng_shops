import re

with open(r'D:\TNGSHOPS\PaginaWeb\src\components\Hero.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

badge = '          <motion.div className="hero-badge" variants={fadeUp}>\n            <span className="hero-badge-dot" />\n            Nuevas fragancias 2025\n          </motion.div>\n\n'
content = content.replace('<motion.h1 variants={containerVariants}>', badge + '          <motion.h1 variants={containerVariants}>')

content = content.replace('<Link to="/tienda" className="btn btn-primary"', '<Link to="/tienda" className="btn btn-primary btn-hero"')
content = content.replace('<Link to="/nosotros" className="btn btn-outline"', '<Link to="/nosotros" className="btn btn-outline btn-hero"')

content = content.replace('Fragancias originales con env\u00edo r\u00e1pido y asesor\u00eda por WhatsApp.', 'Fragancias originales Lattafa, Armaf y m\u00e1s, con env\u00edo r\u00e1pido y asesor\u00eda personal por WhatsApp.')

social = '          <motion.div className="hero-social" variants={fadeUp}>\n            <div className="hero-avatars">\n              <div className="hero-avatar" style={{backgroundImage: \'url(https://i.pravatar.cc/32?img=1)\'}} />\n              <div className="hero-avatar" style={{backgroundImage: \'url(https://i.pravatar.cc/32?img=5)\'}} />\n              <div className="hero-avatar" style={{backgroundImage: \'url(https://i.pravatar.cc/32?img=8)\'}} />\n              <div className="hero-avatar" style={{backgroundImage: \'url(https://i.pravatar.cc/32?img=11)\'}} />\n              <div className="hero-avatar hero-avatar--more">+</div>\n            </div>\n            <div className="hero-stars">\n              <span className="hero-stars-icons">\u2605\u2605\u2605\u2605\u2605</span>\n              <span className="hero-stars-text">4.8/5 \u00b7 200+ rese\u00f1as</span>\n            </div>\n          </motion.div>\n\n'
content = content.replace('</motion.div>\n        </motion.div>\n\n        {/* Columna de imagen con anillos */}', '</motion.div>\n          ' + social + '        </motion.div>\n\n        {/* Columna de imagen con anillos */}')

content = content.replace('<div className="hero-glow" aria-hidden="true" />', '<div className="hero-glow" aria-hidden="true" />\n          <div className="hero-glow hero-glow--alt" aria-hidden="true" />')

content = content.replace('<img\n              src="/images/bannerTng_shops.png"', '<div className="hero-image-glass" />\n            <img\n              src="/images/bannerTng_shops.png"')

content = content.replace('{/* Gradiente pulsante detr\u00e1s de la imagen */}', '{/* Gradiente pulsante dual */}')

with open(r'D:\TNGSHOPS\PaginaWeb\src\components\Hero.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Hero.jsx updated successfully')