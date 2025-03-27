import os
from utils.pdf_extractor import extract_table_from_pdf
from utils.csv_processor import process_and_save_csv
from utils.compressor import compress_csv

def main():
    print("\nIniciando extração e transformação de dados...\n")

    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    input_pdf = os.path.join(base_dir, 'data', 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf')
    output_csv = os.path.join(base_dir, 'data', 'tabela_rol.csv')
    output_zip = os.path.join(base_dir, 'data', 'vinicius_ribeiro.zip')

    try:

        print("Extraindo dados do PDF...")  
        df = extract_table_from_pdf(input_pdf)
        

        print("Processando e salvando CSV...")
        process_and_save_csv(df, output_csv)
        

        print("Compactando arquivo CSV...")
        compress_csv(output_csv, output_zip)
        
        print("\nProcesso concluído com sucesso!\n")
        
    except Exception as e:
        print(f"Erro durante o processamento: {e}")

if __name__ == "__main__":
    main()
