#!/bin/sh

servidor=$(hostname)
destinatario="admin@seguinet.coom"

# Generar reporte de cambios en el sistema de archivos
reporte=$(/usr/sbin/aide --check)

# Enviar reporte por mail
asunto="Reporte diario AIDE para $servidor"
echo "$reporte" | /bin/mail -s "$asunto" $destinatario

# Actualizar la base de datos:
/usr/sbin/aide --init
cp -f /var/lib/aide/aide.db.new.gz /var/lib/aide/aide.db.gz