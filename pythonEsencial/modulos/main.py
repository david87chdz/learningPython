import cuadrado
from cuadrado import perimetro_cuadrado 
from cuadrado import perimetro_cuadrado as pt
lado = 5
cuadrado = {
    "lado": lado,
    "area": cuadrado.area_cuadrado(lado),
    "perimetro": perimetro_cuadrado(lado)
}

print(cuadrado)
perimetro = pt(lado)
print(perimetro)