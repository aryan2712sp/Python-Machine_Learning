#################################################################################################
#
#   Program Name : Program3.py (Assignment_11)
#   Description  : Write a program which accepts one number from user and prints sum of digits
#   Function     : SumDigits()
#   Author       : Aryan Shailendrasingh Pardeshi
#   Date         : 22/01/2026
#
##################################################################################################

#    Input  : 7521
#    Output : 15

def SumDigits(No):
    Sum = 0
    Digit = 0

    while No > 0:
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    return Sum


def main():
    Value = 0
    Ret = 0

    print("Enter the number : ")
    Value = int(input())

    Ret = SumDigits(Value)

    print("Sum of digits in", Value, "is", Ret)


if __name__ == "__main__":
    main()
