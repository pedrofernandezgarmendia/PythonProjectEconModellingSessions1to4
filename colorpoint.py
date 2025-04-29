from point import Point
import random

class PointException(Exception): # in case something went wrong
    pass # doesn't add any extra functionality

class ColorPoint(Point):
    def __init__(self, x, y, color):
        # raise an exception if we try to have not a number
        if not isinstance(x, (int, float)):
            raise PointException("x must be an number")
        if not isinstance(y, (int, float)):
            raise PointException("y must be an number")
# ensure data integrity by preventing the creation of a ColorPoint with non-numeric coordinates

        super().__init__(x, y) # this replaces the self.x and self.y
        self.color = color # set the values

    def __str__(self): # method to control how the point is printed
        return f"<{self.color}: {self.x}, {self.y}>"

if __name__ == "__main__": # code inside this block only runs when the script is executed directly, not when it’s imported as a module
    p = ColorPoint(1, 2, "red")
    print(p.distance_orig()) #calculates the distance origin
    print(p) # string representation of the object
    # colors = ["red", "green", "blue", "yellow", "black", "magenta",
    #           "cyan", "white", "burgundy", "periwinkle", "marsala"]
    # color_points = []
    # for i in range(10):
    # color_points.append(
    # ColorPoint(random.randint(-10, 10),
    # random.randint(-10, 10), # used for generating random numbers within a range (a-c)
    # random.choice(colors))) # random element from a list
    #
    # print(color_points)
    # color_points.sort() # sort the points
    # print(color_points)

    # append is to add an element to the end of a list