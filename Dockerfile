# backend/Dockerfile
FROM python:3.11-slim

# apt-get install -y netcat-openbsd &&
RUN apt-get update && apt-get install -y gunicorn && rm -rf /var/lib/apt/lists/* 

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY backend/. /app/

# Entrypoint-Skript hinzufügen
#COPY entrypoint.sh /entrypoint.sh
#RUN dos2unix /entrypoint.sh
#RUN chmod +x /entrypoint.sh
RUN python manage.py collectstatic

# Port freigeben (optional)
EXPOSE 8080

# Entrypoint festlegen
#ENTRYPOINT ["sh", "/entrypoint.sh"]

# Standardbefehl zum Starten des Servers
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "backend.wsgi"]
