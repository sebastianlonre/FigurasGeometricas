import math
from figuraGeometrica import FiguraGeometrica
from excepciones import ValorGeometricoInvalido

class Triangulo(FiguraGeometrica):
    """Triángulo definido por tres lados."""
    def __init__(self, lado1, lado2, lado3):
        self.__l1 = float(lado1)
        self.__l2 = float(lado2)
        self.__l3 = float(lado3)

        try:
            self.validarMedidaLado([lado1, lado2, lado3])
        except ValorGeometricoInvalido as e:
            print(f"error: {e}")
        super().__init__(lados=3)

    @property
    def lado1(self):
        return self.__l1

    @lado1.setter
    def lado1(self, v):
        self.__l1 = v

    @property
    def lado2(self):
        return self.__l2

    @lado2.setter
    def lado2(self, v):
        self.__l2 = v

    @property
    def lado3(self):
        return self.__l3

    @lado3.setter
    def lado3(self, v):
        self.__l3 = v

    def perimetro(self):
        return self.__l1 + self.__l2 + self.__l3
    
    def area(self):
        # Fórmula de Herón
        s = self.perimetro() / 2.0
        return math.sqrt(s * (s - self.__l1) * (s - self.__l2) * (s - self.__l3))
    
    def validarDesigualdad(self):
        if not (self.__l1 + self.__l2 > self.__l3 and
                self.__l1 + self.__l3 > self.__l2 and
                self.__l2 + self.__l3 > self.__l1):
            self.mensajeValidacion = "No cumple con la desigualdad triangular."
            raise ValorGeometricoInvalido(self.mensajeValidacion)
        
    def __str__(self) -> str:
        return f"Triangulo(Lado 1={self.lado1}, Lado 2={self.lado2}, Lado 3={self.lado3})"
