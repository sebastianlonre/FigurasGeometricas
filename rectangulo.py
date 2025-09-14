from figuraGeometrica import FiguraGeometrica
from excepciones import ValorGeometricoInvalido

class Rectangulo(FiguraGeometrica):
    def __init__(self, base: float, altura: float):
        super().__init__(lados=4)      
        self.validarMedidaLado([base, altura])
        self.__base = base
        self.__altura = altura             

    @property
    def base(self) -> float:
        return self._base

    @base.setter
    def base(self, valor):
        self._base = float(valor)

    @property
    def altura(self) -> float:
        return self._altura

    @altura.setter
    def altura(self, valor):
        self._altura = float(valor)

    def area(self) -> float:
        return (self.__base * self.__altura)/2

    def perimetro(self) -> float:
        return 2 * (self.__base * self.__altura)

    def __str__(self) -> str:
        return f"Rectangulo(base={self.base}, altura={self.altura})"