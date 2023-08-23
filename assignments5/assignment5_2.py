class Circle:
    PI = 3.14
    def __init__(self):
        self.Radius = 0
        self.Area = 0
        self.Circumference = 0
    def Accept(self):
        self.Radius = int(input("Radius of circle: "))
    def CalculateArea(self):
        self.Area = self.Radius*self.Radius*self.PI
    def CalculateCircumference(self):
        self.Circumference = 2*self.PI*self.Radius
    def Display(self):
        print("Radius: ", self.Radius)
        print("Area: ", round(self.Area, 2))
        print("Circumference: ", round(self.Circumference, 2))

Obj1 = Circle()
Obj2 = Circle()
Obj1.Accept()
Obj1.CalculateArea()
Obj1.CalculateCircumference()
Obj1.Display()
Obj2.Accept()
Obj2.CalculateArea()
Obj2.CalculateCircumference()
Obj2.Display()