import csv

#r de read
with open("datos.csv", "r", encoding="UTF-8") as archivo:
    reader = csv.reader(archivo)
    #Si ponemos solo next(reader) saltamos la fila de las columnas
    columnas = next(reader)
    print("Columnas", columnas)
    for fila in reader:
        #Podemos poner el indice para solo imprimir por ejemplo el nombre
        #Si quremos todo print(fila)
        print(fila[0])
#Otra forma
with open("datos.csv", "r", encoding="UTF-8") as archivo:
    #DictReader para obtenerlos como diccionarios
    reader = csv.DictReader(archivo)
    for fila in reader:
        #Si queremos imprimirlo todo print(fila)
        print(fila["nombre"])