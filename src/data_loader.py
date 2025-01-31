# gaming_analytics/load_data.py
import pandas as pd
from .utils import connect_to_db

def load_data():
    conn = connect_to_db()
    cur = conn.cursor()

    players = pd.read_csv('Data/players.csv')
    for _, row in players.iterrows():
        cur.execute("INSERT INTO player_dim (username, region, playtime, join_date) VALUES (%s, %s, %s, %s)",
                    (row['username'], row['region'], row['playtime'], row['join_date']))
    conn.commit()

    games = pd.read_csv('Data/games.csv')
    for _, row in games.iterrows():
        cur.execute("INSERT INTO game_dim (title, genre, developer, release_date) VALUES (%s, %s, %s, %s)",
                    (row['title'], row['genre'], row['developer'], row['release_date']))
    conn.commit()

    achievements = pd.read_csv('Data/achievements.csv')
    for _, row in achievements.iterrows():
        cur.execute("INSERT INTO achievement_dim (name, description, difficulty, reward) VALUES (%s, %s, %s, %s)",
                    (row['name'], row['description'], row['difficulty'], row['reward']))
    conn.commit()

    times = pd.read_csv('Data/time.csv')
    for _, row in times.iterrows():
        cur.execute("INSERT INTO time_dim (time_id, timestamp, hour, day, month, year) VALUES (%s, %s, %s, %s, %s, %s)",
                    (row['time_id'], row['timestamp'], row['hour'], row['day'], row['month'], row['year']))
    conn.commit()

    achievement_facts = pd.read_csv('Data/achievement_facts.csv')
    for _, row in achievement_facts.iterrows():
        cur.execute("INSERT INTO achievement_fact (player_id, game_id, achievement_id, time_id, completion_time, score_earned) VALUES (%s, %s, %s, %s, %s, %s)",
                    (row['player_id'], row['game_id'], row['achievement_id'], row['time_id'], row['completion_time'], row['score_earned']))
    conn.commit()

    print("Data loaded into PostgreSQL!")