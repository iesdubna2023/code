import math


class Figure2D:
    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color


class Point2D(Figure2D):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def area(self):
        return 0

    def mirror_point(self, pm):
        result_x = 2 * pm.x - self.x
        result_y = 2 * pm.y - self.y
        return Point2D(result_x, result_y)

    # y = kx + b
    def mirror_line(self, line):
        n = Point2D(0, 0)
        n.x = (line.point_1.x - line.point_2.x)
        n.y = (line.point_1.y - line.point_2.y)
        length = math.sqrt(n.x * n.x + n.y * n.y)
        n.x /= length
        n.y /= length
        dot2 = 2 * (n.x * self.x + n.y * self.y)
        return Point2D(self.x - dot2 * n.x, self.y - dot2 * n.y)

    def belongs_point(self, point):
        return self.x == point.x and self.y == point.y


class Segment2D(Figure2D):
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    @property
    def area(self):
        return 0

    def mirror_point(self, pm):
        return Segment2D(self.point_1.mirror_point(pm),
                         self.point_2.mirror_point(pm))

    def mirror_line(self, line):
        return Segment2D(self.point_1.mirror_line(line),
                         self.point_2.mirror_line(line))

    def belongs_point(self, point):
        if self.len() == 0:
            return 0
        return (abs(self.point_2.x - self.point_1.x) >=
                abs(self.point_2.x-point.x) + abs(self.point_1.x - point.x)) \
            and (abs(self.point_2.y - self.point_1.y) >=
                 abs(self.point_2.y - point.y) + abs(self.point_1.y - point.y))

    def len(self):
        return ((self.point_1.x - self.point_2.x) ** 2 +
                (self.point_1.y - self.point_2.y) ** 2) ** 0.5


class Triangle2D(Figure2D):
    def __init__(self, point_1, point_2, point_3):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3

    def area(self):
        a = Segment2D(self.point_1, self.point_2).len()
        b = Segment2D(self.point_1, self.point_3).len()
        c = Segment2D(self.point_2, self.point_3).len()
        if (a < b + c) and (b < a + c) and (c < a + b):
            p = (a + b + c) / 2
            return (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return 0

    def mirror_point(self, pm):
        return Triangle2D(self.point_1.mirror_point(pm),
                          self.point_2.mirror_point(pm),
                          self.point_3.mirror_point(pm))

    def mirror_line(self, line):
        return Triangle2D(self.point_1.mirror_line(line),
                          self.point_2.mirror_line(line),
                          self.point_3.mirror_line(line))

    def belongs_point(self, point):
        t = Triangle2D(self.point_1, self.point_2, point)
        t1 = Triangle2D(self.point_1, self.point_3, point)
        t2 = Triangle2D(self.point_2, self.point_3, point)
        return not (t.area() + t1.area() + t2.area() > self.area())
