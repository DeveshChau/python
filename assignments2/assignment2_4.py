# addition of factors
import math
def addFactors(num):
    if num < 0:
        print("Provide positive number")
    elif num == 0:
        print("0")
    else:
        ans = 0
        for i in range(1, math.ceil((num+1)/2)):
            if num%i==0:
                ans = ans+i
        print("Addition of factors is: ", ans)
def main():
    number = int(input("Enter a number: "))
    addFactors(number)
if __name__ == "__main__":
    main()
