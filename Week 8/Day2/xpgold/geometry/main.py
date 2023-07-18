import math

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius**2

    def print_definition(self):
        print("A circle is a closed curve where all points on the curve are equidistant from the center.")

# Example usage
my_circle = Circle(5.0)
print(f"Perimeter: {my_circle.perimeter()}")
print(f"Area: {my_circle.area()}")
my_circle.print_definition()
