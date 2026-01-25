####################################################################################################
##
##   Program Name : Assignment23_2.py
##   Description  : Bank account operations using class.
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder Name :", self.Name)
        print("Account Balance :", self.Amount)

    def Deposit(self):
        Value = float(input("Enter amount to deposit : "))
        self.Amount += Value

    def Withdraw(self):
        Value = float(input("Enter amount to withdraw : "))
        if Value <= self.Amount:
            self.Amount -= Value
        else:
            print("Insufficient balance")

    def CalculateInterest(self):
        return (self.Amount * BankAccount.ROI) / 100

def main():
    Obj1 = BankAccount("Aryan", 10000)
    Obj1.Display()
    Obj1.Deposit()
    Obj1.Withdraw()
    Obj1.Display()
    print("Interest :", Obj1.CalculateInterest())
    print("-----------------------------")

    Obj2 = BankAccount("Marvellous", 50000)
    Obj2.Display()
    Obj2.Deposit()
    Obj2.Withdraw()
    Obj2.Display()
    print("Interest :", Obj2.CalculateInterest())

if __name__ == "__main__":
    main()
