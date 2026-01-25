####################################################################################################
##
##   Program Name : Program4.py 
##   Discription  : Write a lambda function which accepts two numbers and returns minimum number.
##   Function     : Minimum()
##   Author       : Aryan Shailendrasingh Pardeshi
##   Date         : 25/01/2026
##
####################################################################################################

Minimum = lambda No1, No2 : No1 if No1 < No2 else No2

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))
    Ret = Minimum(Value1, Value2)
    print("Minimum number is :", Ret)

if __name__ == "__main__":
    main()
