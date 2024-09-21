# Error: sintaxis
print "Hola"

# Error: Variable indefinida
print(variable)

# Error: división por cero
print(1/0)

# Error: tipo de dato
print("Hola" + 2)

#Raise exceptions
def validar_x(x):
    if x < 0.5:
        raise Exception("La variable x  debe ser mayor a 0.5")
    else:
        print("X es mayor a 1")

x = 0.3
resultado = validar_x(x)
print(resultado)

#Assertions error
def calcular_promedio(lista):
    assert len(lista) > 0, "La lista está vacía"
    return sum(lista) / len(lista)


promedio = calcular_promedio(lista=[])
promedio = calcular_promedio(lista=[1, 2, 3])
print(promedio)

#Try error
def calcular_promedio(lista):
    assert len(lista) > 0, "La lista está vacía"
    return sum(lista) / len(lista)


try:
    promedio = calcular_promedio(["texto"])
    print(promedio)
except AssertionError as assert_error:
    print("La función no fue ejecutada")
    print("Excepción:", assert_error)
except Exception as e:
    print("Excepción:", e)

print("Ya no estoy en el bloque try-except")