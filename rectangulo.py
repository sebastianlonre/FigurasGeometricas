from figuraGeometrica import FiguraGeometrica
from excepciones import ValorGeometricoInvalido

class Rectangulo(FiguraGeometrica):
    def __init__(self, base: float, altura: float):
        super().__init__(lados=4)      
        
        self.__base = base
        self.__altura = altura
        
        try:
            self.validarMedidaLado([base, altura])
        except ValorGeometricoInvalido as e:
            print(f"error: {e}")                

    @property
    def base(self) -> float:
        return self.__base

    @base.setter
    def base(self, valor):
        self.__base = float(valor)

    @property
    def altura(self) -> float:
        return self.__altura

    @altura.setter
    def altura(self, valor):
        self._altura = float(valor)

    def area(self) -> float:
        return self.base * self.altura

    def perimetro(self) -> float:
        return 2 * (self.base * self.altura)

    def __str__(self) -> str:
        return f"Rectangulo(base={self.base}, altura={self.altura})"