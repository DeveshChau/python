# Copy file from src to dest
from sys import *
import os
import time
def DirectoryTravel(DirName):
    print("We are going to Scan the Directory : ",DirName)

    flag = os.path.isabs(DirName)

    if flag == False:
        DirName = os.path.abspath(DirName)

    exist = os.path.isdir(DirName)

    if exist:
        directory = argv[2]
        try: 
            os.mkdir(directory) 
        except OSError as error: 
            print("error: destination directory already exist")
            return  
        for foldername, subfoldername, filename in os.walk(DirName):
            for fname in filename:
                try:
                    f = open(os.path.join(directory, fname), 'x')
                    f.close() 
                except FileExistsError:
                    print("Can not rename file name exist")
    else:
        print("Invalid path")
def main():
    print("-------------- Automation Script --------------")

    print("Automation Script Name : ",argv[0])

    if(len(argv) != 3):
        print("Invalid number of arguments")
        exit()

    if(argv[1] == "-h" or argv[1] == "-H"):    # Flag for displaying help
        print("This automation script is used to Copy file from src to dest")
        exit()
    
    elif(argv[1] == "-u" or argv[1] == "-U"):    # Flag for displaying the usage of script
        print("Usage : Name_Of_Script First_Argument second_Argument")
        print("Example : Demo.py Demo temp")
        exit()

    else:
        starttime = time.time()
        DirectoryTravel(argv[1])
        endtime = time.time()

        print("The script took time to execute as : ",endtime-starttime)

if __name__ == "__main__":
    main()