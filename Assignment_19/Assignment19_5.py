####################################################################################################
##
##   Program Name : Assignment19_5.py
##   Description  : Filter prime numbers, map multiply by 2 and find maximum.
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

from functools import reduce

def ChkPrime(No):
    if No <= 1:
        return False
    for i in range(2, No):
        if No % i == 0:
            return False
    return True

def main():
    Data = list(map(int, input("Enter list elements : ").split()))

    FData = list(filter(ChkPrime, Data))
    print("List after filter :", FData)

    MData = list(map(lambda No : No * 2, FData))
    print("List after map :", MData)

    RData = reduce(lambda A, B : A if A > B else B, MData)
    print("Output of reduce :", RData)

if __name__ == "__main__":
    main()
