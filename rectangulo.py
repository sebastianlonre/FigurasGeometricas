from figuraGeometrica import FiguraGeometrica
from excepciones import ValorGeometricoInvalido

class Rectangulo(FiguraGeometrica):
    def __init__(self, base: float, altura: float):
        super().__init__(lados=4)      
        self.__base = base
        self.__altura = altura             

    @property
    def getBase(self) -> float:
        return self._base

    def base(self, valor):
        if valor <= 0:
            raise ValorGeometricoInvalido("La base debe ser positivo.")
        self._base = float(valor)

    @property
    def getAltura(self) -> float:
        return self._altura

    def altura(self, valor):
        if valor <= 0:
            raise ValorGeometricoInvalido("La altura debe ser positivo.")
        self._altura = float(valor)

    def area(self) -> float:
        return (self.__base * self.__altura)/2

    def perimetro(self) -> float:
        return 2 * (self.__base * self.__altura)

    def __str__(self) -> str:
        return f"Rectangulo(base={self.base}, altura={self.altura})"