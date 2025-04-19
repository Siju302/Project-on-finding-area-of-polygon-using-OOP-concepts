# Parent class
class Polygon:
    def __init__(self, perimeter, apothem):
        self.perimeter = perimeter
        self.apothem = apothem

    # Method to get area of polygon 
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

# Object creation
obj = Square(4)

# Calling method display
obj.display()