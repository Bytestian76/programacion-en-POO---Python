from modelo_animal import Animal 

class Cocodrilo(Animal):
    def __init__(self, nombre, habitat, longitud):
        super().__init__(nombre, habitat)
        self.longitud = longitud

    def morder(self):
        print(f"{self.nombre} muerde — mide {self.longitud}m")
