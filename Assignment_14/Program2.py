####################################################################################################
##
##   Program Name : Program2.py 
##   Discription  : Write a lambda function which accepts one number and returns cube of that number.
##   Function     : Cube()
##   Author       : Aryan Shailendrasingh Pardeshi
##   Date         : 25/01/2026
##
####################################################################################################

Cube = lambda No : No * No * No

def main():
    Value = int(input("Enter number : "))
    Ret = Cube(Value)
    print("Cube is :", Ret)

if __name__ == "__main__":
    main()
