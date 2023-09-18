# copy content of the file.
import os
from sys import *
import shutil

def copyFile(fileName):
    for currentFolder, subFolders, files in os.walk(os.getcwd()):
        for file in files:
            if file == fileName:
                try:
                    source = os.path.join(currentFolder,fileName)
                    destination = os.path.join(currentFolder,"Demo.txt")
                    shutil.copyfile(source, destination)
                except shutil.SameFileError:
                    print("source and destination represent same file")
def main():
    if(len(argv) != 2):
        print("invalid number of arguments")
    if(argv[1] == "-u" or argv[1] == "-U"):
        print("usage: python programName fileName")
        print("sample: python scipt.py source.txt")
        exit()
    elif(argv[1] == "-h" or argv[1] == "-H"):
        print("To copy content of the file")
        exit()
    else:
        copyFile(argv[1])
if __name__ == "__main__":
    main()