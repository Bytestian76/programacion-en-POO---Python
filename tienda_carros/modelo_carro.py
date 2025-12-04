class Carro():
    def __init__(self, velocidad, diseño, motor):
        self.velocidad = velocidad
        self.diseño = diseño
        self.motor = motor
        
    def encender_auto(self):
        print(f"El auto está arrancando")
        
    def acelerar_auto(self):
        aceleracion = (input(f"Introduzca una velocidad a la que el auto acelera"))
        print(f"El auto está acelerando a {aceleracion} km/h")
        
    def mostrar_info(self):
        print(f"Informacion del auto:")
        print(f"Velocidad máxima: {self.velocidad}")
        print(f"Diseño: {self.diseño}")
        print(f"Motor: {self.motor}")
    
    