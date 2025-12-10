from modelo_animal import Animal 

class Escarabajo(Animal):
    def __init__(self, nombre, habitat, tipo):
        super().__init__(nombre, habitat)
        self.tipo = tipo

    def esconderse(self):
        print(f"{self.nombre} se esconde — Tipo: {self.tipo}")

