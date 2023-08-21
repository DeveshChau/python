# accept N number and return addition of prime numbers
import MarvellousNum
from functools import reduce
def ListPrime(numList):
    primeList = []
    for i in numList:
        if MarvellousNum.chkPrime(i):
            primeList.append(i)
    return (reduce(lambda a,b:a+b,primeList), primeList)
def main():
    numbers = int(input("Enter Count: " ))
    numberList = []
    for i in range(numbers):
        numberList.append(int(input("Enter number {0}: ".format(i+1))))
    addition,primeNumbers = ListPrime(numberList)
    print("Addition is: ", addition, primeNumbers)
if __name__ == "__main__":
    main()