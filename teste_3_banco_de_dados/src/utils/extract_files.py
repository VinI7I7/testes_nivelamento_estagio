import os
import zipfile
import re

SAVE_FOLDER = "data"
EXTRACT_FOLDER = "extract_data"

os.makedirs(EXTRACT_FOLDER, exist_ok=True)

def extract_all_zips():
    zip_filename = re.compile(r"^[1-4]T\d{4}\.zip$")  

    zip_files = [f for f in os.listdir(SAVE_FOLDER) if zip_filename.match(f)]

    for zip_file in zip_files:
        zip_path = os.path.join(SAVE_FOLDER, zip_file)
        extract_path = os.path.join(EXTRACT_FOLDER, os.path.splitext(zip_file)[0])

        if os.path.exists(extract_path) and os.listdir(extract_path):
            print(f"Arquivo já extraído: {zip_file}, pulando...")
            continue

        os.makedirs(extract_path, exist_ok=True)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        print(f"Extração concluída: {zip_file}")

