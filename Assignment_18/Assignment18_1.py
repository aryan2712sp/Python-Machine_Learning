####################################################################################################
##
##   Program Name : Assignment18_1.py
##   Description  : Addition of all elements from list.
##   Function     : AddList()
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

def AddList(Data):
    Sum = 0
    for No in Data:
        Sum = Sum + No
    return Sum

def main():
    Size = int(input("Enter number of elements : "))
    Data = []

    print("Enter elements : ")
    for i in range(Size):
        Data.append(int(input()))

    Result = AddList(Data)
    print("Addition is :", Result)

if __name__ == "__main__":
    main()
