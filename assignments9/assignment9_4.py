# compare content of the file.
import os
from sys import *
import hashlib 

def hashfile(path, blocksize = 1024):
    fd = open(path, 'rb')
    hasher = hashlib.md5()
    buf = fd.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)

    fd.close
    return hasher.hexdigest()

def compareFile(fileName1, fileName2):
    hash1 = ''
    hash2 = ''
    for currentFolder, subFolders, files in os.walk(os.getcwd()):
        for file in files:
            if file == fileName1:
                hash1 = hashfile(os.path.join(currentFolder,fileName1))
            elif file == fileName2:
                hash2 = hashfile(os.path.join(currentFolder,fileName2))
    if hash1 == hash2:
        print("Success")
    else:
        print("Failuer")
def main():
    if(argv[1] == "-u" or argv[1] == "-U"):
        print("usage: python programName fileName1 fileName2")
        print("sample: python scipt.py source1.txt source2.txt")
        exit()
    elif(argv[1] == "-h" or argv[1] == "-H"):
        print("To compare content of the file.")
        exit()
    elif(len(argv) != 3):
        print("invalid number of arguments")
    else:
        compareFile(argv[1], argv[2])
if __name__ == "__main__":
    main()