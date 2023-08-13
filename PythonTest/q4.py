'''4. Implementa una clase en Python llamada `Rectangulo` que tenga atributos de longitud y ancho. La clase debe tener un método llamado `calcular_area` que devuelva el área del rectángulo.
'''

class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
        
    def calcular_area(self):
        return self.largo * self.ancho
    
rectangulo = Rectangulo(10, 5)
print(rectangulo.calcular_area())