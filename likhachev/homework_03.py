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

    def mirror_line(self, p1, p2):
        a = p2.y - p1.y
        b = p1.x - p2.x
        c = -p1.x * (p2.y - p1.y) + p1.y * (p2.x - p1.x)
        x = self.x - 2 * a * (a * self.x + b * self.y + c) / (a ** 2 + b ** 2)
        y = self.y - 2 * b * (a * self.x + b * self.y + c) / (a ** 2 + b ** 2)
        return Point2D(x, y)

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

    def mirror_line(self, p1, p2):
        p1 = self.p1.mirror_line(p1, p2)
        p2 = self.p2.mirror_line(p1, p2)
        return Segment2D(p1, p2)

    def belongs_point(self, point):
        x1, y1 = self._start_point
        x2, y2 = self._end_point
        x, y = point
        d = (x - x1) * (y2 - y1) - (y - y1) * (x2 - x1)
        if d == 0:
            return x1 <= x <= x2 or x2 <= x <= x1 and y1 <= y <= y2 or y2 <= y <= y1
        return False


class Triangle2D(Figure2D):
    def init(self, p1, p2, p3):
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3

    def area(self):
        a = self._p1.distance_to(self._p2)
        b = self._p2.distance_to(self._p3)
        c = self._p3.distance_to(self._p1)
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5

    def mirror_point(self, point):
        mp1 = self._p1.mirror_point(point)
        mp2 = self._p2.mirror_point(point)
        mp3 = self._p3.mirror_point(point)
        return Triangle2D(mp1, mp2, mp3)

    def mirror_line(self, line):
        ml1 = self._p1.mirror_line(line)
        ml2 = self._p2.mirror_line(line)
        ml3 = self._p3.mirror_line(line)
        return Triangle2D(ml1, ml2, ml3)

    def belongs_point(self, point):
        v1 = self._p1.vector_to(self._p2)
        v2 = self._p1.vector_to(self._p3)
        v3 = self._p1.vector_to(point)
        if (v1.cross(v2) > 0) == (v1.cross(v3) > 0) == (v2.cross(v3) > 0):
            return True
        return False
