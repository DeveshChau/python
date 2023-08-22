# Lambda to return power of 3
def main():
    number = int(input("Enter a Number: "))
    result = (lambda num: num*num)(number)
    print('Square of {0}: '.format(number),result)
if __name__ == "__main__":
    main()