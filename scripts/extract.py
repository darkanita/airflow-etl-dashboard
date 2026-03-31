import pandas as pd
import os

def extract_data():
    url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
    df = pd.read_csv(url)
    
    os.makedirs('/usr/local/airflow/dags/data', exist_ok=True)
    df.to_csv('/usr/local/airflow/dags/data/airtravel_raw.csv', index=False)
    print("✅ CSV descargado y guardado.")
