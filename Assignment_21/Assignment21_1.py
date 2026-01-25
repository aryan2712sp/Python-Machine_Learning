####################################################################################################
##
##   Program Name : Assignment21_1.py
##   Description  : Display prime and non-prime numbers using threads.
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

import threading

def ChkPrime(No):
    if No < 2:
        return False
    for i in range(2, int(No / 2) + 1):
        if No % i == 0:
            return False
    return True

def Prime(Data):
    print("Prime Numbers : ", end="")
    for i in Data:
        if ChkPrime(i):
            print(i, end=" ")
    print()

def NonPrime(Data):
    print("Non-Prime Numbers : ", end="")
    for i in Data:
        if not ChkPrime(i):
            print(i, end=" ")
    print()

def main():
    Data = list(map(int, input("Enter elements : ").split()))

    T1 = threading.Thread(target=Prime, args=(Data,), name="Prime")
    T2 = threading.Thread(target=NonPrime, args=(Data,), name="NonPrime")

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()
