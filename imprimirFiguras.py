def imprimirFiguras(figuras):
    print(f"{'#':<3} {'Tipo':<12} {'Descripción':<50} {'Área':<10} {'Perímetro':<10}")
    print("-" * 83)
    
    for i, figura in enumerate(figuras, start=1):
        print(f"{i:<3} "
              f"{type(figura).__name__:<12} "
              f"{str(figura):<35} "
              f"{figura.area():<10.2f} "
              f"{figura.perimetro():<10.2f}")
