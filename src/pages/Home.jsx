/**
 * Home.jsx - Página principal de tng_shops
 * 
 * Es la página de aterrizaje que combina:
 * - Hero (bienvenida llamativa)
 * - Badges (ventajas)
 * - Tienda (productos destacados)
 * - Nosotros (información de la marca)
 * - Contacto
 * 
 * Es una página de una sola sección que muestra todo el contenido,
 * ideal para captar clientes desde el primer vistazo.
 */

import { Link } from 'react-router-dom';
import SEO from '../components/SEO';
import Hero from '../components/Hero';
import Badges from '../components/Badges';
import Testimonials from '../components/Testimonials';
import BrandsSection from '../components/BrandsSection';
import ProductGrid from '../components/ProductGrid';
import FeaturedCarousel from '../components/FeaturedCarousel';
import CollectionsShowcase from '../components/CollectionsShowcase';
import About from '../components/About';
import Contact from '../components/Contact';
import Newsletter from '../components/Newsletter';
import products from '../data/products';
import collections from '../data/collections';

export default function Home() {
  // Mostrar solo 6 productos destacados en el homepage
  const bestSellers = collections.find((c) => c.id === 'best-sellers');
  const featuredIds = bestSellers ? bestSellers.filter : (p) => [11, 1, 3, 21, 23, 12].includes(p.id);
  const featuredProducts = products.filter(featuredIds).slice(0, 6);

  return (
    <>
      <SEO description="Perfumes originales Lattafa y Armaf. Envío rápido y asesoría personal por WhatsApp. Las mejores fragancias orientales al mejor precio." />
      <main id="main-content">
        <Hero />
        <Badges />
        <Testimonials />
        <BrandsSection />
        <CollectionsShowcase />
        <FeaturedCarousel products={products} />
        <section id="tienda" className="shop" aria-labelledby="shop-title">
          <div className="container">
            <header className="shop-head">
              <div>
                <h2 id="shop-title"><span>T</span>ienda</h2>
                <p>Nuestros perfumes más populares</p>
              </div>
              <Link to="/tienda" className="btn btn-primary" style={{ fontSize: '0.9rem', padding: '0.6rem 1.5rem', textDecoration: 'none', display: 'inline-flex', alignItems: 'center', gap: '0.4rem' }}>
                Ver más productos →
              </Link>
            </header>
            <ProductGrid products={featuredProducts} />
          </div>
        </section>
        <About />
        <Newsletter />
        <Contact />
      </main>
    </>
  );
}
