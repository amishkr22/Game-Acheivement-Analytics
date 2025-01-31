import pandas as pd
from .utils import connect_to_db

def analyze_data(query):
    conn = connect_to_db()
    df = pd.read_sql(query, conn)
    conn.close()
    return df