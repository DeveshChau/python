# check whether a number is positive, negative or zero 
def ChkNum(value):
    """Check number is zero positive or negative"""
    if (value == 0): return "Zero"
    if (value > 0): return "Positive number"
    return "Negative number"
def main():
    number = int(input("Enter a number: "))
    ans = ChkNum(number)
    print(ans)
if __name__ == "__main__":
    main()