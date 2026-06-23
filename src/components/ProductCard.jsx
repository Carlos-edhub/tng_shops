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
        <div className="card-media">
          {product.isNew && <span className="card-badge card-badge-new">Nuevo</span>}
          {discount > 0 && <span className="card-badge card-badge-discount">-{discount}%</span>}
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

        <span className="card-brand">{product.brand}</span>
        <h3 className="card h3">{product.name}</h3>

        {product.family && <div className="card-notes">{product.family}</div>}
        <p className="card-desc">{product.description}</p>

        {/* Intensity & Longevity bars */}
        {!compact && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.15rem', marginTop: '0.15rem' }}>
            <IntensityBar value={product.intensity || 3} label="Int." />
            <IntensityBar value={product.longevity || 3} label="Dur." />
          </div>
        )}

        <div className="card-meta">
          <span className="card-notes">{product.notes}</span>
          <span className="card-volume">{product.volume}</span>
        </div>
      </Link>

      {!compact && (
      <div className="card-foot">
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', width: '100%' }}>
          <span className="price" aria-label={`Precio ${product.price} euros`}>
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
            className="btn btn-primary btn-sm"
            onClick={handleAddToCart}
            aria-label={`Añadir ${product.name} al carrito`}
          >
            Añadir
          </button>
          <button
            className="btn btn-whatsapp btn-sm"
            onClick={() => orderProduct(product.name)}
            aria-label={`Comprar ${product.name} por WhatsApp`}
            title="Comprar por WhatsApp"
          >
            WhatsApp
          </button>
        </div>
      </div>
      )}
    </motion.article>
  );
}