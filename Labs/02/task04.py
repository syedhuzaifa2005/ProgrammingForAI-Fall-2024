def employee(name, salary = 10000):
    taxrate = 0.02
    salaryaftertax = salary * (1 - taxrate)
    print(f"Name of the Employtee is : {name}")
    print(f"Salary of the employee after taxation is: pkr{salaryaftertax}")

employee("huzaifa", 79000)
employee("haris")