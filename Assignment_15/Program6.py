####################################################################################################
##
##   Program Name : Program6.py
##   Discription  : Write a lambda function using reduce() to get minimum element.
##   Function     : Minimum()
##   Author       : Aryan Shailendrasingh Pardeshi
##   Date         : 25/01/2026
##
####################################################################################################

from functools import reduce

Minimum = lambda A, B : A if A < B else B

def main():
    Data = [23, 45, 11, 89, 34]
    Result = reduce(Minimum, Data)
    print("Minimum element :", Result)

if __name__ == "__main__":
    main()
