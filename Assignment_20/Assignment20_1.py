####################################################################################################
##
##   Program Name : Assignment20_1.py
##   Description  : Display first 10 even and odd numbers using threads.
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

import threading

def Even():
    for i in range(2, 21, 2):
        print("Even :", i)

def Odd():
    for i in range(1, 20, 2):
        print("Odd  :", i)

def main():
    T1 = threading.Thread(target=Even, name="Even")
    T2 = threading.Thread(target=Odd, name="Odd")

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()
