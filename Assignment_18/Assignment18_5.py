####################################################################################################
##
##   Program Name : Assignment18_5.py
##   Description  : Addition of prime numbers from list.
##   Function     : ListPrime()
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

import MarvellousNum

def ListPrime(Data):
    Sum = 0
    for No in Data:
        if MarvellousNum.ChkPrime(No):
            Sum = Sum + No
    return Sum

def main():
    Size = int(input("Enter number of elements : "))
    Data = []

    print("Enter elements : ")
    for i in range(Size):
        Data.append(int(input()))

    Result = ListPrime(Data)
    print("Addition of prime numbers is :", Result)

if __name__ == "__main__":
    main()
