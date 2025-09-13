class FiguraGeometrica:
    def __init__(self, lados):
        self.__lados = lados
        self.__mensajeValidacion = ""
        self.__ok = True

    def getLados(self):
        return self.__lados

    def setLados(self, numeroLados):
        self.__lados = numeroLados

    @property
    def mensajeValidacion(self):
        return self.__mensajeValidacion

    @mensajeValidacion.setter
    def mensajeValidacion(self, mensaje):
        self.__ok = False
        self.__mensajeValidacion = mensaje

    @property
    def ok(self):
        return self.__ok
