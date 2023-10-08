import pandas as pd
import datetime
import os

def df_to_parquet(df, dir_path, filename):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    anomes = datetime.date.today().strftime('%Y%m')
    df.to_parquet(f'{dir_path}/{filename}_{anomes}.snappy.parquet', compression = 'snappy')
    