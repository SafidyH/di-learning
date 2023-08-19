import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Either radius or diameter must be provided.")

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * self.radius**2

    def __str__(self):
        return f"Circle with radius {self.radius}"

    def __repr__(self):
        return f"Circle(radius={self.radius})"

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

# Example usage:
circle1 = Circle(radius=3)
circle2 = Circle(diameter=8)

print(circle1)  # Output: Circle with radius 3
print(circle2)  # Output: Circle with radius 4.0

print(circle1.diameter)  # Output: 6.0
print(circle2.area)      # Output: 50.26548245743669

circle3 = circle1 + circle2
print(circle3)  # Output: Circle with radius 7.0

print(circle1 == circle2)  # Output: False
print(circle1 >= circle3)  # Output: False

circles_list = [circle1, circle2, circle3]
sorted_circles = sorted(circles_list)
print(sorted_circles)  # Output: [Circle(radius=4.0), Circle(radius=6.0), Circle(radius=7.0)]
