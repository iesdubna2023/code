from abc import ABCMeta, abstractmethod


class Figure2D:
    __metaclass__ = ABCMeta

    def __repr__(self):
        return f"{self.__class__}"

    @abstractmethod
    def __iter__(self):
        """"Итератор по полям объекта"""

    def _is_uniqueness_points(self, *points):
        """Проверяет точки на уникальность"""
        unique = set(points)
        if len(unique) == len(points):
            return True
        return None

    @abstractmethod
    def area(self):
        """Вычисляет площадь фигуры"""

    @abstractmethod
    def mirror_point(self, point):
        """Отражает фигуру относительно точки"""

    @abstractmethod
    def mirror_line(self, line):
        """Отражает фигуру относительно прямой"""

    @abstractmethod
    def belongs_point(self, point):
        """Проверяет на принадлежность точки к фигуре"""


class Point2D(Figure2D):
    __slots__ = ("x", "y")

    def __init__(self, x: float, y: float):
        super().__init__()
        self.x = x
        self.y = y

    def __iter__(self):
        yield self.x
        yield self.y

    def __repr__(self):
        return f"{self.__class__} {tuple(self.__iter__())}"

    def area(self) -> float:
        return 0

    def mirror_point(self, point) -> "Point2D":
        """Отражает фигуру относительно точки"""
        dx = self.x - point.x
        dy = self.y - point.y
        return Point2D(point.x - dx, point.y - dy)

    def mirror_line(self, line) -> "Point2D":
        """Отражает фигуру относительно прямой"""
        p_0 = [self.x, self.y]
        a = line.p1.y - line.p2.y
        b = line.p2.x - line.p1.x
        c = - (a * line.p1.x + b * line.p1.y)
        term1 = b ** 2 - a ** 2
        term2 = -2 * a * b
        term3 = -2 * a * b
        term4 = a ** 2 - b ** 2
        return Point2D((term1 * p_0[0] + term2 * p_0[1]
                        - 2 * c * a) / (a ** 2 + b ** 2),
                       (term3 * p_0[0] + term4 * p_0[1]
                        - 2 * c * b) / (a ** 2 + b ** 2))

    def belongs_point(self, point) -> bool:
        """Проверяет на принадлежность точки к фигуре"""
        return (self.x, self.y) == tuple(point)


class Segment2D(Figure2D):
    __slots__ = ("p1", "p2")

    def __init__(self, p1: Point2D, p2: Point2D):
        super().__init__()
        if super()._is_uniqueness_points((p1.x, p1.y), (p2.x, p2.y)):
            self.p1 = p1
            self.p2 = p2
        else:
            raise ValueError("Точки совпадают.")

    def __iter__(self):
        yield tuple(self.p1)
        yield tuple(self.p2)

    def __repr__(self):
        return f"{self.__class__} {tuple(self.__iter__())}"

    def area(self) -> float:
        """Вычисляет площадь фигуры"""
        return 0

    def mirror_point(self, point: Point2D) -> "Segment2D":
        """Отражает фигуру относительно точки"""
        ref1 = self.p1.mirror_point(point)
        ref2 = self.p2.mirror_point(point)
        return Segment2D(ref1, ref2)

    def mirror_line(self, line) -> "Segment2D":
        """Отражает фигуру относительно прямой"""
        ref1 = self.p1.mirror_point(line.p1)
        ref2 = self.p2.mirror_point(line.p2)
        return Segment2D(ref1, ref2)

    def belongs_point(self, point: Point2D) -> bool:
        """Проверяет на принадлежность точки к фигуре"""
        m = (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)
        b = self.p1.y - m * self.p1.x
        if abs(point.y - (m * point.x + b)) > 1e-6:
            return False
        dot_product = (point.x - self.p1.x) * \
                      (self.p2.x - self.p1.x) + (point.y - self.p1.y) * \
                      (self.p2.y - self.p1.y)
        if dot_product < 0 or dot_product > (self.p2.x - self.p1.x)**2 \
                + (self.p2.y - self.p1.y)**2:
            return False
        return True


class Triangle2D(Figure2D):
    def __init__(self, p1: Point2D, p2: Point2D, p3: Point2D):
        super().__init__()
        if self._is_triangle(p1, p2, p3):
            self.p1 = p1
            self.p2 = p2
            self.p3 = p3
        else:
            raise ValueError("Из данных точек невозможно создать треугольник.")

    def __iter__(self):
        yield tuple(self.p1)
        yield tuple(self.p2)
        yield tuple(self.p3)

    def __repr__(self):
        return f"{self.__class__} {tuple(self.__iter__())}"

    def _is_triangle(self, *points) -> bool:
        """Проверяет точки на валидность к треугольнику"""
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        side1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        side2 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
        side3 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
        if side1 + side2 > side3 and \
                side1 + side3 > side2 and \
                side2 + side3 > side1:
            return True
        return False

    def area(self) -> float:
        """Вычисляет площадь фигуры"""
        x1, y1 = self.p1
        x2, y2 = self.p2
        x3, y3 = self.p3
        return abs(x1 * (y2 - y3)
                   + x2 * (y3 - y1)
                   + x3 * (y1 - y2)) / 2.0

    def mirror_point(self, point: Point2D) -> "Triangle2D":
        """Отражает фигуру относительно точки"""
        ref1 = self.p1.mirror_point(point)
        ref2 = self.p2.mirror_point(point)
        ref3 = self.p3.mirror_point(point)
        return Triangle2D(ref1, ref2, ref3)

    def mirror_line(self, line: Segment2D) -> "Triangle2D":
        """Отражает фигуру относительно прямой"""
        ref1 = self.p1.mirror_line(line)
        ref2 = self.p2.mirror_line(line)
        ref3 = self.p3.mirror_line(line)
        return Triangle2D(ref1, ref2, ref3)

    def belongs_point(self, point: Point2D) -> bool:
        """Проверяет на принадлежность точки к фигуре"""
        x, y = point
        x1, y1 = self.p1
        x2, y2 = self.p2
        x3, y3 = self.p3
        alpha = ((y2 - y3) * (x - x3)
                 + (x3 - x2) * (y - y3)) / ((y2 - y3) * (x1 - x3)
                                            + (x3 - x2) * (y1 - y3))
        beta = ((y3 - y1) * (x - x3)
                + (x1 - x3) * (y - y3)) / ((y2 - y3) * (x1 - x3)
                                           + (x3 - x2) * (y1 - y3))
        gamma = 1 - alpha - beta
        return 0 <= alpha <= 1 and 0 <= beta <= 1 and 0 <= gamma <= 1
