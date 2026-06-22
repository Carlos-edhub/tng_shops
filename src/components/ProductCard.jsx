import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import { useWhatsApp } from '../hooks/useWhatsApp';
import { useCartDispatch, CART_ACTIONS } from '../context/CartContext';
import { useToast } from '../context/ToastContext';

function IntensityBar({ value, label }) {
  const colors = ['#203B36', '#2B4D46', '#3A6B62', '#5E8B82', '#8FB5AC'];
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: '0.35rem' }}>
      <span style={{ fontSize: '0.65rem', color: 'var(--text-muted)', minWidth: '20px' }}>{label}</span>
      <div style={{ display: 'flex', gap: '2px', flex: 1 }}>
        {[1,2,3,4,5].map((i) => (
          <div
            key={i}
            style={{
              height: '4px',
              flex: 1,
              borderRadius: '2px',
              background: i <= value ? colors[value - 1] : 'var(--border)',
              transition: 'background 0.3s ease',
            }}
          />
        ))}
      </div>
    </div>
  );
}

export default function ProductCard({ product, index = 0, compact = false }) {
  const { orderProduct } = useWhatsApp();
  const dispatch = useCartDispatch();
  const { addToast } = useToast();

  const handleAddToCart = () => {
    dispatch({
      type: CART_ACTIONS.ADD,
      product: {
        id: product.id,
        name: product.name,
        price: product.price,
        image: product.image,
      },
    });
    addToast(`${product.name} añadido al carrito`, 'success');
  };

  const discount = product.originalPrice ? Math.round((1 - product.price / product.originalPrice) * 100) : 0
  const lowStock = product.stock !== undefined && product.stock <= 5

  const categoryColors = {
    Hombre: { bg: 'rgba(32,59,54,0.08)', text: '#203B36', border: 'rgba(32,59,54,0.15)' },
    Mujer: { bg: 'rgba(216,200,168,0.2)', text: '#8B7355', border: 'rgba(216,200,168,0.3)' },
    Unisex: { bg: 'rgba(32,59,54,0.05)', text: '#5E5E5E', border: 'rgba(0,0,0,0.1)' },
  };
  const cc = categoryColors[product.category] || categoryColors.Unisex;

  return (
    <motion.article
      className="card"
      data-name={product.name}
      initial={{ opacity: 0, y: 30 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4, delay: index * 0.05 }}
      whileHover={{ y: -6 }}
    >
      <Link to={`/producto/${product.id}`} style={{ textDecoration: 'none', color: 'inherit' }}>
        <div
          className="card-media"
          style={{
            width: '100%',
            height: '190px',
            background: 'var(--bg)',
            borderRadius: 'var(--radius-md)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            overflow: 'hidden',
            position: 'relative',
            marginBottom: '0.25rem',
          }}
        >
          {product.isNew && <span className="card-badge card-badge-new" style={{ position: 'absolute', top: '0.4rem', left: '0.4rem', zIndex: 2, fontSize: '0.6rem', fontWeight: 600, padding: '0.15rem 0.45rem', borderRadius: 'var(--radius-sm)', background: 'var(--accent)', color: '#fff', textTransform: 'uppercase', letterSpacing: '0.5px' }}>Nuevo</span>}
          {discount > 0 && <span className="card-badge card-badge-discount" style={{ position: 'absolute', top: '0.4rem', right: '0.4rem', zIndex: 2, fontSize: '0.6rem', fontWeight: 600, padding: '0.15rem 0.45rem', borderRadius: 'var(--radius-sm)', background: 'var(--accent-light)', color: 'var(--accent)' }}>-{discount}%</span>}
          {lowStock && !product.isNew && (
            <div style={{ position: 'absolute', bottom: '0.4rem', left: '0.4rem', right: '0.4rem', zIndex: 2, display: 'flex', alignItems: 'center', gap: '0.3rem' }}>
              <div style={{ flex: 1, height: '3px', background: 'rgba(0,0,0,0.08)', borderRadius: '2px', overflow: 'hidden' }}>
                <div style={{ width: `${(product.stock / 5) * 100}%`, height: '100%', background: product.stock <= 2 ? '#ef4444' : '#C8B48A', borderRadius: '2px', transition: 'width 0.5s ease' }} />
              </div>
              <span style={{ fontSize: '0.55rem', color: 'var(--text-secondary)', fontWeight: 500 }}>Quedan {product.stock}</span>
            </div>
          )}
          <img
            src={product.image}
            alt={`${product.name} perfume`}
            loading="lazy"
            style={{
              width: '100%',
              height: '100%',
              objectFit: 'contain',
              padding: '0.75rem',
              transition: 'transform 0.5s cubic-bezier(0.4, 0, 0.2, 1)',
            }}
          />
        </div>

        {/* Brand + Category pill */}
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: '0.4rem' }}>
          <span style={{ fontSize: '0.7rem', fontWeight: 600, color: 'var(--accent)', textTransform: 'uppercase', letterSpacing: '0.8px' }}>{product.brand}</span>
          <span style={{ fontSize: '0.6rem', fontWeight: 600, padding: '0.1rem 0.5rem', borderRadius: '999px', background: cc.bg, color: cc.text, border: `1px solid ${cc.border}` }}>
            {product.category}
          </span>
        </div>

        <h3 style={{ fontSize: '1rem', margin: '0.15rem 0 0.1rem', fontWeight: 600, color: 'var(--text)', letterSpacing: '-0.3px', lineHeight: 1.3 }}>{product.name}</h3>

        {/* Family */}
        {product.family && (
          <div style={{ fontSize: '0.7rem', color: 'var(--text-muted)', marginBottom: '0.15rem', fontStyle: 'italic' }}>
            {product.family}
          </div>
        )}

        <p className="card-desc" style={{ color: 'var(--text-secondary)', fontSize: '0.8rem', margin: '0.1rem 0', lineHeight: 1.5, flexGrow: 1 }}>{product.description}</p>

        {/* Intensity & Longevity bars */}
        {!compact && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.15rem', marginTop: '0.15rem' }}>
            <IntensityBar value={product.intensity || 3} label="Int." />
            <IntensityBar value={product.longevity || 3} label="Dur." />
          </div>
        )}

        <div className="card-meta" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', gap: '0.4rem', marginTop: '0.2rem' }}>
          <span className="card-notes" style={{ fontSize: '0.7rem', color: 'var(--text-muted)', lineHeight: 1.3, flex: 1 }}>{product.notes}</span>
          <span className="card-volume" style={{ fontSize: '0.65rem', color: 'var(--text-muted)', whiteSpace: 'nowrap', background: 'var(--surface-hover)', padding: '0.1rem 0.4rem', borderRadius: '4px' }}>{product.volume}</span>
        </div>
      </Link>

      {!compact && (
      <div className="card-foot" style={{ flexDirection: 'column', gap: '0.4rem', marginTop: 'auto', paddingTop: '0.4rem', borderTop: '1px solid var(--border)' }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', width: '100%' }}>
          <span className="price" aria-label={`Precio ${product.price} euros`} style={{ fontSize: '1.15rem', fontWeight: 600, color: 'var(--accent)', letterSpacing: '-0.3px' }}>
            {product.price.toFixed(2)}€
          </span>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            {product.originalPrice && (
              <span style={{ color: 'var(--text-muted)', fontSize: '0.8rem', textDecoration: 'line-through' }}>
                {product.originalPrice.toFixed(2)}€
              </span>
            )}
            {product.price >= 30 && (
              <span style={{ fontSize: '0.55rem', fontWeight: 500, color: '#22c55e', background: 'rgba(34,197,94,0.08)', padding: '0.1rem 0.35rem', borderRadius: '4px', border: '1px solid rgba(34,197,94,0.15)' }}>
                Envío gratis
              </span>
            )}
          </div>
        </div>
        <div style={{ display: 'flex', gap: '0.4rem', width: '100%' }}>
          <button
            className="btn btn-primary"
            onClick={handleAddToCart}
            aria-label={`Añadir ${product.name} al carrito`}
            style={{
              flex: 1, fontSize: '0.8rem', padding: '0.5rem 0.75rem',
              background: 'var(--accent)',
              border: 'none', color: '#fff', fontWeight: 600,
              borderRadius: 'var(--radius-sm)',
              cursor: 'pointer',
              transition: 'all 0.25s ease',
            }}
            onMouseEnter={(e) => { e.target.style.background = 'var(--accent-hover)'; e.target.style.transform = 'translateY(-1px)'; }}
            onMouseLeave={(e) => { e.target.style.background = 'var(--accent)'; e.target.style.transform = 'translateY(0)'; }}
          >
            Añadir
          </button>
          <button
            className="btn btn-outline"
            onClick={() => orderProduct(product.name)}
            aria-label={`Comprar ${product.name} por WhatsApp`}
            style={{
              flex: 1, fontSize: '0.8rem', padding: '0.5rem 0.75rem',
              background: 'rgba(37,211,102,0.08)',
              border: '1px solid rgba(37,211,102,0.15)',
              color: '#25D366', fontWeight: 600,
              borderRadius: 'var(--radius-sm)',
              cursor: 'pointer',
              transition: 'all 0.25s ease',
            }}
            title="Comprar por WhatsApp"
            onMouseEnter={(e) => { e.target.style.background = '#20BD5A'; e.target.style.color = '#fff'; e.target.style.transform = 'translateY(-1px)'; }}
            onMouseLeave={(e) => { e.target.style.background = 'rgba(37,211,102,0.08)'; e.target.style.color = '#25D366'; e.target.style.transform = 'translateY(0)'; }}
          >
            WhatsApp
          </button>
        </div>
      </div>
      )}
    </motion.article>
  );
}