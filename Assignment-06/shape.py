from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


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
        return math.pi * self.radius ** 2


if __name__ == "__main__":
    # Cannot instantiate abstract class
    try:
        shape = Shape()
    except TypeError as e:
        print(f"Error when creating Shape: {e}")
    
    # Create rectangle
    rectangle = Rectangle(5, 3)
    print(f"Rectangle area: {rectangle.area()}")
    
    # Create circle
    circle = Circle(4)
    print(f"Circle area: {circle.area():.2f}")
