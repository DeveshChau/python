import assignment2_1_1
def main():
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    print('Addition: ', assignment2_1_1.Add(num1, num2))
    print('Subtraction: ', assignment2_1_1.Sub(num1, num2))
    print('Multiplication: ', assignment2_1_1.Mult(num1, num2))
    print('Division: ', assignment2_1_1.Div(num1, num2))
if __name__ == "__main__":
    main()