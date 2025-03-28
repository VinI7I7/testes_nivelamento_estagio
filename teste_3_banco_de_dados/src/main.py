from utils.download_files import download_all_files
from utils.extract_files import extract_all_zips

def main():
    download_all_files()

    extract_all_zips()

if __name__ == "__main__":
    main()
