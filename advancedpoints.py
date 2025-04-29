from colorpoint import ColorPoint, PointException
class AdvancedPoint(ColorPoint):
    COLORS = ["red", "blue", "green", "yellow", "black", "white", "periwinkle"]
    def __init__(self, x, y, color):
        if color not in self.COLORS:
            raise TypeError(f"Invalid color, must be one of {self.COLORS}") # ensures that the color is valid
        self._x = x
        self._y = y
        self._color = color

    @property # you can access an attribute like a variable, but behind the scenes, it runs a method
    def x(self):
        return self._x # getter method

    @x.setter
    def x(self, value):
        self._x = value # "setter" method # assigns the new value to _x

    @property
    def y(self): # allows controlled access to the private variable _y
        return self._y

    @property
    def color(self):
        return self._color # keeps _color protected

    @classmethod # To modify class-level data (COLORS in this case)
    def add_color(cls, color):
        """
        Adds a new valid color for our class
        """
        cls.COLORS.append(color) # adds a new color to the COLORS list

    @staticmethod # utility function that doesn’t depend on class or instance
    def from_tuple(coordinate, color="red"):
        """
        Creates a new point from a tuple rather than 2 individual values
        """
        x, y = coordinate
        return AdvancedPoint(x, y, color)

    @staticmethod
    def distance_2_points(p1, p2):
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5 # distance between the two points

    def distance_to_other(self, p):
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5 # distance between current object (self) and p

AdvancedPoint.add_color("blue")
p = AdvancedPoint(1, 2, "blue")
print(p.x) # prints 1 — calls the x getter
print(p) # will print memory address unless __str__ is defined
print(p.distance_orig()) # distance to origin: sqrt(1² + 2²) = √5 ≈ 2.236
p2 = AdvancedPoint.from_tuple((3, 2)) # creates a second point
print(p2)
print(AdvancedPoint.distance_2_points(p, p2)) # measures is the physical distance between point p and point p2
print(p.distance_to_other(p2)) # straight-line distance from point p to point p2