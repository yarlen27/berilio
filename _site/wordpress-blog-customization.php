<?php
/**
 * PERSONALIZACIÓN PARA EL BLOG DE BERILIO
 * 
 * INSTRUCCIONES:
 * 1. En WordPress Admin del blog, ve a: Apariencia > Editor de temas > functions.php
 * 2. Agrega este código al final del archivo
 * 
 * O alternativamente:
 * 1. Instala el plugin "Code Snippets"
 * 2. Crea un nuevo snippet con este código
 */

// Agregar link "Volver al sitio principal" en el menú
add_filter('wp_nav_menu_items', 'add_berilio_home_link', 10, 2);
function add_berilio_home_link($items, $args) {
    if ($args->theme_location == 'primary' || $args->theme_location == 'menu-1') {
        $home_link = '<li class="menu-item berilio-home-link"><a href="https://berilio.co">← Sitio Principal</a></li>';
        $items = $home_link . $items;
    }
    return $items;
}

// Agregar estilos personalizados para mantener coherencia con el sitio principal
add_action('wp_head', 'berilio_blog_styles');
function berilio_blog_styles() {
    ?>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700;800&display=swap');
        
        /* Variables de Berilio */
        :root {
            --berilio-primary: #2196F3;
            --berilio-primary-dark: #1565C0;
            --berilio-primary-darker: #10519D;
            --berilio-text-primary: #2D2D2D;
            --berilio-text-secondary: #666666;
        }
        
        /* Aplicar fuente de Berilio */
        body {
            font-family: 'JetBrains Mono', monospace !important;
        }
        
        h1, h2, h3, h4, h5, h6 {
            font-family: 'JetBrains Mono', monospace !important;
            color: var(--berilio-text-primary) !important;
        }
        
        /* Estilizar link de regreso */
        .berilio-home-link a {
            background: var(--berilio-primary) !important;
            color: white !important;
            padding: 8px 16px !important;
            border-radius: 8px !important;
            text-decoration: none !important;
            font-weight: 500 !important;
            transition: background 0.3s !important;
        }
        
        .berilio-home-link a:hover {
            background: var(--berilio-primary-dark) !important;
        }
        
        /* Links con color de Berilio */
        a {
            color: var(--berilio-primary);
        }
        
        a:hover {
            color: var(--berilio-primary-dark);
        }
        
        /* Botones con estilo Berilio */
        .button, .wp-block-button__link, input[type="submit"] {
            background: var(--berilio-primary) !important;
            border-radius: 8px !important;
            font-family: 'JetBrains Mono', monospace !important;
            font-weight: 500 !important;
            transition: all 0.3s !important;
        }
        
        .button:hover, .wp-block-button__link:hover, input[type="submit"]:hover {
            background: var(--berilio-primary-dark) !important;
            transform: translateY(-1px);
        }
    </style>
    <?php
}

// Agregar barra superior con navegación al sitio principal
add_action('wp_body_open', 'berilio_top_bar');
function berilio_top_bar() {
    ?>
    <div style="background: #10519D; color: white; padding: 10px 0; text-align: center; font-family: 'JetBrains Mono', monospace;">
        <div style="max-width: 1200px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; padding: 0 20px;">
            <div>
                <a href="https://berilio.co" style="color: white; text-decoration: none; font-weight: 600;">
                    ← Berilio.co
                </a>
            </div>
            <div style="font-size: 14px;">
                Blog oficial de Berilio - Software de gestión ISO
            </div>
            <div>
                <a href="https://berilio.co#contacto" style="color: white; text-decoration: none; background: rgba(255,255,255,0.2); padding: 5px 15px; border-radius: 5px;">
                    Contactar
                </a>
            </div>
        </div>
    </div>
    <?php
}

// Cambiar el título del sitio para el blog
add_filter('bloginfo', 'berilio_blog_title', 10, 2);
function berilio_blog_title($output, $show) {
    if ($show == 'name') {
        return 'Blog Berilio';
    }
    if ($show == 'description') {
        return 'Insights sobre gestión ISO y cumplimiento normativo';
    }
    return $output;
}
?>