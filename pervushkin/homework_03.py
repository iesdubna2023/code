import math


class Figure2D:
    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color


class Point2D(Figure2D):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return "x = {1}, y = {0}".format(self.x, self.y)

    def area(self):
        return 0

    def mirror_point(self, pm):
        result_x = 2 * pm.x - self.x
        result_y = 2 * pm.y - self.y
        return Point2D(result_x, result_y)

    def mirror_line(self, line):
        n = Point2D(0, 0)
        n.x = (line.p1.x - line.p2.x)
        n.y = (line.p1.y - line.p2.y)
        length = math.sqrt(n.x * n.x + n.y * n.y)
        n.x /= length
        n.y /= length
        dot2 = 2 * (n.x * self.x + n.y * self.y)
        return Point2D(self.x - dot2 * n.x, self.y - dot2 * n.y)

    def belongs_point(self, point):
        return self.x == point.x and self.y == point.y


class Segment2D(Figure2D):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def area(self):
        return 0

    def mirror_point(self, pm):
        return Segment2D(self.p1.mirror_point(pm),
                         self.p2.mirror_point(pm))

    def mirror_line(self, line):
        return Segment2D(self.p1.mirror_line(line),
                         self.p2.mirror_line(line))

    def belongs_point(self, point):
        if self.len() == 0:
            return 0
        return (abs(self.p2.x - self.p1.x)
                >= abs(self.p2.x - point.x)
                + abs(self.p1.x - point.x)) \
            and (abs(self.p2.y - self.p1.y)
                 >= abs(self.p2.y - point.y)
                 + abs(self.p1.y - point.y))

    def len(self):
        return ((self.p1.x - self.p2.x) ** 2
                + (self.p1.y - self.p2.y) ** 2) ** 0.5


class Triangle2D(Figure2D):
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def area(self):
        a = Segment2D(self.p1, self.p2).len()
        b = Segment2D(self.p1, self.p3).len()
        c = Segment2D(self.p2, self.p3).len()
        if (a < b + c) and (b < a + c) and (c < a + b):
            p = (a + b + c) / 2
            return round((p * (p - a) * (p - b) * (p - c)) ** 0.5, 10)
        return 0

    def mirror_point(self, pm):
        return Triangle2D(self.p1.mirror_point(pm),
                          self.p2.mirror_point(pm),
                          self.p3.mirror_point(pm))

    def mirror_line(self, line):
        return Triangle2D(self.p1.mirror_line(line),
                          self.p2.mirror_line(line),
                          self.p3.mirror_line(line))

    def belongs_point(self, point):
        t = Triangle2D(self.p1, self.p2, point)
        t1 = Triangle2D(self.p1, self.p3, point)
        t2 = Triangle2D(self.p2, self.p3, point)
        return (t.area() + t1.area() + t2.area()) <= self.area()
