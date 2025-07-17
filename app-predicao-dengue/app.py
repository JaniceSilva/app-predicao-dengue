import streamlit as st
from supabase_config import supabase
import pandas as pd
import joblib
import tensorflow as tf
from datetime import datetime

st.set_page_config(page_title="Predição de Arboviroses", layout="wide")
st.title("🦟 Predição de Casos de Dengue por Município")

municipio = st.selectbox("Escolha o município:", ["rio-de-janeiro", "campinas", "salvador"])
dados = supabase.table("casos_diarios").select("*").eq("municipio", municipio).order("data").execute().data
df = pd.DataFrame(dados)

if df.empty:
    st.warning("Nenhum dado disponível para este município.")
else:
    df['data'] = pd.to_datetime(df['data'])
    st.line_chart(df.set_index('data')['casos'], use_container_width=True)

    modelo = tf.keras.models.load_model("model/modelo_lstm.h5")
    st.success("✅ Modelo carregado e pronto para prever (simulado)")