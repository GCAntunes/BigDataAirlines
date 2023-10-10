import pandas as pd


def get_df_from_parquet(path: str) -> pd.DataFrame:
    return pd.read_parquet(path)
