from excepciones import ValorGeometricoInvalido

class FiguraGeometrica:
    def __init__(self, lados):
        self.__lados = lados
        self.__mensajeValidacion = ""
        self.__ok = True

    @property
    def lados(self):
        return self.__lados

    @lados.setter
    def lados(self, numeroLados):
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
    
    def validarMedidaLado(self, lados):
        for lado in lados:
            if lado < 0:
                self.mensajeValidacion = "Longitud no valida, debe de ser mayor a 0, la figura no se guardara"
                raise ValorGeometricoInvalido(self.mensajeValidacion)