a = 2
b = 2

if a < b:
    print("A es menor que B")
elif a == b:
    print("A y B son iguales")
else: 
    print("A es mayor que B")

c= False
if type(c) is bool:
      print("C es un booleano")
else:
     print("C no es un booleano")

#Bucles For
# Iterar un string
for letra in "Texto":
    print(letra)


# Iterar una lista
lenguajes = ["python", "java", "javascript", "golang"]
for elemento in lenguajes:
    print(elemento)


# La instrucción break rompe el ciclo
lenguajes = ["python", "java", "javascript", "golang"]
for elemento in lenguajes:
    print(elemento)
    break


# Instrucción break dentro de una condición
lenguajes = ["python", "java", "javascript", "golang"]
for elemento in lenguajes:
    if elemento == "javascript":
        break
print(elemento)


# Instrucción continue dentro de una condición
lenguajes = ["python", "java", "javascript", "golang"]
for elemento in lenguajes:
    if elemento == "javascript":
        continue
print(elemento)


# Función range()
# Si le damos dos números nos lleva desde el punto de partida al final
for element in range(1, 6):
    print(element)
    
# Iterar una lista con ciclo for
lenguajes = ["python", "java", "javascript", "golang"]
for elemento in lenguajes:
    print(elemento)

# Iterar una lista con ciclo for, usando range() y len()
lenguajes = ["python", "java", "javascript", "golang"]
for index in range(len(lenguajes)):
    print("Index:", index)
    print("Element:", lenguajes[index])
    
#Iterando un diccionario con for
lenguaje = {
    "nombre": "python",
    "creador": "Guido Van Rossum"
}

# Iterar un diccionario
for llave in lenguaje:
    print(llave)
    print(lenguaje[llave])


# Iterar un diccionario usando keys()
for valor in lenguaje.keys():
    print(valor)


# Iterar un diccionario usando values()
for valor in lenguaje.values():
    print(valor)


# Iterar un diccionario usando items()
for llave, valor in lenguaje.items():
    print(llave, valor)

# Ciclo while 
i = 1
while 1 <= 5:
    print(i)
    i += 1


# Uso de la instrucción break
i = 1
while 1 <= 5:
    if i == 3:
        break
    print(i)
    i += 1


# Uso de la instrucción continue
i = 1
while 1 <= 5:
    if i == 3:
        continue
    print(i)
    i += 1
    
# Iterar una lista con ciclo while
lenguajes = ["python", "java", "javascript", "golang"]
i = 0
while i < len(lenguajes):
    print(lenguajes[i])
    i += 1