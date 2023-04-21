import math


class Figure2D:
    def __init__(self, array):
        self.points = array

    def area(self):
        if int(len(self.points)) <= 2:
            return 0
        elif int(len(self.points)) == 3:
            a = math.sqrt((self.points[1][0] - self.points[0][0])**2
                          + (self.points[1][1] - self.points[0][1])**2)
            b = math.sqrt((self.points[2][0] - self.points[1][0])**2
                          + (self.points[2][1] - self.points[1][1])**2)
            c = math.sqrt((self.points[0][0] - self.points[2][0])**2
                          + (self.points[0][1] - self.points[2][1])**2)
            p = (a + b + c) / 2
            S = math.sqrt(p * (p - a) * (p - b) * (p - c))
            return S
        else:
            return "Ошибка!!!"

    def mirror_point(self, figure):
        # проверка, что переданная фигура является объектом класса точки
        if (isinstance(figure, Point2D)):
            x1, y1 = figure.points[0][0], figure.points[0][1]
        # проверка, что переданная фигура является набором координат
        elif (isinstance(figure, (tuple, list))) and len(figure) == 2:
            x1, y1 = figure[0], figure[1]
        else:
            print("Передана не точка!")
            return
        for i in range(0, len(self.points)):
            self.points[i][0] = x1 - (self.points[i][0] - x1)
            self.points[i][1] = y1 - (self.points[i][1] - y1)

    def mirror_line(self, figure):
        # проверка, что переданная фигура является объектом класса отрезок
        if (isinstance(figure, Segment2D)):
            x1, y1, x2, y2 = (figure.points[0][0], figure.points[0][1],
                              figure.points[1][0], figure.points[1][1])
        # проверка, что переданная фигура является набором координат
        elif (isinstance(figure, (tuple, list))) and len(figure) == 4:
            x1, y1, x2, y2 = figure[0], figure[1], figure[2], figure[3]
        else:
            print("Передана не линия!")
            return
        for i in range(0, len(self.points)):
            x3, y3 = self.points[i][0], self.points[i][1]
            x4 = round(((x2 - x1) * (y2 - y1) * (y3 - y1) + x1 * pow(y2 - y1, 2)
                        + x3 * pow(x2 - x1, 2))
                       / (pow(y2 - y1, 2) + pow(x2 - x1, 2)))
            y4 = round((y2 - y1) * (x4 - x1) / (x2 - x1) + y1)
            self.points[i][0] = x4 + (x4 - x3)
            self.points[i][1] = y4 + (y4 - y3)

    def belongs_point(self, figure):
        # проверка, что переданная фигура является объектом класса точки
        if (isinstance(figure, Point2D)):
            x1, y1 = figure.points[0][0], figure.points[0][1]
        # проверка, что переданная фигура является набором координат
        elif (isinstance(figure, (tuple, list))) and len(figure) == 2:
            x1, y1 = figure[0], figure[1]
        else:
            print("Передана не точка!")
            return
        return x1, y1


class Point2D(Figure2D):
    def __init__(self, x1, y1):
        self.points = [[x1, y1]]

    def belongs_point(self, figure):
        # вызов одноименной функции из родительского класса для проверки фигуры
        x1, y1 = super().belongs_point(figure)

        if self.points[0][0] == x1 and self.points[0][1] == y1:
            return True
        else:
            return False


class Segment2D(Figure2D):
    def init(self, p1, p2):
        self.points = [p1, p2]

    def belongs_point(self, figure):
        x1, y1 = super().belongs_point(figure)
        x2, y2, x3, y3 = self.points[0].points[0][0], \
            self.points[0].points[0][1], \
            self.points[1].points[0][0], self.points[1].points[0][1]

        answer = (x2 == x3 and x2 == x1 and min(y2, y3)<= y1 <=max(y2, y3))
        if not answer:
            answer = (y2 == y3 and y2 == y1 and min(x2, x3)<= x1 <=max(x2, x3))
        if not answer:
            a = y2-y3
            b = x3-x2
            c = x2y3 - x3y2
            answer = (a * x1 + b * y1 + c == 0)
        return answer


class Triangle2D(Figure2D):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.points = [[x1, y1], [x2, y2], [x3, y3]]

    def belongs_point(self, figure):
        x, y = super().belongs_point(figure)
        xp = (self.points[0][0], self.points[1][0], self.points[2][0])
        yp = (self.points[0][1], self.points[1][1], self.points[2][1])
        answer = False
        for i in range(len(xp)):
            a = (yp[i] <= y and y < yp[i - 1])
            b = (yp[i - 1] <= y and y < yp[i])
            c = (xp[i - 1] - xp[i])
            d = (y - yp[i]) / (yp[i - 1] - yp[i]) + xp[i]
            if ((a or b) and x > (c * d)):
                answer = not answer
        return answer
