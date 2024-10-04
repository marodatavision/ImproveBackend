#!/bin/sh

# Warten, bis die Datenbank bereit ist
echo "Warte auf die Datenbank..."

while ! nc -z db 5432; do
  sleep 0.1
done

echo "Datenbank ist bereit!"

# Migrationen ausführen
python manage.py migrate

# DB leeren
python manage.py flush --no-input

# Testdaten laden
python manage.py loaddata initial_data.json

# Statischen Dateien sammeln (optional)
# python manage.py collectstatic --noinput

# Entwicklungsserver starten
exec "$@"
