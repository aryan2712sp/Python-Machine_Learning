####################################################################################################
##
##   Program Name : Assignment19_4.py
##   Description  : Filter even numbers, square them and add.
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

from functools import reduce

def main():
    Data = list(map(int, input("Enter list elements : ").split()))

    FData = list(filter(lambda No : No % 2 == 0, Data))
    print("List after filter :", FData)

    MData = list(map(lambda No : No * No, FData))
    print("List after map :", MData)

    RData = reduce(lambda A, B : A + B, MData)
    print("Output of reduce :", RData)

if __name__ == "__main__":
    main()
