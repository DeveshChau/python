# Write ChkNum() to find even odd number 
def ChkNum(value):
    """Check number is even or odd"""
    if value%2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
def main():
    number = int(input("Enter a number: "))
    ChkNum(number)
if (__name__ == "__main__"):
    main()