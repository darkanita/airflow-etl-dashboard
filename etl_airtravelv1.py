from airflow import DAG
from airflow.operators.python_operator import PythonOperator  # cambio clave en 1.10
from datetime import datetime
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),   # en 1.10 va dentro de default_args
    'depends_on_past': False,
}

dag = DAG(
    dag_id='etl_airtravel',
    default_args=default_args,
    schedule_interval='@daily',            # schedule_interval, no schedule
    catchup=False,
    # tags no es soportado en 1.10, se elimina
)

extract = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    provide_context=False,                 # argumento requerido explícitamente en 1.10
    dag=dag,                               # referencia explícita al DAG
)

transform = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    provide_context=False,
    dag=dag,
)

load = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    provide_context=False,
    dag=dag,
)

extract >> transform >> load
