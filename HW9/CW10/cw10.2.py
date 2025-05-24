from math import pi


class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

    def __lt__(self, other):
        return self.area() < other.area()


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length**2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius**2)


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


def main():

    square = Square(4)
    circle = Circle(3)
    triangle = Triangle(5, 6)

    shapes = [square, circle, triangle]

    print("Before sorting:")
    for shape in shapes:
        print(f"{shape.__class__.__name__}: Area = {shape.area()}")

    shapes.sort()

    print("\nAfter sorting:")
    for shape in shapes:
        print(f"{shape.__class__.__name__}: Area = {shape.area()}")


if __name__ == "__main__":
    main()
