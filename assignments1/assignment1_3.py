# Addition of two number
def add(value1, value2):
    """Addition of 2 numbers"""
    return value1 + value2
def main():
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    ans = add(number1, number2)
    print("Addition is: ", ans)
if __name__ == "__main__":
    main()