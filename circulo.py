import math
from figuraGeometrica import FiguraGeometrica
from excepciones import ValorGeometricoInvalido

class Circulo(FiguraGeometrica):
<<<<<<< HEAD
    def __init__(self, radio: float):
        super().__init__(lados=0)      
        self.radio = radio             

    @property
    def getRadio(self) -> float:
=======
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
        self.radio = radio       
              
    # -----------------------------------------------------------------
    # Propiedad con validación
    # -----------------------------------------------------------------
    @property
    def getRadio(self) -> float:
        """float: radio actual del círculo."""
>>>>>>> e9661b5f012bed4c8418148a37f161321a0441a3
        return self._radio

    @radio.setter
    def radio(self, valor):
<<<<<<< HEAD
=======
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
>>>>>>> e9661b5f012bed4c8418148a37f161321a0441a3
        if valor <= 0:
            raise ValorGeometricoInvalido("El radio debe ser positivo.")
        self._radio = float(valor)

<<<<<<< HEAD
    def area(self) -> float:
        return math.pi * (self.radio ** 2)

    def perimetro(self) -> float:
        return 2 * math.pi * self.radio

=======
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
>>>>>>> e9661b5f012bed4c8418148a37f161321a0441a3
    def __str__(self) -> str:
        return f"Circulo(radio={self.radio})"