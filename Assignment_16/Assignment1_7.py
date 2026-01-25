####################################################################################################
##
##   Program Name : Assignment1_7.py
##   Description  : Check whether number is divisible by 5.
##   Function     : DivisibleByFive()
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

def DivisibleByFive(No):
    return No % 5 == 0

def main():
    Value = int(input("Enter number : "))
    Result = DivisibleByFive(Value)
    print(Result)

if __name__ == "__main__":
    main()
