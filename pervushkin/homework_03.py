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

    def mirror_line(self, line):
        p1 = line.point_1
        p2 = line.point_2
        k = (p2.y - p1.y) / (p2.x - p1.x)
        b = (p2.x * p1.y + p1.x * p2.y) / (p2.x - p1.x)
        d = (self.x + (self.y - b) * k) / (1 + k ** 2)
        return Point2D(2 * d - self.x, 2 * d * k - self.y + 2 * b)

    def belongs_point(self, point):
        return self.x == point.x and self.y == point.y


class Segment2D(Figure2D):
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def area(self):
        return 0

    def mirror_point(self, pm):
        return Segment2D(self.point_1.mirror_point(pm), self.point_2.mirror_point(pm))

    def mirror_line(self, line):
        return Segment2D(self.point_1.mirror_line(line), self.point_2.mirror_line(line))

    def belongs_point(self, point):
        if self.len() == 0:
            return 0
        else:
            line_check = (point.x - self.point_1.x)/(self.point_2.x - self.point_1.x) == \
                         (point.y - self.point_1.y)/(self.point_2.y - self.point_1.y)
            if line_check == 0:
                return 0
            else:
                if self.point_1.x != self.point_2.x:
                    if self.point_1.x > self.point_2.x:
                        return self.point_2.x < point.x < self.point_1.x
                    else:
                        return self.point_1.x < point.x < self.point_2.x
                else:
                    if self.point_1.y > self.point_2.y:
                        return self.point_2.y < point.y < self.point_1.y
                    else:
                        return self.point_1.y < point.y < self.point_2.y

    def len(self):
        return ((self.point_1.x - self.point_2.x) ** 2 +
                (self.point_1.y - self.point_2.y) ** 2) ** 0.5


class Triangle2D(Figure2D):
    def __init__(self, point_1, point_2, point_3):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3

    def area(self):
        a = Segment2D(self.point_1, self.point_2).len()
        b = Segment2D(self.point_1, self.point_3).len()
        c = Segment2D(self.point_2, self.point_3).len()
        if a < b + c and b < a + c and c < a + b:
            p = (a + b + c) / 2
            return (p * (p - a) * (p - b) * (p - c)) ** 0.5
        else:
            return 0

    def mirror_point(self, pm):
        return Triangle2D(self.point_1.mirror_point(pm), self.point_2.mirror_point(pm),
                          self.point_3.mirror_point(pm))

    def mirror_line(self, line):
        return Triangle2D(self.point_1.mirror_line(line), self.point_2.mirror_line(line),
                          self.point_3.mirror_line(line))

    def belongs_point(self, point):
        a = Triangle2D(self.point_1, self.point_2, point)
        b = Triangle2D(self.point_1, self.point_3, point)
        c = Triangle2D(self.point_2, self.point_3, point)
        return not (a.area() + b.area() + c.area() > self.area())
