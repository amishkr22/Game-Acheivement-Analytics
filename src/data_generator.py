import os
from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta
import uuid

# Load environment variables
DATA_DIR = os.getenv("DATA_DIR", "Data")
PLAYERS_FILE = os.getenv("PLAYERS_FILE", "players.csv")
GAMES_FILE = os.getenv("GAMES_FILE", "games.csv")
ACHIEVEMENTS_FILE = os.getenv("ACHIEVEMENTS_FILE", "achievements.csv")
TIME_FILE = os.getenv("TIME_FILE", "time.csv")
ACHIEVEMENT_FACTS_FILE = os.getenv("ACHIEVEMENT_FACTS_FILE", "achievement_facts.csv")

# Ensure directory exists
os.makedirs(DATA_DIR, exist_ok=True)

def generate_data():
    fake = Faker()

    players = [{
        'player_id': i, 
        'username': fake.user_name(), 
        'region': fake.country(), 
        'playtime': random.randint(10, 500), 
        'join_date': fake.date()
    } for i in range(1, 101)]
    pd.DataFrame(players).to_csv(os.path.join(DATA_DIR, PLAYERS_FILE), index=False)

    games = [{
        'game_id': i, 
        'title': fake.catch_phrase(), 
        'genre': random.choice(['Action', 'RPG', 'Strategy', 'Sports']), 
        'developer': fake.company(), 
        'release_date': fake.date()
    } for i in range(1, 11)]
    pd.DataFrame(games).to_csv(os.path.join(DATA_DIR, GAMES_FILE), index=False)

    achievements = [{
        'achievement_id': i, 
        'name': fake.word(), 
        'description': fake.sentence(), 
        'difficulty': random.choice(['Easy', 'Medium', 'Hard']), 
        'reward': random.randint(10, 100)
    } for i in range(1, 51)]
    pd.DataFrame(achievements).to_csv(os.path.join(DATA_DIR, ACHIEVEMENTS_FILE), index=False)

    timestamps = [{
        'time_id': str(uuid.uuid4()), 
        'timestamp': datetime.now() - timedelta(days=random.randint(1, 365)), 
        'hour': random.randint(0, 23), 
        'day': random.randint(1, 31), 
        'month': random.randint(1, 12), 
        'year': random.randint(2020, 2023)
    } for _ in range(1000)]
    pd.DataFrame(timestamps).to_csv(os.path.join(DATA_DIR, TIME_FILE), index=False)

    achievement_facts = [{
        'player_id': random.randint(1, 100), 
        'game_id': random.randint(1, 10), 
        'achievement_id': random.randint(1, 50), 
        'time_id': random.choice(timestamps)['time_id'], 
        'completion_time': random.randint(60, 3600), 
        'score_earned': random.randint(10, 100)
    } for _ in range(1000)]
    pd.DataFrame(achievement_facts).to_csv(os.path.join(DATA_DIR, ACHIEVEMENT_FACTS_FILE), index=False)

    print(f"Data generated and saved in {DATA_DIR}!")