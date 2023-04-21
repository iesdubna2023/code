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
        x_diff = point.x - self.x
        y_diff = point.y - self.y
        return Point2D(point.x + x_diff, point.y + y_diff)

    def mirror_line(self, point1, point2):
        x_diff = point2.x - point1.x
        y_diff = point2.y - point1.y
        d = x_diff * x_diff + y_diff * y_diff
        if d == 0:
            return Point2D(self.x, self.y)
        u = ((self.x - point1.x) * x_diff + (self.y - point1.y) * y_diff) / d
        return Point2D(point1.x + u * x_diff, point1.y + u * y_diff)

    def belongs_point(self, point):
        return self.x == point.x and self.y == point.y


class Segment2D(Figure2D):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def area(self):
        return 0

    def mirror_point(self, point):
        return Segment2D(self.p1.mirror_point(point),
                         self.p2.mirror_point(point))

    def mirror_line(self, point1, point2):
        return Segment2D(self.p1.mirror_line(point1, point2),
                         self.p2.mirror_line(point1, point2))

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

    def mirror_point(self, point):
        return Triangle2D(self.p1.mirror_point(point),
                          self.p2.mirror_point(point),
                          self.p3.mirror_point(point))

    def mirror_line(self, point1, point2):
        return Triangle2D(self.p1.mirror_line(point1, point2),
                          self.p2.mirror_line(point1, point2),
                          self.p3.mirror_line(point1, point2))

    def belongs_point(self, point):
        x, y = point.x, point.y
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
