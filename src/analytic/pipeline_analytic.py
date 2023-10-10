from extract import get_df_from_parquet
from transform import view_cia
from load import df_to_parquet

if __name__ == '__main__':
    df_air_cia = get_df_from_parquet('./output/AIR_CIA/')
    df_vra = get_df_from_parquet('./output/VRA/')
    df_aerodromos = get_df_from_parquet('./output/AERODROMOS/')
    
    df_view_cia = view_cia(df_air_cia, df_vra, df_aerodromos)
    
    df_to_parquet(df_view_cia, './output/VIEW_CIA', 'view_cia')