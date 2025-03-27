import requests
import os
from bs4 import BeautifulSoup

URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

DATA_FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))), 'data')

def get_pdf_links():
    response = requests.get(URL)
    if response.status_code != 200:
        print("Erro ao acessar a página.")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    
    links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.endswith(".pdf") and ("Anexo_I" in href or "Anexo_II" in href):
            links.append(href)

    return links

def download_pdfs():
    os.makedirs(DATA_FOLDER, exist_ok=True)
    links = get_pdf_links()
    
    new_links = [link for link in links if not os.path.exists(os.path.join(DATA_FOLDER, os.path.basename(link)))]

    if not new_links:
        print("Todos os anexos já estão baixados.")
        return

    print(f"{len(new_links)} arquivos serão baixados.")

    for link in new_links:
        filename = os.path.basename(link)
        filepath = os.path.join(DATA_FOLDER, filename)

        response = requests.get(link)
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"Baixado: {filename}")
        else:
            print(f"Falha ao baixar: {filename}")