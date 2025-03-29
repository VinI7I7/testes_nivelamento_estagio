import os
import pandas as pd
from .configs import Config

def get_csv_path():
    if os.path.exists(Config.DATA_PATH):
        return Config.DATA_PATH
    raise FileNotFoundError("Arquivo CSV não encontrado")

def load_data():
    try:
        csv_path = get_csv_path()
        df = None

        for encoding in Config.ENCODINGS:
            try:
                df = pd.read_csv(csv_path, encoding=encoding, sep=';')
                break
            except UnicodeDecodeError:
                continue

        if df is None:
            raise Exception("Não foi possível ler o arquivo CSV")
        
        return df
    except Exception as e:
        raise
