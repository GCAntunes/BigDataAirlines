# BIG DATA AIRLINES

## Sobre o Projeto

Esse repositório foi feito para um estudo pontual de ETL, utilizando dados de aviação, realizando uma pequena padronização nos headers e datatypes e salvando em formato parquet. Na sequência esses parquet serão lidos e análises dos dados serão feitas, usando a biblioteca streamlit para a exposição dos insights

## Premissas básicas

Esse projeto foi desenvolvido pensando utilizando Poetry para gerenciamento de dependências e o Pyenv para gerenciamento da versão do Python.

Para instalação do Pyenv, você pode seguir o manual oficial [aqui](https://github.com/pyenv/pyenv/#installation). Para o Poetry você pode consultar este [material](https://python-poetry.org/docs/#installation)

Também é utilizado uma API para consultar os dados dos aeródromos. Para utilizar a API é necessário realizar um cadastro no [Rapid API](https://rapidapi.com/) e recuperar sua chave de API, que será utilizada no passo 4. Você pode seguir esse [tutorial](https://docs.rapidapi.com/docs/keys-and-key-rotation) para recuperar sua chave

### Instalação e Configuração

1. Clone o repositório
```bash
git clone https://github.com/GCAntunes/BigDataAirlines.git
cd BigDataAirlines
```

2. Configure a versão do Python com `pyenv`:

```bash
pyenv install 3.10
pyenv local 3.10
```

3. Configure o poetry para utilizar a versão do Python instalada anteriormente:

```bash
poetry env use 3.10
```

4. Configure a varíavel de ambiente para utilizar a API:

```bash
export API_KEY=SUA_CHAVE_DO_RAPID_API
```

5. Instale as dependências necessárias:

```bash
poetry install
```

5. Ative o ambiente virtual:

```bash
poetry shell
```

6. Realize os testes para garantir o funcionamento da pipeline:

```bash
task test
```

7. Execute o seguinte comando para ver a documentação do projeto:

```bash
task doc
```
VocÊ também pode consultar a documentação [aqui](https://gcantunes.github.io/BigDataAirlines/)

8. Execute a pipeline de staging:

```bash
task run_staging
```

9. Verifique se o arquivo foi gerado corretamente:

```bash
task output_test
```

10. Execute a pipeline analítica:

```bash
task run_analytic
```

11. Veja os resultados em um dashboard:

```bash
task dashboard
```