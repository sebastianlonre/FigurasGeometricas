import math

class ValorGeometricoInvalido(ValueError):
    pass

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.__lado1 = 0.0
        self.__lado2 = 0.0
        self.__lado3 = 0.0
        # usar setters para validar
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.__validar_triangulo()

    # propiedades simples
    @property
    def lado1(self) -> float:
        return self.__lado1

    @lado1.setter
    def lado1(self, v: float) -> None:
        v = float(v)
        if v <= 0:
            raise ValorGeometricoInvalido("Cada lado debe ser > 0.")
        self.__lado1 = v

    @property
    def lado2(self) -> float:
        return self.__lado2

    @lado2.setter
    def lado2(self, v: float) -> None:
        v = float(v)
        if v <= 0:
            raise ValorGeometricoInvalido("Cada lado debe ser > 0.")
        self.__lado2 = v

    @property
    def lado3(self) -> float:
        return self.__lado3

    @lado3.setter
    def lado3(self, v: float) -> None:
        v = float(v)
        if v <= 0:
            raise ValorGeometricoInvalido("Cada lado debe ser > 0.")
        self.__lado3 = v

    def __validar_triangulo(self) -> None:
        a, b, c = self.__lado1, self.__lado2, self.__lado3
        if not (a + b > c and a + c > b and b + c > a):
            raise ValorGeometricoInvalido("No cumple la desigualdad triangular.")

    # API básica
    def perimetro(self) -> float:
        return self.__lado1 + self.__lado2 + self.__lado3

    def area(self) -> float:
        s = self.perimetro() / 2.0
        a, b, c = self.__lado1, self.__lado2, self.__lado3
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    def __str__(self) -> str:
        return f"Triangulo(l1={self.__lado1}, l2={self.__lado2}, l3={self.__lado3})"
