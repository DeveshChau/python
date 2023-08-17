# Factorial of a number
def factorial(num):
    ans = 1
    if num < 0:
        print("Number should be positive")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            ans = ans*i
        print("Factorail is", ans)
def main():
    number = int(input("Enter a number: "))
    factorial(number)
if __name__ == "__main__":
    main()