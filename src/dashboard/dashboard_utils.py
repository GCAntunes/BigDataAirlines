import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def plota_rotas(df: pd.DataFrame) -> go.Figure():
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
                mode='lines',
                line=dict(width=1, color='red'),
                hoverinfo='text',
                text=f"""Rota: {df['rota'][i]}<br>Empresa área: {df['razao_social'][i]}<br>Número de viagens: {df['num_viagens'][i]}"""
                # legend = df_view_cia['rota']
                # opacity = float(df_view_cia['cnt'][i]) / float(df_view_cia['cnt'].max()),
            )
        )
    fig.update_geos(lataxis_showgrid=True, lonaxis_showgrid=True)
    fig.update_layout(
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
    return fig
    