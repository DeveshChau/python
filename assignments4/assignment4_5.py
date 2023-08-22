# Filter prime, Map multiply2, Reduce Maximum of list
from functools import reduce
import math
def chkPrime(num):
    for i in range(2,math.ceil(num/2)+1):
        if num % i == 0:
            return False
    return True
def main():
    listLen = int(input('How many number: '))
    data = []
    for i in range(listLen):
        data.append(int(input('Enter {0} of numbers: '.format(i+1))))
    primeList = list(filter(chkPrime, data))
    multiply2 = list(map(lambda num: num*2, primeList))
    Maximum = reduce(lambda a,b: a if a > b else b, multiply2)
    print("List after filter: ", primeList)
    print("List after map: ", multiply2)
    print("Output of reduce: ", Maximum)
if __name__ == "__main__":
    main()