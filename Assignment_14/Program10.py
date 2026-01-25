####################################################################################################
##
##   Program Name : Program10.py
##   Discription  : Write a lambda function which accepts three numbers and returns largest number.
##   Function     : Maximum()
##   Author       : Aryan Shailendrasingh Pardeshi
##   Date         : 25/01/2026
##
####################################################################################################

Maximum = lambda No1, No2, No3 : No1 if (No1 >= No2 and No1 >= No3) else (No2 if No2 >= No3 else No3)

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))
    Value3 = int(input("Enter third number : "))
    Ret = Maximum(Value1, Value2, Value3)
    print("Largest number is :", Ret)

if __name__ == "__main__":
    main()
