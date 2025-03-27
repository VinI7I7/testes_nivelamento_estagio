import pandas as pd
import pdfplumber
from tqdm import tqdm

def extract_table_from_pdf(pdf_path):
    all_tables = []
    
    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        
        with tqdm(total=total_pages, desc="Extraindo páginas", unit="pág") as pbar:
            for page_num, page in enumerate(pdf.pages, 1):
                tables = page.extract_tables()
                for table in tables:
                    try:
                        df = pd.DataFrame(table[1:], columns=table[0])
                        all_tables.append(df)
                    except Exception as e:
                        print(f"\nErro ao processar tabela na página {page_num}: {str(e)}")
                        continue
                
                pbar.update(1)
                pbar.set_description(f"Página {page_num}/{total_pages} - {len(all_tables)} tabelas encontradas")
    
    if all_tables:
        print("\nCombinando todas as tabelas...")
        final_df = pd.concat(all_tables, ignore_index=True)
        final_df = final_df.dropna(how='all')
        print(f"Total de tabelas processadas: {len(all_tables)}")
        return final_df
    else:
        raise Exception("Nenhuma tabela encontrada no PDF")