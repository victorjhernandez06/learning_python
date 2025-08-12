class Cuadrado:
    def __init__(self,ancho, alto): #-->funcion constructora
        self.ancho = ancho
        self.alto = alto
    def calcularArea(self):
        area = self.ancho * self.alto
        return area


figura =  Cuadrado(10,12)
print(figura.ancho) #--> 10
print(figura.alto) #--> 12
print(figura.calcularArea()) #-->120



