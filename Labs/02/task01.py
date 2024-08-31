def trapezoid_area(a, b, h):
    return h * (a + b) / 2

def parallelogram_area(a, b):
    return a * b

def cylinder_properties(r, h):
    pi = 3.14
    surface_area = 2 * pi * r * (r + h)
    volume = pi * (r ** 2) * h
    return f"The surface area of the cylinder is {surface_area}\nThe volume of the cylinder is {volume}"

print("The area of trapezoid is", trapezoid_area(3, 5, 5))
print("The area of parallelogram is", parallelogram_area(7, 3))
print(cylinder_properties(3, 4))
