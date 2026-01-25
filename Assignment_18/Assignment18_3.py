####################################################################################################
##
##   Program Name : Assignment18_3.py
##   Description  : Find minimum number from list.
##   Function     : Minimum()
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

def Minimum(Data):
    Min = Data[0]
    for No in Data:
        if No < Min:
            Min = No
    return Min

def main():
    Size = int(input("Enter number of elements : "))
    Data = []

    print("Enter elements : ")
    for i in range(Size):
        Data.append(int(input()))

    Result = Minimum(Data)
    print("Minimum number is :", Result)

if __name__ == "__main__":
    main()
