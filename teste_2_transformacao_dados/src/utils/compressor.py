import os
import zipfile

def compress_csv(csv_path, zip_path):

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_path, arcname=os.path.basename(csv_path)) 