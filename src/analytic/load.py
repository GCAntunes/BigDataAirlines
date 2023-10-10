import os

import pandas as pd


def df_to_parquet(df: pd.DataFrame, dir_path: str, filename: str):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    df.to_parquet(
        f'{dir_path}/{filename}.snappy.parquet', compression='snappy'
    )
