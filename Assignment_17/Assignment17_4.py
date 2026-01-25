####################################################################################################
##
##   Program Name : Assignment2_4.py
##   Description  : Addition of factors
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

def SumFactors(No):
    Sum = 0
    for i in range(1, No):
        if No % i == 0:
            Sum = Sum + i
    return Sum

def main():
    Value = int(input("Enter number : "))
    Result = SumFactors(Value)
    print("Addition of factors is :", Result)

if __name__ == "__main__":
    main()
