# Print following patter for given number
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

def printPattern(num):
    for i in range(num):
        j = 1
        while(j<num+1):
            print(j, end=' ')
            j = j+1
        print()
            
def main():
    number = int(input("Enter a number: "))
    printPattern(number)
if __name__ == "__main__":
    main()