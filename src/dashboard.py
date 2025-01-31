import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import psycopg2

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

# Create a bar chart
fig = px.bar(df, x='username', y='total_score', title='Top Players by Total Score')

# Create the Dash app
app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children='Gaming Achievement Dashboard'),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)