# Lambda to return multiplication of 2 numbers
from functools import reduce
def main():
    number1 = int(input("Enter 1st Number: "))
    number2 = int(input("Enter 2nd Number: "))
    result = reduce(lambda num1,num2: num1*num2, [number1,number2])
    print('Multiplication of {0} and {1}: '.format(number1,number2),result)
if __name__ == "__main__":
    main()