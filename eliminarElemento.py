from imprimirFiguras import imprimirFiguras

def eliminarElemento(figuras):
    imprimirFiguras(figuras)
    seleccion = int(input("Digita el # del elemento a eliminar: "))
    
    if 1 <= seleccion <= len(figuras):
        figuras.pop(seleccion - 1)
    else:
        print("Número inválido")
    
    return figuras
