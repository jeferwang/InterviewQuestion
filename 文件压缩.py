#!/usr/bin/python
import gzip
import tarfile
import os

f = tarfile.TarFile('D:/压缩包.tar', 'w')
startdir = "C:/Users/Jeffrey/.PyCharm2017.3"
for dirpath, dirnames, filenames in os.walk(startdir):
    for filename in filenames:
        print(os.path.join(dirpath, filename))
        f.add(os.path.join(dirpath, filename))
f.close()
with open("D:/压缩包.tar", 'rb') as plain_file:
    with gzip.open("D:/压缩包.tar.gz", 'wb') as zip_file:
        zip_file.writelines(plain_file)
