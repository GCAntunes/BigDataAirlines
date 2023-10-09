import asyncio
import io
import os
import re

import aiohttp
import pandas as pd
import unidecode


def snake_case(column: str) -> str:
    return unidecode.unidecode(
        '_'.join(
            re.sub(
                '([A-Z][a-z]+)',
                r' \1',
                re.sub(
                    '([A-Z]+)',
                    r' \1',
                    re.sub(r'\.', '_', column.replace('-', ' ')),
                ),
            ).split()
        ).lower()
    )

def separa_icao_iata(df: pd.DataFrame) -> pd.DataFrame:
    df[['icao', 'iata']] = df['icao_iata'].str.split(pat=' ',n=1, expand=True)
    return df.drop(columns=['icao_iata'])


async def create_aero_df(client, code: str) -> pd.DataFrame:
    url = 'https://airport-info.p.rapidapi.com/airport'
    headers = {
        'X-RapidAPI-Key': os.getenv('API_KEY'),
        'X-RapidAPI-Host': 'airport-info.p.rapidapi.com',
    }
    params = {'icao': code}
    async with client.get(url, headers=headers, params=params) as response:
        return pd.json_normalize(await response.json())


async def get_all_dfs_async(icao_code: list) -> list:
    async with aiohttp.ClientSession() as client:
        futures = [create_aero_df(client, code) for code in icao_code]
        return await asyncio.gather(*futures)


def concat_lst_df(icao_code: list) -> pd.DataFrame:
    lst_dfs = asyncio.get_event_loop().run_until_complete(
        get_all_dfs_async(icao_code)
    )
    return pd.concat(lst_dfs)


if __name__ == '__main__':
    case_1 = 'CamelCase'
    print(snake_case(case_1))

    case_2 = 'pascalCase'
    print(snake_case(case_2))

    case_3 = 'teste.com.ponto'
    print(snake_case(case_3))
