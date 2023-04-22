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

    def mirror_point(self, point):
        x = 2 * point.x - self.x
        y = 2 * point.y - self.y
        return Point2D(x, y)

    def mirror_line(self, pm):
        p1 = pm.p1
        p2 = pm.p2
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
        p1 = self.p1.mirror_point(point)
        p2 = self.p2.mirror_point(point)
        return Segment2D(p1, p2)

    def mirror_line(self, line):
        return Segment2D(
            self.p1.mirror_line(line),
            self.p2.mirror_line(line)
        )

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
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def area(self):
        ab = ((self.p1.x - self.p2.x) ** 2
              + (self.p1.y - self.p2.y) ** 2) ** 0.5
        ac = ((self.p1.x - self.p3.x) ** 2
              + (self.p1.y - self.p3.y) ** 2) ** 0.5
        bc = ((self.p2.x - self.p3.x) ** 2
              + (self.p2.y - self.p3.y) ** 2) ** 0.5
        p = (ab + ac + bc) / 2
        return round((p * (p - ab) * (p - ac) * (p - bc)) ** 0.5, 10)

    def mirror_point(self, pointm):
        return Triangle2D(self.p1.mirror_point(pointm),
                          self.p2.mirror_point(pointm),
                          self.p3.mirror_point(pointm))

    def mirror_line(self, mline):
        return Triangle2D(self.p1.mirror_line(mline),
                          self.p2.mirror_line(mline),
                          self.p3.mirror_line(mline))

    def belongs_point(self, p):
        x, y = p.x, p.y
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y
        x3, y3 = self.p3.x, self.p3.y
        a = ((y2 - y3) * (x - x3)
             + (x3 - x2) * (y - y3)) / ((y2 - y3) * (x1 - x3)
                                        + (x3 - x2) * (y1 - y3))
        b = ((y3 - y1) * (x - x3)
             + (x1 - x3) * (y - y3)) / ((y2 - y3) * (x1 - x3)
                                        + (x3 - x2) * (y1 - y3))
        c = 1 - a - b
        return 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1
