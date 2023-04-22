import math


class Figure2D:
    def __init__(self):
        pass

    def area(self):
        return 0


class Point2D(Figure2D):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mirror_point(self, point):
        x = 2 * point.x - self.x
        y = 2 * point.y - self.y
        return Point2D(x, y)

    def mirror_line(self, segment):
        x1, y1 = segment.p1.x, segment.p1.y
        x2, y2 = segment.p2.x, segment.p2.y
        x3, y3 = self.x, self.y
        a = (x2 - x1) * (y2 - y1) * (y3 - y1)
        b = x1 * pow(y2 - y1, 2) + x3 * pow(x2 - x1, 2)
        x4 = round((a + b) / (pow(y2 - y1, 2) + pow(x2 - x1, 2)))
        y4 = round((y2 - y1) * (x4 - x1) / (x2 - x1) + y1)
        x = x4 + (x4 - x3)
        y = y4 + (y4 - y3)
        return Point2D(x, y)

    def belongs_point(self, figure):
        x, y = figure.x, figure.y
        return self.x == x and self.y == y


class Segment2D(Figure2D):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def mirror_point(self, point):
        p1 = self.p1.mirror_point(point)
        p2 = self.p2.mirror_point(point)
        return Segment2D(p1, p2)

    def mirror_line(self, segment):
        p1 = self.p1.mirror_line(segment)
        p2 = self.p2.mirror_line(segment)
        return Segment2D(p1, p2)

    def belongs_point(self, point):
        x, y = point.x, point.y
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y

        answer = (x1 == x2 and x1 == x and min(y1, y2) <= y <= max(y1, y2))
        if not answer:
            z = y1 == y2 and y1 == y
            v = min(x1, x2) <= x <= max(x1, x2)
            answer = (z and v)
        if not answer:
            a = y1 - y2
            b = x2 - x1
            c = x1 * y2 - x2 * y1
            answer = (a * x + b * y + c == 0)
        return answer


class Triangle2D(Figure2D):
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def area(self):
        a = math.sqrt((self.p2.x - self.p1.x) ** 2
                      + (self.p2.y - self.p1.y) ** 2)
        b = math.sqrt((self.p3.x - self.p2.x) ** 2
                      + (self.p3.y - self.p2.y) ** 2)
        c = math.sqrt((self.p1.x - self.p3.x) ** 2
                      + (self.p1.y - self.p3.y) ** 2)
        p = (a + b + c) / 2
        S = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return round(S)

    def mirror_point(self, point):
        p1 = self.p1.mirror_point(point)
        p2 = self.p2.mirror_point(point)
        p3 = self.p3.mirror_point(point)
        return Triangle2D(p1, p2, p3)

    def mirror_line(self, segment):
        p1 = self.p1.mirror_line(segment)
        p2 = self.p2.mirror_line(segment)
        p3 = self.p3.mirror_line(segment)
        return Triangle2D(p1, p2, p3)

    def belongs_point(self, point):
        # Если сумма площадей треугольников с новой точкой
        # равно площади треугольника, значит эта точка принадлежит ему
        t1 = Triangle2D(self.p1, self.p2, point)
        t2 = Triangle2D(self.p1, self.p3, point)
        t3 = Triangle2D(self.p2, self.p3, point)
        return not (t1.area() + t2.area() + t3.area() > self.area())
