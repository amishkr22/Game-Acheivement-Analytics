# gaming_analytics/utils.py
import psycopg2

def connect_to_db():
    """Connect to the PostgreSQL database."""
    conn = psycopg2.connect(
        dbname="your-db-name", # Replace with your database name
        user="your-username",  # Replace with your username
        password="your-password",  # Replace with your password
        host="localhost"
    )
    return conn