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

    def area(self):
        return 0.0

    def mirror_point(self, point):
        return Point2D(2 * point.x - self.x, 2 * point.y - self.y)

    def mirror_line(self, line):
        pass

    def belongs_point(self, point):
        return self.x == point.x and self.y == point.y


class Segment2D(Figure2D):
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def area(self):
        return 0.0

    def mirror_point(self, point):
        return Segment2D(
            self.start_point.mirror_point(point),
            self.end_point.mirror_point(point)
        )

    def mirror_line(self, p1, p2):
        m = (p2.y - p1.y) / (p2.x - p1.x)
        b = p1.y - m * p1.x
        c = self.start_point.x
        d = self.start_point.y
        e = self.end_point.x
        f = self.end_point.y
        start_x = (c + (2 * m * (d - b))) / (1 + m ** 2)
        start_y = (2 * m * start_x) + (2 * b) - d
        end_x = (e + (2 * m * (f - b))) / (1 + m ** 2)
        end_y = (2 * m * end_x) + (2 * b) - f

        return Segment2D(Point2D(start_x, start_y), Point2D(end_x, end_y))

    def belongs_point(self, point):
        if point.x < min(self.start_point.x, self.end_point.x) or point.x > max(self.start_point.x, self.end_point.x):
            return False
        if point.y < min(self.start_point.y, self.end_point.y) or point.y > max(self.start_point.y, self.end_point.y):
            return False
        a = self.end_point.y - self.start_point.y
        b = self.start_point.x - self.end_point.x
        c = -self.start_point.y * (self.start_point.x - self.end_point.x) + self.start_point.x * (
                    self.start_point.y - self.end_point.y)
        return abs(a * point.x + b * point.y + c) < 1e-9


class Triangle2D(Figure2D):
    def init(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def area(self):
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p3.distance(self.p1)
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    def mirror_point(self, p):
        return Triangle2D(self.p1.mirror_point(p), self.p2.mirror_point(p),
                          self.p3.mirror_point(p))

    def mirror_line(self, line):
        return Triangle2D(self.p1.mirror_line(line), self.p2.mirror_line(line),
                          self.p3.mirror_line(line))

    def belongs_point(self, p):
        a = (self.p2.y - self.p3.y) * (p.x - self.p3.x) + (self.p3.x - self.p2.x) * (
                p.y - self.p3.y)
        b = (self.p3.y - self.p1.y) * (p.x - self.p3.x) + (self.p1.x - self.p3.x) * (
                p.y - self.p3.y)
        c = 1 - a - b
        return 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1
