# Première étape : Utilisez l'image PostgreSQL officielle en tant que base
FROM postgres:latest

# Installez les dépendances PostgreSQL
RUN apt-get update \
    && apt-get install -y libpq-dev

# Définissez les variables d'environnement pour la connexion à la base de données
ENV POSTGRES_DB mydatabase
ENV POSTGRES_USER myuser
ENV POSTGRES_PASSWORD mypassword

# Copiez le script Python et le fichier CSV dans le conteneur
COPY init_db.py /docker-entrypoint-initdb.d/
COPY NFLstats.csv /docker-entrypoint-initdb.d/

# Deuxième étape : Utilisez une deuxième étape pour ajouter Python
FROM python:3.9-slim

# Copiez les fichiers de l'application Flask
COPY app.py /app/app.py
COPY plot.html /app/templates/plot.html
COPY script.py /app/script.py
COPY statsNFL.csv /app/statsNFL.csv
COPY postgre_vis.py /app/postgre_vis.py

# Installez les dépendances pour l'application Flask
RUN pip install pandas matplotlib Flask psycopg2-binary

# Copiez le script wait-for-it.sh dans le conteneur
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Définissez le répertoire de travail
WORKDIR /app

# Commande pour lancer la visualisation après l'attente
CMD ["/wait-for-it.sh", "db:5432", "--", "python", "/app/postgre_vis.py"]
