import math

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определть методы позволяющие вычислить: Площадь, высоту и периметр фигуры

# Задача-2: Написать Класс Равнобочная трапеция, заданной координатами 4-х точек.
#  Предусмотреть в классе методы: проверка, является ли фигура равнобочной трапецией;
#  вычисления: длины сторон, периметр, площадь.

a = {"x": 1, "y": 1}
b = {"x": 2, "y": 5}
c = {"x": 5, "y": 1}

aa = {"x": 1, "y": 1}
bb = {"x": 2, "y": 3}
cc = {"x": 5, "y": 3}
dd = {"x": 6, "y": 1}


class Figure:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def basis(p01, p02):
        return math.sqrt((p02["x"] - p01["x"]) ** 2 + (p02["y"] - p01["y"]) ** 2)


class Triangle(Figure):
    def __init__(self, a, b, c):
        Figure.__init__(self, "Triangle")
        self.A = a
        self.B = b
        self.C = c
        self.a = Figure.basis(a, b)
        self.b = Figure.basis(b, c)
        self.c = Figure.basis(c, a)

    def height_a(a, b, c):
        p = (a + b + c) / 2
        return 2 * math.sqrt(p * (p - a) * (p - b) * (p - c)) / 2

    def basis(p01, p02):
        return math.sqrt((p02["x"] - p01["x"]) ** 2 + (p02["y"] - p01["y"]) ** 2)

    @property
    def square(self):
        return (self.a * Triangle.height_a(self.a, self.b, self.c)) / 2

    @property
    def perimeter(self):
        return self.a + self.b + self.c


class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        Figure.__init__(self, "Trapeze")
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.ab = Figure.basis(a, b)
        self.bc = Figure.basis(b, c)
        self.cd = Figure.basis(c, d)
        self.da = Figure.basis(d, a)

    def basis(p01, p02):
        return math.sqrt((p02["x"] - p01["x"]) ** 2 + (p02["y"] - p01["y"]) ** 2)

    @property
    def is_right(self):
        if self.ab == self.cd:
            return self.bc, self.da, self.ab
        elif self.bc == self.da:
            return self.ab, self.cd, self.bc
        else:
            return False

    @property
    def perimeter(self):
        return self.ab + self.bc + self.cd + self.da

    @property
    def square(self):
        a = self.is_right[0]
        b = self.is_right[1]
        c = self.is_right[2]
        return (a + b) / 4 * math.sqrt(4 * c ** 2 - (a - b) ** 2)


tr1 = Triangle(a, b, c)
print(tr1.type)
print("Square = ", tr1.square)
print("Perimeter = ", tr1.perimeter)

trap1 = Trapeze(aa, bb, cc, dd)
print(trap1.type)
print("Square = ", trap1.perimeter)
print("Perimeter = ", trap1.square)
