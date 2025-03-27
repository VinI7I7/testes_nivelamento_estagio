import os
import zipfile

def compress_pdfs():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    data_folder = os.path.join(base_dir, 'data')
    zip_filename = os.path.join(data_folder, 'anexos.zip')

    if not os.path.exists(data_folder):
        print("Erro: A pasta 'data' não existe. Certifique-se de que ela foi criada antes de compactar.")
        return

    if os.path.exists(zip_filename):
        print(f"O arquivo ZIP  já existe. ")
        return


    pdf_files = [f for f in os.listdir(data_folder) if f.endswith('.pdf')]
    
    if not pdf_files:
        print("Nenhum arquivo PDF encontrado para compactar.")
        return

    try:
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for pdf in pdf_files:
                pdf_path = os.path.join(data_folder, pdf)
                zipf.write(pdf_path, arcname=pdf)  
                print(f"Arquivo '{pdf}' adicionado ao ZIP.")
        print(f"PDFs compactados com sucesso")
    except Exception as e:
        print(f"Erro ao compactar os arquivos: {e}")