import pytest

from src.transform import snake_case


@pytest.mark.parametrize(
    'input, expected',
    [
        ('pascalCase', 'pascal_case'),
        ('CamelCase', 'camel_case'),
        ('ICAOCode', 'icao_code'),
        ('error.message', 'error_message'),
    ],
)
def test_snake_case(input, expected):
    assert snake_case(input) == expected
