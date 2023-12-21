import os
import zipfile

def extract_zip(file_name, pswd):
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall(pwd=pswd.encode('ascii'))
    if file_name.endswith('.zip'):
        os.remove(file_name)
    print(f"extracted {file_name} : {pswd}")


zip_files = [file_name for file_name in os.listdir() if file_name.endswith('.zip')]
while zip_files:
    pswd = open("password.txt", "r").read().strip()
    extract_zip(zip_files[0],pswd)
    zip_files = [file_name for file_name in os.listdir() if file_name.endswith('.zip')]
