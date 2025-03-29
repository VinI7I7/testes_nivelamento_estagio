from fastapi import FastAPI
from typing import List
import pandas as pd
from pydantic import BaseModel

csv_path = 'C:\Projetos\testes_nivelamento_estagio\data\Relatorio_cadop.csv'

def load_csv():
    return pd.read_csv(csv_path, sep=";", encoding="utf-8")

app = FastAPI()

class Operadora(BaseModel):
    Registro_ANS: int
    CNPJ: str
    Razao_Social: str
    Nome_Fantasia: str
    Modalidade: str
    Logradouro: str
    Numero: int
    Complemento: str
    Bairro: str
    Cidade: str
    UF: str
    CEP: str
    DDD: int
    Telefone: str
    Fax: str
    Endereco_eletronico: str
    Representante: str
    Cargo_Representante: str
    Regiao_de_Comercializacao: int
    Data_Registro_ANS: str

@app.get("/busca_operadoras/", response_model=List[Operadora])
async def search_operators(query: str):
    df = load_csv()
    result = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]
    return result.to_dict(orient="records")
