# Gaming Achievement Analytics

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

A web application built with **Streamlit** and **PostgreSQL** to analyze gaming achievements. Users can enter SQL queries, visualize the results, and manage data.

---
## Project Description

The **Gaming Achievement Analytics** project is a data-driven web application designed to help game developers, analysts, and enthusiasts explore and analyze gaming achievement data. The application allows users to interact with a PostgreSQL database, execute SQL queries, and visualize the results in real-time.

## Features

- **Interactive Query Tool**: Enter SQL queries and view results as tables and charts.
- **Data Generation**: Generate fake gaming data and save it to CSV files.
- **Data Loading**: Load CSV data into a PostgreSQL database.
- **Visualizations**: Automatically generate bar charts for query results.

---

## Approach

The project follows a **data pipeline approach** to generate, load, and analyze gaming achievement data. Here’s an overview of the steps:

1. **Data Generation**:
   - Synthetic data is generated using the **Faker** library in Python.
   - The data includes:
     - **Players**: Usernames, regions, playtime, and join dates.
     - **Games**: Titles, genres, developers, and release dates.
     - **Achievements**: Names, descriptions, difficulty levels, and rewards.
     - **Achievement Facts**: Records of players completing achievements, including timestamps and scores.

2. **Data Loading**:
   - The generated data is saved to CSV files.
   - A Python script loads the CSV data into a **PostgreSQL** database using the `psycopg2` library.

3. **Data Analysis**:
   - Users can enter SQL queries to analyze the data.
   - The application executes the queries and displays the results in a table.
   - A bar chart is automatically generated for queries with numeric results.

4. **Web Interface**:
   - The **Streamlit** framework is used to create a user-friendly web interface.
   - Users can interact with the application through a sidebar and main display area.

---

## Star Schema Design

The database is designed using a **star schema**, a common data warehouse design pattern. The star schema consists of a central **fact table** surrounded by **dimension tables**. Here’s how the tables are structured:

### Fact Table
- **`achievement_fact`**:
  - Contains records of players completing achievements.
  - **Columns**:
    - `achievement_fact_id` (Primary Key): Unique identifier for each record.
    - `player_id` (Foreign Key): References `player_dim`.
    - `game_id` (Foreign Key): References `game_dim`.
    - `achievement_id` (Foreign Key): References `achievement_dim`.
    - `time_id` (Foreign Key): References `time_dim`.
    - `completion_time`: Time taken to complete the achievement (in seconds).
    - `score_earned`: Points earned for completing the achievement.

### Dimension Tables
1. **`player_dim`**:
   - Contains details about players.
   - **Columns**:
     - `player_id` (Primary Key): Unique identifier for each player.
     - `username`: Player's username.
     - `region`: Player's region or country.
     - `playtime`: Total hours played by the player.
     - `join_date`: Date the player joined the platform.

2. **`game_dim`**:
   - Contains details about games.
   - **Columns**:
     - `game_id` (Primary Key): Unique identifier for each game.
     - `title`: Title of the game.
     - `genre`: Genre of the game (e.g., Action, RPG, Strategy).
     - `developer`: Developer of the game.
     - `release_date`: Release date of the game.

3. **`achievement_dim`**:
   - Contains details about achievements.
   - **Columns**:
     - `achievement_id` (Primary Key): Unique identifier for each achievement.
     - `name`: Name of the achievement.
     - `description`: Description of the achievement.
     - `difficulty`: Difficulty level (e.g., Easy, Medium, Hard).
     - `reward`: Points or rewards for completing the achievement.

4. **`time_dim`**:
   - Contains timestamps for achievement completions.
   - **Columns**:
     - `time_id` (Primary Key): Unique identifier for each timestamp.
     - `timestamp`: Timestamp of the achievement completion.
     - `hour`: Hour of the day.
     - `day`: Day of the month.
     - `month`: Month of the year.
     - `year`: Year.

---

## Datasets

The project uses the following datasets, which are generated synthetically:

### 1. **Players (`player_dim`)**
   - Contains details about players.
   - **Columns**:
     - `player_id` (Primary Key): Unique identifier for each player.
     - `username`: Player's username.
     - `region`: Player's region or country.
     - `playtime`: Total hours played by the player.
     - `join_date`: Date the player joined the platform.

### 2. **Games (`game_dim`)**
   - Contains details about games.
   - **Columns**:
     - `game_id` (Primary Key): Unique identifier for each game.
     - `title`: Title of the game.
     - `genre`: Genre of the game (e.g., Action, RPG, Strategy).
     - `developer`: Developer of the game.
     - `release_date`: Release date of the game.

### 3. **Achievements (`achievement_dim`)**
   - Contains details about achievements.
   - **Columns**:
     - `achievement_id` (Primary Key): Unique identifier for each achievement.
     - `name`: Name of the achievement.
     - `description`: Description of the achievement.
     - `difficulty`: Difficulty level (e.g., Easy, Medium, Hard).
     - `reward`: Points or rewards for completing the achievement.

### 4. **Time (`time_dim`)**
   - Contains timestamps for achievement completions.
   - **Columns**:
     - `time_id` (Primary Key): Unique identifier for each timestamp.
     - `timestamp`: Timestamp of the achievement completion.
     - `hour`: Hour of the day.
     - `day`: Day of the month.
     - `month`: Month of the year.
     - `year`: Year.

### 5. **Achievement Facts (`achievement_fact`)**
   - Contains records of players completing achievements.
   - **Columns**:
     - `achievement_fact_id` (Primary Key): Unique identifier for each record.
     - `player_id` (Foreign Key): References `player_dim`.
     - `game_id` (Foreign Key): References `game_dim`.
     - `achievement_id` (Foreign Key): References `achievement_dim`.
     - `time_id` (Foreign Key): References `time_dim`.
     - `completion_time`: Time taken to complete the achievement (in seconds).
     - `score_earned`: Points earned for completing the achievement.

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
   - Update the connection details in `src/utils.py` if necessary.

4. **Generate and Load Data**:
   - Run the following commands to generate fake data and load it into the database:
     ```bash
     python -m src.generate_data
     python -m src.load_data
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