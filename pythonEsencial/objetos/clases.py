class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def cumplir_anios(self ,edad):
        self.edad = edad
        print(f"Feliz Cumpleaños #{self.edad}")


paco = Persona(nombre="Paco", edad=20)
paco.cumplir_anios(27)

#Herencia
class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cumplir_anios(self):
        self.edad += 1
        print(f"Feliz Cumpleaños #{self.edad}")


class Empleado(Persona):

    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def trabajar(self, horas_trabajadas):
        print(f"{self.nombre} ha trabajado {horas_trabajadas} horas")


paco = Empleado(nombre="Paco", edad=20)
paco.trabajar(horas_trabajadas= 16)