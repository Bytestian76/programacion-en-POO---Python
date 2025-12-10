from modelo_animal import Animal
from modelo_animal_caballo import Caballo
from modelo_animal_cocodrilo import Cocodrilo
from modelo_animal_pato import Pato
from modelo_animal_pez import Pez
from modelo_animal_escarabajo import Escarabajo

# Objetos
a12 = Animal("Juan", "Terrestre")
a1 = Caballo("Spirit", "pradera", "Mustang")
a2 = Pato("Lucas", "laguna", "verde")
a3 = Escarabajo("Buggy", "hojarasca", "rinoceronte")
a4 = Pez("Nemo", "océano", "payaso")
a5 = Cocodrilo("DonCoco", "pantano", 4)

a12.moverse(); a12.comunicarse()
a1.moverse(); a1.relinchar()
a2.moverse(); a2.graznar()
a3.moverse(); a3.esconderse()
a4.moverse(); a4.nadar()
a5.moverse(); a5.morder()