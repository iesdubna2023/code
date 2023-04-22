import math

from PIL import Image, ImageDraw

im = Image.new('RGB', (500, 500), (255, 255, 255))
draw = ImageDraw.Draw(im)


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

    def draw(self, color='black'):
        for i in range(0, len(self.points)):
            a = self.points[i].x
            b = self.points[i].y
            c = self.points[(i + 1) % len(self.points)].x
            d = self.points[(i + 1) % len(self.points)].y
            draw.line((a, b, c, d), fill=color, width=1)
        im.save('image.jpg', quality=95)


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

# """Figure = Figure2D(((50, 100), (200, 400), (325, 130),  (100, 20)))
# Figure.draw()
# print("Figure", Figure.area())"""

# point1 = Point2D(200, 200)
# point1.draw()
# print("Point2D", point1.area())

# """figure_segment = Segment2D(380, 450, 380, 400)
# figure_segment.draw()
# print("Segment2D", figure_segment.area())"""

# triangle1 = Triangle2D(Point2D(100, 100), Point2D(200, 75), Point2D(150, 250))
# triangle1.draw(color='red')
# print("Triangle2D", triangle1.area())
# triangle1.mirror_point(point1)
# triangle1.draw(color='blue')


# ###### mirror_line

# ### Triangle

# segment1 = Segment2D(Point2D(230, 120), Point2D(450, 350))
# segment1.draw()

# triangle1.mirror_line(segment1)
# triangle1.draw(color='green')

# ### Segment

# segment2 = Segment2D(Point2D(160, 450), Point2D(170, 350))
# segment2.draw()

# segment3 = Segment2D(Point2D(50, 350), Point2D(150, 430))
# segment3.draw(color='red')

# segment3.mirror_line(segment2)
# segment3.draw(color='blue')

# ### Point

# segment4 = Segment2D(Point2D(400, 400), Point2D(460, 460))
# segment4.draw(color='red')

# point2 = Point2D(410, 450)
# point2.draw()

# point2.mirror_line(segment4)
# point2.draw(color='blue')

# ### Belongs_point

# point_true = Point2D(50, 50)
# print("Принадлежность точки (50, 50) точке (150, 50) =", point_true.belongs_point(point_true))

# segment = Segment2D(Point2D(20, 20), Point2D(80, 80))
# segment.draw()
# print("Принадлежность точки (50, 50) линии (20, 20, 80, 80) =", segment.belongs_point(point_true))

# triangle = Triangle2D(Point2D(20, 60), Point2D(60, 60), Point2D(40, 20))
# triangle.draw()
# print("Принадлежность точки (50, 50) треугольнику (20, 60, 60, 60, 40, 20) =", triangle.belongs_point(point_true))

# point_true.draw(color="red")

# point_false = Point2D(80, 50)
# point_false.draw(color="blue")
# print("Принадлежность точки (100, 50) точке (150, 50) =", point_true.belongs_point(point_false))
# print("Принадлежность точки (100, 50) линии (20, 20, 80, 80) =", segment.belongs_point(point_false))
# print("Принадлежность точки (100, 50) треугольнику (20, 60, 60, 60, 40, 20) =", triangle.belongs_point(point_false))
