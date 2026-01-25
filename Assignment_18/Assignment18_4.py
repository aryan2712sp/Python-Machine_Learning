####################################################################################################
##
##   Program Name : Assignment18_4.py
##   Description  : Find frequency of number from list.
##   Function     : Frequency()
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

def Frequency(Data, No):
    Count = 0
    for i in Data:
        if i == No:
            Count += 1
    return Count

def main():
    Size = int(input("Enter number of elements : "))
    Data = []

    print("Enter elements : ")
    for i in range(Size):
        Data.append(int(input()))

    Value = int(input("Enter element to search : "))
    Result = Frequency(Data, Value)
    print("Frequency is :", Result)

if __name__ == "__main__":
    main()
