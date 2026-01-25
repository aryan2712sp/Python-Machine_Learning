####################################################################################################
##
##   Program Name : Assignment2_2.py
##   Description  : Display square star pattern
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

def Display(No):
    for i in range(No):
        for j in range(No):
            print("*", end=" ")
        print()

def main():
    Value = int(input("Enter number : "))
    Display(Value)

if __name__ == "__main__":
    main()
