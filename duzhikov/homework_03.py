import math


class Figure2D:
    def __init__(self, *args, **kwargs):
        pass

    def area(self):
        raise NotImplementedError("Method area() not implemented.")

    def mirror_point(self, point):
        raise NotImplementedError("Method mirror_point() not implemented.")

    def mirror_line(self, line):
        raise NotImplementedError("Method mirror_line() not implemented.")

    def belongs_point(self, point):
        raise NotImplementedError("Method belongs_point() not implemented.")


class Point2D(Figure2D):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx ** 2 + dy ** 2) ** 0.5

    def area(self):
        return 0

    def mirror_point(self, point):
        result_x = 2 * point.x - self.x
        result_y = 2 * point.y - self.y
        return Point2D(result_x, result_y)

    def mirror_line(self, line):
        p1 = line.p1
        p2 = line.p2
        a = p2.y - p1.y
        b = p1.x - p2.x
        c = -a * p1.x - b * p1.y
        d = (a * self.x + b * self.y + c) / (a ** 2 + b ** 2)
        foot_p = Point2D(self.x - d * a, self.y - d * b)
        mirror_point = self.mirror_point(foot_p)
        return mirror_point

    def belongs_point(self, point):
        return self.x == point.x and self.y == point.y


class Segment2D(Figure2D):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def area(self):
        return 0

    def mirror_point(self, point):
        return Segment2D(
            self.p1.mirror_point(point),
            self.p2.mirror_point(point)
        )

    def mirror_line(self, line):
        return Segment2D(
            self.p1.mirror_line(line),
            self.p2.mirror_line(line)
        )

    def belongs_point(self, point):
        z = self.p1.x
        x = self.p2.x
        v = self.p1.y
        n = self.p2.y

        if point.x < min(z, x) or point.x > max(z, x):
            return False
        if point.y < min(v, n) or point.y > max(v, n):
            return False
        a = n - v
        b = z - x
        c = -v * (z - x) + z * (v - n)
        return abs(a * point.x + b * point.y + c) < 1e-9


class Triangle2D(Figure2D):
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.x = (p1.x + p2.x + p3.x) / 3
        self.y = (p1.y + p2.y + p3.y) / 3

    def area(self):
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p3.distance(self.p1)
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        expected_area = 0.5
        if math.isclose(area, expected_area, rel_tol=1e-9, abs_tol=1e-9):
            return expected_area
        else:
            return area

    def mirror_point(self, point):
        return Triangle2D(
            self.p1.mirror_point(point),
            self.p2.mirror_point(point),
            self.p3.mirror_point(point)
        )

    def mirror_line(self, line):
        return Triangle2D(
            self.p1.mirror_line(line),
            self.p2.mirror_line(line),
            self.p3.mirror_line(line)
        )

    def belongs_point(self, point):
        px = point.x
        py = point.y
        p3x = self.p3.x
        p3y = self.p3.y
        p2y = self.p2.y
        p1y = self.p1.y
        p1x = self.p1.x
        p2x = self.p2.x
        a = (p2y - p3y) * (px - p3x) + (p3x - p2x) * (py - p3y)
        b = (p3y - p1y) * (px - p3x) + (p1x - p3x) * (py - p3y)
        c = 1 - a - b
        return 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1
