import datetime
import os

import pandas as pd


def df_to_parquet(df: pd.DataFrame, dir_path: str, filename: str):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    anomes = datetime.date.today().strftime('%Y%m')
    df.to_parquet(
        f'{dir_path}/{filename}_{anomes}.snappy.parquet', compression='snappy'
    )
