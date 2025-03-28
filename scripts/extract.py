import pandas as pd
import os

def extract_data():
    url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
    df = pd.read_csv(url)
    
    os.makedirs('/opt/airflow/dags/data', exist_ok=True)
    df.to_csv('/opt/airflow/dags/data/airtravel_raw.csv', index=False)
    print("✅ CSV descargado y guardado.")
