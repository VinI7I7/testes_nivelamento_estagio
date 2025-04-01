import pandas as pd

def replace_abbreviations(df):
    od_map = {
        'OD': 'Seg. Odontológica',
        'AMB': 'Seg. Ambulatorial'
    }
    
    for col in df.columns:
        if col in ['OD', 'AMB']:
            df[col] = df[col].replace(od_map)
    
    return df

def process_and_save_csv(df, output_path):

    df = df.dropna(how='all')
    
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    
    
    df = replace_abbreviations(df)
    
    df = df.drop_duplicates()
    
    
    if 'Código' in df.columns:
        df = df.sort_values('Código')
    
    df.to_csv(output_path, 
              index=False, 
              encoding='utf-8-sig',  
              sep=',',  
              quoting=1,  
              lineterminator='\n')  