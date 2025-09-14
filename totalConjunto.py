def totalConjunto(figuras):
    sumaArea = 0
    sumaPerimetro = 0

    for figura in figuras:
        sumaArea += figura.area()
        sumaPerimetro += figura.perimetro()
    
    print("Totales del conjunto actual:\n")
    print(f"Cantidad {len(figuras)}\n")
    print(f"Área total: {sumaArea} \n")
    print(f"Perímetro total: {sumaPerimetro} \n")
    