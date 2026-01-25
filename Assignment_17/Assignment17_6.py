####################################################################################################
##
##   Program Name : Assignment2_6.py
##   Description  : Reverse star pattern
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

def Display(No):
    for i in range(No, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

def main():
    Value = int(input("Enter number : "))
    Display(Value)

if __name__ == "__main__":
    main()
