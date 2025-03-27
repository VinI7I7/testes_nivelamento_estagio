import pandas as pd
import pdfplumber

def extract_table_from_pdf(pdf_path):
    all_tables = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                df = pd.DataFrame(table[1:], columns=table[0])
                all_tables.append(df)
    
    if all_tables:
        final_df = pd.concat(all_tables, ignore_index=True)
        final_df = final_df.dropna(how='all')
        return final_df
    else:
        raise Exception("Nenhuma tabela encontrada no PDF") 