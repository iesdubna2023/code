class Figure2D:
    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color


class Point2D(Figure2D):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def area(self):
        return 0

    def mirror_point(self, pm):
        result_x = 2 * pm.x - self.x
        result_y = 2 * pm.y - self.y
        return Point2D(result_x, result_y)

    # y = kx + b
    def mirror_line(self, line):
        p = [self.x, self.y]
        a = line.p1.y - line.p2.y
        b = line.p2.x - line.p1.x
        c = - (a * line.p1.x + b * line.p1.y)
        term1 = b ** 2 - a ** 2
        term12 = -2 * a * b
        term2 = a ** 2 - b ** 2
        return Point2D((term1 * p[0] + term12 * p[1] - 2 * c * a)
                       / (a ** 2 + b ** 2),
                       (term12 * p[0] + term2 * p[1] - 2 * c * b)
                       / (a ** 2 + b ** 2))

    def belongs_point(self, point):
        return self.x == point.x and self.y == point.y


class Segment2D(Figure2D):
    def __init__(self, point_1, point_2):
        self.p1 = point_1
        self.p2 = point_2

    def area(self):
        return 0

    def mirror_point(self, pm):
        return Segment2D(
            self.p1.mirror_point(pm),
            self.p2.mirror_point(pm)
        )

    def mirror_line(self, line):
        return Segment2D(
            self.p1.mirror_line(line),
            self.p2.mirror_line(line)
        )

    def belongs_point(self, pb):
        return ((pb.x - self.p1.x)
                * (self.p2.y - self.p1.y)
                - (self.p2.x - self.p1.x)
                * (pb.y - self.p1.y) == 0
                and (self.p1.x < pb.x < self.p2.x
                     or self.p2.x < pb.x < self.p1.x))


class Triangle2D(Figure2D):
    def __init__(self, point_1, point_2, point_3):
        self.p1 = point_1
        self.p2 = point_2
        self.p3 = point_3

    def area(self):
        return abs(1 / 2 * ((self.p1.x - self.p3.x)
                            * (self.p2.y - self.p3.y)
                            - (self.p2.x - self.p3.x)
                            * (self.p1.y - self.p3.y)))

    def mirror_point(self, pm):
        return Triangle2D(
            self.p1.mirror_point(pm),
            self.p2.mirror_point(pm),
            self.p3.mirror_point(pm)
        )

    def mirror_line(self, line):
        return Triangle2D(
            self.p1.mirror_line(line),
            self.p2.mirror_line(line),
            self.p3.mirror_line(line)
        )

    def belongs_point(self, point):
        a = Triangle2D(self.p1, self.p2, point)
        b = Triangle2D(self.p1, self.p3, point)
        c = Triangle2D(self.p2, self.p3, point)
        return not (a.area() + b.area() + c.area() > self.area())
