####################################################################################################
##
##   Program Name : Assignment21_3.py
##   Description  : Demonstrate shared variable update using Lock.
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

import threading

Counter = 0
Lock = threading.Lock()

def Increment():
    global Counter
    for i in range(100000):
        Lock.acquire()
        Counter += 1
        Lock.release()

def main():
    T1 = threading.Thread(target=Increment)
    T2 = threading.Thread(target=Increment)
    T3 = threading.Thread(target=Increment)

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

    print("Final Counter Value :", Counter)

if __name__ == "__main__":
    main()
