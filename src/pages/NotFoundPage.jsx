import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';

export default function NotFoundPage() {
  return (
    <main id="main-content">
      <section className="shop" style={{ textAlign: 'center', padding: '6rem 0', minHeight: '60vh', display: 'flex', alignItems: 'center' }}>
        <div className="container">
          <motion.div
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
          >
            <span style={{ fontSize: '5rem', fontWeight: 700, color: 'var(--accent)', display: 'block', lineHeight: 1 }}>404</span>
            <h1 style={{ fontSize: '2rem', fontWeight: 700, margin: '1rem 0 0.5rem' }}>Página no encontrada</h1>
            <p style={{ color: 'var(--text-secondary)', marginBottom: '2rem', fontSize: '1.125rem', maxWidth: 400, margin: '0.5rem auto 2rem' }}>
              La página que buscas no existe o ha sido movida.
            </p>
            <Link to="/" className="btn btn-primary">Volver al inicio</Link>
          </motion.div>
        </div>
      </section>
    </main>
  );
}
