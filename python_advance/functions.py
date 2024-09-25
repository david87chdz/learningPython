def calcular_area_cuadrado(lado):
    """Calcular el area de un cuadrado"""
    area = lado * lado
    return area

area_cuadrado=calcular_area_cuadrado(lado=5)
print (area_cuadrado)

#Parametros args
#def calcular_perimetro(lado1, lado_2, lado_3, lado_4):
#    """Calcular perimetro de una figura de cuatro lados"""
#    perimetro = lado1 + lado_2+ lado_3+ lado_4
#    return perimetro

def calcular_perimetro(*args):
    #Para ver que trae args
    print(args)
    perimetro = 0
    for lado in args:
        perimetro+=lado
    return perimetro;

perimetro = calcular_perimetro(1,2,3,4,10)
print(perimetro)

#Variable **kwargs
def funcion_kwargs(**kwargs):
    print(kwargs)
    for llave, valor in kwargs.items():
        print(f"llave: {llave}, valor: {valor}")
    print(kwargs["nombre"], kwargs["apellido"])
funcion_kwargs(nombre="Paco", apellido= "Botero")


#orden parámetros
def parametros_ordenados(nombre, apellidos, *args, **kwargs):
    pass

#def parametros_desordenados(nombre, apellidos, **kwargs, *args):
#    pass

#Casos de uso funciones lambda
lista_numeros = [1,2,3,4,5,6,7,8,9]
lista_pares = list(filter(lambda numero: numero %2 == 0, lista_numeros))
print(lista_pares)

nueva_lista = list(map(lambda numero: numero*10, lista_numeros))
print(nueva_lista)