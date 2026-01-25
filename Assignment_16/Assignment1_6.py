####################################################################################################
##
##   Program Name : Assignment1_6.py
##   Description  : Check whether number is Positive, Negative or Zero.
##   Function     : CheckNumber()
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

def CheckNumber(No):
    if No > 0:
        print("Positive Number")
    elif No < 0:
        print("Negative Number")
    else:
        print("Zero")

def main():
    Value = int(input("Enter number : "))
    CheckNumber(Value)

if __name__ == "__main__":
    main()
