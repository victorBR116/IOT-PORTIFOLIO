import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import time

engine = create_engine('postgresql://postgres:1234@db:5432/postgres')

def load_data(view_name):
    last_error = None
    for i in range(10):
        try:
            return pd.read_sql(f"SELECT * FROM {view_name}", engine)
        except Exception as e:
            last_error = e
            st.warning(f"Tentativa {i+1}/10 - Esperando view '{view_name}' estar pronta...")
            time.sleep(2)
    st.error(f"Erro ao carregar view '{view_name}': {last_error}")
    return pd.DataFrame()


st.title('Dashboard de Temperaturas IoT')

st.header('Média de Temperatura por Dispositivo')
df_avg_temp = load_data('avg_temp_por_dispositivo')
if not df_avg_temp.empty:
    fig1 = px.bar(df_avg_temp, x='device_id', y='avg_temp')
    st.plotly_chart(fig1)

st.header('Leituras por Hora do Dia')
df_leituras_hora = load_data('leituras_por_hora')
if not df_leituras_hora.empty:
    fig2 = px.line(df_leituras_hora, x='hora', y='contagem')
    st.plotly_chart(fig2)

st.header('Temperaturas Máximas e Mínimas por Dia')
df_temp_max_min = load_data('temp_max_min_por_dia')
if not df_temp_max_min.empty:
    fig3 = px.line(df_temp_max_min, x='data', y=['temp_max', 'temp_min'])
    st.plotly_chart(fig3)
