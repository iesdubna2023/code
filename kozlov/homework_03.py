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
        p1 = segment.p1
        p1 = segment.p2
        if p1.x - p1.x != 0:
            a = (p1.y - p1.y) / (p1.x - p1.x)
            b = (p1.x * p1.y + p1.x * p1.y) / (p1.x - p1.x)
            c = (self.x + (self.y - b) * a) / (1 + a ** 2)
            return Point2D(2 * c - self.x, 2 * c * a - self.y + 2 * b)
        else:
            return Point2D(2 * p1.x - self.x, self.y)

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
