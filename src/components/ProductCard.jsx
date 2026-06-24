import { useState } from 'react';
import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import { useWhatsApp } from '../hooks/useWhatsApp';
import { useCartDispatch, CART_ACTIONS } from '../context/CartContext';
import { useToast } from '../context/ToastContext';

function IntensityBar({ value, label }) {
  const colors = ['#203B36', '#2B4D46', '#3A6B62', '#5E8B82', '#8FB5AC'];
  return (
    <div className="intensity-bar">
      <span className="intensity-label">{label}</span>
      <div className="intensity-track">
        {[1,2,3,4,5].map((i) => (
          <div
            key={i}
            className="intensity-segment"
            style={{
              background: i <= value ? colors[value - 1] : 'var(--border)',
            }}
          />
        ))}
      </div>
    </div>
  );
}

export default function ProductCard({ product, index = 0, compact = false }) {
  const [isFavorite, setIsFavorite] = useState(false);
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
          <button
            className="favorite-btn"
            onClick={(e) => {
              e.preventDefault();
              e.stopPropagation();
              setIsFavorite(!isFavorite);
              addToast(isFavorite ? 'Eliminado de favoritos' : 'Añadido a favoritos', 'success');
            }}
            aria-label={isFavorite ? 'Eliminar de favoritos' : 'Añadir a favoritos'}
            style={{ right: discount > 0 ? '3.5rem' : '0.4rem' }}
          >
            {isFavorite ? '❤️' : '🤍'}
          </button>
          {lowStock && !product.isNew && (
            <div className="stock-indicator">
              <div className="stock-bar">
                <div 
                  className={`stock-fill ${product.stock <= 2 ? 'low' : ''}`}
                  style={{ width: `${(product.stock / 5) * 100}%` }}
                />
              </div>
              <span className="stock-text">Quedan {product.stock}</span>
            </div>
          )}
          <img
            src={product.image}
            alt={`${product.name} perfume`}
            loading="lazy"
            className="card-media-img"
          />
        </div>

        <span className="card-brand">{product.brand}</span>
        <h3 className="card h3">{product.name}</h3>

        {product.family && <div className="card-notes">{product.family}</div>}
        <p className="card-desc">{product.description}</p>

        {/* Intensity & Longevity bars */}
        {!compact && (
          <div className="card-bars">
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
        <div className="card-price-row">
          <span className="price" aria-label={`Precio ${product.price} euros`}>
            {product.price.toFixed(2)}€
          </span>
          <div className="card-price-extras">
            {product.originalPrice && (
              <span className="price-old">{product.originalPrice.toFixed(2)}€</span>
            )}
            {product.price >= 30 && (
              <span className="free-shipping-badge">Envío gratis</span>
            )}
          </div>
        </div>
        <div className="card-buttons">
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