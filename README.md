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
```

## 🚀 Cómo ejecutar el proyecto

### ✅ Opción 1: Ejecutar **localmente con Docker**

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/etl-airflow-sqlite-streamlit.git
cd etl-airflow-sqlite-streamlit
```

2. Levanta Apache Airflow:
```bash
docker-compose up airflow-init
docker-compose up
```

3. Abre Airflow en http://localhost:8080
   Usuario: airflow | Contraseña: airflow

4. Corre el dashboard de Streamlit:

```bash
pip install -r requirements.txt
streamlit run dashboard/app.py
```

### 💻 Opción 2: Ejecutar en GitHub Codespaces
Este proyecto está preparado con un entorno .devcontainer para ejecutarse directamente en la nube sin necesidad de configuración local.

#### 📦 ¿Qué se instala automáticamente?
* Python 3.10
* Apache Airflow 2.10.5
* Streamlit + pandas + matplotlib
* SQLite
* Carpetas preconfiguradas (/data, /scripts, /dashboard)

#### 🧭 Pasos para usar Codespaces
1. Entra a tu repositorio en GitHub
2. Haz clic en: Code → Open with Codespaces → New codespace
3. Espera que se construya el entorno (~2–3 minutos)
4. En el terminal del Codespace:

### 🔐 Crea el usuario de Airflow:
```bash
airflow users create \
  --username airflow \
  --firstname Air \
  --lastname Flow \
  --role Admin \
  --email airflow@example.com \
  --password airflow
```

### 🚀 Inicia Airflow:
```bash
airflow webserver --port 8080 &
airflow scheduler &
```
5. Abre el puerto 8080 (Airflow UI) desde el menú de puertos de Codespaces
6. En otra terminal, corre el dashboard de Streamlit:
   
```bash
streamlit run dashboard/app.py
```
7. Abre el puerto 8501 para ver el dashboard

📊 ¿Qué muestra el dashboard?
- 📋 Tabla interactiva filtrable por año
- 📈 Gráfico de líneas por mes
- 📊 Gráfico de barras comparativo
- Layout responsive (tabla arriba, gráficos en dos columnas)

## 📄 Licencia
Este proyecto está bajo la licencia MIT.
Puedes usarlo, modificarlo y compartirlo libremente con atribución.

## ✨ Autor
Desarrollado por @darkanita
Con ❤️ para enseñar y aprender ciencia de datos, pipelines y visualización.

