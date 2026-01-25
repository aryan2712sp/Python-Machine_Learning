####################################################################################################
##
##   Program Name : Program4.py
##   Discription  : Write a lambda function using reduce() to add all elements.
##   Function     : Add()
##   Author       : Aryan Shailendrasingh Pardeshi
##   Date         : 25/01/2026
##
####################################################################################################

from functools import reduce

Add = lambda A, B : A + B

def main():
    Data = [10, 20, 30, 40]
    Result = reduce(Add, Data)
    print("Addition is :", Result)

if __name__ == "__main__":
    main()
