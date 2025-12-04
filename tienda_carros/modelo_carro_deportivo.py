from modelo_carro import Carro
class Carro_deportivo(Carro):
    def __init__(self, velocidad, diseño, motor, marca, modelo):
        super().__init__(velocidad, diseño, motor)
        self.marca = marca
        self.modelo = modelo
        
    def correr_auto(self):
        print(f"El {self.modelo} corre a una velocidad de {self.velocidad} ")
    
    def derrapar_auto(self):
        print(f"El auto está derrapando")
        print(f"*Suena Tokyo Drift de Teriyaki Boyz*") 
        
    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Diseño: {self.diseño}")
        print(f"Motor: {self.motor}")
        print(f"Velocidad: {self.velocidad} km/h")
