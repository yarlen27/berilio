#!/usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuth
import json

# Configuración
WP_URL = "https://berilio.co"
WP_USER = "admin"
WP_PASS = "AjAP i1M9 lhLv wWCj 68NN PmCB"

auth = HTTPBasicAuth(WP_USER, WP_PASS)

# HTML que debería funcionar mejor con cualquier tema
html_content = """
<!-- wp:html -->
<script>
// Ocultar elementos del tema cuando cargue la página
document.addEventListener('DOMContentLoaded', function() {
    // Ocultar header del tema
    var header = document.querySelector('header, .site-header, .header, #header, #masthead');
    if(header) header.style.display = 'none';
    
    // Ocultar footer del tema
    var footer = document.querySelector('footer, .site-footer, .footer, #footer, #colophon');
    if(footer) footer.style.display = 'none';
    
    // Ocultar sidebar
    var sidebar = document.querySelector('.sidebar, aside, #sidebar');
    if(sidebar) sidebar.style.display = 'none';
    
    // Ocultar título de página
    var title = document.querySelector('.entry-title, .page-title, h1.title');
    if(title) title.style.display = 'none';
    
    // Expandir contenido
    var content = document.querySelector('.entry-content, .content, .site-content, #content');
    if(content) {
        content.style.maxWidth = '100%';
        content.style.padding = '0';
        content.style.margin = '0';
    }
    
    // Expandir contenedor principal
    var container = document.querySelector('.container, .wrapper, .site');
    if(container) {
        container.style.maxWidth = '100%';
        container.style.padding = '0';
        container.style.margin = '0';
    }
});
</script>

<style>
/* Ocultar elementos del tema */
body.page-id-7 header,
body.page-id-7 .site-header,
body.page-id-7 #masthead,
body.page-id-7 footer,
body.page-id-7 .site-footer,
body.page-id-7 #colophon,
body.page-id-7 .entry-header,
body.page-id-7 .page-header,
body.page-id-7 aside,
body.page-id-7 .sidebar,
body.page-id-7 .navigation,
body.page-id-7 .nav-links,
body.page-id-7 .entry-meta {
    display: none !important;
}

/* Expandir contenido */
body.page-id-7 .site-content,
body.page-id-7 .content-area,
body.page-id-7 .entry-content,
body.page-id-7 #content,
body.page-id-7 .container,
body.page-id-7 .wrapper {
    max-width: 100% !important;
    width: 100% !important;
    padding: 0 !important;
    margin: 0 !important;
}

body.page-id-7 {
    margin: 0 !important;
    padding: 0 !important;
}

/* Reset WordPress defaults */
body.page-id-7 .entry-content > * {
    max-width: none !important;
}
</style>
<!-- /wp:html -->

<!-- wp:group {"layout":{"type":"constrained","contentSize":"100%"}} -->
<div class="wp-block-group">
<!-- wp:html -->
<iframe src="https://yarlen27.github.io/berilio/" 
        style="width: 100vw; height: 100vh; border: none; margin: 0; padding: 0; position: fixed; top: 0; left: 0; z-index: 999999;"
        frameborder="0">
</iframe>
<!-- /wp:html -->
</div>
<!-- /wp:group -->
"""

# Opción alternativa: Usar el HTML directo hospedado en GitHub
html_github = """
<!-- wp:html -->
<script>
window.location.href = 'https://yarlen27.github.io/berilio/';
</script>
<p>Redirigiendo a Berilio...</p>
<!-- /wp:html -->
"""

def update_page_gutenberg():
    """Actualizar usando bloques de Gutenberg"""
    pages_url = f"{WP_URL}/wp-json/wp/v2/pages/7"
    
    page_data = {
        "content": html_content,
        "title": "Berilio - Software de gestión ISO",
        "status": "publish"
    }
    
    response = requests.post(pages_url, json=page_data, auth=auth)
    
    if response.status_code == 200:
        print(f"✅ Página actualizada con iframe")
        print(f"   La página ahora muestra el sitio desde GitHub Pages")
        return True
    else:
        print(f"Error: {response.status_code}")
        return False

def create_redirect_page():
    """Crear página que redirija a GitHub Pages"""
    pages_url = f"{WP_URL}/wp-json/wp/v2/pages"
    
    page_data = {
        "title": "Berilio Redirect",
        "content": html_github,
        "status": "publish",
        "slug": "berilio-redirect"
    }
    
    response = requests.post(pages_url, json=page_data, auth=auth)
    
    if response.status_code == 201:
        page_id = response.json()['id']
        print(f"✅ Página de redirección creada")
        print(f"   ID: {page_id}")
        print(f"   URL: {WP_URL}/?page_id={page_id}")
        return page_id
    else:
        print(f"Error: {response.status_code}")
        return None

if __name__ == "__main__":
    print("Actualizando página con iframe...")
    update_page_gutenberg()
    
    print("\n" + "="*50)
    print("ALTERNATIVA: Subir el sitio a GitHub Pages")
    print("="*50)
    print("1. Haz commit y push de tu proyecto a GitHub")
    print("2. Ve a Settings → Pages en tu repositorio")
    print("3. Activa GitHub Pages desde la rama 'master'")
    print("4. Tu sitio estará en: https://[tu-usuario].github.io/berilio/")
    print("\nUna vez hecho esto, la página de WordPress mostrará")
    print("tu sitio real mediante un iframe.")