####################################################################################################
##
##   Program Name : Assignment21_2.py
##   Description  : Find maximum and minimum element from list using threads.
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

import threading

def Maximum(Data):
    print("Maximum element :", max(Data))

def Minimum(Data):
    print("Minimum element :", min(Data))

def main():
    Data = list(map(int, input("Enter elements : ").split()))

    T1 = threading.Thread(target=Maximum, args=(Data,), name="Maximum")
    T2 = threading.Thread(target=Minimum, args=(Data,), name="Minimum")

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()
