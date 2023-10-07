import glob
import pandas as pd

def extract_vra_json(path: str)  -> pd.DataFrame:

    all_files =  glob.glob(path)
    df_vra = pd.concat((pd.read_json(file, encoding = 'utf_8_sig',dtype=True) for file in all_files) , ignore_index=True) 
    return df_vra 
    
if __name__ == '__main__':
    df_vra = extract_vra_json('VRA*/*.json')
    print(df_vra)
    