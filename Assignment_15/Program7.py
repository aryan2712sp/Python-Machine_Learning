####################################################################################################
##
##   Program Name : Program7.py
##   Discription  : Write a lambda function using filter() to get strings with length > 5.
##   Function     : CheckLength()
##   Author       : Aryan Shailendrasingh Pardeshi
##   Date         : 25/01/2026
##
####################################################################################################

CheckLength = lambda Str : len(Str) > 5

def main():
    Data = ["Python", "Java", "Angular", "C", "JavaScript"]
    Result = list(filter(CheckLength, Data))
    print("Filtered strings :", Result)

if __name__ == "__main__":
    main()
