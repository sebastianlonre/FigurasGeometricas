import math

class ValorGeometricoInvalido(ValueError):
    pass

class Triangulo:
    """Triángulo definido por tres lados."""
    def __init__(self, lado1, lado2, lado3):
        self.__l1 = float(lado1)
        self.__l2 = float(lado2)
        self.__l3 = float(lado3)

        if self.__l1 <= 0 or self.__l2 <= 0 or self.__l3 <= 0:
            raise ValorGeometricoInvalido("Cada lado debe ser > 0.")

        # Desigualdad triangular
        if not (self.__l1 + self.__l2 > self.__l3 and
                self.__l1 + self.__l3 > self.__l2 and
                self.__l2 + self.__l3 > self.__l1):
            raise ValorGeometricoInvalido("No cumple la desigualdad triangular.")

    @property
    def lado1(self):
        return self.__l1

    @lado1.setter
    def lado1(self, v):
        v = float(v)
        if v <= 0:
            raise ValorGeometricoInvalido("Cada lado debe ser > 0.")
        self.__l1 = v

    @property
    def lado2(self):
        return self.__l2

    @lado2.setter
    def lado2(self, v):
        v = float(v)
        if v <= 0:
            raise ValorGeometricoInvalido("Cada lado debe ser > 0.")
        self.__l2 = v

    @property
    def lado3(self):
        return self.__l3

    @lado3.setter
    def lado3(self, v):
        v = float(v)
        if v <= 0:
            raise ValorGeometricoInvalido("Cada lado debe ser > 0.")
        self.__l3 = v

    def perimetro(self):
        return self.__l1 + self.__l2 + self.__l3

    def area(self):
        # Fórmula de Herón
        s = self.perimetro() / 2.0
        return math.sqrt(s * (s - self.__l1) * (s - self.__l2) * (s - self.__l3))

    def __str__(self):
        return f"Triangulo(l1={self.__l1}, l2={self.__l2}, l3={self.__l3})"
