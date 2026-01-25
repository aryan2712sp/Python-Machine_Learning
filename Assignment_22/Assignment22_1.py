####################################################################################################
##
##   Program Name : Assignment22_1.py
##   Description  : Demonstration of class with instance and class variables.
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

class Demo:
    Value = 10

    def __init__(self, No1, No2):
        self.no1 = No1
        self.no2 = No2

    def Fun(self):
        print("Value of no1 :", self.no1)
        print("Value of no2 :", self.no2)

    def Gun(self):
        print("Value of no1 :", self.no1)
        print("Value of no2 :", self.no2)

def main():
    Obj1 = Demo(11, 21)
    Obj2 = Demo(51, 101)

    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()

if __name__ == "__main__":
    main()
