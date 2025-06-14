#Clase de una Marca
class Adidas:
    def __init__(self, personalidad, impacto):
        self.personalidad = personalidad
        self.impacto = impacto

    def categorias(self):
        return f"esta categoria tiene la personalidad de {self.personalidad}, y genera el siguiente impacto {self.impacto}"
    
zapatilla1 = Adidas("canchera", "juvenil")

print(zapatilla1.categorias())
