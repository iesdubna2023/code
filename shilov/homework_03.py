import math


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

    def belongs_point(self, point_belong):
        return self.x == point_belong.x and self.y == point_belong.y

    def mirror_point(self, pm):
        result_x = 2 * pm.x - self.x
        result_y = 2 * pm.y - self.y
        return Point2D(result_x, result_y)

    def mirror_line(self, segment):
        shiftp_x = self.x - segment.p2.x
        shiftp_y = self.y - segment.p2.y
        shiftb_x = segment.p1.x - segment.p2.x
        shiftb_y = segment.p1.y - segment.p2.y
        if shiftb_x == 0:
            mirror_result = Point2D(-shiftp_x + segment.p2.x,
                                    shiftp_y + segment.p2.y)
        elif shiftb_y == 0:
            mirror_result = Point2D(shiftp_x + segment.p2.x,
                                    -shiftp_y + segment.p2.y)
        else:
            len_AB = math.sqrt((shiftb_x) ** 2 + (shiftb_y) ** 2)
            cos = shiftb_x / len_AB
            sin = shiftb_y / len_AB
            turn_p_x = shiftp_x * cos + shiftp_y * sin
            turn_p_y = -shiftp_x * sin + shiftp_y * cos
            a = complex(turn_p_x, turn_p_y)
            c = a.conjugate()
            x = c.real * cos - c.imag * sin + segment.p2.x
            y = c.real * sin + c.imag * cos + segment.p2.y
            mirror_result = Point2D(x, y)
        return mirror_result


class Segment2D(Figure2D):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def area(self):
        return 0

    def mirror_point(self, pm):
        return Segment2D(self.p1.mirror_point(pm),
                         self.p2.mirror_point(pm))

    def mirror_line(self, pl):
        return Segment2D(self.p1.mirror_line(pl),
                         self.p2.mirror_line(pl))

    def belongs_point(self, pb):
        if ((pb.x - self.p1.x)
            * (self.p2.y - self.p1.y)
            - (self.p2.x - self.p1.x)
            * (pb.y - self.p1.y) == 0
            and (self.p1.x < pb.x < self.p2.x
                 or self.p2.x < pb.x < self.p1.x)):
            return True
        return False


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
        return Triangle2D(self.p1.mirror_point(pm),
                          self.p2.mirror_point(pm),
                          self.p3.mirror_point(pm))

    def mirror_line(self, pl):
        return Triangle2D(self.p1.mirror_line(pl),
                          self.p2.mirror_line(pl),
                          self.p3.mirror_line(pl))

    def belongs_point(self, point):
        triangle = Triangle2D(self.p1, self.p2, self.p3)
        triangle1 = Triangle2D(self.p1, self.p2, point)
        triangle2 = Triangle2D(self.p1, point, self.p3)
        triangle3 = Triangle2D(point, self.p2, self.p3)
        sm = triangle1.area() + triangle2.area() + triangle3.area()
        orig = triangle.area()
        return math.isclose(sm, orig)
