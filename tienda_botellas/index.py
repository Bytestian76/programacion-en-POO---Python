from modelo_botella import Botella
from modelo_botella_plastico import Botella_plastico

#Codigo principal
#Aquí va la lógica del negocio 

#Instancia del padre
objBotella = Botella("Coca-Cola", "1.5L", "Especial")
objBotella.imprimir_info()

#Instancia Hija
objBotella_plastica = Botella_plastico("Pepsi", "500mL", "Común", "Redondo", "Plástico", "Sin tinte")
dato_out = objBotella_plastica.imprimir_info()
print(dato_out) 


