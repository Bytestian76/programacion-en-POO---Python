from modelo_carro import Carro
from modelo_carro_deportivo import Carro_deportivo
from modelo_carro_camion import Carro_camion
from modelo_carro_van import Carro_van


print("=== PRUEBA DE CLASES NEA ===")

# ----- Carro normal -----
carro_normal = Carro(velocidad=80, diseño="Sedán", motor="1.6")
print("\n--- Carro Básico ---")
carro_normal.encender_auto()
carro_normal.acelerar_auto()

# ----- Carro Deportivo -----
carro_depor = Carro_deportivo(
    velocidad=120, 
    diseño="Deportivo", 
    motor="V8", 
    marca="Nissan", 
    modelo="GTR"
)

print("\n--- Carro Deportivo ---")
carro_depor.mostrar_info()
carro_depor.correr_auto()
carro_depor.derrapar_auto()

# ----- Camión -----
camion = Carro_camion(
    velocidad=60, 
    diseño="Carga Pesada", 
    motor="Turbo Diesel", 
    capacidad_carga=15000, 
    ejes=4
)

print("\n--- Camión ---")
camion.encender_auto()
camion.cargar(3000)
camion.tocar_bocina()
camion.descargar()

# ----- Van -----
van = Carro_van(
    velocidad=70, 
    diseño="Pasajeros", 
    motor="2.0", 
    num_asientos=12, 
    tipo_uso="Transporte Público"
)

print("\n--- Van ---")
van.encender_auto()
van.abrir_puerta_corrediza()
van.transportar(10)
