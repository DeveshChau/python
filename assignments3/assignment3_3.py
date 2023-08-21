# accept N number and return min num
def minNum(numList):
    return min(numList)
def main():
    numbers = int(input("Enter Count: " ))
    numberList = []
    for i in range(numbers):
        numberList.append(int(input("Enter number {0}: ".format(i+1))))
    result = minNum(numberList)
    print("Minimum number is: ", result)
if __name__ == "__main__":
    main()