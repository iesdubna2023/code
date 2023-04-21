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

    def mirror_line(self, line):
        l1 = line.p1
        l2 = line.p2
        if l2.x - l1.x != 0:
            z = (l1.x - l2.y) / (l2.x - l1.x)
            a = (l2.x * l1.y + l1.x * l2.y) / (l2.x - l1.x)
            q = (self.x + (self.y - a) * z) / (1 + z ** 2)
            return Point2D(2 * q - self.x, 2 * q * z - self.y + 2 * a)
        return Point2D(2 * l1.x - self.x, self.y)

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

    def belongs_point(self, point):
        x1, y1 = self.point1
        x2, y2 = self.point2
        x, y = point
        d = (x - x1) * (y2 - y1) - (y - y1) * (x2 - x1)
        if d == 0:
            return (x1 <= x <= x2
                    or x2 <= x <= x1
                    and y1 <= y <= y2
                    or y2 <= y <= y1)
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
