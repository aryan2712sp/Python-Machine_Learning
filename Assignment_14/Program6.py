####################################################################################################
##
##   Program Name : Program6.py
##   Discription  : Write a lambda function which accepts one number and returns True if odd.
##   Function     : CheckOdd()
##   Author       : Aryan Shailendrasingh Pardeshi
##   Date         : 25/01/2026
##
####################################################################################################

CheckOdd = lambda No : No % 2 != 0

def main():
    Value = int(input("Enter number : "))
    Ret = CheckOdd(Value)
    print("Is number odd :", Ret)

if __name__ == "__main__":
    main()
