#!/bin/bash

# Script para compilar Jekyll y preparar para subir a cPanel

echo "🔨 Compilando Jekyll..."
PATH="$HOME/.local/share/gem/ruby/3.3.0/bin:$PATH" bundle exec jekyll build

echo "✅ Compilación completa!"
echo ""
echo "📁 Archivos listos en _site/"
echo ""

# Configuración FTP
FTP_HOST=""  # Ejemplo: ftp.berilio.co o berilio.co
FTP_USER=""  # Tu usuario de cPanel
FTP_PASS=""  # Tu contraseña de cPanel
FTP_DIR="/public_html"  # Directorio destino

if [ -n "$FTP_HOST" ] && [ -n "$FTP_USER" ] && [ -n "$FTP_PASS" ]; then
    echo "📤 Subiendo por FTP a $FTP_HOST..."
    
    # Instalar lftp si no está instalado
    if ! command -v lftp &> /dev/null; then
        echo "Instalando lftp..."
        sudo apt-get install -y lftp
    fi
    
    # Subir archivos
    lftp -u "$FTP_USER,$FTP_PASS" "ftp://$FTP_HOST" <<EOF
set ssl:verify-certificate no
mirror -R --delete --verbose _site/ $FTP_DIR
quit
EOF
    
    echo "✅ Sitio actualizado en berilio.co"
else
    echo "⚠️  Configura las credenciales FTP en este archivo:"
    echo "   FTP_HOST: Servidor FTP (ej: ftp.berilio.co)"
    echo "   FTP_USER: Tu usuario de cPanel"
    echo "   FTP_PASS: Tu contraseña de cPanel"
    echo ""
    echo "Para subir manualmente:"
    echo "1. Abre el File Manager de cPanel"
    echo "2. Navega a public_html"
    echo "3. Sube todo el contenido de _site/"
fi