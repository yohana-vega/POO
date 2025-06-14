#POLIMORFISMO


#Clase persona (Plantilla)
class Persona:
    def __init__(self, nombre, DNI):
        self._nombre = nombre
        self.DNI = DNI

#Esta funcion es para acceseder al nombre.
    def get_nombre(self):
        return self._nombre


#Esta función permite cambiar el dato del atributo nombre.   
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre


    def datos(self):
        return f"el nombre de la persona es: {self._nombre}, y su DNI es: {self.DNI}"


class Estudiante(Persona):
    def datos(self):
        return f"Hola mi nombre es {self._nombre}, mi DNI es {self.DNI} y soy estudiante."

class Profesor(Persona):
   def datos(self):
        return f"Hola mi nombre es {self._nombre}, mi DNI es {self.DNI} y soy profesor."
   
#Polimorfismo (distintos objetos responden diferente al mismo metodo)

personas = [
    Persona("marisol", 18827112),
    Estudiante("vanesa",3254689),
    Profesor("Raul", 46888222)
]

for p in personas:
    print(p.datos())
