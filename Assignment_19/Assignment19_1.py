####################################################################################################
##
##   Program Name : Assignment19_1.py
##   Description  : Return power of two of given number.
##   Function     : PowerTwo()
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

PowerTwo = lambda No : No * No

def main():
    Value = int(input("Enter number : "))
    Result = PowerTwo(Value)
    print("Result is :", Result)

if __name__ == "__main__":
    main()
