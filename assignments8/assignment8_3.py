i = 5
def displayPattern(n):
    global i
    if(i > 0):
        print(i, end=' ')
        i-=1
        displayPattern(n)
def main():
    displayPattern(5)
if __name__ == "__main__":
    main()