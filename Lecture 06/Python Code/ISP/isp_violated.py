# filepath: c:\Users\ankus\Desktop\LLD\LLD\Lecture 06\Python Code\ISP\isp_violated.py
# Single interface for all shapes (Violates ISP)
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def volume(self):
        raise NotImplementedError("Subclasses must implement this method.")


# Square is a 2D shape but is forced to implement volume()
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def volume(self):
        raise NotImplementedError("Volume not applicable for Square")  # Unnecessary method


# Rectangle is also a 2D shape but is forced to implement volume()
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def volume(self):
        raise NotImplementedError("Volume not applicable for Rectangle")  # Unnecessary method


# Cube is a 3D shape, so it actually has a volume
class Cube(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return 6 * self.side * self.side

    def volume(self):
        return self.side * self.side * self.side
