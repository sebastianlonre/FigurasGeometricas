from imprimirFiguras import imprimirFiguras

def filtrarData(figuras, filtro):
    datosFiltrados = list(filter(lambda figura: type(figura).__name__ == filtro, figuras))
    imprimirFiguras(datosFiltrados)