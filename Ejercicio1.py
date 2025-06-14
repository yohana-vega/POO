#Clase persona (Plantilla)
class Persona:
    def __init__(self, nombre, DNI):
        self.nombre = nombre
        self.DNI = DNI

    def datos(self):
        return f"el nombre de la persona es: {self.nombre}, y su DNI es: {self.DNI}"
    
#Objeto
persona1 = Persona("yohana", 40000686)

print(persona1.datos())

