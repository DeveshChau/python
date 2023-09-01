class BankAccount:
    ROI = 10.5
    def __init__(self, name, amount):
        self.Name = name
        self.Amount = amount
    def Deposite(self, amount):
        self.Amount = self.Amount+amount
    def Withdraw(self, amount):
        self.Amount = self.Amount-amount
    def calculateIntrest(self):
        intrest = BankAccount.ROI * (self.Amount/100)
        print(intrest)
    def Display(self):
        print("Name:", self.Name, ", Amount: ", self.Amount)
Obj1 = BankAccount("user1", 5000)
Obj1.Deposite(1000)
Obj1.Withdraw(900)
Obj1.Display()
Obj1.calculateIntrest()