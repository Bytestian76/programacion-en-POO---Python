from modelo_animal import Animal

class Pato(Animal):
    def __init__(self, nombre, habitat, color):
        super().__init__(nombre, habitat)
        self.color = color

    def graznar(self):
        print(f"{self.nombre} dice cuack — Color: {self.color}")

