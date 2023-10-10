import asyncio

import pandas as pd
from extract import extract_air_csv, extract_vra_json
from load import df_to_parquet
from transform import concat_lst_df, get_all_dfs_async, separa_icao_iata, snake_case

from rich.progress import Progress

if __name__ == '__main__':
    progress = Progress()
    progress.start()
    pipeline_task = progress.add_task("Lendo json's de VRA...", total = 100)
    df_vra = extract_vra_json('./data/VRA/*.json')
    
    progress.update(pipeline_task, advance=25, description= "Lendo csv's de AIR_CIA")
    df_air_cia = extract_air_csv('./data/AIR_CIA/*.csv')
    
    progress.update(pipeline_task, advance=25, description= "Padronizando nome das colunas")
    df_air_cia = df_air_cia.rename(
        columns={column: snake_case(column) for column in df_air_cia.columns}
    )

    df_air_cia = separa_icao_iata(df_air_cia)

    df_vra = df_vra.rename(
        columns={column: snake_case(column) for column in df_vra.columns}
    )
    df_vra = df_vra.astype({'codigo_autorizacao': 'string'})

    icao_code = set(
        list(df_vra['icao_aerodromo_origem'].unique())
        + list(df_vra['icao_aerodromo_destino'].unique())
    )
    
    progress.update(pipeline_task, advance=25, description= "Chamando API Airport Info")
    df_aerodromos = concat_lst_df(icao_code)

    df_aerodromos = df_aerodromos.rename(
        columns={
            column: snake_case(column) for column in df_aerodromos.columns
        }
    ).loc[pd.isnull(df_aerodromos['error.text'])]

    df_aerodromos['state'] = df_aerodromos['state'].str.replace(
        'State of ', ''
    )
    df_aerodromos = df_aerodromos[pd.isnull(df_aerodromos.error_text)]
    progress.update(pipeline_task, advance=24, description= "Salvando os .parquet's")
    load_list = [
        [df_air_cia, 'output/AIR_CIA', 'air_cia'],
        [df_aerodromos, 'output/AERODROMOS', 'aerodromos'],
        [df_vra, 'output/VRA', 'vra'],
    ]
   
    [
        df_to_parquet(df, dir_path, filename)
        for df, dir_path, filename in load_list
    ]
    progress.update(pipeline_task, advance=1,description= "Finalizado!")
    progress.stop()