from src.extract import extract_air_csv, extract_vra_json

if __name__ == '__main__':
    df_vra = extract_vra_json('./data/VRA/*.json')
    df_air_cia = extract_air_csv('./data/AIR_CIA/*.csv')

    print(df_vra)
    print(df_air_cia)
