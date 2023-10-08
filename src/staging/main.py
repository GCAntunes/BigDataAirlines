import asyncio

import pandas as pd

from src.extract import extract_air_csv, extract_vra_json
from src.load import df_to_parquet
from src.transform import concat_lst_df, get_all_dfs_async, snake_case

if __name__ == '__main__':
    df_vra = extract_vra_json('./data/VRA/*.json')
    df_air_cia = extract_air_csv('./data/AIR_CIA/*.csv')

    df_air_cia = df_air_cia.rename(
        columns={column: snake_case(column) for column in df_air_cia.columns}
    )
    df_vra = df_vra.rename(
        columns={column: snake_case(column) for column in df_vra.columns}
    )
    df_vra = df_vra.astype({'codigo_autorizacao': 'string'})

    icao_code = set(
        list(df_vra['icao_aerodromo_origem'].unique())
        + list(df_vra['icao_aerodromo_destino'].unique())
    )

    df_aerodromos = concat_lst_df(icao_code)
    df_aerodromos = df_aerodromos.rename(
        columns={
            column: snake_case(column) for column in df_aerodromos.columns
        }
    ).loc[pd.isnull(df_aerodromos['error.text'])]

    # df_aerodromos = df_aerodromos[pd.isnull(df_aerodromos.error_text)]
    load_list = [
        [df_air_cia, 'output/AIR_CIA', 'air_cia'],
        [df_aerodromos, 'output/AERODROMOS', 'aerodromos'],
        [df_vra, 'output/VRA', 'vra'],
    ]
    [
        df_to_parquet(df, dir_path, filename)
        for df, dir_path, filename in load_list
    ]
