class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point(Shape):
    pass


class Circle(Point):
    def __init__(self, a, z, radius):
        self.a = a
        self.z = z
        self.radius = radius

    def contains(self, point):
        center = []
        radius = []
        for i in self.__dict__.values():
            center.append(i)
        for i in point.__dict__.values():
            radius.append(i)
        return (radius[0] - center[0]) ** 2 + (radius[1] - center[1]) ** 2 <= center[2] * center[2]


p = Point(1, 42)
c = Circle(0, 0, 10)
print(c.contains(p))
