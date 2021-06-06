class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point(Shape):
    pass


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def contains(self, clazz):
        center = []
        radius = []
        for i in self.__dict__.values():
            center.append(i)
        for i in clazz.__dict__.values():
            radius.append(i)
        if (radius[0] - center[0]) ** 2 + (radius[1] - center[1]) ** 2 <= center[2] * center[2]:
            return True
        else:
            return False


p = Point(1, 42)
c = Circle(0, 0, 10)
print(c.contains(p))
