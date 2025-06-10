class TwoDimensionalShape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")

class ThreeDimensionalShape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")
    
    def volume(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Square(TwoDimensionalShape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Rectangle(TwoDimensionalShape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Cube(ThreeDimensionalShape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return 6 * self.side * self.side

    def volume(self):
        return self.side * self.side * self.side

def main():
    square = Square(4)
    rectangle = Rectangle(5, 3)
    cube = Cube(2)

    print(f"Area of Square: {square.area()}")
    print(f"Area of Rectangle: {rectangle.area()}")
    print(f"Area of Cube: {cube.area()}")
    print(f"Volume of Cube: {cube.volume()}")

if __name__ == "__main__":
    main()