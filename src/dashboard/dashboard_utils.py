import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def plota_rotas(df: pd.DataFrame) -> go.Figure:
    fig = go.Figure(layout={'width': 800, 'height': 800})
    flight_paths = []
    for i in range(len(df)):
        fig.add_trace(
            go.Scattergeo(
                locationmode='ISO-3',
                lon=[
                    df['longitude_origem'][i],
                    df['longitude_destino'][i],
                ],
                lat=[
                    df['latitude_origem'][i],
                    df['latitude_destino'][i],
                ],
                mode='lines+markers',
                line=dict(width=1.2),                
                hoverinfo='text',
                text=f"""Rota: {df['rota'][i]}
                <br>Empresa área: {df['razao_social'][i]}
                <br>Número de viagens: {df['num_viagens'][i]}
                <br>Estado origem: {df['estado_uf_origem'][i]}
                <br>Estado destino: {df['estado_uf_destino'][i]}""",
                name = df['rota'][i]
                # opacity = float(df_view_cia['cnt'][i]) / float(df_view_cia['cnt'].max()),
            )
        )
    fig.update_geos(lataxis_showgrid=True, lonaxis_showgrid=True)
    fig.update_layout(
        #title_text='Principal rota de cada Companhia Aérea',
        legend_title_text = 'Rota',
        showlegend=True,
        
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
    return fig

def plota_aeroportos(df: pd.DataFrame) -> go.Figure:
    fig2 = px.scatter_geo(df, lat = 'latitude', lon='longitude', 
                         hover_data={'icao_aerodromo':True, 'total_operacoes':True, 'razao_social':True, 'latitude':False, 'longitude':False}, 
                         size ='total_operacoes_normalizado',
                         color = 'razao_social', 
                         hover_name = 'name',                         
                         #labels = 'razao_social',
                         color_discrete_sequence= px.colors.qualitative.Light24,
                         width = 800,
                         height = 800)
    fig2.update_layout(legend_title_text='Companhia Aérea',showlegend=True)
    return fig2   