####################################################################################################
##
##   Program Name : Assignment2_1.py
##   Description  : Use Arithmetic module
##   Author       : Aryan Shailendrasingh Pardeshi
##
####################################################################################################

import Arithmetic

def main():
    A = int(input("Enter first number : "))
    B = int(input("Enter second number : "))

    print("Addition :", Arithmetic.Add(A, B))
    print("Subtraction :", Arithmetic.Sub(A, B))
    print("Multiplication :", Arithmetic.Mult(A, B))
    print("Division :", Arithmetic.Div(A, B))

if __name__ == "__main__":
    main()
