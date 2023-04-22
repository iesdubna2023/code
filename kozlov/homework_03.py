import math


class Figure2D:
    def __init__(self):
        self.x = None
        self.y = None
        self.p1 = None
        self.p2 = None
        self.p3 = None

    def area(self):
        return 0

    def mirror_point(self, figure):
        return

    def mirror_line(self, figure):
        return


class Point2D(Figure2D):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mirror_point(self, figure):
        x, y = figure.x, figure.y
        self.x = x - (self.x - x)
        self.y = y - (self.y - y)

    def mirror_line(self, figure):
        x1, y1 = figure.p1.x, figure.p1.y
        x2, y2 = figure.p2.x, figure.p2.y
        x3, y3 = self.x, self.y
        a = (x2 - x1) * (y2 - y1) * (y3 - y1)
        b = x1 * pow(y2 - y1, 2) + x3 * pow(x2 - x1, 2)
        x4 = round((a + b) / (pow(y2 - y1, 2) + pow(x2 - x1, 2)))
        y4 = round((y2 - y1) * (x4 - x1) / (x2 - x1) + y1)
        self.x = x4 + (x4 - x3)
        self.y = y4 + (y4 - y3)

    def belongs_point(self, figure):
        x, y = figure.x, figure.y

        if self.x == x and self.y == y:
            return True
        else:
            return False


class Segment2D(Figure2D):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def mirror_point(self, figure):
        x, y = figure.x, figure.y
        self.p1.x = x - (self.p1.x - x)
        self.p1.y = y - (self.p1.y - y)
        self.p2.x = x - (self.p2.x - x)
        self.p2.y = y - (self.p2.y - y)

    def mirror_line(self, figure):
        x1, y1 = figure.p1.x, figure.p1.y
        x2, y2 = figure.p2.x, figure.p2.y

        x3, y3 = self.p1.x, self.p1.y
        a = (x2 - x1) * (y2 - y1) * (y3 - y1)
        b = x1 * pow(y2 - y1, 2) + x3 * pow(x2 - x1, 2)
        x4 = round((a + b) / (pow(y2 - y1, 2) + pow(x2 - x1, 2)))
        y4 = round((y2 - y1) * (x4 - x1) / (x2 - x1) + y1)
        self.p1.x = x4 + (x4 - x3)
        self.p1.y = y4 + (y4 - y3)

        x3, y3 = self.p2.x, self.p2.y
        a = (x2 - x1) * (y2 - y1) * (y3 - y1)
        b = x1 * pow(y2 - y1, 2) + x3 * pow(x2 - x1, 2)
        x4 = round((a + b) / (pow(y2 - y1, 2) + pow(x2 - x1, 2)))
        y4 = round((y2 - y1) * (x4 - x1) / (x2 - x1) + y1)
        self.p2.x = x4 + (x4 - x3)
        self.p2.y = y4 + (y4 - y3)

    def belongs_point(self, figure):
        x, y = figure.x, figure.y
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y

        answer = (x1 == x2 and x1 == x and min(y1, y2) <= y <= max(y1, y2))
        if not answer:
            z = y1 == y2 and y1 == y
            v = min(x1, x2) <= x <= max(x1, x2)
            answer = (z and v)
        if not answer:
            a = y1 - y2
            b = x2 - x1
            c = x1 * y2 - x2 * y1
            answer = (a * x + b * y + c == 0)
        return answer


class Triangle2D(Figure2D):
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def area(self):
        a = math.sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2)
        b = math.sqrt((self.p3.x - self.p2.x) ** 2 + (self.p3.y - self.p2.y) ** 2)
        c = math.sqrt((self.p1.x - self.p3.x) ** 2 + (self.p1.y - self.p3.y) ** 2)
        p = (a + b + c) / 2
        S = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return S

    def mirror_point(self, figure):
        x, y = figure.x, figure.y
        self.p1.x = x - (self.p1.x - x)
        self.p1.y = y - (self.p1.y - y)
        self.p2.x = x - (self.p2.x - x)
        self.p2.y = y - (self.p2.y - y)
        self.p3.x = x - (self.p3.x - x)
        self.p3.y = y - (self.p3.y - y)

    def mirror_line(self, figure):
        x1, y1 = figure.p1.x, figure.p1.y
        x2, y2 = figure.p2.x, figure.p2.y

        x3, y3 = self.p1.x, self.p1.y
        a = (x2 - x1) * (y2 - y1) * (y3 - y1)
        b = x1 * pow(y2 - y1, 2) + x3 * pow(x2 - x1, 2)
        x4 = round((a + b) / (pow(y2 - y1, 2) + pow(x2 - x1, 2)))
        y4 = round((y2 - y1) * (x4 - x1) / (x2 - x1) + y1)
        self.p1.x = x4 + (x4 - x3)
        self.p1.y = y4 + (y4 - y3)

        x3, y3 = self.p2.x, self.p2.y
        a = (x2 - x1) * (y2 - y1) * (y3 - y1)
        b = x1 * pow(y2 - y1, 2) + x3 * pow(x2 - x1, 2)
        x4 = round((a + b) / (pow(y2 - y1, 2) + pow(x2 - x1, 2)))
        y4 = round((y2 - y1) * (x4 - x1) / (x2 - x1) + y1)
        self.p2.x = x4 + (x4 - x3)
        self.p2.y = y4 + (y4 - y3)

        x3, y3 = self.p3.x, self.p3.y
        a = (x2 - x1) * (y2 - y1) * (y3 - y1)
        b = x1 * pow(y2 - y1, 2) + x3 * pow(x2 - x1, 2)
        x4 = round((a + b) / (pow(y2 - y1, 2) + pow(x2 - x1, 2)))
        y4 = round((y2 - y1) * (x4 - x1) / (x2 - x1) + y1)
        self.p3.x = x4 + (x4 - x3)
        self.p3.y = y4 + (y4 - y3)

    def belongs_point(self, figure):
        x, y = figure.x, figure.y
        xp = (self.p1.x, self.p2.x, self.p3.x)
        yp = (self.p1.y, self.p2.y, self.p3.y)
        answer = False
        for i in range(len(xp)):
            a = (yp[i] <= y and y < yp[i - 1])
            b = (yp[i - 1] <= y and y < yp[i])
            c = (xp[i - 1] - xp[i])
            d = (y - yp[i]) / (yp[i - 1] - yp[i]) + xp[i]
            if ((a or b) and x > (c * d)):
                answer = not answer
        return answer
