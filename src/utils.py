# gaming_analytics/utils.py
import psycopg2

def connect_to_db():
    """Connect to the PostgreSQL database."""
    conn = psycopg2.connect(
        dbname="gaming_analytics",
        user="postgres",  # Replace with your username
        password="Amish@22",  # Replace with your password
        host="localhost"
    )
    return conn