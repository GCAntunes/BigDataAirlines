import glob

import pandas as pd

"""
Módulo com as funções de extração.
"""


def extract_vra_json(path: str) -> pd.DataFrame:
    """
    Função que lê a pasta de json's de VRA e retorna um único Pandas Dataframe

    Params:
        path (str): Caminho dos jsons de VRA
    Return:
        df_vra (pd.DataFrame): Dataframe resultante da compilação de todos os jsons
    """

    all_files = glob.glob(path)
    df_vra = pd.concat(
        (
            pd.read_json(file, encoding='utf_8_sig', dtype=True)
            for file in all_files
        ),
        ignore_index=True,
    )
    return df_vra


def extract_air_csv(path: str) -> pd.DataFrame:
    """
    Função que lê a pasta de csv's de AIR_CIA e retorna um único Pandas Dataframe

    Params:
        path (str): Caminho dos csv's de AIR_CIA
    Return:
        df_vra (pd.DataFrame): Dataframe resultante da compilação de todos os csv's
    """

    all_files = glob.glob(path)
    df_air_cia = pd.concat(
        [pd.read_csv(file, sep=';') for file in all_files], ignore_index=True
    )
    return df_air_cia


if __name__ == '__main__':
    df_vra = extract_vra_json('./data/VRA/*.json')
    print(df_vra)
    df_air_cia = extract_air_csv('./data/AIR_CIA/*.csv')
    print(df_air_cia)
