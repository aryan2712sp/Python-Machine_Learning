####################################################################################################
##
##   Program Name : Assignment1_8.py
##   Description  : Print "*" given number of times.
##   Function     : Display()
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

def Display(No):
    for i in range(No):
        print("*", end=" ")

def main():
    Value = int(input("Enter number : "))
    Display(Value)

if __name__ == "__main__":
    main()
