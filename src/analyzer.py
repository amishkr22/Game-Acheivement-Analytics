import pandas as pd
import matplotlib.pyplot as plt
from .utils import connect_to_db

def analyze_data(query):
    conn = connect_to_db()
    df = pd.read_sql(query, conn)
    conn.close()

    # Plot the data
    df.plot(kind='bar', x=df.columns[0], y=df.columns[1], title='Query Results')
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])
    plt.show()