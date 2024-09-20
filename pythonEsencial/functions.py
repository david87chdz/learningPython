APELLIDO = "Pinto"


def funcion():
    print("Mi primera función")
    nombre = "Ana"
    print(f"Mi nombre es {nombre} {APELLIDO}")

funcion()
#print(nombre)
#print(APELLIDO)

#Función con argumentos
def perimetro_cuadrado(lado, unidades):
    perimetro = lado * 4
    print(f"El perimetro es {perimetro} {unidades}")


perimetro_cuadrado(25, "metros")
perimetro_cuadrado(lado=25, unidades="metros")

#Retorno valores función
def perimetro_cuadrado(lado):
    perimetro = lado * 4
    return perimetro


def area_cuadrado(lado):
    area = lado * lado
    return area


lado = 25
perimetro = perimetro_cuadrado(lado=lado)
area = area_cuadrado(lado=lado)

print(f"Area: {area}\nPerimetro: {perimetro}")


def no_return():
    #Se usa para que no devuelva nada
    pass

test = no_return() 
print(test)  # Esto imprimirá: None


def calcular_cuadrado(lado):
    perimetro = lado * 4
    area = lado * lado
    return perimetro, area


lado = 25
perimetro, area = calcular_cuadrado(lado)
print(f"Area: {area}\nPerimetro: {perimetro}")

"""Podemos guardar todo en una tupla
resultado = calcular_cuadrado(lado=5)
print(resultado) #salida(25, 20)"""

#Documentar una función
def perimetro_cuadrado(lado):
    """Calcula el perimetro de un cuadrado."""

    perimetro = lado * 4
    return perimetro


def area_cuadrado(lado):
    """Calculo del area de un cuadrado.

    Esta función recibe el valor de un lado de un cuadrado y a partir
    de este calcula y retorna su área.

    Args:
        lado (int): medida del lado del cuadrado
    
    Returns:
        area (int): area del cuadrado
    """

    area = lado * lado
    return area