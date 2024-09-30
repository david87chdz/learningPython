#Importamos la libreria csv nativa de python
import csv
#Libreria de os (Operative systems)
import os

ruta = "csv_vacio.csv"
ruta_absoluta = "D:\Develop\learningPython\python_advance\csv\csv_vacio.csv"

"""
os.path.join() Nos permite unir las rutas
Donde se encuentra el archivo y nuestro archivo
Primer argumento os.getcwd() nos permite obtener la ruta de nuesta ubicación
Segundo parametro el nombre de nuestro archivo
Esta segunda forma es mejor ya q nos grantiza la compatibilidad
entre diferentes sistemas operativos 
"""
ruta_absoluta_os = os.path.join(os.getcwd(), "csv_vacio.csv")

print(ruta_absoluta)
print(ruta_absoluta_os)

#Ponemos la w que es la de writer que es la forma en la que lo vamoa a abrir
archivo_abierto = open(ruta_absoluta_os, "w")
#Indicamos el archivo y el delimitador
writer = csv.writer(archivo_abierto, delimiter=",")
#Cerramos el archivo
archivo_abierto.close()