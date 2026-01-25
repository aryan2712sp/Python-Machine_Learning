####################################################################################################
##
##   Program Name : Assignment2_9.py
##   Description  : Count digits
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

def CountDigits(No):
    Count = 0
    while No > 0:
        Count += 1
        No //= 10
    return Count

def main():
    Value = int(input("Enter number : "))
    Result = CountDigits(Value)
    print("Number of digits :", Result)

if __name__ == "__main__":
    main()
