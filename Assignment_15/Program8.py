####################################################################################################
##
##   Program Name : Program8.py
##   Discription  : Write a lambda function using filter() to get numbers divisible by 3 and 5.
##   Function     : Divisible()
##   Author       : Aryan Shailendrasingh Pardeshi
##   Date         : 25/01/2026
##
####################################################################################################

Divisible = lambda No : (No % 3 == 0) and (No % 5 == 0)

def main():
    Data = [10, 15, 30, 45, 20]
    Result = list(filter(Divisible, Data))
    print("Divisible by 3 and 5 :", Result)

if __name__ == "__main__":
    main()
