####################################################################################################
##
##   Program Name : Program3.py
##   Discription  : Write a lambda function using filter() to get odd numbers.
##   Function     : CheckOdd()
##   Author       : Aryan Shailendrasingh Pardeshi
##   Date         : 25/01/2026
##
####################################################################################################

CheckOdd = lambda No : No % 2 != 0

def main():
    Data = [1, 2, 3, 4, 5, 6]
    Result = list(filter(CheckOdd, Data))
    print("Odd numbers :", Result)

if __name__ == "__main__":
    main()
