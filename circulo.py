import math
from figuraGeometrica import FiguraGeometrica
from excepciones import ValorGeometricoInvalido

class Circulo(FiguraGeometrica):
    """
    Representa un círculo.

    Hereda de ``FiguraGeometrica`` con *0* lados para que el
    sistema de clasificación por número de lados siga funcionando.

    Atributos
    ----------
    radio : float
        Radio del círculo (debe ser > 0).

    Raises
    ------
    ValorGeometricoInvalido
        Si se intenta establecer un radio menor o igual que 0.
    """
    
    # -----------------------------------------------------------------
    # Construcción
    # -----------------------------------------------------------------
    def __init__(self, radio: float):
        """
        Parametros
        ----------
        radio : float
            Radio inicial del círculo.

        Nota
        -----
        La validación se delega al *setter* ``radio``.
        """
        super().__init__(lados=0)      
        self.__radio = radio       
              
    # -----------------------------------------------------------------
    # Propiedad con validación
    # -----------------------------------------------------------------
    @property
    def getRadio(self) -> float:
        """float: radio actual del círculo."""
        return self._radio

    def radio(self, valor):
        """
        Asigna un nuevo valor al radio tras comprobar que sea positivo.

        Parametros
        ----------
        valor : float
            Nuevo radio.

        Raises
        ------
        ValorGeometricoInvalido
            Si ``valor`` ≤ 0.
        """
        if valor <= 0:
            raise ValorGeometricoInvalido("El radio debe ser positivo.")
        self.__radio = float(valor)

    def area(self) -> float:
        return math.pi * (self.radio ** 2)

    def perimetro(self) -> float:
        return 2 * math.pi * self.radio

    # -----------------------------------------------------------------
    # Operaciones geométricas
    # -----------------------------------------------------------------
    def area(self) -> float:
        """
        Devuelve el área del círculo.

        Fórmula
        -------
        :math:`A = \\pi r^{2}`
        """
        return math.pi * (self.radio ** 2)

    def perimetro(self) -> float:
        """
        Devuelve el perímetro (circunferencia) del círculo.

        Fórmula
        -------
        :math:`P = 2\\pi r`
        """ 
        return 2 * math.pi * self.radio

    # -----------------------------------------------------------------
    # Representación legible
    # -----------------------------------------------------------------
    def __str__(self) -> str:
        return f"Circulo(radio={self.radio})"