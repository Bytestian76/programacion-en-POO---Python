from modelo_carro import Carro

class Carro_camion(Carro):
    def __init__(self, velocidad, diseño, motor, capacidad_carga, ejes):
        super().__init__(velocidad, diseño, motor)
        self.capacidad_carga = capacidad_carga
        self.ejes = ejes

    def cargar(self, peso):
        print(f"El camión está cargando {peso} kg...")

    def descargar(self):
        print("El camión está descargando la mercancía...")

    def tocar_bocina(self):
        print("*bocina de camión*")
