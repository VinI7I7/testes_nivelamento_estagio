import os
import pandas as pd

SAVE_FOLDER = "extract_data"  

def fix_csv(input_file, output_file):
    df = pd.read_csv(input_file, delimiter=';', quotechar='"')

    df.columns = df.columns.str.replace('"', '').str.strip()

    if 'VL_SALDO_INICIAL' in df.columns and 'VL_SALDO_FINAL' in df.columns:
        df['VL_SALDO_INICIAL'] = df['VL_SALDO_INICIAL'].str.replace(',', '.').astype(float)
        df['VL_SALDO_FINAL'] = df['VL_SALDO_FINAL'].str.replace(',', '.').astype(float)

        df.to_csv(output_file, index=False, sep=';')
    else:
        print(f"Colunas 'VL_SALDO_INICIAL' ou 'VL_SALDO_FINAL' não encontradas em {input_file}")

def process_csv():
    for root, dirs, files in os.walk(SAVE_FOLDER):
        for file_name in files:
            if file_name.endswith(".csv"):
                input_file = os.path.join(root, file_name)
                output_file = os.path.join(SAVE_FOLDER, f"{file_name}")
                print(f"Processando arquivo: {input_file}")
                fix_csv(input_file, output_file)

if __name__ == "__main__":
    process_csv()
