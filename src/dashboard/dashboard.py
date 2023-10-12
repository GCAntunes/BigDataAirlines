import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from dashboard_utils import plota_rotas

st.set_page_config(layout='wide')

df_view_cia = pd.read_parquet('output/VIEW_CIA/view_cia.snappy.parquet')
df_ranking_aero_cia = pd.read_parquet('output/RANKING_AERO_CIA/ranking_aero_cia.snappy.parquet')
# st.dataframe(df_view_cia)

comp_aerea_1 = st.multiselect(
    label='Filtre por companhia aérea',
    options=df_view_cia['razao_social'],
    default=None,
)

geo_fig = go.Figure(layout={'width': 800, 'height': 800})

df_view_cia_filt = df_view_cia[
    df_view_cia['razao_social'].isin(comp_aerea_1)
].reset_index(drop=True)

st.dataframe(df_view_cia_filt)

placeholder = st.empty()

with placeholder.container():

    geo_fig = plota_rotas(df_view_cia_filt)
    st.plotly_chart(geo_fig, use_container_width=True)
    
comp_aerea_2 = st.multiselect(
    label='Filtre por companhia aérea',
    options=df_ranking_aero_cia['razao_social'],
    default=None,
)
df_ranking_aero_cia_filt = df_ranking_aero_cia[df_ranking_aero_cia['razao_social'].isin(comp_aerea_2)]
st.dataframe(df_ranking_aero_cia_filt)    

placeholder2 = st.empty()

with placeholder2.container():
    #st.dataframe(df_ranking_aero_cia)
    fig = px.scatter_geo(df_ranking_aero_cia_filt, lat = 'latitude', lon='longitude', 
                         hover_data={'icao_aerodromo':True, 'total_operacoes':True, 'razao_social':True, 'latitude':False, 'longitude':False}, 
                         size = 'total_operacoes', 
                         hover_name = 'name',
                         width = 1000,
                         height = 1000,
                         title = 'Companhia área com mais operações em cada aeroporto')
    st.plotly_chart(fig, use_container_width=True)