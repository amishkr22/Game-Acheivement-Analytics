import os
import psycopg2

def connect_to_db():
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME", "your-db-name"),
        user=os.getenv("DB_USER", "your-username"),
        password=os.getenv("DB_PASS", "your-password"),
        host=os.getenv("DB_HOST", "localhost"),
    )
    return conn