n = int(input("Enter a Number: "))
def Factorial(n):
    if(n == 0  or  n == 1):
        return 1
    else:
        return (n * Factorial(n-1))

print("The factorial of", n, "is", Factorial(n))
