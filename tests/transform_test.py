from src.transform import snake_case

def test_snake_case():
    assert snake_case('pascalCase') == 'pascal_case'