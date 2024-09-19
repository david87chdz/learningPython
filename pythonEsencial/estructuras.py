#Listas
# Declarar una lista
lenguajes = ["python", "java", "javascript", "golang"]
print(lenguajes)

# Las listas pueden contener elementos de diferentes tipos
lista_a = [True, 1, 2.0, "python", 1] 
print(lista_a)

# Usamos indices para extraer un elemento
print(lenguajes[0])

# La función len() devuelve el tamaño de la lista
print(len(lenguajes))

# Usamos índices negativos para obtener las posiciones de la
# lista desde el último hasta el primero
print(lenguajes[-1])

# Usamos slicing para obtener una sublista
print(lenguajes[1:3])

# Litas anidadas
programacion = [lenguajes, "dedicacion", "practica"]
print(programacion)
print(programacion[0][0])

# Modificamos una posición asignandole un nuevo valor
lenguajes[0] = "dart"
print(lenguajes)

# append() permite añadir elemertos al final de la lista
lenguajes.append("python")
print(lenguajes)

# extend() permite unir dos listas
otros_lenguajes = ["c++", "c#"]
lenguajes.extend(otros_lenguajes)
print(lenguajes)

# Eliminación de elementos de la lista
lenguajes.pop(2)
lenguajes.pop("python")

#Tuplas
# Declarar una tupla
lenguajes = ("python", "java", "javascript", "golang")

lenguajes = "python", "java", "javascript", "golang"
print(lenguajes)

# Extraer elementos usando índices
print(lenguajes[0])
print(lenguajes[-1])
#No permiten la modificación de los elementos

#Diccionarios
# Declarar un diccionario
lenguaje = {
    "nombre": "python",
    "creador": "Guido Van Rossum"
}
print(lenguaje["nombre"])

# Añadir nuevas llaves y valores
lenguaje["año_lanzamiento"] = 1991
print(lenguaje)

# Sobreescribir el valor de una llave
lenguaje["año_lanzamiento"] = 1999
print(lenguaje)

lenguaje["caracteristicas"] = ["sencillo" , "facil", "genial"]

# items() retorna una lista de tuplas (llave, valor)
print(lenguaje.items())

# keys() retorna una lista de las llaves del diccionario
print(lenguaje.keys())

# values() retorna una lista de los valores del diccionario
print(lenguaje.values())

#Sets
# Declarar un set
set_a = {1, 2, 3}
print(type(set_a), set_a)

# Si hay elementos repetidos solo se conserva el elemento una vez
set_b = {1, 2, 3, 4, 5, 1}
print(set_b)

# Puede tener elementos de diferentes tipos
set_c = {1, 2, True, "texto"}
print(set_c)

# Añadir elementos al set
set_a .add(4)

# Actualizar un set
set_a.update([4, 5, 6])

# Tamaño de un set
len(set_a)

# Eliminar un elemento de un set
set_a.discard(2)
set_a.remove(2)

# Eliminar todos los elementos de un set
set_a.clear()