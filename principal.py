from operaciones import area_cuadrado,area_circulo,area_triangulo,area_rectangulo,area_rombo,area_paralelogramo,area_pentagono,area_hexagono
from interfaz import menu,datos_cuadrado,datos_circulo,datos_triangulo,datos_rectangulo,mostrar_circulo,mostrar_cuadrado,mostrar_triangulo,mostrar_rectangulo,datos_rombo,mostrar_rombo,datos_paralelogramo,mostrar_paralelogramo,datos_pentagono,mostrar_pentagono,datos_hexagono,mostrar_hexagono

#variables menu
CUADRADO = 1
CIRCULO = 2
TRIANGULO = 3
RECTANGULO = 4
ROMBO = 5
PARALELOGRAMO = 6
PENTAGONO = 7
HEXAGONO = 8
SALIR = 9

opcion = 0

while opcion != SALIR:
    #Opcion menu
    opcion = menu()
    if opcion == CUADRADO:
        #Llamar la funcion de solicitar datos
        lado = datos_cuadrado()
        #Llamae a area
        area = area_cuadrado(lado)
        #Llamar a mostrar datos
        mostrar_cuadrado(area)
    elif opcion == CIRCULO:
        #Llamar la funcion de solicitar datos
        radio = datos_circulo()
        #Llamae a area
        area = area_circulo(radio)
        #Llamar a mostrar datos
        mostrar_circulo(area)
    elif opcion == TRIANGULO:
        #Llamar la funcion de solicitar datos
        base,altura = datos_triangulo()
        #Llamae a area
        area = area_triangulo(base,altura)
        #Llamar a mostrar datos
        mostrar_triangulo(area)
    elif opcion == RECTANGULO:

        ancho,altura = datos_rectangulo()
        area = area_rectangulo(ancho,altura)
        mostrar_rectangulo(area)

    elif opcion == ROMBO:

        diagonal_mayor,diagonal_menor = datos_rombo()
        area = area_rombo(diagonal_mayor,diagonal_menor)
        mostrar_rombo(area)   

    elif opcion == PARALELOGRAMO:

        base,altura = datos_paralelogramo()
        area = area_paralelogramo(base,altura)
        mostrar_paralelogramo(area)  

    elif opcion == PENTAGONO:

        lado,apotema = datos_pentagono()
        area = area_pentagono(lado,apotema)
        mostrar_pentagono(area) 

    elif opcion == HEXAGONO:

        lado,apotema = datos_hexagono()

        area = area_hexagono(lado,apotema)

        mostrar_hexagono(area) 

    elif opcion == SALIR:
        print("Gracias por utilizar la calculadora de figuras geometricas!!!")       
    else:
        print("Opción Erronea!!!")