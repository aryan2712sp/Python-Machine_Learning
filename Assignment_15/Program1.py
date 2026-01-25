####################################################################################################
##
##   Program Name : Program1.py
##   Discription  : Write a lambda function using map() to return square of each number.
##   Function     : SquareX()
##   Author       : Aryan Shailendrasingh Pardeshi
##   Date         : 25/01/2026
##
####################################################################################################

SquareX = lambda No : No * No

def main():
    Data = [1, 2, 3, 4, 5]
    Result = list(map(SquareX, Data))
    print("Squares :", Result)

if __name__ == "__main__":
    main()
