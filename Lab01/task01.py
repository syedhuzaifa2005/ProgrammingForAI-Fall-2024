mass = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
BMI = mass / (height ** 2)
print("Your BMI is:", round(BMI, 3), "kg/m²")