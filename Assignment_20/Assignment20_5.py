####################################################################################################
##
##   Program Name : Assignment20_5.py
##   Description  : Thread synchronization using join().
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

import threading

def Thread1():
    for i in range(1, 51):
        print("Thread1 :", i)

def Thread2():
    for i in range(50, 0, -1):
        print("Thread2 :", i)

def main():
    T1 = threading.Thread(target=Thread1, name="Thread1")
    T2 = threading.Thread(target=Thread2, name="Thread2")

    T1.start()
    T1.join()     # Thread2 waits until Thread1 completes

    T2.start()
    T2.join()

if __name__ == "__main__":
    main()
