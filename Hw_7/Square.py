import math


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


class Triangle(Shape):
    def __init__(self, height, weight, x, y):
        super().__init__(x, y)
        self.height = height
        self.weight = weight

    def square(self):

        return self.height * self.weight / 2


class Parallelogram(Shape):
    def __init__(self, x, y, a, b, angle):
        super().__init__(x, y)
        self.angle = angle
        self.a = a
        self.b = b

    def square(self):
        return self.a * self.b * math.sin(math.radians(self.angle))


class Scene:
    def __init__(self):
        self._figures = []

    def add_figure(self, figure):
        self._figures.append(figure)

    def square(self):
        for i in self._figures:
            print(i.square())

    def total_square(self):
        return sum(i.square() for i in self._figures)


p = Point(1, 42)
c = Circle(0, 0, 10)
c.contains(p)
triang = Triangle(0, 0, 3, 4)
paral = Parallelogram(0, 0, 4, 6, 38)
scene = Scene()
scene.add_figure(triang)
scene.add_figure(paral)
scene.square()
print(scene.total_square())
