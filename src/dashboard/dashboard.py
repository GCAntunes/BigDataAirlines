import pandas as pd
import streamlit as st

st.set_page_config(layout='wide')

df_air_cia = pd.read_parquet('output/AIR_CIA/air_cia_202310.snappy.parquet')
df_aerodromos = pd.read_parquet(
    'output/AERODROMOS/aerodromos_202310.snappy.parquet'
)
df_vra = pd.read_parquet('output/VRA/vra_202310.snappy.parquet')

st.dataframe(df_air_cia)
st.dataframe(df_aerodromos)
# st.dataframe(df_vra)
