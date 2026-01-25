####################################################################################################
##
##   Program Name : Assignment1_10.py
##   Description  : Display length of entered name.
##   Function     : NameLength()
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

def NameLength(Name):
    return len(Name)

def main():
    Value = input("Enter name : ")
    Result = NameLength(Value)
    print("Length of name is :", Result)

if __name__ == "__main__":
    main()
