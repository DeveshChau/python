# Return number of digits in number
def digitCount(num):
    print(len(str(num)))
            
def main():
    number = int(input("Enter a number: "))
    digitCount(number)
if __name__ == "__main__":
    main()