def menu():
    validacion = True
    while (validacion):
        print("=== Gestor de Figuras Geométricas ===\n1) Agregar figura\n2) Listar figuras\n3) Totales (área y perímetro)\n4) Filtrar por tipo\n5) Eliminar figura por índice\n6) Salir")
        seleccion = int(input("opción"))
        if validacion == 6:
            validacion = False
