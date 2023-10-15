from zipfile import ZipFile 
from fnmatch import fnmatch
import os

filezip = "zip-23588.zip"
txtfile = "password.txt"

while(filezip):
    print(0,txtfile,filezip)
    pswd = open(txtfile,"r").read()
    ZipFile(filezip,"r").extractall(pwd=pswd.strip().encode('ascii'))

    files = ZipFile(filezip,"r").namelist()
    os.remove(filezip)
    print(1,files)

    filezip = files[0] if (fnmatch(files[0], "*.zip")) else False
    txtfile = files[1] if (fnmatch(files[1], "*.txt")) else False
    print(2,txtfile,filezip)


