import pandas as pd

def replace_abbreviations(df):

    od_map = {
        'OD': 'Segmentação Odontológica',
        'AMB': 'Segmentação Ambulatorial'
    }
    
    for col in df.columns:
        if col in ['OD', 'AMB']:
            df[col] = df[col].replace(od_map)
    
    return df

def process_and_save_csv(df, output_path):


    df = df.dropna(how='all')
    
    df = replace_abbreviations(df)
    
    df.to_csv(output_path, index=False, encoding='utf-8')