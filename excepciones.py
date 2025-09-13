class ValorGeometricoInvalido(Exception):
    """
    Se lanza cuando se recibe un dato geométrico imposible o no positivo:
    • radio ≤ 0
    • lado/altura/base ≤ 0
    • triángulo que viola la desigualdad triangular
    """
    pass


class FiguraNoEncontrada(Exception):
    """
    Se lanza al intentar acceder, eliminar o filtrar una figura
    cuyo índice o tipo no existe en la colección.
    """
    pass


class OpcionMenuInvalida(Exception):
    """
    Se lanza cuando el usuario introduce una opción del menú
    que no corresponde a ninguna acción válida.
    """
    pass
