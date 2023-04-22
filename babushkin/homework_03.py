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

    def mirror_point(self, p):
        p_x = p.x - self.x
        p_y = p.y - self.y
        return Point2D(p.x + p_x, p.y + p_y)

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

    def belongs_point(self, p):
        return self.x == p.x and self.y == p.y


class Segment2D(Figure2D):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def area(self):
        return 0

    def mirror_point(self, p):
        return Segment2D(self.p1.mirror_point(p),
                         self.p2.mirror_point(p))

    def mirror_line(self, p1):
        return Segment2D(self.p1.mirror_line(p1),
                         self.p2.mirror_line(p1))

    def belongs_point(self, pb):
        return ((pb.x - self.p1.x)
                * (self.p2.y - self.p1.y)
                - (self.p2.x - self.p1.x)
                * (pb.y - self.p1.y) == 0
                and (self.p1.x < pb.x < self.p2.x
                     or self.p2.x < pb.x < self.p1.x))


class Triangle2D(Figure2D):
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def area(self):
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y
        x3, y3 = self.p3.x, self.p3.y
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)

    def mirror_point(self, p):
        return Triangle2D(self.p1.mirror_point(p),
                          self.p2.mirror_point(p),
                          self.p3.mirror_point(p))

    def mirror_line(self, p1):
        return Triangle2D(self.p1.mirror_line(p1),
                          self.p2.mirror_line(p1),
                          self.p3.mirror_line(p1))

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
