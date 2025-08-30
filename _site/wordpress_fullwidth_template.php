<?php
/**
 * Template Name: Página Completa Sin Tema
 * Template Post Type: page
 * 
 * INSTRUCCIONES:
 * 1. Sube este archivo a: /wp-content/themes/[tu-tema-actual]/
 * 2. En WordPress, edita la página
 * 3. En "Atributos de página" → "Plantilla", selecciona "Página Completa Sin Tema"
 * 4. Actualiza la página
 */
?>
<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
    <meta charset="<?php bloginfo('charset'); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php wp_title(''); ?></title>
    <?php wp_head(); ?>
</head>
<body>
<?php
while (have_posts()) : the_post();
    the_content();
endwhile;
?>
<?php wp_footer(); ?>
</body>
</html>