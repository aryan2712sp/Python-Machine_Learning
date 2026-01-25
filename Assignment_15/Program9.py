####################################################################################################
##
##   Program Name : Program9.py
##   Discription  : Write a lambda function using reduce() to get product of all elements.
##   Function     : Multiply()
##   Author       : Aryan Shailendrasingh Pardeshi
##   Date         : 25/01/2026
##
####################################################################################################

from functools import reduce

Multiply = lambda A, B : A * B

def main():
    Data = [1, 2, 3, 4]
    Result = reduce(Multiply, Data)
    print("Product is :", Result)

if __name__ == "__main__":
    main()
