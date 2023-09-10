# Summation of digit
def summation(n):
    if n == 0:
        return 0
    return (n % 10 + summation(int(n / 10)))
def main():
    no = int(input("Enter a number: "))
    result = summation(no)
    print("Sum", result)
if __name__ == "__main__":
    main()