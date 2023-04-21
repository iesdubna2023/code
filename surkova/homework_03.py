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

    def belongs_point(self, point):
        return self.x == point.x and self.y == point.y

    def normal_to_line(self, line):
        (A, B) = (line.p1, line.p2)
        x = ((A.x ** 2) * self.x
             - 2 * A.x * B.x * self.x
             + (B.x ** 2) * self.x
             + B.x * (A.y - B.y) * (A.y - self.y)
             - A.x * (A.y - B.y) * (B.y - self.y)
             ) / ((A.x - B.x)**2 + (A.y - B.y)**2)
        y = ((B.x ** 2) * A.y
             + (A.x ** 2) * B.y
             + B.x * self.x * (B.y - A.y)
             - A.x * (self.x * (B.y - A.y) + B.x * (B.y + A.y))
             + ((A.y - B.y) ** 2) * self.y
             ) / ((A.x - B.x)**2 + (A.y - B.y)**2)
        return Point2D(x, y)

    def mirror_line(self, line):
        (A, B) = (line.p1, line.p2)
        parall = Segment2D(self.mirror_point(A),
                           self.mirror_point(B))
        return self.normal_to_line(parall)


class Segment2D(Figure2D):
    def __init__(self, point_1, point_2):
        self.p1 = point_1
        self.p2 = point_2

    def area(self):
        return 0

    def mirror_point(self, pm):
        point_1_prime = self.p1.mirror_point(pm)
        point_2_prime = self.p2.mirror_point(pm)
        return Segment2D(point_1_prime, point_2_prime)

    def belongs_point(self, pm):
        ifa = 0 <= (pm.x - self.p1.x) * self.p2.x \
            <= (self.p1.x - self.p2.x) ** 2
        ifb = 0 <= (pm.y - self.p1.y) * self.p2.y \
            <= (self.p1.y - self.p2.y) ** 2
        ifc = (pm.x - self.p1.x) * (self.p2.y - self.p1.y) \
            - (self.p2.x - self.p1.x) * (pm.y - self.p1.y) == 0
        return ifa and ifb and ifc

    def mirror_line(self, line):
        return Segment2D(self.p1.mirror_line(line),
                         self.p2.mirror_line(line))


class Triangle2D(Figure2D):
    def __init__(self, point_1, point_2, point_3):
        self.p1 = point_1
        self.p2 = point_2
        self.p3 = point_3

    def area(self):
        ab = ((self.p1.x - self.p2.x) ** 2
              + (self.p1.y - self.p2.y) ** 2) ** 0.5
        ac = ((self.p1.x - self.p3.x) ** 2
              + (self.p1.y - self.p3.y) ** 2) ** 0.5
        bc = ((self.p2.x - self.p3.x) ** 2
              + (self.p2.y - self.p3.y) ** 2) ** 0.5
        p = (ab + ac + bc) / 2
        return round((p * (p - ab) * (p - ac) * (p - bc)) ** 0.5, 10)

    def mirror_point(self, pm):
        point_1_prime = self.p1.mirror_point(pm)
        point_2_prime = self.p2.mirror_point(pm)
        point_3_prime = self.p3.mirror_point(pm)
        return Triangle2D(point_1_prime, point_2_prime, point_3_prime)

    def belongs_point(self, pm):
        a = (self.p1.x - pm.x) * (self.p2.y - self.p1.y) \
            - (self.p2.x - self.p1.x) * (self.p1.y - pm.y)
        b = (self.p2.x - pm.x) * (self.p3.y - self.p2.y) \
            - (self.p3.x - self.p2.x) * (self.p2.y - pm.y)
        c = (self.p3.x - pm.x) * (self.p1.y - self.p3.y) \
            - (self.p1.x - self.p3.x) * (self.p3.y - pm.y)
        return (a <= 0 and b <= 0 and c <= 0) or (a > 0 and b > 0 and c > 0)

    def mirror_line(self, line):
        return Triangle2D(self.p1.mirror_line(line),
                          self.p2.mirror_line(line),
                          self.p3.mirror_line(line))
