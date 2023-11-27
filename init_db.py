import psycopg2
import csv

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

# Création de la table dans la base de données
cur.execute('''
    CREATE TABLE IF NOT EXISTS nfl_stats (
        Year INT,
        Week INT,
        Display_Name VARCHAR(255),
        First_Name VARCHAR(255),
        Nick_Name VARCHAR(255),
        Last_Name VARCHAR(255),
        Team VARCHAR(255),
        Position VARCHAR(255),
        player_Id INT,
        defensive_Assists INT,
        defensive_Interceptions INT,
        defensive_Interceptions_Yards INT,
        defensive_Forced_Fumble INT,
        defensive_Passes_Defensed INT,
        defensive_Sacks INT,
        defensive_Safeties INT,
        defensive_Solo_Tackles INT,
        defensive_Total_Tackles INT,
        defensive_Tackles_For_A_Loss INT,
        touchdowns_Defense INT,
        fumbles_Lost INT,
        fumbles_Total INT,
        kickoff_Returns_Touchdowns INT,
        kickoff_Returns_Yards INT,
        kick_Returns INT,
        kick_Returns_Average_Yards FLOAT,
        kick_Returns_Long INT,
        kick_Returns_Touchdowns INT,
        kick_Returns_Yards INT,
        kicking_Fg_Att INT,
        kicking_Fg_Long INT,
        kicking_Fg_Made INT,
        kicking_Xk_Att INT,
        kicking_Xk_Made INT,
        opponent_Fumble_Recovery INT,
        passing_Attempts INT,
        passing_Completions INT,
        passing_Interceptions INT,
        passing_Touchdowns INT,
        passing_Yards INT,
        punt_Returns INT,
        punt_Returns_Average_Yards FLOAT,
        punt_Returns_Long INT,
        punt_Returns_Touchdowns INT,
        punting_Average_Yards FLOAT,
        punting_Long INT,
        punting_Punts INT,
        punting_Punts_Inside_20 INT,
        receiving_Receptions INT,
        receiving_Target INT,
        receiving_Touchdowns INT,
        receiving_Yards INT,
        rushing_Attempts INT,
        rushing_Average_Yards FLOAT,
        rushing_Touchdowns INT,
        rushing_Yards INT,
        total_Points_Scored INT
    );
''')

with open('/docker-entrypoint-initdb.d/NFLstats.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        cur.execute('''
            INSERT INTO nfl_stats VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            );
        ''', tuple(row))


conn.commit()
cur.close()
conn.close()
