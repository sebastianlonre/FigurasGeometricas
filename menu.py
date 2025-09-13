def menu():
    validacion = True
    while (validacion):
        print("=== Gestor de Figuras Geométricas ===\n1) Agregar figura\n2) Listar figuras\n3) Totales (área y perímetro)\n4) Filtrar por tipo\n5) Eliminar figura por índice\n6) Salir")
        seleccion = int(input("opción: "))

        match(seleccion):
            case 1:
                print("agregar figura")
            case 2:
                print("listar")
            case 3:
                print("totales area")
            case 4:
                print("filtrar tipo")
            case 5:
                print("eliminar figuras")
            case 6:
                validacion = False