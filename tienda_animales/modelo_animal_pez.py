from modelo_animal import Animal

class Pez(Animal):
    def __init__(self, nombre, habitat, especie):
        super().__init__(nombre, habitat)
        self.especie = especie

    def nadar(self):
        print(f"{self.nombre} está nadando — Especie: {self.especie}")

