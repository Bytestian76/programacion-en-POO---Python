from modelo_carro import Carro

class Carro_van(Carro):
    def __init__(self, velocidad, diseño, motor, num_asientos, tipo_uso):
        super().__init__(velocidad, diseño, motor)
        self.num_asientos = num_asientos
        self.tipo_uso = tipo_uso

    def abrir_puerta_corrediza(self):
        print("La puerta corrediza se abrió... cuidado")

    def transportar(self, cantidad_personas):
        print(f"Llevando {cantidad_personas} personas al barrio, en una van tipo {self.tipo_uso}.")
