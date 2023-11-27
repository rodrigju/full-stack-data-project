import psycopg2
import subprocess
import sys

# Attend que la base de données PostgreSQL soit prête
subprocess.run(["/wait-for-it.sh", "db:5432", "--timeout=30", "--strict", "--", "python", "/app/postgre_vis.py"])

# Connexion à la base de données PostgreSQL
conn = psycopg2.connect(
    dbname='mydatabase',
    user='myuser',
    password='mypassword',
    host='db',  # Nom du service Docker Compose pour le service PostgreSQL
    port='5432'
)

# Création d'un curseur
cur = conn.cursor()

# Requête SQL pour récupérer les noms des joueurs de l'équipe PIT en 2017
query = '''
    SELECT Display_Name
    FROM nfl_stats
    WHERE Team = 'PIT' AND Year = 2017;
'''

# Exécution de la requête
cur.execute(query)

# Récupération des résultats
results = cur.fetchall()

# Affichage des noms des joueurs
print("Noms des joueurs de l'équipe PIT en 2017:")
for row in results:
    print(row[0])

# Fermeture du curseur et de la connexion
cur.close()
conn.close()
