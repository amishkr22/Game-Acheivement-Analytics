import pandas as pd
from .utils import connect_to_db

def analyze_top_players():
    """Returns the top 10 players based on total score earned."""
    query = """
    SELECT p.username, SUM(af.score_earned) AS total_score
    FROM achievement_fact af
    JOIN player_dim p ON af.player_id = p.player_id
    GROUP BY p.username
    ORDER BY total_score DESC
    LIMIT 10;
    """
    conn = connect_to_db()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def analyze_most_difficult_achievements():
    """Finds the hardest achievements with the least completions."""
    query = """
    SELECT a.name, COUNT(*) AS completions
    FROM achievement_fact af
    JOIN achievement_dim a ON af.achievement_id = a.achievement_id
    WHERE a.difficulty = 'Hard'
    GROUP BY a.name
    ORDER BY completions ASC;
    """
    conn = connect_to_db()
    df = pd.read_sql(query, conn)
    conn.close()
    return df