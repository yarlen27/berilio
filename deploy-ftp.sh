#!/bin/bash

# Script para compilar Jekyll y subir por FTP a cPanel

echo "🔨 Compilando Jekyll..."
PATH="$HOME/.local/share/gem/ruby/3.3.0/bin:$PATH" bundle exec jekyll build

echo "✅ Compilación completa!"
echo ""

# Configuración FTP
FTP_HOST="berilio.co"  # o ftp.berilio.co si no funciona
FTP_USER="admin@berilio.co"
FTP_PASS="Elhylden.12"
FTP_DIR="/"

if [ -z "$FTP_PASS" ]; then
    echo "⚠️  Por favor, edita este archivo y agrega tu contraseña FTP"
    echo "   Línea 14: FTP_PASS=\"tu_contraseña\""
    exit 1
fi

echo "📤 Subiendo por FTP a $FTP_HOST..."

# Instalar lftp si no está instalado
if ! command -v lftp &> /dev/null; then
    echo "Instalando lftp..."
    sudo apt-get install -y lftp
fi

# Subir archivos
lftp -u "$FTP_USER,$FTP_PASS" "ftp://$FTP_HOST" <<EOF
set ssl:verify-certificate no
set ftp:ssl-allow no
mirror -R --delete --verbose --parallel=5 _site/ $FTP_DIR
quit
EOF

if [ $? -eq 0 ]; then
    echo "✅ Sitio actualizado exitosamente en berilio.co"
else
    echo "❌ Error al subir. Verifica:"
    echo "   - Servidor FTP: $FTP_HOST (prueba también ftp.berilio.co)"
    echo "   - Usuario: $FTP_USER"
    echo "   - Contraseña configurada correctamente"
    echo "   - Puerto 21 abierto"
fi