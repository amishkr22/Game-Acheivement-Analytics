import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="gaming_analytics",
    user="postgres",  # Replace with your username
    password="Amish@22",  # Replace with your password
    host="localhost"
)

# Query top players by total score
query = """
SELECT p.username, SUM(af.score_earned) AS total_score
FROM achievement_fact af
JOIN player_dim p ON af.player_id = p.player_id
GROUP BY p.username
ORDER BY total_score DESC
LIMIT 10;
"""
df = pd.read_sql(query, conn)

# Plot the data
df.plot(kind='bar', x='username', y='total_score', title='Top Players by Total Score')
plt.xlabel('Username')
plt.ylabel('Total Score')
plt.show()

# Close the connection
conn.close()