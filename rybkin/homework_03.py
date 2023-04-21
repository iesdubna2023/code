from typing import Tuple
import math


class FigureError(Exception):
    """Исключение для обработки ошибок в Figure2D"""
    def __init__(self, message):
        super().__init__(message)


class Figure2D:
    __slots__ = ("__max_points", "__points")

    def __init__(self, *points: Tuple[float, float], max_points=0):
        self.__max_points = max_points
        self.__points = self._correct_points(points)

    def __repr__(self):
        return f"{self.__class__} {self.figure_points}"

    def __eq__(self, other):
        """Оператор сравнения фигур"""
        return self.figure_points == other.figure_points

    @property
    def figure_points(self):
        """Возвращает точки фигуры"""
        return self.__points

    @figure_points.setter
    def figure_points(self, *points):
        """Устанавливает точки фигуры"""
        self.__points = self._correct_points(*points)

    def _correct_points(self, *points):
        """Возвращает точки, если они проходят проверку"""
        if self._is_uniqueness_points(*points):
            if len(*points) == self.__max_points:
                return list(*points)
#            raise FigureError(f"Данная фигура не
    #            поддерживает {len(*points)} точек.")

    def _is_uniqueness_points(self, points):
        """Проверяет точки на уникальность"""
        unique = set(points)
        if len(unique) == len(points):
            return True
#        raise FigureError("Некоторые точки фигуры совпадают.")

    def area(self):
        """Вычисляет площадь фигуры"""
#        raise FigureError("Данный метод должен быть переопределён.")

    def mirror_point(self, point: Tuple[float, float]):
        """Отражает фигуру относительно точки"""
#        raise FigureError("Данный метод должен быть переопределён.")

    def mirror_line(self,
                    line: Tuple[Tuple[float, float], Tuple[float, float]]):
        """Отражает фигуру относительно прямой"""
#        raise FigureError("Данный метод должен быть переопределён.")

    def belongs_point(self, point: Tuple[float, float]):
        """Проверяет на принадлежность точки к фигуре"""
#       raise FigureError("Данный метод должен быть переопределён.")


class Point2D(Figure2D):
    def __init__(self, *points: Tuple[float, float]):
        super().__init__(*points, max_points=1)

    def __repr__(self):
        return f"{self.__class__} {self.figure_points}"

    def area(self) -> float:
        return 0

    def mirror_point(self, point: Tuple[float, float]) -> "Point2D":
        """Отражает фигуру относительно точки"""
        dx = self.figure_points[0][0] - point[0]
        dy = self.figure_points[0][1] - point[1]
        return Point2D((point[0] - dx, point[1] - dy))

    def mirror_line(self,
                    line: Tuple[Tuple[float, float], Tuple[float, float]]) \
            -> "Point2D":
        """Отражает фигуру относительно прямой"""
        direction_vector = Point2D((line[1][0] - line[0][0],
                                   line[1][1] - line[0][1]))
        point_vector = Point2D((self.figure_points[0][0]
                                - line[0][0],
                                self.figure_points[0][1] - line[0][1]))

        projection = (point_vector.figure_points[0][0]
                      * direction_vector.figure_points[0][1] +
                      point_vector.figure_points[0][1]
                      * direction_vector.figure_points[0][1]) / \
                     (direction_vector.figure_points[0][0] ** 2
                      + direction_vector.figure_points[0][1] ** 2)

        reflected_vector = Point2D((2 * projection
                                    * direction_vector.figure_points[0][0]
                                    - point_vector.figure_points[0][0],
                                   2 * projection
                                    * direction_vector.figure_points[0][1]
                                    - point_vector.figure_points[0][1]))

        reflected_x = line[0][0] + reflected_vector.figure_points[0][0]
        reflected_y = line[0][1] + reflected_vector.figure_points[0][1]

        return Point2D((reflected_x, reflected_y))

    def belongs_point(self, point: Tuple[float, float]) -> bool:
        """Проверяет на принадлежность точки к фигуре"""
        return self.figure_points[0] == point


class Segment2D(Figure2D):
    def __init__(self, *points: Tuple[float, float]):
        super().__init__(*points, max_points=2)

    def __repr__(self):
        return f"{self.__class__} - класс для 2D отрезка. {self.figure_points}"

    def area(self) -> float:
        """Вычисляет площадь фигуры"""
        return 0

    def mirror_point(self, point: Tuple[float, float]) -> "Segment2D":
        """Отражает фигуру относительно точки"""
        x0, y0 = point
        x1, y1 = self.figure_points[0]
        x2, y2 = self.figure_points[1]
        v1 = (x1 - x0, y1 - y0)
        v2 = (-v1[1], v1[0])
        new_x1, new_y1 = x1 + 2 * v2[0], y1 + 2 * v2[1]
        new_x2, new_y2 = x2 + 2 * v2[0], y2 + 2 * v2[1]
        return Segment2D((new_x1, new_y1), (new_x2, new_y2))

    def mirror_line(self,
                    line: Tuple[Tuple[float, float], Tuple[float, float]]) \
            -> "Segment2D":
        """Отражает фигуру относительно прямой"""
        x1, y1 = line[0]
        x2, y2 = line[1]
        a = y2 - y1
        b = x1 - x2
        c = x2 * y1 - x1 * y2
        x3, y3 = self.figure_points[0]
        x4, y4 = self.figure_points[1]
        xm = (x3 + x4) / 2
        ym = (y3 + y4) / 2
        if a == 0:
            x = xm
            y = y3
        elif b == 0:
            x = x3
            y = ym
        else:
            k = -a / b
            d = ym - k * xm
            x = (d - c / a) / (a / b + b / a)
            y = k * x + d
        x1p = x1 - 2 * ((a * x + b * y + c) / (a**2 + b**2)) * a
        y2p = y2 - 2 * ((a * x + b * y + c) / (a**2 + b**2)) * b
        x3p = x3 - 2 * ((a * x + b * y + c) / (a**2 + b**2)) * a
        y3p = y3 - 2 * ((a * x + b * y + c) / (a**2 + b**2)) * b
        return Segment2D((x1p, y2p), (x3p, y3p))

    def belongs_point(self, point: Tuple[float, float]) -> bool:
        """Проверяет на принадлежность точки к фигуре"""
        x1, y1 = self.figure_points[0]
        x2, y2 = self.figure_points[1]
        x0, y0 = point
        if x1 == x2:
            return min(y1, y2) <= y0 <= max(y1, y2)
        else:
            a = y1 - y2
            b = x2 - x1
            c = x1 * y2 - x2 * y1
            return abs(a * x0 + b * y0 + c) < 1e-6


class Triangle2D(Figure2D):
    def __init__(self, *points: Tuple[float, float]):
        super().__init__(*points, max_points=3)
        if not self._is_triangle(*points):
            raise FigureError("Из данных точек невозможно создать треугольник.")

    def __repr__(self):
        return f"{self.__class__} {self.figure_points}"

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
        x1, y1 = self.figure_points[0]
        x2, y2 = self.figure_points[1]
        x3, y3 = self.figure_points[2]
        return abs(x1 * (y2 - y3)
                   + x2 * (y3 - y1)
                   + x3 * (y1 - y2)) / 2.0

    def mirror_point(self, point: Tuple[float, float]) -> "Triangle2D":
        """Отражает фигуру относительно точки"""
        x, y = point
        new_p1 = (2 * x - self.figure_points[0][0], 2 * y
                  - self.figure_points[0][1])
        new_p2 = (2 * x - self.figure_points[1][0], 2 * y
                  - self.figure_points[1][1])
        new_p3 = (2 * x - self.figure_points[2][0], 2 * y
                  - self.figure_points[2][1])
        return Triangle2D(new_p1, new_p2, new_p3)

    def mirror_line(self,
                    line: Tuple[Tuple[float, float], Tuple[float, float]]) \
            -> "Triangle2D":
        """Отражает фигуру относительно прямой"""
        x1, y1 = line[0]
        x2, y2 = line[1]
        dx, dy = x2 - x1, y2 - y1
        length = math.sqrt(dx ** 2 + dy ** 2)
        nx, ny = -dy / length, dx / length
        proj_p1 = (self.figure_points[0][0] * nx
                   + self.figure_points[0][1] * ny
                   - x1 * nx - y1 * ny) * nx + x1, \
            (self.figure_points[0][0] * nx
             + self.figure_points[0][1] * ny
             - x1 * nx - y1 * ny) * ny + y1
        proj_p2 = (self.figure_points[1][0] * nx
                   + self.figure_points[1][1] * ny
                   - x1 * nx - y1 * ny) * nx + x1, \
            (self.figure_points[1][0] * nx
             + self.figure_points[1][1] * ny
             - x1 * nx - y1 * ny) * ny + y1
        proj_p3 = (self.figure_points[2][0] * nx
                   + self.figure_points[2][1] * ny
                   - x1 * nx - y1 * ny) * nx + x1, \
            (self.figure_points[2][0] * nx
             + self.figure_points[2][1] * ny
             - x1 * nx - y1 * ny) * ny + y1
        refl_p1 = (self.figure_points[0][0]
                   - 2 * (proj_p1[0] - x1), self.figure_points[0][1]
                   - 2 * (proj_p1[1] - y1))
        refl_p2 = (self.figure_points[1][0]
                   - 2 * (proj_p2[0] - x1), self.figure_points[1][1]
                   - 2 * (proj_p2[1] - y1))
        refl_p3 = (self.figure_points[2][0]
                   - 2 * (proj_p3[0] - x1), self.figure_points[2][1]
                   - 2 * (proj_p3[1] - y1))
        return Triangle2D(refl_p1, refl_p2, refl_p3)

    def belongs_point(self, point: Tuple[float, float]) -> bool:
        """Проверяет на принадлежность точки к фигуре"""
        x, y = point
        x1, y1 = self.figure_points[0]
        x2, y2 = self.figure_points[1]
        x3, y3 = self.figure_points[2]
        alpha = ((y2 - y3) * (x - x3)
                 + (x3 - x2) * (y - y3)) / ((y2 - y3) * (x1 - x3)
                                            + (x3 - x2) * (y1 - y3))
        beta = ((y3 - y1) * (x - x3)
                + (x1 - x3) * (y - y3)) / ((y2 - y3) * (x1 - x3)
                                           + (x3 - x2) * (y1 - y3))
        gamma = 1 - alpha - beta
        return 0 <= alpha <= 1 and 0 <= beta <= 1 and 0 <= gamma <= 1
