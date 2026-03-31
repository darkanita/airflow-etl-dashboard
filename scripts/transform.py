import pandas as pd

def transform_data():
    df = pd.read_csv('/usr/local/airflow/dags/data/airtravel_raw.csv')
    df_long = df.melt(id_vars=["Month"], var_name="Year", value_name="Passengers")
    df_long.to_csv('/usr/local/airflow/dags/data/airtravel_transformed.csv', index=False)
    print("✅ Datos transformados y guardados.")
