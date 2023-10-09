# Página Inicial - BigDataAirlines

O intuito desse repositório é um pequeno estudo de caso utilizando dados de aviação, disponibilizados em diferentes formatos de arquivo, nominalmente json e csv. Além do consumo de uma [API](https://rapidapi.com/Active-api/api/airport-info) a partir dos dados presentes nesses arquivos.

Na sequência, os dados passam por uma pipeline analítica com os resultados sendo apresentados em um Dashboard via streamlit

```mermaid
---
title: Diagrama da solução
---
flowchart LR
    aircia["air_cia_1.csv
    .
    .
    .
    air_cia_n.csv"]
    vra["vra_1.json
    .
    .
    .
    vra_n.csv"]
    staging["Camada Staging"]
    API["API Airport Info"]
    analytic["Camada Analítica"]
    aircia -- air_cia.parquet --> staging
    vra -- vra.parquet --> staging
    vra -- icao_code --> API
    API -- aerodromos.parquet --> staging
    staging -- pipeline analítica --> analytic
    analytic --> Dashboard
```


