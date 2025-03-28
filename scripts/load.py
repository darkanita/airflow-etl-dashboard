import sqlite3
import pandas as pd
import os

def load_data():
    db_path = '/opt/airflow/dags/data/airtravel.db'
    conn = sqlite3.connect(db_path)

    df = pd.read_csv('/opt/airflow/dags/data/airtravel_transformed.csv')
    df.to_sql('airtravel_data', conn, if_exists='replace', index=False)
    conn.close()
    print("✅ Datos cargados en SQLite.")
