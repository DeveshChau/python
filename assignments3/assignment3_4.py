# accept N number and return frequency of given list
def frequency(numList, val):
    count = 0
    for i in numList:
        if i == val:
            count = count + 1
    return count
def main():
    numbers = int(input("Enter Count: " ))
    numberList = []
    for i in range(numbers):
        numberList.append(int(input("Enter number {0}: ".format(i+1))))
    element = int(input("Element to search: "))
    result = frequency(numberList, element)
    print("Frequency of {0} is: ".format(element), result)
if __name__ == "__main__":
    main()