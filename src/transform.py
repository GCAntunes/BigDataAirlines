import re

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


if __name__ == '__main__':
    case_1 = 'CamelCase'
    print(snake_case(case_1))

    case_2 = 'pascalCase'
    print(snake_case(case_2))

    case_3 = 'teste.com.ponto'
    print(snake_case(case_3))
