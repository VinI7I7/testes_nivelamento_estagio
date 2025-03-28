import os
import requests
from bs4 import BeautifulSoup
import re

URL_DC = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/"
URL_OP = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/"
SAVE_FOLDER = "data"

os.makedirs(SAVE_FOLDER, exist_ok=True)

def get_current_years():
    response = requests.get(URL_DC)
    if response.status_code != 200:
        print("Erro ao acessar a página de demonstrações contábeis.")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    years = sorted(
        [int(a.text.strip("/")) for a in soup.find_all('a', href=True) if re.match(r"\d{4}/", a.text)],
        reverse=True
    )   
    return years[:2]  

def get_file_links(url, year=None, extension=".zip"):
    url = f"{url}{year}/" if year else url
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Erro ao acessar {url}")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    return [url + a['href'] for a in soup.find_all('a', href=True) if a['href'].endswith(extension)]

def download_file(url):
    filename = url.split("/")[-1]  
    save_path = os.path.join(SAVE_FOLDER, filename)

    if os.path.exists(save_path):
        print(f"Arquivo já existe: {filename}, pulando download.")
        return


    response = requests.get(url, stream=True)

    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Download concluído: {filename}")
    else:
        print(f"Erro ao baixar {filename}")

def download_all_files():
    recent_years = get_current_years()
    if not recent_years:
        print("Nenhum ano disponível para download.")
        return
    
    print(f"Baixando arquivos dos anos: {recent_years}")

    for year in recent_years:
        file_links = get_file_links(URL_DC, year)
        for file_url in file_links:
            download_file(file_url)
    
    op_links = get_file_links(URL_OP, extension=".csv")
    for op_url in op_links:
        if "Relatorio_cadop.csv" in op_url: 
            download_file(op_url)
            break 


