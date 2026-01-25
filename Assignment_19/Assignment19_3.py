####################################################################################################
##
##   Program Name : Assignment19_3.py
##   Description  : Filter, map and reduce operations on list.
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

from functools import reduce

def main():
    Data = list(map(int, input("Enter list elements : ").split()))

    FData = list(filter(lambda No : No >= 70 and No <= 90, Data))
    print("List after filter :", FData)

    MData = list(map(lambda No : No + 10, FData))
    print("List after map :", MData)

    RData = reduce(lambda A, B : A * B, MData)
    print("Output of reduce :", RData)

if __name__ == "__main__":
    main()
