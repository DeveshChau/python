# accept N number and return addition
from functools import reduce
def add(numList):
    return reduce(lambda a,b:a+b,numList)
def main():
    numbers = int(input("Enter Count: " ))
    numberList = []
    for i in range(numbers):
        numberList.append(int(input("Enter number {0}: ".format(i+1))))
    result = add(numberList)
    print("Addition is: ", result)
if __name__ == "__main__":
    main()