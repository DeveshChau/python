# Check number is prime or not
import math
def isPrime(num):
    for i in range(2, math.ceil((num+1)/2)):
        if num%i==0:
            return print("Number is not prime")
        return print("Number is prime")
def main():
    number = int(input("Enter a number: "))
    isPrime(number)
if __name__ == "__main__":
    main()