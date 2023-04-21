class Figure2D:
    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color


class Point2D(Figure2D):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):  # площадь фигуры
        return 0

    def mirror_point(self, pm):  # отражение по точке
        result_x = 2 * pm.x - self.x
        result_y = 2 * pm.y - self.y
        return Point2D(result_x, result_y)

    def belongs_point(self, point):  # проверка принадлежности фигуры
        return self.x == point.x and self.y == point.y

    def mirror_line(self, pm):
        # отражение точки относительно прямой
        # можно реализовать с помощью отражения относительно
        # точки, являющейся пересечению прямой и её перпендикуляра,
        # проходящего через исходную точку
        p1 = pm.p1
        p2 = pm.p2
        a = p2.y - p1.y
        b = p1.x - p2.x
        c = -a * p1.x - b * p1.y
        d = (a * self.x + b * self.y + c) / (a ** 2 + b ** 2)
        foot_p = Point2D(self.x - d * a, self.y - d * b)
        mirror_point = self.mirror_point(foot_p)
        return mirror_point


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

    def mirror_point(self, p):
        return Triangle2D(self.p1.mirror_point(p),
                          self.p2.mirror_point(p),
                          self.p3.mirror_point(p)
                          )

    def mirror_line(self, l1):
        return Triangle2D(self.p1.mirror_line(l1),
                          self.p2.mirror_line(l1),
                          self.p3.mirror_line(l1)
                          )

    def belongs_point(self, point):
        a = Triangle2D(self.p1, self.p2, point)
        b = Triangle2D(self.p1, self.p3, point)
        c = Triangle2D(self.p2, self.p3, point)
        return not (a.area() + b.area() + c.area() > self.area())
