####################################################################################################
##
##   Program Name : Assignment1_3.py
##   Description  : Accept two numbers and return their addition.
##   Function     : Add()
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

def Add(No1, No2):
    return No1 + No2

def main():
    A = int(input("Enter first number : "))
    B = int(input("Enter second number : "))
    Result = Add(A, B)
    print("Addition is :", Result)

if __name__ == "__main__":
    main()
