from extract import get_df_from_parquet
from load import df_to_parquet
from transform import view_cia, view_aero

from rich.progress import Progress

if __name__ == '__main__':
    progress = Progress()
    progress.start()
    
    pipeline_task = progress.add_task("Lendo parquet's da camada Staging")
    df_air_cia = get_df_from_parquet('./output/AIR_CIA/')
    df_vra = get_df_from_parquet('./output/VRA/')
    df_aerodromos = get_df_from_parquet('./output/AERODROMOS/')
    
    progress.update(pipeline_task, advance=25, description= "Gerando df_view_cia")
    df_view_cia = view_cia(df_air_cia, df_vra, df_aerodromos)
    
    progress.update(pipeline_task, advance = 35)
    df_ranking_aero_cia = view_aero(df_air_cia, df_vra, df_aerodromos)    
    
    progress.update(pipeline_task, advance=30, description= "Salvando os .parquet's na camada Analítica")
    df_to_parquet(df_view_cia, './output/VIEW_CIA', 'view_cia')
    df_to_parquet(df_ranking_aero_cia, './output/RANKING_AERO_CIA', 'ranking_aero_cia')
    progress.update(pipeline_task, advance=10, description= 'Finalizado!')
    progress.stop()