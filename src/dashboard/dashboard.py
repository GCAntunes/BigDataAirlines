import pandas as pd
import streamlit as st

st.set_page_config(layout='wide')

df_view_cia = pd.read_parquet('output/VIEW_CIA/view_cia.snappy.parquet')

st.dataframe(df_view_cia)


