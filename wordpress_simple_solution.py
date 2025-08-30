#!/usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuth

WP_URL = "https://berilio.co"
WP_USER = "admin"
WP_PASS = "AjAP i1M9 lhLv wWCj 68NN PmCB"

auth = HTTPBasicAuth(WP_USER, WP_PASS)

# Leer nuestro HTML y CSS originales
with open('index.html', 'r') as f:
    html = f.read()

with open('styles.css', 'r') as f:
    css = f.read()

# Leer el logo SVG
with open('berilio-logo.svg', 'r') as f:
    logo_svg = f.read()

# Reemplazar referencias locales con contenido inline
html = html.replace('<link rel="stylesheet" href="styles.css">', f'<style>{css}</style>')
html = html.replace('src="berilio-logo.svg"', f'src="data:image/svg+xml,{logo_svg.replace("#", "%23").replace('"', "'")}"')
html = html.replace('href="features.html"', 'href="#features"')
html = html.replace('<script src="script.js"></script>', '')

# Agregar CSS para ocultar COMPLETAMENTE el tema de WordPress
wordpress_override = """
<style>
/* Ocultar TODO el tema de WordPress */
body > *:not(.berilio-wrapper) {
    display: none !important;
}

body {
    margin: 0 !important;
    padding: 0 !important;
}

.berilio-wrapper {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    width: 100vw !important;
    height: 100vh !important;
    overflow-y: auto !important;
    background: white !important;
}
</style>

<div class="berilio-wrapper">
""" + html.replace('<body>', '').replace('</body>', '') + """
</div>
"""

# Actualizar la página
pages_url = f"{WP_URL}/wp-json/wp/v2/pages/7"

page_data = {
    "content": wordpress_override,
    "title": "",  # Sin título para que no aparezca
    "status": "publish"
}

response = requests.post(pages_url, json=page_data, auth=auth)

if response.status_code == 200:
    print("✅ Página actualizada correctamente")
    print("   Debería verse exactamente como el index.html original")
else:
    print(f"Error: {response.status_code}")
    print(response.text)