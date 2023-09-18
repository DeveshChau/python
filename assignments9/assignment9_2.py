# show content of file present in current folder tree
import os
from sys import *
def findAndReadFile(fileName):
    for currentFolder, subFolders, files in os.walk(os.getcwd()):
        for file in files:
            if file == fileName:
                f = open(os.path.join(currentFolder,fileName), 'r')
                print(f.read())
                f.close()
                break
def main():
    if(len(argv) != 2):
        print("invalid number of arguments")
    if(argv[1] == "-u" or argv[1] == "-U"):
        print("usage: python programName fileName")
        print("sample: python script.py source.txt")
        exit()
    elif(argv[1] == "-h" or argv[1] == "-H"):
        print("To show content of file present in current folder tree")
        exit()
    else:
        findAndReadFile(argv[1])
if __name__ == "__main__":
    main()