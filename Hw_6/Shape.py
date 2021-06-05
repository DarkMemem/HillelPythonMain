class Shape:

    def __init__(self, center_x=0, center_y=0):
        self.center_x = center_x
        self.center_y = center_y


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle(Shape, Point):

    def xy(self, center_x, center_y, r, x, y):
        super().__init__(center_x, center_y)
        super().__init__(x, y)

    @property
    def contains(self):
        if (Point.x - Shape.center_x) * (Point.x1 - center_x) + (Point.y - center_y) * (Point.y - center_y) <= r * r:
            return True
        else:
            return False


p = Point(1, 42)

c = Circle(0, 0, 10)
print(c.contains)
