from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta
import uuid

def generate_data():
    fake = Faker()

    players = [{
        'player_id': i, 
        'username': fake.user_name(), 
        'region': fake.country(), 
        'playtime': random.randint(10, 500), 
        'join_date': fake.date()
        }for i in range(1, 101)]
    pd.DataFrame(players).to_csv('Data/players.csv', index=False)

    games = [{
        'game_id': i, 
        'title': fake.catch_phrase(), 
        'genre': random.choice(['Action', 'RPG', 'Strategy', 'Sports']), 
        'developer': fake.company(), 
        'release_date': fake.date()
        } for i in range(1, 11)]
    pd.DataFrame(games).to_csv('Data/games.csv', index=False)

    achievements = [{
        'achievement_id': i, 
        'name': fake.word(), 
        'description': fake.sentence(), 
        'difficulty': random.choice(['Easy', 'Medium', 'Hard']), 
        'reward': random.randint(10, 100)
        } for i in range(1, 51)]
    pd.DataFrame(achievements).to_csv('Data/achievements.csv', index=False)

    timestamps = [{
        'time_id': str(uuid.uuid4()), 
        'timestamp': datetime.now() - timedelta(days=random.randint(1, 365)), 
        'hour': random.randint(0, 23), 
        'day': random.randint(1, 31), 
        'month': random.randint(1, 12), 
        'year': random.randint(2020, 2023)
        } for _ in range(1000)]
    pd.DataFrame(timestamps).to_csv('Data/time.csv', index=False)

    achievement_facts = [{
        'player_id': random.randint(1, 100), 
        'game_id': random.randint(1, 10), 
        'achievement_id': random.randint(1, 50), 
        'time_id': random.choice(timestamps)['time_id'], 
        'completion_time': random.randint(60, 3600), 
        'score_earned': random.randint(10, 100)
        } for _ in range(1000)]
    pd.DataFrame(achievement_facts).to_csv('Data/achievement_facts.csv', index=False)

    print("Data generated and saved to CSV files!")