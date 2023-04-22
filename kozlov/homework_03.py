import math


class Figure2D:
    def __init__(self):
        self.points = ()
        pass

    def area(self):
        return 0

    def mirror_point(self, figure):
        x, y = figure.x, figure.y
        for i in range(len(self.points)):
            self.points[i].x = x - (self.points[i].x - x)
            self.points[i].y = y - (self.points[i].y - y)

    def mirror_line(self, figure):
        if len(self.points) < 1:
            return
        x1, y1 = self.points[0].x, self.points[0].y
        x2, y2 = self.points[1].x, self.points[1].y
        for i in range(0, len(self.points)):
            x3, y3 = self.points[i].x, self.points[i].y
            a = (x2 - x1) * (y2 - y1) * (y3 - y1)
            b = x1 * pow(y2 - y1, 2) + x3 * pow(x2 - x1, 2)
            x4 = round((a + b) / (pow(y2 - y1, 2) + pow(x2 - x1, 2)))
            y4 = round((y2 - y1) * (x4 - x1) / (x2 - x1) + y1)
            self.points[i].x = x4 + (x4 - x3)
            self.points[i].y = y4 + (y4 - y3)


class Point2D(Figure2D):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.points = []

    def mirror_point(self, figure):
        x, y = figure.x, figure.y
        self.x = x - (self.x - x)
        self.y = y - (self.y - y)

    def mirror_line(self, figure):
        x1, y1 = figure.points[0].x, figure.points[0].y
        x2, y2 = figure.points[1].x, figure.points[1].y
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
        self.points = (p1, p2)

    def belongs_point(self, figure):
        x, y = figure.x, figure.y
        x1, y1 = self.points[0].x, self.points[0].y
        x2, y2 = self.points[1].x, self.points[1].y

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
        self.points = (p1, p2, p3)

    def area(self):
        a1 = (self.points[1].x - self.points[0].x) ** 2
        a2 = (self.points[1].y - self.points[0].y) ** 2
        a = math.sqrt(a1 + a2)
        b1 = (self.points[2].x - self.points[1].x) ** 2
        b2 = (self.points[2].y - self.points[1].y) ** 2
        b = math.sqrt(b1 + b2)
        c1 = (self.points[0].x - self.points[2].x) ** 2
        c2 = (self.points[0].y - self.points[2].y) ** 2
        c = math.sqrt(c1 + c2)
        p = (a + b + c) / 2
        S = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return S

    def belongs_point(self, figure):
        x, y = figure.x, figure.y
        xp = (self.points[0].x, self.points[1].x, self.points[2].x)
        yp = (self.points[0].y, self.points[1].y, self.points[2].y)
        answer = False
        for i in range(len(xp)):
            a = (yp[i] <= y and y < yp[i - 1])
            b = (yp[i - 1] <= y and y < yp[i])
            c = (xp[i - 1] - xp[i])
            d = (y - yp[i]) / (yp[i - 1] - yp[i] + 1) + xp[i]
            if ((a or b) and x > (c * d)):
                answer = not answer
        return answer
