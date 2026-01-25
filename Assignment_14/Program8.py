####################################################################################################
##
##   Program Name : Program8.py
##   Discription  : Write a lambda function which accepts two numbers and returns addition.
##   Function     : Addition()
##   Author       : Aryan Shailendrasingh Pardeshi
##   Date         : 25/01/2026
##
####################################################################################################

Addition = lambda No1, No2 : No1 + No2

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))
    Ret = Addition(Value1, Value2)
    print("Addition is :", Ret)

if __name__ == "__main__":
    main()
