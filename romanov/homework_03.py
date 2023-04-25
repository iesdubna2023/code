import math


class Figure2D:
    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color


class Point2D(Figure2D):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return 0

    def belongs_point(self, belong_point):
        return self.x == belong_point.x and self.y == belong_point.y

    def mirror_point(self, mirror_point):
        result_x = 2 * mirror_point.x - self.x
        result_y = 2 * mirror_point.y - self.y
        return Point2D(result_x, result_y)

    def mirror_line(self, mirror_line):
        p = [self.x, self.y]
        a = mirror_line.p1.y - mirror_line.p2.y
        b = mirror_line.p2.x - mirror_line.p1.x
        c = - (a * mirror_line.p1.x + b * mirror_line.p1.y)
        term1 = b ** 2 - a ** 2
        term12 = -2 * a * b
        term2 = a ** 2 - b ** 2
        return Point2D((term1 * p[0] + term12 * p[1] - 2 * c * a)
                       / (a ** 2 + b ** 2),
                       (term12 * p[0] + term2 * p[1] - 2 * c * b)
                       / (a ** 2 + b ** 2))


class Segment2D(Figure2D):
    def __init__(self, point_1, point_2):
        self.p1 = point_1
        self.p2 = point_2

    def area(self):
        return 0

    def mirror_point(self, mirror_point):
        point_1_prime = self.p1.mirror_point(mirror_point)
        point_2_prime = self.p2.mirror_point(mirror_point)
        return Segment2D(point_1_prime, point_2_prime)

    def mirror_line(self, mirror_line):
        return Segment2D(self.p1.mirror_line(mirror_line),
                         self.p2.mirror_line(mirror_line))

    def belongs_point(self, belong_point):
        return ((belong_point.x - self.p1.x)
                * (self.p2.y - self.p1.y)
                - (self.p2.x - self.p1.x)
                * (belong_point.y - self.p1.y) == 0
                and (self.p1.x < belong_point.x < self.p2.x
                     or self.p2.x < belong_point.x < self.p1.x))


class Triangle2D(Figure2D):
    def __init__(self, point_1, point_2, point_3):
        self.p1 = point_1
        self.p2 = point_2
        self.p3 = point_3

    def area(self):
        return abs(1 / 2 * ((self.p1.x - self.p3.x)
                            * (self.p2.y - self.p3.y)
                            - (self.p2.x - self.p3.x)
                            * (self.p1.y - self.p3.y)))

    def mirror_point(self, mirror_point):
        return Triangle2D(self.p1.mirror_point(mirror_point),
                          self.p2.mirror_point(mirror_point),
                          self.p3.mirror_point(mirror_point))

    def mirror_line(self, segment):
        return Triangle2D(self.p1.mirror_line(segment),
                          self.p2.mirror_line(segment),
                          self.p3.mirror_line(segment))

    def belongs_point(self, point):
        triangle1 = Triangle2D(self.p1, self.p2, point)
        triangle2 = Triangle2D(self.p1, point, self.p3)
        triangle3 = Triangle2D(point, self.p2, self.p3)
        sm = triangle1.area() + triangle2.area() + triangle3.area()
        orig = self.area()
        return math.isclose(sm, orig)
