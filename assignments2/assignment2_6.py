# Print following patter for given number
# * * * * *
# * * * *
# * * * 
# * *
# *

def printPattern(num):
    for i in range(num,0,-1):
        print('* '*i)
def main():
    number = int(input("Enter a number: "))
    printPattern(number)
if __name__ == "__main__":
    main()