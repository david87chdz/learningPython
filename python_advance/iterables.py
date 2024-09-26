numeros = [1,2,3]
#Para crear el iterador 
iterador = iter(numeros)

print(type (iterador))

#Para recorrer el iterador
#print(next(iterador))
#print(next(iterador))
#print(next(iterador))

for elemento in iterador:
    print(elemento)



"""
Por defecto inicializa el índice en 0
enumerate(iterable, start=0)
"""

nombres = ["Paco", "Emilio", "Javier", "Ana"]
nombres_enumerados = enumerate(nombres, start=5)
print(list(nombres_enumerados))

for indice, elemento in enumerate(nombres):
    print(indice, elemento)