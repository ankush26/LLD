# filepath: c:\Users\ankus\Desktop\LLD\LLD\Lecture 05\Python Code\OCP\OCP_violated.py

# This file demonstrates a violation of the Open/Closed Principle (OCP).
# It contains a class that requires modification to add new functionality.

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

# Function to calculate total area of shapes
def calculate_total_area(shapes):
    total_area = 0
    for shape in shapes:
        total_area += shape.area()
    return total_area

# Example usage
shapes = [Rectangle(10, 5), Circle(7)]
print(f"Total area: {calculate_total_area(shapes)}")