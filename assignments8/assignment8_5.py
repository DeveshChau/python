# factorial of digit
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
def main():
    no = int(input("Enter a number: "))
    result = factorial(no)
    print("Sum", result)
if __name__ == "__main__":
    main()