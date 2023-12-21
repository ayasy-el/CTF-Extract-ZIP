import os
from pyunpack import Archive


def extract_zip(file_name, pswd):
    Archive(file_name,password=pswd).extractall('.')
    if file_name.endswith('.zip'):
        os.remove(file_name)
    print(f"extracted {file_name} : {pswd}")


zip_files = [file_name for file_name in os.listdir() if file_name.endswith('.zip')]
while zip_files:
    pswd = open("password.txt", "r").read().strip()
    extract_zip(zip_files[0],pswd)
    zip_files = [file_name for file_name in os.listdir() if file_name.endswith('.zip')]
