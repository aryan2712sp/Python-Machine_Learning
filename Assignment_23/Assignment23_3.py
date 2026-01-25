####################################################################################################
##
##   Program Name : Assignment23_3.py
##   Description  : Number operations using class.
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

class Numbers:
    def __init__(self):
        self.Value = int(input("Enter number : "))

    def ChkPrime(self):
        if self.Value < 2:
            return False
        for i in range(2, int(self.Value / 2) + 1):
            if self.Value % i == 0:
                return False
        return True

    def Factors(self):
        print("Factors are :", end=" ")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        Sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                Sum += i
        return Sum

    def ChkPerfect(self):
        return self.SumFactors() == self.Value

def main():
    Obj1 = Numbers()
    Obj1.Factors()
    print("Is Prime :", Obj1.ChkPrime())
    print("Is Perfect :", Obj1.ChkPerfect())
    print("-----------------------------")

    Obj2 = Numbers()
    Obj2.Factors()
    print("Is Prime :", Obj2.ChkPrime())
    print("Is Perfect :", Obj2.ChkPerfect())

if __name__ == "__main__":
    main()
