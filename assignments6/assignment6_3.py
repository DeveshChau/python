import math
class Arithmetic:
    ROI = 10.5
    def __init__(self, value):
        self.Value = value
    def ChkPrime(self):
        for i in range(2, math.ceil((self.Value+1)/2)):
            if self.Value%i==0:
                return False
        return True
    def Perfect(self):
        divisors_sum = self.SumFactors()
        print(divisors_sum)
        return divisors_sum == self.Value
    def Factors(self):
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i)
    def SumFactors(self):
        factor = [1]
        for i in range(2,self.Value):
            if self.Value%i==0:
                factor.append(i)
        return sum(factor)
Obj1 = Arithmetic(6)
print(Obj1.ChkPrime())
print(Obj1.Perfect())
Obj1.Factors()
Obj1.SumFactors()