import math
from figuraGeometrica import FiguraGeometrica
from excepciones import ValorGeometricoInvalido

class Circulo(FiguraGeometrica):
    def __init__(self, radio: float):
        super().__init__(lados=0)      
        self.radio = radio             

    @property
    def getRadio(self) -> float:
        return self._radio

    @radio.setter
    def radio(self, valor):
        if valor <= 0:
            raise ValorGeometricoInvalido("El radio debe ser positivo.")
        self._radio = float(valor)

    def area(self) -> float:
        return math.pi * (self.radio ** 2)

    def perimetro(self) -> float:
        return 2 * math.pi * self.radio

    def __str__(self) -> str:
        return f"Circulo(radio={self.radio})"