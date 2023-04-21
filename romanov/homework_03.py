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
        p_1 = mirror_line.p1
        p_2 = mirror_line.p2
        if p_2.x - p_1.x != 0:
            k = (p_2.y - p_1.y) / (p_2.x - p_1.x)
            b = (p_2.x * p_1.y + p_1.x * p_2.y) / (p_2.x - p_1.x)
            d = (self.x + (self.y - b) * k) / (1 + k ** 2)
            return Point2D(2 * d - self.x, 2 * d * k - self.y + 2 * b)
        else:
            return Point2D(2 * p_1.x - self.x, self.y)


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
        if ((belong_point.x - self.p1.x)
                * (self.p2.y - self.p1.y)
                - (self.p2.x - self.p1.x)
                * (belong_point.y - self.p1.y) == 0
                and (self.p1.x < belong_point.x < self.p2.x
                     or self.p2.x < belong_point.x < self.p1.x)):
            return True
        return False


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

    def mirror_line(self, point_1):
        return Triangle2D(self.p1.mirror_point(point_1),
                          self.p2.mirror_point(point_1),
                          self.p3.mirror_point(point_1))

    def belongs_point(self, point):
        triangle = Triangle2D(self.p1, self.p2, self.p3)
        triangle1 = Triangle2D(self.p1, self.p2, point)
        triangle2 = Triangle2D(self.p1, point, self.p3)
        triangle3 = Triangle2D(point, self.p2, self.p3)
        sm = triangle1.area() + triangle2.area() + triangle3.area()
        orig = triangle.area()
        return math.isclose(sm, orig)
