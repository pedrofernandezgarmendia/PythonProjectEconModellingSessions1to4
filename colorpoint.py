from point import Point
import random

class PointException(Exception):
    pass

class ColorPoint(Point):
    def __init__(self, x, y, color):
        # raise an exception if we try to have not a number
        if not isinstance(x, (int, float)):
            raise PointException("x must be an number")
        if not isinstance(y, (int, float)):
            raise PointException("y must be an number")

        super().__init__(x, y) # this replaces the self.x and self.y
        self.color = color

    def __str__(self):
        return f"<{self.color}: {self.x}, {self.y}>"

if __name__ == "__main__":
    p = ColorPoint(1, 2, "red")
    print(p.distance_orig())
    print(p)
    # colors = ["red", "green", "blue", "yellow", "black", "magenta",
    #           "cyan", "white", "burgundy", "periwinkle", "marsala"]
    # color_points = []
    # for i in range(10):
    #     color_points.append(
    #         ColorPoint(random.randint(-10, 10),
    #                    random.randint(-10, 10),
    #                    random.choice(colors)))
    #
    # print(color_points)
    # color_points.sort()
    # print(color_points)