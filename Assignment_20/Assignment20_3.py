####################################################################################################
##
##   Program Name : Assignment20_3.py
##   Description  : Extract even and odd elements from list using threads.
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

import threading

def EvenList(Data):
    EvenSum = 0
    print("Even Elements :", end=" ")
    for i in Data:
        if i % 2 == 0:
            print(i, end=" ")
            EvenSum += i
    print("\nSum of Even Elements :", EvenSum)

def OddList(Data):
    OddSum = 0
    print("Odd Elements :", end=" ")
    for i in Data:
        if i % 2 != 0:
            print(i, end=" ")
            OddSum += i
    print("\nSum of Odd Elements :", OddSum)

def main():
    Data = list(map(int, input("Enter list elements : ").split()))

    T1 = threading.Thread(target=EvenList, args=(Data,), name="EvenList")
    T2 = threading.Thread(target=OddList, args=(Data,), name="OddList")

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()
