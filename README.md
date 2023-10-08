# BIG DATA AIRLINES

## Sobre o Projeto

Esse repositório foi feito para um estudo pontual de ETL, utilizando dados de aviação, realizando uma pequena padronização nos headers e datatypes e salvando em formato parquet. Na sequência esses parquet serão lidos e análises dos dados serão feitas, usando a biblioteca streamlit para a exposição dos insights

## Premissas básicas

Esse projeto foi desenvolvido pensando no ambiente Linux, utilizando Poetry para gerenciamento de dependências eo Pyenv para gerenciamento da versão do Python.

### Instalação e Configuração

1. Clone o repositório
```bash
git clone https://github.com/GCAntunes/BigDataAirlines.git
cd BigDataAirlines
```

2. Configure a versão correta do Python com `pyenv`:

```bash
pyenv install 3.10
pyenv local 3.10
```

3. Configure o poetry para utilizar a versão do Python instalada anteriormente:

```bash
poetry env use 3.10
```

4. Ative o ambiente virtual:

```bash
poetry shell
```

5. Execute o seguinte comando para realizar os testes para garantir o funcionamento da pipeline:

```bash
task test
```

6. Execute o seguinte comando para ver a documentação do projeto:

```bash
task doc
```

7. Execute o seguinte comando para executar a pipeline:

```bash
task run
```

8. Verifique na pasta data/output se o arquivo foi gerado corretamente.