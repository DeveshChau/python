# calculate frequency of string in given file
import os
from sys import *
def calculateFrequency(fileName,  string):
    for currentFolder, subFolders, files in os.walk(os.getcwd()):
        for file in files:
            if file == fileName:
                f = open(os.path.join(currentFolder,fileName), 'r')
                frequency = f.read().count(string)
                f.close()
                return frequency

def main():
    if(argv[1] == "-u" or argv[1] == "-U"):
        print("usage: python programName fileName string")
        print("sample: python script.py source.txt stringtosearch")
        exit()
    elif(argv[1] == "-h" or argv[1] == "-H"):
        print("To calculate frequency of string in given file")
        exit()
    elif(len(argv) != 3):
        print("invalid number of arguments")
    else:
        result = calculateFrequency(argv[1], argv[2])
        print("Frequency: ", result)
if __name__ == "__main__":
    main()