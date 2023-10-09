from extract import get_df_from_parquet
from transform import view_cia

if __name__ == '__main__':
    df_air_cia = get_df_from_parquet('./output/AIR_CIA/')
    df_vra = get_df_from_parquet('./output/VRA/')
    df_aerodromos = get_df_from_parquet('./output/AERODROMOS/')
    
    df_view_cia = view_cia(df_air_cia, df_vra, df_aerodromos)
    
    print(df_view_cia)
    
    print(df_view_cia.columns)
    
    df_view_cia.to_parquet('output/VIEW_CIA/view_cia.snappy.parquet', compression='snappy')