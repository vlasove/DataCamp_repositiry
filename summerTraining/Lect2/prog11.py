class Figure:
    def __init__(self, color, material):
        self.Color = color
        self.Material = material


class Triangle(Figure):
    def __init__(self, color, material, a, b, c):
        super().__init__(color, material)
        self.A = a
        self.B = b
        self.C = c

    def perimeter(self):
        return self.A + self.B + self.C


class Circle(Figure):
    def __init__(self, color, material, radius):
        super().__init__(color, material)
        self.R = radius

    def perimeter(self):
        return 2*3.14*self.R
