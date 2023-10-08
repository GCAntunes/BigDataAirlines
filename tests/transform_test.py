import pytest
import requests
import os

from src.transform import snake_case


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

def test_integration_aiport_api():
    url = 'https://airport-info.p.rapidapi.com/airport'
    params = params = {'icao': '3166'}
    headers = {
        'X-RapidAPI-Key': os.getenv('API_KEY'),
        'X-RapidAPI-Host': 'airport-info.p.rapidapi.com',
    }
    response = requests.get(url, params=params, headers=headers)
    assert response.status_code == 200
