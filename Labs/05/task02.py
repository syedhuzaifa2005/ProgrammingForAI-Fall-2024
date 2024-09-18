class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

rectangle = Rectangle(10, 5)
triangle = Triangle(10, 5)
square = Square(7)

print(f"Area of the rectangle: {rectangle.area()}")
print(f"Area of the triangle: {triangle.area()}")
print(f"Area of the square: {square.area()}")
