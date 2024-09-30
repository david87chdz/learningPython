import csv

columnas = ["nombre", "apellido", "edad"]
dato = ["Paco", "Botero", 26]

datos_lista = [
    ["Paco", "Botero", 26],
    ["Javier", "Quiñonez", 24],
    ["Emilio", "Tafur", 25]
]
datos_dict = [
    {"nombre": "Paco", "apellido": "Botero", "edad": 26},
    {"nombre": "Javier", "apellido": "Quiñonez", "edad": 24},
    {"nombre": "Emilio", "apellido": "Tafur", "edad": 25}
]

""" 
#para escribirle y cerrarle
archivo = open("datos.csv","w")
writer = csv.writer(archivo, delimiter=",")
archivo.close() """

""" 
#Así pasamos la lista de datos pero nos crea una linea vacia entre medias
with open("datos.csv", "w") as archivo:
    writer = csv.writer(archivo, delimiter=",")
    #Creamos la primera linea que tendrá el nombre de las columnas
    #Writerow significa escribir una fila
    writer.writerow(columnas)
    #Escribimos la fila de datos
    writer.writerow(dato) 
    """

""" 
#Con newline quitamos la línea vacía
with open("datos.csv", "w", newline="") as archivo:
    writer = csv.writer(archivo, delimiter=",")
    #Creamos la primera linea que tendrá el nombre de las columnas
    writer.writerow(columnas)
    #Writerows en plurar para indicar que vamos a escribir varias listas
    writer.writerows(datos_lista) 
    """

#No necesitamos cerrarlo con la variable with
#Newline nos indica que no queremos linea vacia cada vez que cambiamos de fila
#Archivo es un alias que le damos
with open("datos.csv", "w", newline="") as archivo:
    #Para escribir diccionarios
    writer = csv.DictWriter(archivo, fieldnames=columnas)
    #Para que nos escriba la primera fila con el nombre de las columnas
    writer.writeheader()
    #Usamos writerows en plural para varias filas
    writer.writerows(datos_dict)