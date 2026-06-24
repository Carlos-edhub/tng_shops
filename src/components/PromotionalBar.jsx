import { useState, useEffect, useCallback } from 'react'
import { Link } from 'react-router-dom'

const messages = [
  '🚚 Envío gratis desde 30€',
  '🎁 2 muestras gratis con cada pedido',
  '🏷️ Código: BIENVENIDO10 — 10% off',
]

export default function PromotionalBar() {
  const [index, setIndex] = useState(0)
  const [isAnimating, setIsAnimating] = useState(false)

  const next = useCallback(() => {
    setIsAnimating(true)
    setTimeout(() => {
      setIndex((i) => (i + 1) % messages.length)
      setIsAnimating(false)
    }, 300)
  }, [])

  useEffect(() => {
    const t = setInterval(next, 4000)
    return () => clearInterval(t)
  }, [next])

  return (
    <div className="promo-bar">
      <div className="container promo-bar-inner">
        <div className="promo-bar-carousel">
          <div 
            className="promo-bar-slider" 
            style={{ 
              transform: `translateX(-${index * 100}%)`,
              transition: isAnimating ? 'transform 0.3s ease-in-out' : 'none'
            }}
          >
            {messages.map((msg, i) => (
              <div key={i} className="promo-bar-slide">
                <span className="promo-bar-text">{msg}</span>
              </div>
            ))}
          </div>
        </div>
        <div className="promo-bar-actions">
          <Link to="/servicios" className="promo-bar-link">Servicios</Link>
          <Link to="/fidelidad" className="promo-bar-link">Fidelidad</Link>
        </div>
      </div>
    </div>
  )
}
