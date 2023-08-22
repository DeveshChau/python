# Filter Even, Map square, Reduce addition of list
from functools import reduce
def main():
    listLen = int(input('How many number: '))
    data = []
    for i in range(listLen):
        data.append(int(input('Enter {0} of numbers: '.format(i))))
    even = list(filter(lambda num: num%2 == 0, data))
    square = list(map(lambda num: num*num, even))
    add = reduce(lambda num1, num2: num1+num2, square)
    print("List after filter: ", even)
    print("List after map: ", square)
    print("Output of reduce: ", add)
if __name__ == "__main__":
    main()