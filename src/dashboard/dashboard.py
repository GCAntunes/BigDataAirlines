import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

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

    flight_paths = []
    for i in range(len(df_view_cia_filt)):
        geo_fig.add_trace(
            go.Scattergeo(
                locationmode='ISO-3',
                lon=[
                    df_view_cia_filt['longitude_origem'][i],
                    df_view_cia_filt['longitude_destino'][i],
                ],
                lat=[
                    df_view_cia_filt['latitude_origem'][i],
                    df_view_cia_filt['latitude_destino'][i],
                ],
                mode='lines',
                line=dict(width=1, color='red'),
                hoverinfo='text',
                text=f"""Rota: {df_view_cia_filt['rota'][i]}<br>Empresa área: {df_view_cia_filt['razao_social'][i]}<br>Número de viagens: {df_view_cia_filt['num_viagens'][i]}"""
                # legend = df_view_cia['rota']
                # opacity = float(df_view_cia['cnt'][i]) / float(df_view_cia['cnt'].max()),
            )
        )
    geo_fig.update_geos(lataxis_showgrid=True, lonaxis_showgrid=True)
    geo_fig.update_layout(
        title_text='Principal rota de cada Companhia Aérea',
        showlegend=False,
        geo=dict(
            scope='world',
            projection_type='azimuthal equal area',
            showland=True,
            landcolor='rgb(243, 243, 243)',
            countrycolor='rgb(204, 204, 204)',
            lataxis=dict(range=[-35, 30]),
            lonaxis=dict(range=[-90, -20]),
        ),
    )

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