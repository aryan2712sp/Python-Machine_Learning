####################################################################################################
##
##   Program Name : Assignment21_4.py
##   Description  : Calculate sum and product of list elements using threads.
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

import threading
from functools import reduce

SumResult = 0
ProductResult = 1

def SumList(Data):
    global SumResult
    SumResult = sum(Data)

def ProductList(Data):
    global ProductResult
    ProductResult = reduce(lambda a, b: a * b, Data)

def main():
    Data = list(map(int, input("Enter elements : ").split()))

    T1 = threading.Thread(target=SumList, args=(Data,), name="SumThread")
    T2 = threading.Thread(target=ProductList, args=(Data,), name="ProductThread")

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Sum of elements :", SumResult)
    print("Product of elements :", ProductResult)

if __name__ == "__main__":
    main()
