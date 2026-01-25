####################################################################################################
##
##   Program Name : Program1.py 
##   Discription  : Write a lambda function which accepts one number and returns square of that number.
##   Function     : Square()
##   Author       : Aryan Shailendrasingh Pardeshi
##   Date         : 25/01/2026
##
####################################################################################################

def Square(No):
    return No * No

def main():
    Value = int(input("Enter number : "))
    Ret = Square(Value)
    print("Square is :", Ret)

if __name__ == "__main__":
    main()
