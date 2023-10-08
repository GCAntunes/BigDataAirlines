import pytest
import requests
import os
import glob

from src.transform import snake_case

param_list = [
    ('data/AIR_CIA/ANAC_*.csv'),
    ('data/VRA/VRA_*.json'),
]
@pytest.mark.parametrize('input', param_list)
def test_if_input_files_exist(input):
    assert glob.glob(input)

def test_api_key_env():
    api_key = os.getenv('API_KEY')
    assert api_key != None
    assert type(api_key) == str
  
def test_integration_airport_api():
    url = 'https://airport-info.p.rapidapi.com/airport'
    params = params = {'icao': '3166'}
    headers = {
        'X-RapidAPI-Key': os.getenv('API_KEY'),
        'X-RapidAPI-Host': 'airport-info.p.rapidapi.com',
    }
    response = requests.get(url, params=params, headers=headers)
    assert response.status_code == 200

@pytest.mark.parametrize(
    'input, expected',
    [
        ('pascalCase', 'pascal_case'),
        ('CamelCase', 'camel_case'),
        ('skewer-case', 'skewer_case'),
        ('ICAOCode', 'icao_code'),
        ('error.message', 'error_message'),
    ],
)
def test_snake_case(input, expected):
    assert snake_case(input) == expected


