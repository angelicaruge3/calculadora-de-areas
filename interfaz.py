#funcion menu
def menu():
    """
    Muestra el menu al usuario y devuelve la opcion digitada en formato int
    """
    print("\n Calculadora de figuras geometricas")
    print("1. Calcular area del cuadrado")
    print("2. Calcular area del circulo")
    print("3. Calcular area del triangulo")
    print("4. Calcular area del rectangulo")
    print("5. Calcular area del rombo")
    print("6. Calcular area del paralelogramo")
    print("7. Calcular area del pentagono")
    print("8. Calcular area del hexagono")
    print("9. Salir")
    op = int(input("Digite la opción: "))
    return op

#funcion solicitar datos
def datos_cuadrado():
    """
    Solicitar el lado del cuadrado y lo transforma y retorna float
    """
    lado = float(input("Digite el lado: "))
    return lado

#funcion solicitar datos
def datos_circulo():
    """
    Solicitar el radio del circulo y lo transforma y retorna float
    """
    radio = float(input("Digite el radio: "))
    return radio

#funcion solicitar datos
def datos_triangulo():
    """
    Solicitar base y altura del triangulo y lo transforma y retorna float base y altura
    """
    base = float(input("Digite la base: "))
    altura = float(input("Digite la altura: "))
    return base,altura

def datos_rectangulo():

    ancho = float(input("Digite el ancho del rectangulo:"))
    altura = float(input("Digite la altura del rectangulo:"))
    return ancho,altura

def datos_rombo():

    diagonal_mayor = float(input("Digite la diagonal mayor:"))
    diagonal_menor = float(input("Digite la diagonal menor:"))
    return diagonal_mayor,diagonal_menor

def datos_paralelogramo():

    base = float(input("Digite la base:"))
    altura = float(input("Digite la altura:"))
    return base,altura

def datos_pentagono():

    lado = float(input("Digite el lado:"))
    apotema = float(input("Digite el apotema:"))
    return lado,apotema

def datos_hexagono():

    lado = float(input("Digite el lado:"))
    apotema = float(input("Digite el apotema:"))
    return lado,apotema

#Funcion mostrar datos
def mostrar_cuadrado(area):
    """
    Muestra el area del cuadrado al usuario final
    """
    print(f"El area del cuadrado es {area} mts^2")

def mostrar_circulo(area):
    """
    Muestra el area del circulo al usuario final
    """
    print(f"El area del circulo es {area} mts^2")

def mostrar_triangulo(area):
    """
    Muestra el area del triangulo al usuario final
    """
    print(f"El area del triangulo es {area} mts^2")

def mostrar_rectangulo(area):
    print(f"El area del rectangulo es {area} mts'2")

def mostrar_rombo(area):
    print(f"El area del rombo es {area} mts'2")

def mostrar_paralelogramo(area):
    print(f"El area del paralelogramo es {area} mts'2")

def mostrar_pentagono(area):
    print(f"El area del pentagono es {area} mts'2")

def mostrar_hexagono(area):
    print(f"El area del hexagono es {area} mts'2")