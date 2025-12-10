from modelo_animal import Animal

class Caballo(Animal):
    def __init__(self, nombre, habitat, raza):
        super().__init__(nombre, habitat)
        self.raza = raza

    def relinchar(self):
        print(f"{self.nombre} relincha — Raza: {self.raza}")

