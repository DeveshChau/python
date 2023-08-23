class Demo:
    Value = 0
    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2
    def Fun(self):
        print(self.no1, self.no2)
    def Gun(self):
        print(self.no1, self.no2)
number1 = int(input("Enter First Number: "))
number2 = int(input("Enter Second Number: "))
Demo(number1, number2)
Obj1 = Demo(11,21)
Obj2 = Demo(51,101)
Obj1.Fun()
Obj1.Gun()
Obj2.Fun()
Obj2.Gun()
