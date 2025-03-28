# ✈️ ETL con Apache Airflow, SQLite y Streamlit

Proyecto educativo para aprender a construir pipelines ETL usando Apache Airflow, almacenar datos en SQLite y visualizarlos en un dashboard interactivo con Streamlit.

---

## 🧠 ¿Qué hace este proyecto?

✅ Extrae un CSV público con datos de vuelos  
✅ Transforma los datos usando `pandas` (formato largo)  
✅ Carga los datos en una base de datos SQLite  
✅ Visualiza la información con Streamlit (gráficos y tabla interactiva)  

---

## 🛠️ Tecnologías usadas

- [Apache Airflow 2.10.5](https://airflow.apache.org/)
- Python 3.10
- Pandas
- SQLite
- Streamlit
- Docker + Docker Compose

---

## 🗂️ Estructura del proyecto

```plaintext
airflow-etl-sqlite-streamlit/
├── dags/                  # DAG principal de Airflow
│   └── etl_airtravel.py
├── scripts/               # Scripts de ETL
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── dashboard/             # App de Streamlit
│   └── app.py
├── data/                  # CSVs y base de datos SQLite generada
├── docker-compose.yaml
├── requirements.txt       # Dependencias para Streamlit
└── README.md
