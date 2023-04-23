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
        c = (pow(y2 - y1, 2) + pow(x2 - x1, 2))
        if c == 0:
            x = self.x
        else:
            x4 = round((a + b) / c)
            x = x4 + (x4 - x3)
        if (x2 - x1) == 0:
            y = self.y
        else:
            y4 = round((y2 - y1) * (x4 - x1) / (x2 - x1) + y1)
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
        a = (point.x - self.p1.x)
        b = (self.p2.y - self.p1.y)
        c = (self.p2.x - self.p1.x)
        d = (point.y - self.p1.y)
        e = (a * b - c * d) == 0

        f = self.p1.x < point.x < self.p2.x
        g = self.p2.x < point.x < self.p1.x
        return e and (f or g)


class Triangle2D(Figure2D):
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def area(self):
        a = (self.p1.x - self.p3.x)
        b = (self.p2.y - self.p3.y)
        c = (self.p2.x - self.p3.x)
        d = (self.p1.y - self.p3.y)

        return abs(1 / 2 * (a * b - c * d))

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
        # равна площади треугольника, значит эта точка принадлежит ему
        t1 = Triangle2D(self.p1, self.p2, point)
        t2 = Triangle2D(self.p1, self.p3, point)
        t3 = Triangle2D(self.p2, self.p3, point)
        return round(t1.area() + t2.area() + t3.area()) == round(self.area())
