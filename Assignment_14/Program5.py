####################################################################################################
##
##   Program Name : Program5.py 
##   Discription  : Write a lambda function which accepts one number and returns True if even.
##   Function     : CheckEven()
##   Author       : Aryan Shailendrasingh Pardeshi
##   Date         : 25/01/2026
##
####################################################################################################

CheckEven = lambda No : No % 2 == 0

def main():
    Value = int(input("Enter number : "))
    Ret = CheckEven(Value)
    print("Is number even :", Ret)

if __name__ == "__main__":
    main()
