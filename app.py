import streamlit as st
import pandas as pd
import supabase
import datetime
from supabase import create_client
import json
import toml
import os

# Configurar el cliente de Supabase
try:
    secrets_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'secrets.toml'))
    secrets = toml.load(secrets_path)
except FileNotFoundError:
    st.error('El archivo secrets.toml no se encontró. Asegúrate de que esté presente en el directorio raíz.')
    st.stop()
SUPABASE_URL = secrets['SUPABASE']['URL']
SUPABASE_KEY = secrets['SUPABASE']['KEY']

supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Cargar el archivo CSV de datos iniciales
@st.cache_data
def cargar_datos():
    return pd.read_csv('mining_data.csv')

def insertar_resultado_prediccion(prediccion_exito):
    data = {
        "fecha": datetime.datetime.now().isoformat(),  # Convertir datetime a una cadena en formato ISO
        "exito_predicho": prediccion_exito
    }
    supabase_client.table("resultados_prediccion").insert(data).execute()

# Definir la interfaz de usuario con Streamlit
st.title("Modelo Predictivo para Proceso Minero")

# Cargar datos y mostrarlos
st.write("Datos iniciales para entrenamiento:")
datos = cargar_datos()
st.dataframe(datos)

# Normalización de los datos
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

columnas_numericas = ['numero_trabajadores', 'produccion_obtenida', 'consumo_energia', 'calidad_mineral']
datos_normalizados = pd.DataFrame(scaler.fit_transform(datos[columnas_numericas]), columns=columnas_numericas)

datos.update(datos_normalizados)

st.write("Datos normalizados:")
st.dataframe(datos)

# Dummy Predictor: vamos a simular una predicción simple
st.subheader("Predicción del proceso")
if st.button("Predecir Exito"):
    exito_predicho = True if datos['calidad_mineral'].mean() > 7 else False
    insertar_resultado_prediccion(exito_predicho)
    st.write(f"Resultado de predicción: {'Exitoso' if exito_predicho else 'No Exitoso'}")
