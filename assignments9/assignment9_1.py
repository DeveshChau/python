# check file exist in current directory tree or not
import os
from sys import *
def findFile(fileName):
    for currentFolder, subFolders, files in os.walk(os.getcwd()):
        for file in files:
            if file == fileName:
                print("File found")
                break
def main():
    if(len(argv) != 2):
        print("invalid number of arguments")
    if(argv[1] == "-u" or argv[1] == "-U"):
        print("usage: python programName fileName")
        print("sample: python find.py source.txt")
        exit()
    elif(argv[1] == "-h" or argv[1] == "-H"):
        print("To check if file exist in current directory")
        exit()
    else:
        findFile(argv[1])
if __name__ == "__main__":
    main()