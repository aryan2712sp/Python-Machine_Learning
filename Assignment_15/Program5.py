####################################################################################################
##
##   Program Name : Program5.py
##   Discription  : Write a lambda function using reduce() to get maximum element.
##   Function     : Maximum()
##   Author       : Aryan Shailendrasingh Pardeshi
##   Date         : 25/01/2026
##
####################################################################################################

from functools import reduce

Maximum = lambda A, B : A if A > B else B

def main():
    Data = [23, 45, 11, 89, 34]
    Result = reduce(Maximum, Data)
    print("Maximum element :", Result)

if __name__ == "__main__":
    main()
