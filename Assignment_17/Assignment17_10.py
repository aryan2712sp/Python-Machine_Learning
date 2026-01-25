####################################################################################################
##
##   Program Name : Assignment2_10.py
##   Description  : Addition of digits
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

def SumDigits(No):
    Sum = 0
    while No > 0:
        Sum = Sum + (No % 10)
        No //= 10
    return Sum

def main():
    Value = int(input("Enter number : "))
    Result = SumDigits(Value)
    print("Addition of digits :", Result)

if __name__ == "__main__":
    main()
