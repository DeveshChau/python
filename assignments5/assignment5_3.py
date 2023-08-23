class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
    def Accept(self):
        self.Value1 = int(input("Enter First Number: "))
        self.Value2 = int(input("Enter Second Number: "))
    def Addition(self):
        print(self.Value1+self.Value2)
    def Subtraction(self):
        print(self.Value1-self.Value2)
    def Multiplication(self):
        print(self.Value1*self.Value2)
    def Division(self):
        print(round(self.Value1/self.Value2, 2))
    
Obj1 = Arithmetic()
Obj2 = Arithmetic()
Obj1.Accept()
Obj1.Addition()
Obj1.Subtraction()
Obj1.Multiplication()
Obj1.Division()
Obj2.Accept()
Obj2.Addition()
Obj2.Subtraction()
Obj2.Multiplication()
Obj2.Division()