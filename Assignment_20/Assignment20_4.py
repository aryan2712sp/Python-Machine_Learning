####################################################################################################
##
##   Program Name : Assignment20_4.py
##   Description  : Count small, capital letters and digits using threads.
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

import threading

def Small(Str):
    Count = sum(1 for ch in Str if ch.islower())
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Small letters :", Count)

def Capital(Str):
    Count = sum(1 for ch in Str if ch.isupper())
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Capital letters :", Count)

def Digits(Str):
    Count = sum(1 for ch in Str if ch.isdigit())
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Digits :", Count)

def main():
    Str = input("Enter string : ")

    T1 = threading.Thread(target=Small, args=(Str,), name="Small")
    T2 = threading.Thread(target=Capital, args=(Str,), name="Capital")
    T3 = threading.Thread(target=Digits, args=(Str,), name="Digits")

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

if __name__ == "__main__":
    main()
