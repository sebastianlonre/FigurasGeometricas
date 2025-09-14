from circulo import Circulo
from rectangulo import Rectangulo
from triangulo import Triangulo
from excepciones import ValorGeometricoInvalido
from imprimirFiguras import imprimirFiguras

def menu():

    validacion = True
    figuras = []

    while (validacion):
        print("=== Gestor de Figuras Geométricas ===\n1) Agregar figura\n2) Listar figuras\n3) Totales (área y perímetro)\n4) Filtrar por tipo\n5) Eliminar figura por índice\n6) Salir")
        seleccion = int(input("opción: "))

        match(seleccion):
            case 1:
                figuraCreada = crearFigura()

                if figuraCreada.ok:
                    figuras.append(figuraCreada)
                    print("se creo con exito la figura")
                else:
                    print(figuraCreada.mensajeValidacion)
            case 2:
                imprimirFiguras(figuras)
            case 3:
                print("totales area")
            case 4:
                print("filtrar tipo")
            case 5:
                print("eliminar figuras")
            case 6:
                validacion = False
            case _:
                print("opcion no valida")

def crearFigura():
    print("Agregar figura\na) Círculo\nb) Rectángulo\nc) Triángulo")
    seleccion = input("Elige tipo (a/b/c): ")

    match(seleccion):
            case "a":
                radio = float(input("Ingrese el radio: "))
                circuloCreado = Circulo(radio)
                return circuloCreado
            case "b":
                base = float(input("Ingrese la base: "))
                altura = float(input("Ingrese la altura: "))
                rectanguloCreado = Rectangulo(base, altura)
                return rectanguloCreado
            case "c":
                lado1 = float(input("Ingrese el lado 1: "))
                lado2 = float(input("Ingrese el lado 2: "))
                lado3 = float(input("Ingrese el lado 3: "))
                trianguloCreado = Triangulo(lado1, lado2, lado3)
                try:
                    trianguloCreado.validarDesigualdad()
                except ValorGeometricoInvalido as e:
                    print(f"error: {e}")
                
                return trianguloCreado

