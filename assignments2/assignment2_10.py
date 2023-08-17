# Return addition of digits in number
def digitCount(num):
    addition = 0
    while len(str(num))>1:
        addition = addition + (num%10)
        num //=10
    print(addition+num)

            
def main():
    number = int(input("Enter a number: "))
    digitCount(number)
if __name__ == "__main__":
    main()