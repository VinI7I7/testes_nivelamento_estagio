from utils.download_files import download_all_files
from utils.extract_files import extract_all_zips
from utils.correct_data import process_csv

def main():
    download_all_files()

    extract_all_zips()

    process_csv()

if __name__ == "__main__":
    main()
