# Filter between 70-90, Map 10, Reduce product of list
from functools import reduce
def main():
    listLen = int(input('How many number: '))
    data = []
    for i in range(listLen):
        data.append(int(input('Enter {0} of numbers: '.format(i))))
    between70_90 = list(filter(lambda num: num >= 70 and num <= 90, data))
    increment = list(map(lambda num: num+10, between70_90))
    product = reduce(lambda num1, num2: num1*num2, increment)
    print("List after filter: ", between70_90)
    print("List after map: ", increment)
    print("Output of reduce: ", product)
if __name__ == "__main__":
    main()