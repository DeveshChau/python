# Print given Number of *
def printStar(val):
    """Print star for given number"""
    for i in range(val):
        print("*")
def main():
    number = int(input("Enter a number: "))
    printStar(number)
if __name__ == "__main__":
    main()