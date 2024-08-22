n = int(input("Enter the number of integers you want to perform operation on: "))
operation = input("Choose the Operation:\n1 for Addition\n2 for Subtraction\n3 for Multiplication\n4 for Division\n")
if(n == 2):
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))

    if(operation == "4"  and  n2 == 0):
        print("Cannot divide by 0")

    switcher = {
        '1': n1 - (-n2),
        '2': n1 - n2,
        '3': n1 * n2,
        '4': n1 / n2
    }

    result = switcher.get(operation, "Invalid operation")
    print("The result is:", result)

elif(n == 3):
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    n3 = float(input("Enter third number: "))

    if(operation == "4"  and  n2 == 0):
        print("Cannot divide by 0")

    switcher = {
        '1': n1 - (-n2) - (-n3),
        '2': n1 - n2 - n3,
        '3': n1 * n2 * n3,
        '4': (n1 * n3) / n2 
    }
    
    result = switcher.get(operation, "Invalid operation")
    print("The result is:", result)

else:
    print("Invalid Number of integers")