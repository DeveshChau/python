# Divisible by 5
def DivisibleBy5(value):
    """Check if given number is divisible by 5"""
    if value%5 == 0: return True
    return False
def main():
    number = int(input("Enter a number: "))
    ans = DivisibleBy5(number)
    print(ans)
if __name__ == "__main__":
    main()
