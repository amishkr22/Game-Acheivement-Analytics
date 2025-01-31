# Gaming Achievement Analytics

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

A web application built with **Streamlit** and **PostgreSQL** to analyze gaming achievements. Users can enter SQL queries, visualize the results, and manage data.

---

## Features

- **Interactive Query Tool**: Enter SQL queries and view results as tables and charts.
- **Data Generation**: Generate fake gaming data and save it to CSV files.
- **Data Loading**: Load CSV data into a PostgreSQL database.
- **Visualizations**: Automatically generate bar charts for query results.

---

## Prerequisites

Before running the project, ensure you have the following installed:

- **Python 3.8+**
- **PostgreSQL**
- **Streamlit**

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/amishkr22/Game-Acheivement-Analytics.git
   cd Game-Acheivement-Analytics
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up PostgreSQL**:
   - Create a database named `gaming_analytics`.
   - Update the connection details in `gaming_analytics/utils.py` if necessary.

4. **Generate and Load Data**:
   - Run the following commands to generate fake data and load it into the database:
     ```bash
     python -m gaming_analytics.generate_data
     python -m gaming_analytics.load_data
     ```

---

## Running the App

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and go to `http://localhost:8501`.

---

## Usage

### Query Tool
- Enter a SQL query in the sidebar (e.g., `SELECT p.username, SUM(af.score_earned) AS total_score FROM achievement_fact af JOIN player_dim p ON af.player_id = p.player_id GROUP BY p.username ORDER BY total_score DESC LIMIT 10;`).
- Click **Run Query** to view the results as a table and a bar chart.

### Data Management
- Use the sidebar to:
  - **Generate Data**: Create fake data and save it to CSV files.
  - **Load Data**: Load CSV data into the PostgreSQL database.

---

## Example Queries

1. **Top Players by Total Score**:
   ```sql
   SELECT p.username, SUM(af.score_earned) AS total_score
   FROM achievement_fact af
   JOIN player_dim p ON af.player_id = p.player_id
   GROUP BY p.username
   ORDER BY total_score DESC
   LIMIT 10;
   ```

2. **Most Difficult Achievements**:
   ```sql
   SELECT a.name, COUNT(*) AS completions
   FROM achievement_fact af
   JOIN achievement_dim a ON af.achievement_id = a.achievement_id
   WHERE a.difficulty = 'Hard'
   GROUP BY a.name
   ORDER BY completions ASC;
   ```

3. **Games with the Most Achievements**:
   ```sql
   SELECT g.title, COUNT(*) AS total_achievements
   FROM achievement_fact af
   JOIN game_dim g ON af.game_id = g.game_id
   GROUP BY g.title
   ORDER BY total_achievements DESC;
   ```

---

## Project Structure

```
gaming_analytics/
│
├── Data/                      # Dataset folder
│   ├── achievement_facts.csv  # Dataset for achievements of player
|   ├── achievements.csv       # Info about achievemetns
|   ├── games.csv              # Data about the game
|   ├── players.csv            # Info about the player
|   ├── time.csv               # Timestamps for the achievements
|    
├── src/                       # Local package
│   ├── __init__.py            # Package initialization
│   ├── analyzer.py            # Generate fake data
│   ├── data_generator.py      # Load data into PostgreSQL
│   ├── data_loader.py         # Query and visualize data
│   └── utils.py               # Utility functions
│
├── app.py                     # Main Streamlit application
├── requirements.txt           # List of dependencies
└── README.md                  # Project documentation
```

---