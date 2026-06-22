import { Component } from 'react';

export default class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  render() {
    if (this.state.hasError) {
      return (
        <main id="main-content" style={{ textAlign: 'center', padding: '6rem 0' }}>
          <div className="container">
            <span style={{ fontSize: '3rem', display: 'block', marginBottom: '1rem' }}>⚠</span>
            <h1>Algo salió mal</h1>
            <p style={{ color: 'var(--text-secondary)', marginBottom: '2rem' }}>
              Ha ocurrido un error inesperado. Intenta recargar la página.
            </p>
            <button
              className="btn btn-primary"
              onClick={() => window.location.reload()}
            >
              Recargar página
            </button>
          </div>
        </main>
      );
    }
    return this.props.children;
  }
}
