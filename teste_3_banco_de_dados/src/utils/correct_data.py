import os
import pandas as pd

SAVE_FOLDER = "extract_data"

def fix_csv(input_file, output_file):
    try:
        df = pd.read_csv(input_file, delimiter=';', quotechar='"')

        df.columns = df.columns.str.replace('"', '').str.strip()

        if 'VL_SALDO_INICIAL' in df.columns and 'VL_SALDO_FINAL' in df.columns:
            df['VL_SALDO_INICIAL'] = df['VL_SALDO_INICIAL'].str.replace(',', '.').astype(float)
            df['VL_SALDO_FINAL'] = df['VL_SALDO_FINAL'].str.replace(',', '.').astype(float)

            if not os.path.exists(output_file):  
                df.to_csv(output_file, index=False, sep=';')
                print(f"Arquivo salvo: {output_file}")
            else:
                print(f"Aviso: {output_file} já existe e não foi sobrescrito.")
        else:
            print(f"Colunas 'VL_SALDO_INICIAL' ou 'VL_SALDO_FINAL' não encontradas em {input_file}")

    except Exception as e:
        print(f"Erro ao processar {input_file}: {e}")

def process_csv():
    if not os.path.exists(SAVE_FOLDER):
        print(f"Pasta '{SAVE_FOLDER}' não encontrada.")
        return

    for root, dirs, files in os.walk(SAVE_FOLDER):
        for file_name in files:
            if file_name.endswith(".csv"):
                input_file = os.path.join(root, file_name)
                output_file = os.path.join(SAVE_FOLDER, file_name)

                if os.path.exists(output_file):
                    print(f"O arquivo {output_file} já existe.")
                    continue  

                print(f"Processando arquivo: {input_file}")
                fix_csv(input_file, output_file)

