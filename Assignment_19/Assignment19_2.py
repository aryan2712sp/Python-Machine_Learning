####################################################################################################
##
##   Program Name : Assignment19_2.py
##   Description  : Multiplication of two numbers using lambda.
##   Function     : Multiply()
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

Multiply = lambda A, B : A * B

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))
    Result = Multiply(Value1, Value2)
    print("Multiplication is :", Result)

if __name__ == "__main__":
    main()
