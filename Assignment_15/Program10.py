####################################################################################################
##
##   Program Name : Program10.py
##   Discription  : Write a lambda function using filter() to count even numbers.
##   Function     : CheckEven()
##   Author       : Aryan Shailendrasingh Pardeshi
##   Date         : 25/01/2026
##
####################################################################################################

CheckEven = lambda No : No % 2 == 0

def main():
    Data = [1, 2, 3, 4, 5, 6, 8]
    Result = len(list(filter(CheckEven, Data)))
    print("Count of even numbers :", Result)

if __name__ == "__main__":
    main()
