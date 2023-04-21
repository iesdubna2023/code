class Figure2D:


    def set_color(self, color):
        self._color = color


    def get_color(self):
        return self._color


class Point2D(Figure2D):


    def __init__(self, x, y):
        self._x, self._y = x, y


    def area(self): 
        return 0


    def mirror_point(self, pm):
        result_x = 2 * pm._x - self._x
        result_y = 2 * pm._y - self._y
        return Point2D(result_x, result_y)
    

    def belongs_point(self, point):
        return self._x == point._x and self._y == point._y
    

    def normal_to_line(self, line):
        (A, B) = (line.point_1, line.point_2)
        x = ((A._x ** 2) * self._x 
             - 2* A._x * B._x * self._x 
             + (B._x ** 2) * self._x 
             + B._x * (A._y - B._y) * (A._y - self._y) 
             - A._x * (A._y - B._y) * (B._y - self._y)
            ) / (
             (A._x - B._x) ** 2 
             + (A._y - B._y) ** 2 
             )
             
        y = ((B._x ** 2) * A._y 
             + (A._x ** 2) * B._y 
             + B._x * self._x * (B._y - A._y) 
             - A._x * (self._x * (B._y - A._y) 
                       + B._x * (B._y + A._y)) 
             + ((A._y - B._y) ** 2) * self._y  
            ) / (
             (A._x - B._x) ** 2 
             + (A._y - B._y) ** 2 
            ) 
        return Point2D(x, y)
        

    def mirror_line(self, line):
        (A, B) = (line.point_1, line.point_2) 
        parall = Segment2D(self.mirror_point(A), 
                           self.mirror_point(B))
        return self.normal_to_line(parall)
    
                
class Segment2D(Figure2D):
    
    
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2


    def area(self):
        return 0
    

    def mirror_point(self, pm):
        point_1_prime = self.point_1.mirror_poin(pm)
        point_2_prime = self.point_2.mirror_poin(pm)
        return Segment2D(point_1_prime, point_2_prime)


    def belongs_point(self, pm):
        ifa = 0 <= (pm._x - self.point_1._x) * (self.point_2._x) <= (self.point_1._x - self.point_2._x) ** 2
        ifb = 0 <= (pm._y - self.point_1._y) * (self.point_2._y) <= (self.point_1._y - self.point_2._y) ** 2
        ifc = (pm._x - self.point_1._x) * (self.point_2._y - self.point_1._y) - (self.point_2._x - self.point_1._x) * (pm._y - self.point_1._y) == 0
        return ifa and ifb and ifc
    

    def mirror_line(self, line):
        # надо просто отразить все точки относительно прямой.
        # ВСЁ!
        return Segment2D(self.point_1.mirror_line(line), 
                         self.point_2.mirror_line(line))

    
class Triangle2D(Figure2D):


    def __init__(self, point_1, point_2, point_3):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3


    def area(self):
        ab = ((self.point_1._x - self.point_2._x)**2 + (self.point_1._y - self.point_2._y)**2)**0.5
        ac = ((self.point_1._x - self.point_3._x)**2 + (self.point_1._y - self.point_3._y)**2)**0.5
        bc = ((self.point_2._x - self.point_3._x)**2 + (self.point_2._y - self.point_3._y)**2)**0.5
        p = (ab + ac + bc)/2
        return (p * (p-ab) * (p-ac) * (p-bc))**0.5
    

    def mirror_point(self, pm):
        point_1_prime = self.point_1.mirror_point(pm)
        point_2_prime = self.point_2.mirror_point(pm)
        point_3_prime = self.point_3.mirror_point(pm)
        return Triangle2D(point_1_prime, point_2_prime, point_3_prime)    


    def belongs_point(self, pm):
        a = (self.point_1._x - pm._x) * (self.point_2._y - self.point_1._y) - (self.point_2._x - self.point_1._x) * (self.point_1._y - pm._y)
        b = (self.point_2._x - pm._x) * (self.point_3._y - self.point_2._y) - (self.point_3._x - self.point_2._x) * (self.point_2._y - pm._y)
        c = (self.point_3._x - pm._x) * (self.point_1._y - self.point_3._y) - (self.point_1._x - self.point_3._x) * (self.point_3._y - pm._y)
        return (a <= 0 and b <= 0 and c <= 0) or (a > 0 and b > 0 and c > 0)
    
    
    def mirror_line(self, line):
        return Triangle2D(self.point_1.mirror_line(line), 
                          self.point_2.mirror_line(line), 
                          self.point_3.mirror_line(line))


class Trapezoid2D(Figure2D): 


    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4


    def area(self):
        return 0.5 * abs(self.p3._y - self.p1._y) * (abs(self.p1._x - self.p2._x) + abs(self.p3._x + self.p4._x))


    def mirror_point(self, pm):
        p1_prime = self.p1.mirror_point(pm)
        p2_prime = self.p2.mirror_point(pm)
        p3_prime = self.p3.mirror_point(pm)
        p4_prime = self.p4.mirror_point(pm)
        return Trapezoid2D(p1_prime, p2_prime, p3_prime, p4_prime)


    def belongs_point(self, pm):
        p1p2 = (self.p1._x - pm._x) * (self.p2._y - self.p1._y) - (self.p2._x - self.p1._x) * (self.p1._y - pm._y)
        p2p3 = (self.p2._x - pm._x) * (self.p3._y - self.p2._y) - (self.p3._x - self.p2._x) * (self.p2._y - pm._y)
        p3p4 = (self.p3._x - pm._x) * (self.p4._y - self.p3._y) - (self.p4._x - self.p3._x) * (self.p3._y - pm._y)
        p4p1 = (self.p4._x - pm._x) * (self.p1._y - self.p4._y) - (self.p1._x - self.p4._x) * (self.p4._y - pm._y)
        return (p1p2 <= 0 and p2p3 <= 0 and p3p4 <= 0 and p4p1 <= 0) or (p1p2 > 0 and p2p3 > 0 and p3p4 > 0 and p4p1 > 0)


    def mirror_line(self, line):
        return Trapezoid2D(self.p1.mirror_line(line), 
                           self.p2.mirror_line(line), 
                           self.p3.mirror_line(line),
                           self.p4.mirror_line(line))


class Rectangle2D(Figure2D):


    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4


    def area(self):
        return abs(self.p1._x - self.p2._x) * abs(self.p1._y - self.p3._y)


    def mirror_point(self, pm):
        p1_prime = self.p1.mirror_point(pm)
        p2_prime = self.p2.mirror_point(pm)
        p3_prime = self.p3.mirror_point(pm)
        p4_prime = self.p4.mirror_point(pm)
        return Rectangle2D(p1_prime, p2_prime, p3_prime, p4_prime)


    def belongs_point(self, pm):
        p1p2 = (self.p1._x - pm._x) * (self.p2._y - self.p1._y) - (self.p2._x - self.p1._x) * (self.p1._y - pm._y)
        p2p3 = (self.p2._x - pm._x) * (self.p3._y - self.p2._y) - (self.p3._x - self.p2._x) * (self.p2._y - pm._y)
        p3p4 = (self.p3._x - pm._x) * (self.p4._y - self.p3._y) - (self.p4._x - self.p3._x) * (self.p3._y - pm._y)
        p4p1 = (self.p4._x - pm._x) * (self.p1._y - self.p4._y) - (self.p1._x - self.p4._x) * (self.p4._y - pm._y)
        return (p1p2 <= 0 and p2p3 <= 0 and p3p4 <= 0 and p4p1 <= 0) or (p1p2 > 0 and p2p3 > 0 and p3p4 > 0 and p4p1 > 0)


    def mirror_line(self, line):
        return Rectangle2D(self.p1.mirror_line(line), 
                           self.p2.mirror_line(line), 
                           self.p3.mirror_line(line),
                           self.p4.mirror_line(line))

class Square2D(Figure2D):


    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4


    def area(self):
        return abs(self.p1._x - self.p2._x) * abs(self.p1._y - self.p3._y)


    def mirror_point(self, pm):
        p1_prime = self.p1.mirror_point(pm)
        p2_prime = self.p2.mirror_point(pm)
        p3_prime = self.p3.mirror_point(pm)
        p4_prime = self.p4.mirror_point(pm)
        return Rectangle2D(p1_prime, p2_prime, p3_prime, p4_prime)


    def belongs_point(self, pm):
        p1p2 = (self.p1._x - pm._x) * (self.p2._y - self.p1._y) - (self.p2._x - self.p1._x) * (self.p1._y - pm._y)
        p2p3 = (self.p2._x - pm._x) * (self.p3._y - self.p2._y) - (self.p3._x - self.p2._x) * (self.p2._y - pm._y)
        p3p4 = (self.p3._x - pm._x) * (self.p4._y - self.p3._y) - (self.p4._x - self.p3._x) * (self.p3._y - pm._y)
        p4p1 = (self.p4._x - pm._x) * (self.p1._y - self.p4._y) - (self.p1._x - self.p4._x) * (self.p4._y - pm._y)
        return (p1p2 <= 0 and p2p3 <= 0 and p3p4 <= 0 and p4p1 <= 0) or (p1p2 > 0 and p2p3 > 0 and p3p4 > 0 and p4p1 > 0)


class Circle2D(Figure2D):


    def __init__(self, p0, r):
        self.p0 = p0
        self.r = r


    def area(self):
        return 3.14 * self.r * self.r


    def mirror_point(self, pm):
        p0_prime = self.p0.mirror_point(pm)
        return Circle2D(p0_prime, self.r)


    def belongs_point(self, pm):
        return ((self.p0._x - pm._x)**2 + (self.p0._y - pm._y)**2) ** 0.5 <= self.r
    

    def mirror_line(self, line):
        return Circle2D(self.p0.mirror_line(line), self.r)
