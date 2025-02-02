import psycopg2
import yaml
import os


def connect_to_db():
    """Connect to the PostgreSQL database."""
    conn = psycopg2.connect(
        dbname="your-db-name", # Replace with your database name
        user="your-username",  # Replace with your username
        password="your-password",  # Replace with your password
        host="localhost"
    )
    return conn

def load_config():
    with open("environment.yml", "r") as file:
        config = yaml.safe_load(file)
    return config.get("config", {})

def get_data_path(filename):
    config = load_config()
    data_dir = config.get("data_dir", "./Data")
    return os.path.join(data_dir, filename)