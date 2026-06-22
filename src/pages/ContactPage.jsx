import SEO from '../components/SEO';
import Contact from '../components/Contact';

export default function ContactPage() {
  return (
    <>
      <SEO title="Contacto" description="Contacta con TNG Shops por WhatsApp o email. Te asesoramos para encontrar tu perfume ideal." />
      <main id="main-content">
        <Contact />
      </main>
    </>
  );
}
