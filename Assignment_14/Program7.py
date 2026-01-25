####################################################################################################
##
##   Program Name : Program7.py
##   Discription  : Write a lambda function which accepts one number and returns True if divisible by 5.
##   Function     : DivisibleByFive()
##   Author       : Aryan Shailendrasingh Pardeshi
##   Date         : 25/01/2026
##
####################################################################################################

DivisibleByFive = lambda No : No % 5 == 0

def main():
    Value = int(input("Enter number : "))
    Ret = DivisibleByFive(Value)
    print("Divisible by 5 :", Ret)

if __name__ == "__main__":
    main()
