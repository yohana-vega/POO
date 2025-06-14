#ENCAPSULAMIENTO
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


#Objeto
persona1 = Persona("yohana", 40000686)

print(persona1.datos())



#HERENCIA
class Estudiante(Persona):
    def __init__(self, nombre, DNI, carrera):
        super().__init__(nombre, DNI)
        self.carrera = carrera
    
    def get_carrera(self):
        return self.carrera
    
    def info(self):
        return f"{self.datos()}, esta estudiando la carrera de: {self.carrera}"


#Objeto
estudiante1 = Estudiante("critian", 33484097, "programacion")

print(estudiante1.info())

