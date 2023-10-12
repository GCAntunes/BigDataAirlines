import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from dashboard_utils import plota_rotas, plota_aeroportos

st.set_page_config(layout='wide')
st.title('Dashboard BigDataAirlines')


df_view_cia = pd.read_parquet('output/VIEW_CIA/view_cia.snappy.parquet')
comp_aerea_1 = st.multiselect(label='Filtre por companhia aérea', options=df_view_cia['razao_social'], default=None)
df_view_cia_filt = df_view_cia[df_view_cia['razao_social'].isin(comp_aerea_1)].reset_index(drop=True)

st.dataframe(df_view_cia_filt)

placeholder = st.empty()
with placeholder.container():
    st.header('Principais rotas de cada companhia aérea.')
    fig_rotas = plota_rotas(df_view_cia_filt)
    st.plotly_chart(fig_rotas, use_container_width=True)


df_ranking_aero_cia = pd.read_parquet('output/RANKING_AERO_CIA/ranking_aero_cia.snappy.parquet')    
comp_aerea_2 = st.multiselect(label='Filtre por companhia aérea', options=df_ranking_aero_cia['razao_social'].unique(), default=None)

df_ranking_aero_cia_filt = df_ranking_aero_cia[df_ranking_aero_cia['razao_social'].isin(comp_aerea_2)]
st.dataframe(df_ranking_aero_cia_filt)    

placeholder2 = st.empty()

with placeholder2.container():
    st.header('Principais rotas de cada companhia aérea.')
    fig_aeroportos = plota_aeroportos(df_ranking_aero_cia_filt)
    st.plotly_chart(fig_aeroportos, use_container_width=True)