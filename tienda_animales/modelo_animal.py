class Animal:
    def __init__(self, nombre, habitat):
        self.nombre = nombre
        self.habitat = habitat

    def moverse(self):
        print(f"{self.nombre} se mueve en {self.habitat}")

    def comunicarse(self):
        print(f"{self.nombre} hace sonidos")

