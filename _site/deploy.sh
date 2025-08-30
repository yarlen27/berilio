#!/bin/bash

# Script para compilar Jekyll y preparar para subir a cPanel

echo "🔨 Compilando Jekyll..."
PATH="$HOME/.local/share/gem/ruby/3.3.0/bin:$PATH" bundle exec jekyll build

echo "✅ Compilación completa!"
echo ""
echo "📁 Archivos listos en _site/"
echo ""
echo "Para subir a cPanel:"
echo "1. Abre el File Manager de cPanel"
echo "2. Navega a public_html"
echo "3. Sube todo el contenido de _site/"
echo ""
echo "O usa FTP:"
echo "ftp tu-servidor.com"
echo "cd public_html"
echo "mput _site/*"

# Opcional: Si tienes configurado FTP, descomenta estas líneas:
# echo "📤 Subiendo por FTP..."
# lftp -u usuario,password ftp://tu-servidor.com -e "mirror -R _site/ /public_html; quit"