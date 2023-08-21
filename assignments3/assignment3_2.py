# accept N number and return max num
def maxNum(numList):
    return max(numList)
def main():
    numbers = int(input("Enter Count: " ))
    numberList = []
    for i in range(numbers):
        numberList.append(int(input("Enter number {0}: ".format(i+1))))
    result = maxNum(numberList)
    print("Maximum number is: ", result)
if __name__ == "__main__":
    main()