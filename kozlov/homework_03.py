import math

from PIL import Image, ImageDraw

im = Image.new('RGB', (500, 500), (255, 255, 255))
draw = ImageDraw.Draw(im)


class Figure2D:
    def __init__(self, array):
        self.points = array

    def area(self):
        if int(len(self.points)) <= 2:
            return 0
        elif int(len(self.points)) == 3:
            a = math.sqrt((self.points[1][0] - self.points[0][0]) ** 2 +
                          (self.points[1][1] - self.points[0][1]) ** 2)
            b = math.sqrt((self.points[2][0] - self.points[1][0]) ** 2 +
                          (self.points[2][1] - self.points[1][1]) ** 2)
            c = math.sqrt((self.points[0][0] - self.points[2][0]) ** 2 +
                          (self.points[0][1] - self.points[2][1]) ** 2)
            p = (a + b + c) / 2
            S = math.sqrt(p * (p - a) * (p - b) * (p - c))
            return S
        else:
            return "Ошибка!!!"

    def mirror_point(self, figure):
        if (isinstance(figure, Point2D)):
            # проверка, что переданная фигура является объектом класса точки
            x1, y1 = figure.points[0][0], figure.points[0][1]
        elif (isinstance(figure, (tuple, list))) and len(
                figure) == 2:
            # проверка, что переданная фигура является набором координат
            x1, y1 = figure[0], figure[1]
        else:
            print("Передана не точка!")
            return
        for i in range(0, len(self.points)):
            self.points[i][0] = x1 - (self.points[i][0] - x1)
            self.points[i][1] = y1 - (self.points[i][1] - y1)

    def mirror_line(self, figure):
        if (isinstance(figure, Segment2D)):
            # проверка, что переданная фигура является объектом класса отрезок
            x1, y1, x2, y2 = figure.points[0][0], figure.points[0][1],\
                figure.points[1][0], figure.points[1][1]
        elif (isinstance(figure, (tuple, list))) and len(
                figure) == 4:
            # проверка, что переданная фигура является набором координат
            x1, y1, x2, y2 = figure[0], figure[1], figure[2], figure[3]
        else:
            print("Передана не линия!")
            return
        for i in range(0, len(self.points)):
            x3, y3 = self.points[i][0], self.points[i][1]
            x4 = round(((x2 - x1) * (y2 - y1) * (y3 - y1) + x1 *
                        pow(y2 - y1, 2) + x3 * pow(x2 - x1, 2)) /
                       (pow(y2 - y1, 2) + pow(x2 - x1, 2)))
            y4 = round((y2 - y1) * (x4 - x1) / (x2 - x1) + y1)
            self.points[i][0] = x4 + (x4 - x3)
            self.points[i][1] = y4 + (y4 - y3)

    def draw(self, color='black'):
        for i in range(0, len(self.points)):
            draw.line((self.points[i][0], self.points[i][1],
                       self.points[(i + 1) % len(self.points)][0],
                       self.points[(i + 1) % len(self.points)][1]),
                      fill=color, width=1)
        im.save('image.jpg', quality=95)

    def belongs_point(self, figure):
        if (isinstance(figure, Point2D)):
            # проверка, что переданная фигура является объектом класса точки
            x1, y1 = figure.points[0][0], figure.points[0][1]
        elif (isinstance(figure, (tuple, list))) and len(
                figure) == 2:
            # проверка, что переданная фигура является набором координат
            x1, y1 = figure[0], figure[1]
        else:
            print("Передана не точка!")
            return
        return x1, y1


class Point2D(Figure2D):
    def __init__(self, x1, y1):
        self.points = [[x1, y1]]

    def belongs_point(self, figure):
        x1, y1 = super().belongs_point(figure)
        # вызов одноименной функции из родительского класса для проверки фигуры

        if self.points[0][0] == x1 and self.points[0][1] == y1:
            return True
        else:
            return False


class Segment2D(Figure2D):
    def __init__(self, x1, y1, x2, y2):
        self.points = [[x1, y1], [x2, y2]]

    def belongs_point(self, figure):
        x1, y1 = super().belongs_point(figure)
        x2, y2, x3, y3 = self.points[0][0], self.points[0][1], \
            self.points[1][0], self.points[1][1]

        answer = (x2 == x3 and x2 == x1 and min(y2, y3) <= y1 <= max(y2, y3))
        if not answer:
            answer = (y2 == y3 and y2 == y1 and
                      min(x2, x3) <= x1 <= max(x2, x3))
        if not answer:
            a = y2 - y3
            b = x3 - x2
            c = x2 * y3 - x3 * y2
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
            if (((yp[i] <= y and y < yp[i - 1]) or \
            (yp[i - 1] <= y and y < yp[i])) and \
            (x > (xp[i - 1] - xp[i]) * (y - yp[i]) \
            / (yp[i - 1] - yp[i]) + xp[i])):
                answer = not answer
        return answer


"""Figure = Figure2D(((50, 100), (200, 400), (325, 130),  (100, 20)))
Figure.draw()
print("Figure", Figure.area())"""

point1 = Point2D(200, 200)
point1.draw()
print("Point2D", point1.area())

"""figure_segment = Segment2D(380, 450, 380, 400)
figure_segment.draw()
print("Segment2D", figure_segment.area())"""

triangle1 = Triangle2D(100, 100, 200, 75, 150, 250)
triangle1.draw(color='red')
print("Triangle2D", triangle1.area())
triangle1.mirror_point(point1)
triangle1.draw(color='blue')

# mirror_line

# Triangle

segment1 = Segment2D(230, 120, 450, 350)
segment1.draw()

triangle1.mirror_line(segment1)
triangle1.draw(color='green')

# Segment

segment2 = Segment2D(160, 450, 170, 350)
segment2.draw()

segment3 = Segment2D(50, 350, 150, 430)
segment3.draw(color='red')

segment3.mirror_line(segment2)
segment3.draw(color='blue')

# Point

segment4 = Segment2D(400, 400, 460, 460)
segment4.draw(color='red')

point2 = Point2D(410, 450)
point2.draw()

point2.mirror_line(segment4)
point2.draw(color='blue')

# Belongs_point

point_true = Point2D(50, 50)
print("Принадлежность точки (50, 50) точке (150, 50) =",
      point_true.belongs_point(point_true))

segment = Segment2D(20, 20, 80, 80)
segment.draw()
print("Принадлежность точки (50, 50) линии (20, 20, 80, 80) =",
      segment.belongs_point(point_true))

triangle = Triangle2D(20, 60, 60, 60, 40, 20)
triangle.draw()
print("Принадлежность точки (50, 50) треугольнику (20, 60, 60, 60, 40, 20) =",
      triangle.belongs_point(point_true))

point_true.draw(color="red")

point_false = Point2D(80, 50)
point_false.draw(color="blue")
print("Принадлежность точки (100, 50) точке (150, 50) =",
      point_true.belongs_point(point_false))
print("Принадлежность точки (100, 50) линии (20, 20, 80, 80) =",
      segment.belongs_point(point_false))
print("Принадлежность точки (100, 50) треугольнику (20, 60, 60, 60, 40, 20) =",
      triangle.belongs_point(point_false))
