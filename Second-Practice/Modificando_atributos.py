class Coche():
    """Una representacion sencilla del coche"""
    def __init__(self,brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.lectura_odometro = 0

    def obtener_nombre_descriptivo(self):
        """Regresa el nombre descriptivo"""
        nombre_largo = str(self.year) + " "+self.brand+' '+self.model
        return nombre_largo

    def leer_odometro(self):
        '''Muestra el kilometraje'''
        print("este coche ha recorrido " + str(self.lectura_odometro)+ " Km")

    def actualizar_odometro(self, kilometraje):
        """Establece la lectura del odometro al valor asignado
            cancela los cambios si retrocedo el valor """
        if kilometraje >= self.lectura_odometro:
            self.lectura_odometro = kilometraje
        else:
            print("No puedes retroceder el valor del odometro")

    def incrementar_odometro(self,kilometros):
        self.lectura_odometro += kilometros

mi_coche_usado =  Coche('Subaru','outback', 2018)
print(mi_coche_usado.obtener_nombre_descriptivo())

mi_coche_usado.actualizar_odometro(23500)
mi_coche_usado.leer_odometro()

mi_coche_usado.incrementar_odometro(100)
mi_coche_usado.leer_odometro()