import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.utils import connect_to_db
from src.data_generator import generate_data
from src.data_loader import load_data

# Load environment variable for data directory
DATA_DIR = os.getenv("DATA_DIR", "Data")

# Title of the app
st.title("🎮 Gaming Achievement Analytics")

# Sidebar for additional options
st.sidebar.header("Options")
query = st.sidebar.text_area("Enter your SQL query here:", height=150)

if st.sidebar.button("Run Query"):
    if query:
        try:
            # Connect to the database
            conn = connect_to_db()

            # Execute the query
            df = pd.read_sql(query, conn)

            # Display the results
            st.write("### Query Results")
            st.write(df)

            # Plot the data
            if not df.empty and df.shape[1] >= 2:
                st.write("### Visualization")
                fig, ax = plt.subplots()
                df.plot(kind='bar', x=df.columns[0], y=df.columns[1], ax=ax)
                ax.set_xlabel(df.columns[0])
                ax.set_ylabel(df.columns[1])
                ax.set_title("Query Results")
                st.pyplot(fig)
            else:
                st.warning("No data available to display.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
        finally:
            conn.close()
    else:
        st.warning("Please enter a SQL query.")

# Data Management Section
st.sidebar.header("Data Management")
if st.sidebar.button("Generate Data"):
    generate_data()
    st.sidebar.success(f"Data generated and saved in {DATA_DIR}!")

if st.sidebar.button("Load Data into Database"):
    load_data()
    st.sidebar.success("Data loaded into PostgreSQL!")

st.sidebar.markdown("---")
st.sidebar.markdown("🚀 **Developed for Data Analytics**")