# abstrack
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    pass


class Circle(Shape):
    pass


ali = Shape()
print(ali.area())
