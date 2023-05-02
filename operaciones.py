#Importar libreria
import math

#Funciones
def area_cuadrado(lado):
    """
    Calcula el area del cuadrado y retorna una variable
    que se llama area en formato float
    """
    area = lado*lado
    return area

def area_circulo(radio):
    """
    Calcula el area del circulo y retorna una variable
    que se llama area en formato float
    """
    area = math.pi*radio**2
    return area

def area_triangulo(base,altura):
    """
    Calcula el area del triangulo y retorna una variable
    que se llama area en formato float
    """
    area = (base*altura)/2
    return area

def area_rectangulo(ancho,altura):

    area = ancho*altura
    return area

def area_rombo(diagonal_mayor,diagonal_menor):

    area = (diagonal_mayor*diagonal_menor)/2
    return area

def area_paralelogramo(base,altura):

    area = (base*altura)
    return area

def area_pentagono(lado,apotema):

    area = (5 * lado*apotema)/2
    return area

def area_hexagono(apotema,lado):
    
    area = (6 * lado *apotema) / 2
    return area