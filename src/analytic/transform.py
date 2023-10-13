import pandas as pd


def view_cia(df_air_cia: pd.DataFrame, df_vra: pd.DataFrame, df_aerodromos:pd.DataFrame) -> pd.DataFrame:
    df_air_cia = df_air_cia[['icao', 'razao_social']]
    df_vra = df_vra[['icao_aerodromo_origem', 'icao_aerodromo_destino', 'situacao_voo', 'icao_empresa_aerea']]
    df_aerodromos_1 = df_aerodromos.loc[:,['icao', 'name', 'state', 'country_iso', 'latitude', 'longitude']]
    df_aerodromos_1['estado_uf_origem'] = df_aerodromos_1['state'] + '/' + df_aerodromos_1['country_iso']
    df_aerodromos_2 = df_aerodromos_1.rename(columns={'estado_uf_origem': 'estado_uf_destino'})
    
    df_ranking_cia = (df_air_cia.merge(df_vra, 'left', left_on= 'icao', right_on= 'icao_empresa_aerea', suffixes=('', '_vra'))
                                .merge(df_aerodromos_1, 'left', left_on = 'icao_aerodromo_origem', right_on= 'icao', suffixes=('', '_aero1'))
                                .merge(df_aerodromos_2, 'left', left_on = 'icao_aerodromo_destino', right_on= 'icao', suffixes=('', '_aero2'))
                                .query("situacao_voo == 'REALIZADO'")
                                .drop(columns = ['icao', 'icao_aerodromo_origem', 'icao_aerodromo_destino', 'icao_empresa_aerea', 'state', 'country_iso', 'state_aero2', 'country_iso_aero2', 'situacao_voo'])
                                .rename(columns = {'icao_aero1': 'icao_origem', 'icao_aero2': 'icao_destino', 'name': 'aeroporto_origem', 'name_aero2': 'aeroporto_destino',
                                                   'latitude': 'latitude_origem', 'longitude': 'longitude_origem', 'latitude_aero2': 'latitude_destino', 'longitude_aero2': 'longitude_destino'})
                                .groupby(['razao_social','icao_origem', 'aeroporto_origem', 'estado_uf_origem', 'icao_destino', 'aeroporto_destino', 'estado_uf_destino', 'latitude_origem', 'longitude_origem', 'latitude_destino', 'longitude_destino'], as_index=False)['razao_social']
                                .agg(['count'])
                               # .sort_values(by=['razao_social', 'count'], axis = 0, ascending=[True, False])                                                        
                                )
        
    df_ranking_cia = (df_ranking_cia.assign(rank =df_ranking_cia.groupby('razao_social')['count'].rank(method='first', ascending=False),
                                            rota = df_ranking_cia['aeroporto_origem'].str.cat(df_ranking_cia['aeroporto_destino'], '-'),
                                            num_viagens_normalizado = (df_ranking_cia['count'] - df_ranking_cia['count'].mean())/(df_ranking_cia['count'].std()))
                                     .query("rank == 1")
                                     .reset_index(drop = True)
                                     .drop(columns='rank')
                                     .rename(columns={'count':'num_viagens'})
                                            )
        
    return df_ranking_cia

def view_aero(df_air_cia: pd.DataFrame, df_vra: pd.DataFrame, df_aerodromos:pd.DataFrame) -> pd.DataFrame:
       df_air_cia = df_air_cia[['icao', 'razao_social']]
       df_vra = df_vra[['icao_aerodromo_origem', 'icao_aerodromo_destino', 'situacao_voo', 'icao_empresa_aerea']]
       df_lat_lon = df_aerodromos[['icao', 'latitude', 'longitude']]
       df_aerodromos = df_aerodromos[['icao', 'name']]       
       
       df_decolagens = (df_air_cia.merge(df_vra, 'left', left_on= 'icao', right_on='icao_empresa_aerea', suffixes=('', '_vra'))
                                  .merge(df_aerodromos, 'right', left_on='icao_aerodromo_origem', right_on='icao', suffixes=('', '_aero'))
                                  .query("situacao_voo == 'REALIZADO'")
                                  .drop(columns = ['icao_aerodromo_destino', 'icao_aero', 'situacao_voo'])
                                  .groupby(['name', 'icao', 'razao_social', 'icao_aerodromo_origem', 'icao_empresa_aerea'], as_index = False)['razao_social']
                                  .agg(['count'])
                                  .rename(columns={'count':'num_decolagens'})
                                   )
       
       df_pousos = (df_air_cia.merge(df_vra, 'left', left_on= 'icao', right_on='icao_empresa_aerea', suffixes=('', '_vra'))
                              .merge(df_aerodromos, 'right', left_on='icao_aerodromo_destino', right_on='icao', suffixes=('', '_aero'))
                              .query("situacao_voo == 'REALIZADO'")
                              .drop(columns = ['icao_aerodromo_origem', 'icao_aero', 'situacao_voo'])
                              .groupby(['name', 'icao', 'razao_social', 'icao_aerodromo_destino', 'icao_empresa_aerea'], as_index = False)['razao_social']
                              .agg(['count'])
                              .rename(columns={'count':'num_pousos'})
                               )
       
       df_ranking_aero_cia = (df_decolagens.merge(df_pousos, 'inner', left_on=['icao_aerodromo_origem', 'icao_empresa_aerea'], right_on=['icao_aerodromo_destino', 'icao_empresa_aerea'], suffixes=('', '_pou'))
                                           #.assign(total_operacoes = df_decolagens.num_decolagens + df_decolagens.num_pousos)
                                           .drop(columns = ['name_pou', 'icao_pou', 'razao_social_pou', 'icao_empresa_aerea', 'icao_aerodromo_destino', 'icao'])
                                           .rename(columns = {'icao_aerodromo_origem': 'icao_aerodromo'}))
       
       df_ranking_aero_cia = df_ranking_aero_cia.assign(total_operacoes = df_ranking_aero_cia.num_decolagens +df_ranking_aero_cia.num_pousos)
       df_ranking_aero_cia = (df_ranking_aero_cia.assign(rank = df_ranking_aero_cia.groupby('name')['total_operacoes'].rank('first', ascending = False),
                                                         total_operacoes_normalizado = abs((df_ranking_aero_cia['total_operacoes'] - df_ranking_aero_cia['total_operacoes'].mean())/(df_ranking_aero_cia['total_operacoes'].std())))
                                                 .query("rank == 1")
                                                 .merge(df_lat_lon, 'inner', left_on='icao_aerodromo', right_on='icao')
                                                 .drop(columns = 'rank')
                                                 )
                                                                                                         
       
       
       
       return df_ranking_aero_cia
       
       