#!/usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuth
import json

# Configuración
WP_URL = "https://berilio.co"
WP_USER = "admin"
WP_PASS = "AjAP i1M9 lhLv wWCj 68NN PmCB"

auth = HTTPBasicAuth(WP_USER, WP_PASS)

# HTML con estilos más específicos y !important para sobrescribir el tema
html_content = """
<!-- Berilio Landing Page -->
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700;800&display=swap');

/* Reset específico para WordPress */
.entry-content > * {
    max-width: none !important;
}

.berilio-wrapper {
    margin: -50px -50px 0 -50px !important;
    padding: 0 !important;
    width: calc(100% + 100px) !important;
    font-family: 'JetBrains Mono', monospace !important;
}

@media (max-width: 768px) {
    .berilio-wrapper {
        margin: -20px -20px 0 -20px !important;
        width: calc(100% + 40px) !important;
    }
}

/* Variables */
.berilio-wrapper {
    --primary-color: #2196F3;
    --primary-dark: #1565C0;
    --primary-darker: #10519D;
    --text-primary: #2D2D2D;
    --text-secondary: #666666;
    --beige: #E3F2FD;
    --mint: #E1F5FE;
    --lavender: #E8EAF6;
    --border-light: #F0F0F0;
}

.berilio-wrapper * {
    box-sizing: border-box !important;
    margin: 0;
    padding: 0;
}

/* Navigation Bar */
.berilio-nav {
    background: rgba(254, 254, 254, 0.98) !important;
    border-bottom: 1px solid #F0F0F0 !important;
    padding: 1rem 3rem !important;
    position: sticky !important;
    top: 0 !important;
    z-index: 1000 !important;
    width: 100% !important;
}

.berilio-nav-container {
    max-width: 1200px !important;
    margin: 0 auto !important;
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
}

.berilio-logo-container {
    display: flex !important;
    align-items: center !important;
    gap: 0 !important;
}

.berilio-logo-svg {
    width: 45px !important;
    height: 45px !important;
}

.berilio-logo-text {
    font-size: 1.7rem !important;
    font-weight: 500 !important;
    color: #2D2D2D !important;
    margin-left: 2px !important;
}

.berilio-nav-menu {
    display: flex !important;
    gap: 2rem !important;
    align-items: center !important;
}

.berilio-nav-link {
    color: #666666 !important;
    text-decoration: none !important;
    font-size: 0.95rem !important;
    font-weight: 500 !important;
    transition: color 0.3s !important;
}

.berilio-nav-link:hover {
    color: #2196F3 !important;
}

.berilio-nav-btn {
    background: #2196F3 !important;
    color: white !important;
    padding: 0.5rem 1.25rem !important;
    border-radius: 8px !important;
    text-decoration: none !important;
    font-size: 0.95rem !important;
    font-weight: 500 !important;
    transition: background 0.3s !important;
}

.berilio-nav-btn:hover {
    background: #1565C0 !important;
    color: white !important;
}

/* Hero Section */
.berilio-hero {
    padding: 5rem 2rem !important;
    text-align: center !important;
    background: white !important;
}

.berilio-hero-container {
    max-width: 800px !important;
    margin: 0 auto !important;
}

.berilio-hero h1 {
    font-size: 2.8rem !important;
    font-weight: 700 !important;
    line-height: 1.3 !important;
    margin: 2rem 0 1.5rem 0 !important;
    color: #2D2D2D !important;
    letter-spacing: -0.5px !important;
    font-family: 'JetBrains Mono', monospace !important;
}

.berilio-subtitle {
    font-size: 1.1rem !important;
    color: #666666 !important;
    margin-bottom: 2.5rem !important;
    line-height: 1.7 !important;
    font-weight: 400 !important;
}

.berilio-actions {
    display: flex !important;
    gap: 1rem !important;
    justify-content: center !important;
    flex-wrap: wrap !important;
}

.berilio-btn {
    padding: 0.875rem 2rem !important;
    border: none !important;
    border-radius: 8px !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
    cursor: pointer !important;
    text-decoration: none !important;
    display: inline-block !important;
    transition: all 0.3s ease !important;
    font-family: 'JetBrains Mono', monospace !important;
}

.berilio-btn-primary {
    background: #2196F3 !important;
    color: white !important;
}

.berilio-btn-primary:hover {
    background: #1565C0 !important;
    transform: translateY(-1px) !important;
    color: white !important;
}

.berilio-btn-secondary {
    background: white !important;
    color: #2D2D2D !important;
    border: 1px solid #F0F0F0 !important;
}

.berilio-btn-secondary:hover {
    border-color: #2196F3 !important;
    color: #2196F3 !important;
    background: white !important;
}

/* Features */
.berilio-features {
    padding: 4rem 2rem !important;
    background: #fafafa !important;
}

.berilio-features-container {
    max-width: 1200px !important;
    margin: 0 auto !important;
}

.berilio-features-grid {
    display: grid !important;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)) !important;
    gap: 2rem !important;
    margin-top: 2rem !important;
}

.berilio-feature-card {
    padding: 2.5rem 2rem !important;
    border-radius: 12px !important;
    transition: transform 0.3s ease !important;
}

.berilio-feature-card.beige {
    background: #E3F2FD !important;
}

.berilio-feature-card.mint {
    background: #E1F5FE !important;
}

.berilio-feature-card.lavender {
    background: #E8EAF6 !important;
}

.berilio-feature-card:hover {
    transform: translateY(-2px) !important;
}

.berilio-feature-icon {
    width: 60px !important;
    height: 60px !important;
    margin-bottom: 1.5rem !important;
    display: block !important;
}

.berilio-feature-card h3 {
    font-size: 1.25rem !important;
    font-weight: 600 !important;
    margin-bottom: 1rem !important;
    color: #2D2D2D !important;
    font-family: 'JetBrains Mono', monospace !important;
}

.berilio-feature-card p {
    color: #666666 !important;
    line-height: 1.6 !important;
    font-size: 1rem !important;
    font-family: 'JetBrains Mono', monospace !important;
}

/* Pricing */
.berilio-pricing {
    padding: 4rem 2rem !important;
    background: #E3F2FD !important;
}

.berilio-pricing-container {
    max-width: 1200px !important;
    margin: 0 auto !important;
    text-align: center !important;
}

.berilio-pricing h2 {
    font-size: 2.5rem !important;
    font-weight: 600 !important;
    margin-bottom: 3rem !important;
    color: #2D2D2D !important;
    font-family: 'JetBrains Mono', monospace !important;
}

.berilio-pricing-cards {
    display: grid !important;
    grid-template-columns: repeat(3, 1fr) !important;
    gap: 2rem !important;
    max-width: 1000px !important;
    margin: 2rem auto 0 !important;
}

.berilio-pricing-card {
    background: white !important;
    padding: 2.5rem 2rem !important;
    border-radius: 12px !important;
    position: relative !important;
    border: 2px solid transparent !important;
}

.berilio-pricing-card.featured {
    border-color: #2196F3 !important;
    transform: scale(1.05) !important;
}

.berilio-badge {
    position: absolute !important;
    top: -12px !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    background: #2196F3 !important;
    color: white !important;
    padding: 0.25rem 1rem !important;
    border-radius: 20px !important;
    font-size: 0.75rem !important;
    font-weight: 600 !important;
}

.berilio-pricing-card h3 {
    font-size: 1.5rem !important;
    margin-bottom: 1rem !important;
    color: #2D2D2D !important;
    font-family: 'JetBrains Mono', monospace !important;
}

.berilio-price {
    margin-bottom: 2rem !important;
}

.berilio-amount {
    font-size: 2.5rem !important;
    font-weight: 700 !important;
    color: #2196F3 !important;
    font-family: 'JetBrains Mono', monospace !important;
}

.berilio-period {
    font-size: 1rem !important;
    color: #666666 !important;
}

.berilio-pricing-features {
    list-style: none !important;
    margin: 0 0 2rem 0 !important;
    text-align: left !important;
    padding: 0 !important;
}

.berilio-pricing-features li {
    padding: 0.5rem 0 0.5rem 1.5rem !important;
    color: #666666 !important;
    position: relative !important;
    font-family: 'JetBrains Mono', monospace !important;
}

.berilio-pricing-features li::before {
    content: '✓' !important;
    position: absolute !important;
    left: 0 !important;
    color: #2196F3 !important;
    font-weight: 600 !important;
}

.berilio-btn-outline {
    padding: 0.75rem 2rem !important;
    background: transparent !important;
    color: #2D2D2D !important;
    border: 1px solid #F0F0F0 !important;
    border-radius: 8px !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
    cursor: pointer !important;
    width: 100% !important;
    transition: all 0.3s ease !important;
    font-family: 'JetBrains Mono', monospace !important;
}

.berilio-btn-outline:hover {
    border-color: #2196F3 !important;
    color: #2196F3 !important;
}

.berilio-pricing-card .berilio-btn-primary {
    width: 100% !important;
}

/* CTA */
.berilio-cta {
    padding: 4rem 2rem !important;
    text-align: center !important;
    background: #E8EAF6 !important;
}

.berilio-cta-container {
    max-width: 700px !important;
    margin: 0 auto !important;
}

.berilio-cta h2 {
    font-size: 2rem !important;
    font-weight: 600 !important;
    margin-bottom: 1rem !important;
    color: #2D2D2D !important;
    font-family: 'JetBrains Mono', monospace !important;
}

.berilio-cta p {
    font-size: 1.1rem !important;
    color: #666666 !important;
    margin-bottom: 2rem !important;
    font-family: 'JetBrains Mono', monospace !important;
}

/* Footer */
.berilio-footer {
    background: #10519D !important;
    color: white !important;
    padding: 3rem 2rem 1rem !important;
}

.berilio-footer-container {
    max-width: 1200px !important;
    margin: 0 auto !important;
    display: grid !important;
    grid-template-columns: 2fr 1fr 1fr !important;
    gap: 3rem !important;
    margin-bottom: 2rem !important;
}

.berilio-footer-brand svg {
    width: 80px !important;
    height: 80px !important;
    margin-bottom: 1.5rem !important;
    opacity: 0.9 !important;
}

.berilio-footer-tagline {
    font-size: 1rem !important;
    opacity: 0.8 !important;
    line-height: 1.6 !important;
    color: white !important;
}

.berilio-footer-column h4 {
    margin-bottom: 1rem !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
    color: white !important;
    font-family: 'JetBrains Mono', monospace !important;
}

.berilio-footer-column ul {
    list-style: none !important;
    padding: 0 !important;
    margin: 0 !important;
}

.berilio-footer-column ul li {
    margin-bottom: 0.75rem !important;
}

.berilio-footer-column ul li a {
    color: rgba(255, 255, 255, 0.7) !important;
    text-decoration: none !important;
    font-size: 0.95rem !important;
    transition: color 0.3s !important;
}

.berilio-footer-column ul li a:hover {
    color: white !important;
}

.berilio-footer-bottom {
    border-top: 1px solid rgba(255, 255, 255, 0.1) !important;
    text-align: center !important;
    padding: 2rem 0 0 0 !important;
    margin-top: 2rem !important;
}

.berilio-footer-bottom p {
    font-size: 0.9rem !important;
    opacity: 0.6 !important;
    color: white !important;
}

/* Responsive */
@media (max-width: 768px) {
    .berilio-nav {
        padding: 1rem 1.5rem !important;
    }
    
    .berilio-nav-menu {
        display: none !important;
    }
    
    .berilio-hero h1 {
        font-size: 2rem !important;
    }
    
    .berilio-features-grid {
        grid-template-columns: 1fr !important;
    }
    
    .berilio-pricing-cards {
        grid-template-columns: 1fr !important;
    }
    
    .berilio-pricing-card.featured {
        transform: none !important;
    }
    
    .berilio-footer-container {
        grid-template-columns: 1fr !important;
        text-align: center !important;
    }
}
</style>

<div class="berilio-wrapper">
    <!-- Navigation -->
    <nav class="berilio-nav">
        <div class="berilio-nav-container">
            <div class="berilio-logo-container">
                <svg class="berilio-logo-svg" viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
                    <defs>
                        <filter id="shadowSoft" x="-50%" y="-50%" width="200%" height="200%">
                            <feDropShadow dx="0" dy="2" stdDeviation="4" flood-opacity="0.15"/>
                        </filter>
                    </defs>
                    <g>
                        <rect x="0" y="0" width="80" height="80" fill="#1565C0" filter="url(#shadowSoft)"/>
                        <text x="5" y="22" font-family="Helvetica Neue, Arial, sans-serif" font-size="16" font-weight="300" fill="rgba(255,255,255,0.9)" text-anchor="start">4</text>
                        <text x="40" y="60" font-family="Helvetica Neue, Arial, sans-serif" font-size="44" font-weight="700" fill="white" text-anchor="middle">Be</text>
                    </g>
                </svg>
                <span class="berilio-logo-text">rilio</span>
            </div>
            <div class="berilio-nav-menu">
                <a href="#features" class="berilio-nav-link">Características</a>
                <a href="#pricing" class="berilio-nav-link">Precios</a>
                <a href="#contacto" class="berilio-nav-link">Empresa</a>
                <a href="#contacto" class="berilio-nav-btn">Contactar</a>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="berilio-hero">
        <div class="berilio-hero-container">
            <h1>Un solo sistema para todas tus certificaciones ISO</h1>
            <p class="berilio-subtitle">
                Deja de mantener carpetas separadas para cada norma. Berilio integra ISO 9001, 14001, 45001 y 27001. 
                Menos burocracia, más control real sobre tu operación.
            </p>
            <div class="berilio-actions">
                <a href="#contacto" class="berilio-btn berilio-btn-primary">Solicitar cotización</a>
                <a href="#features" class="berilio-btn berilio-btn-secondary">Ver características</a>
            </div>
        </div>
    </section>

    <!-- Features -->
    <section class="berilio-features" id="features">
        <div class="berilio-features-container">
            <div class="berilio-features-grid">
                <div class="berilio-feature-card beige">
                    <svg class="berilio-feature-icon" viewBox="0 0 24 24" fill="none" stroke="#2D2D2D" stroke-width="2">
                        <circle cx="12" cy="12" r="10"/>
                        <polyline points="16 12 12 8 12 16"/>
                    </svg>
                    <h3>Ahorra 70% del tiempo en auditorías</h3>
                    <p>Un solo documento sirve para múltiples normas. La misma evidencia cumple requisitos de ISO 9001, 14001 y 45001 simultáneamente. Sin duplicar trabajo.</p>
                </div>
                
                <div class="berilio-feature-card mint">
                    <svg class="berilio-feature-icon" viewBox="0 0 24 24" fill="none" stroke="#2D2D2D" stroke-width="2">
                        <rect x="3" y="3" width="18" height="18" rx="2"/>
                        <path d="M9 9h6v6h-6z"/>
                    </svg>
                    <h3>Mantén tu certificación sin estrés</h3>
                    <p>Dashboard en tiempo real del estado de cumplimiento. Alertas antes de que venzan documentos. Todo listo cuando llegue el auditor externo.</p>
                </div>

                <div class="berilio-feature-card lavender">
                    <svg class="berilio-feature-icon" viewBox="0 0 24 24" fill="none" stroke="#2D2D2D" stroke-width="2">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                        <polyline points="14 2 14 8 20 8"/>
                        <line x1="16" y1="13" x2="8" y2="13"/>
                        <line x1="16" y1="17" x2="8" y2="17"/>
                    </svg>
                    <h3>Reduce costos de consultoría externa</h3>
                    <p>El sistema te guía paso a paso en cada requisito ISO. Plantillas pre-aprobadas. No necesitas un consultor para mantener tu sistema de gestión.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Pricing -->
    <section class="berilio-pricing" id="pricing">
        <div class="berilio-pricing-container">
            <h2>Precios transparentes por usuarios</h2>
            <div class="berilio-pricing-cards">
                <div class="berilio-pricing-card">
                    <h3>Starter</h3>
                    <div class="berilio-price">
                        <span class="berilio-amount">$640K</span>
                        <span class="berilio-period">/mes</span>
                    </div>
                    <ul class="berilio-pricing-features">
                        <li>20 usuarios incluidos</li>
                        <li>Todas las normas ISO</li>
                        <li>250 GB almacenamiento</li>
                    </ul>
                    <button class="berilio-btn-outline">Contactar ventas</button>
                </div>
                
                <div class="berilio-pricing-card featured">
                    <div class="berilio-badge">Más popular</div>
                    <h3>Profesional</h3>
                    <div class="berilio-price">
                        <span class="berilio-amount">$1.340K</span>
                        <span class="berilio-period">/mes</span>
                    </div>
                    <ul class="berilio-pricing-features">
                        <li>50 usuarios incluidos</li>
                        <li>Todas las normas ISO</li>
                        <li>500 GB almacenamiento</li>
                    </ul>
                    <button class="berilio-btn berilio-btn-primary">Contactar ventas</button>
                </div>

                <div class="berilio-pricing-card">
                    <h3>Empresarial</h3>
                    <div class="berilio-price">
                        <span class="berilio-amount">$2.340K</span>
                        <span class="berilio-period">/mes</span>
                    </div>
                    <ul class="berilio-pricing-features">
                        <li>100 usuarios incluidos</li>
                        <li>Todas las normas ISO</li>
                        <li>1 TB almacenamiento</li>
                    </ul>
                    <button class="berilio-btn-outline">Contactar ventas</button>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA -->
    <section class="berilio-cta" id="contacto">
        <div class="berilio-cta-container">
            <h2>¿Necesitas más de 100 usuarios?</h2>
            <p>Tenemos planes personalizados para empresas grandes. Cotización según tus necesidades específicas.</p>
            <a href="mailto:contacto@berilio.co" class="berilio-btn berilio-btn-primary">Contactar ventas</a>
        </div>
    </section>

    <!-- Footer -->
    <footer class="berilio-footer">
        <div class="berilio-footer-container">
            <div class="berilio-footer-brand">
                <svg viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
                    <defs>
                        <filter id="shadowSoft2" x="-50%" y="-50%" width="200%" height="200%">
                            <feDropShadow dx="0" dy="2" stdDeviation="4" flood-opacity="0.15"/>
                        </filter>
                    </defs>
                    <g>
                        <rect x="0" y="0" width="80" height="80" fill="#1565C0" filter="url(#shadowSoft2)"/>
                        <text x="5" y="22" font-family="Helvetica Neue, Arial, sans-serif" font-size="16" font-weight="300" fill="rgba(255,255,255,0.9)" text-anchor="start">4</text>
                        <text x="40" y="60" font-family="Helvetica Neue, Arial, sans-serif" font-size="44" font-weight="700" fill="white" text-anchor="middle">Be</text>
                    </g>
                </svg>
                <p class="berilio-footer-tagline">Software de gestión ISO para empresas que van en serio.</p>
            </div>
            <div class="berilio-footer-column">
                <h4>Producto</h4>
                <ul>
                    <li><a href="#">Características</a></li>
                    <li><a href="#">Precios</a></li>
                    <li><a href="#">Documentación</a></li>
                </ul>
            </div>
            <div class="berilio-footer-column">
                <h4>Empresa</h4>
                <ul>
                    <li><a href="#">Sobre nosotros</a></li>
                    <li><a href="#">Blog</a></li>
                    <li><a href="#">Contacto</a></li>
                </ul>
            </div>
        </div>
        <div class="berilio-footer-bottom">
            <p>&copy; 2025 Berilio. Todos los derechos reservados.</p>
        </div>
    </footer>
</div>
"""

# Actualizar la página
def update_homepage():
    pages_url = f"{WP_URL}/wp-json/wp/v2/pages/7"
    
    page_data = {
        "content": html_content,
        "title": "Berilio - Software de gestión ISO",
        "status": "publish"
    }
    
    response = requests.post(pages_url, json=page_data, auth=auth)
    
    if response.status_code == 200:
        print(f"✅ Página actualizada exitosamente")
        print(f"   URL: {WP_URL}")
        return True
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return False

if __name__ == "__main__":
    update_homepage()