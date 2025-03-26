from utils.downloader import download_pdfs
from utils.compressor import compress_pdfs

def main():
    print("\nIniciando Web Scraping...\n")

    try:
        download_pdfs()
    except Exception as e:
        print(f"Erro ao baixar PDFs: {e}")
        return  

    print("Compactando PDFs...")

    try:
        compress_pdfs()
    except Exception as e:
        print(f"Erro ao compactar PDFs: {e}")
        return 

    print("\nProcesso concluído com sucesso!\n")

if __name__ == "__main__":
    main()
