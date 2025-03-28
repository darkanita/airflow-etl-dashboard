import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# Configuración de la página
st.set_page_config(page_title="Air Travel Dashboard", layout="wide")
st.title("📊 Air Travel Dashboard")

# Cargar datos desde SQLite
conn = sqlite3.connect('data/airtravel.db')
df = pd.read_sql("SELECT * FROM airtravel_data", conn)
conn.close()

# Tabla filtrable
st.subheader("📋 Datos de vuelos (tabla)")
year = st.selectbox("Selecciona el año", sorted(df["Year"].unique()))
filtered = df[df["Year"] == year]
st.dataframe(filtered, use_container_width=True)

# Crear una fila con 2 columnas
col1, col2 = st.columns(2)

# Gráfico de línea en la primera columna
with col1:
    st.subheader("📈 Pasajeros por mes (línea)")
    fig, ax = plt.subplots()
    ax.plot(filtered["Month"], filtered["Passengers"], marker='o')
    plt.xticks(rotation=45)
    st.pyplot(fig, use_container_width=True)

# Gráfico de barras en la segunda columna
with col2:
    st.subheader("📊 Pasajeros por mes (barras)")
    fig2, ax2 = plt.subplots()
    ax2.bar(filtered["Month"], filtered["Passengers"], color='orange')
    plt.xticks(rotation=45)
    st.pyplot(fig2, use_container_width=True)
