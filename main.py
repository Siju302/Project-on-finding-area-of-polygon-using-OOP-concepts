import math

# Parent class
class Polygon:
    def __init__(self, perimeter, apothem):
        self.perimeter = perimeter
        self.apothem = apothem

    def area(self):
        return self.apothem * self.perimeter / 2

    def display(self):
        print("The area of the polygon is", self.area())

# Child class
class Square(Polygon):
    def __init__(self, side):
        self.side = side
        perimeter = 4 * side
        apothem = side / 2
        super().__init__(perimeter, apothem)

# Example usage
obj = Square(4)
obj.display()

# Child class
class Pentagon(Polygon):
    def __init__(self, side):
        self.side = side
        perimeter = 5 * side
        # cot(π/5) = 1 / tan(π/5)
        apothem = (side / 2) / math.tan(math.pi / 5)
        super().__init__(perimeter, apothem)

# Example usage
obj = Pentagon(5)
obj.display()