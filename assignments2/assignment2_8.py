# Print following patter for given number
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4
# 1 2 3 4 5

def printPattern(num):
    for i in range(num+1):
        j = 1
        while(j<i+1):
            print(j, end=' ')
            j = j+1
        print()
            
def main():
    number = int(input("Enter a number: "))
    printPattern(number)
if __name__ == "__main__":
    main()