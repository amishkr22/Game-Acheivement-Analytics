import psycopg2
import pandas as pd

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="gaming_analytics",
    user="postgres",  # Replace with your username
    password="Amish@22",  # Replace with your password
    host="localhost"
)
cur = conn.cursor()

# Load player data
players = pd.read_csv('Data/players.csv')
for _, row in players.iterrows():
    cur.execute("INSERT INTO player_dim (username, region, playtime, join_date) VALUES (%s, %s, %s, %s)",
                (row['username'], row['region'], row['playtime'], row['join_date']))
conn.commit()

# Load game data
games = pd.read_csv('Data/games.csv')
for _, row in games.iterrows():
    cur.execute("INSERT INTO game_dim (title, genre, developer, release_date) VALUES (%s, %s, %s, %s)",
                (row['title'], row['genre'], row['developer'], row['release_date']))
conn.commit()

# Load achievement data
achievements = pd.read_csv('Data/achievements.csv')
for _, row in achievements.iterrows():
    cur.execute("INSERT INTO achievement_dim (name, description, difficulty, reward) VALUES (%s, %s, %s, %s)",
                (row['name'], row['description'], row['difficulty'], row['reward']))
conn.commit()

# Load time data
times = pd.read_csv('Data/time.csv')
for _, row in times.iterrows():
    cur.execute("INSERT INTO time_dim (time_id, timestamp, hour, day, month, year) VALUES (%s, %s, %s, %s, %s, %s)",
                (row['time_id'], row['timestamp'], row['hour'], row['day'], row['month'], row['year']))
conn.commit()

# Load achievement fact data
achievement_facts = pd.read_csv('Data/achievement_facts.csv')
for _, row in achievement_facts.iterrows():
    cur.execute("INSERT INTO achievement_fact (player_id, game_id, achievement_id, time_id, completion_time, score_earned) VALUES (%s, %s, %s, %s, %s, %s)",
                (row['player_id'], row['game_id'], row['achievement_id'], row['time_id'], row['completion_time'], row['score_earned']))
conn.commit()

print("Data loaded into PostgreSQL!")