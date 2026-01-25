####################################################################################################
##
##   Program Name : Assignment1_2.py
##   Description  : Check whether number is Even or Odd.
##   Function     : ChkNum()
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

def ChkNum(No):
    if No % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

def main():
    Value = int(input("Enter number : "))
    ChkNum(Value)

if __name__ == "__main__":
    main()
