# display following pattern for given input number.
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

def printPattern(num):
    for i in range(0,num):
        for j in range(0, num):
            print('*', end=' ')
        print()
def main():
    number = int(input("Enter number for pattern: "))
    printPattern(number)
if __name__ == "__main__":
    main()
