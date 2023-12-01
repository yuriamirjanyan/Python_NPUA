from math import pi

class Shape:
    def __init__(self):
        pass
    def whoami(self):
        print("I'm a shape")


class TwoD(Shape):
    def __init__(self):
        pass
    def area(self):
        print("I'm 2d object, I'll calculate the area")


class ThreeD(Shape):
    def __init__(self):
        pass
    def volume(self):
        print("I'm 3d object, I'll calculate the area")


class Square(TwoD):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a * self.a


class Triangle(TwoD):
    def __init__(self, a, h):
        self.a = a  # himq
        self.h = h  # bardzrutyun

    def area(self):
        return self.a * self.h / 2


class Cube(ThreeD):
    def __init__(self, a):
        self.a = a

    def volume(self):
        return self.a * self.a * self.a


class Cone(ThreeD):
    def __init__(self, h, r):
        self.h = h  # bardzrutyun
        self.r = r  # himqi sharavix

    def volume(self):
        return pi * self.r * self.h


# Testing
sh = Shape()
sh.whoami()

two_D = TwoD()
two_D.area()

three_d = ThreeD()
three_d.volume()

sq = Square(5)
print("Area: ", sq.area())
print(Square.mro())
er = Triangle(7, 5)
print("Area: ", er.area())

kub = Cube(3)
print("Volume: ", kub.volume())

kon = Cone(5, 10)
print("Volume: ", kon.volume())
