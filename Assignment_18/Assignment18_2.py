####################################################################################################
##
##   Program Name : Assignment18_2.py
##   Description  : Find maximum number from list.
##   Function     : Maximum()
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

def Maximum(Data):
    Max = Data[0]
    for No in Data:
        if No > Max:
            Max = No
    return Max

def main():
    Size = int(input("Enter number of elements : "))
    Data = []

    print("Enter elements : ")
    for i in range(Size):
        Data.append(int(input()))

    Result = Maximum(Data)
    print("Maximum number is :", Result)

if __name__ == "__main__":
    main()
