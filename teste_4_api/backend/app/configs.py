import os

class Config:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
    
    DATA_PATH = r'data\Relatorio_cadop.csv'  
    
    ENCODINGS = ['utf-8', 'latin-1']
