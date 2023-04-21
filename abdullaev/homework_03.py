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

    def mirror_point(self, pm):
        result_x = 2 * pm.x - self.x
        result_y = 2 * pm.y - self.y
        return Point2D(result_x, result_y)

    def belongs_point(self, point):
        return self.x == point.x and self.y == point.y
    
    def mirror_line(self, line):
        p1 = line.p1
        p2 = line.p2
        if p2.x - p1.x != 0:
            k = (p2.y - p1.y) / (p2.x - p1.x)
            b = (p2.x * p1.y + p1.x * p2.y) / (p2.x - p1.x)
            d = (self.x + (self.y - b) * k) / (1 + k ** 2)
            return Point2D(2 * d - self.x, 2 * d * k - self.y + 2 * b)
        else:
            return Point2D(2 * p1.x - self.x, self.y)


class Segment2D(Figure2D):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def area(self):
        return 0

    def mirror_point(self, pm):
        return Segment2D(self.p1.mirror_point(pm), self.p2.mirror_point(pm))

    def mirror_line(self, line):
        return Segment2D(self.p1.mirror_line(line), self.p2.mirror_line(line))

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
        return abs(1 / 2 * ((self.p1.x - self.p3.x)
                            * (self.p2.y - self.p3.y)
                            - (self.p2.x - self.p3.x)
                            * (self.p1.y - self.p3.y)))

    def mirror_point(self, pm):
        return Triangle2D(self.p1.mirror_point(pm), self.p2.mirror_point(pm), self.p3.mirror_point(pm))

    def mirror_line(self, line):
        return Triangle2D(self.p1.mirror_line(line), self.p2.mirror_line(line), self.p3.mirror_line(line))

    def belongs_point(self, point):
        a = Triangle2D(self.p1, self.p2, point)
        b = Triangle2D(self.p1, self.p3, point)
        c = Triangle2D(self.p2, self.p3, point)
        return not (a.area() + b.area() + c.area() > self.area())