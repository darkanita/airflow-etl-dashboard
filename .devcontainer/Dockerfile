# Base image: Python 3.10
FROM python:3.10

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libsqlite3-dev \
    default-libmysqlclient-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio de trabajo
WORKDIR /workspace

# Copiar requirements.txt
COPY requirements.txt .

# Instalar dependencias Python (Streamlit + Airflow)
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install apache-airflow==2.10.5 \
    --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.5/constraints-3.10.txt"
