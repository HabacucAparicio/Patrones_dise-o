'''Patron de diseño Adapter
Obtenido del libro:EL gulum de las americas
Creado:Antonio Habacuc Aparicio Pérez
1217100848

Los presos politicos de aquellos tiempos en la cuba Castrista, como medio
de represion hacia ellos tenian expresamente prohibido el mandar cartas
por ellos mismos al exterior, es por ello que adaptaron esta accion
con la ayuda de otras personas libres.

'''

from abc import ABC,abstractmethod

class PersonaLibre(ABC):
    @abstractmethod

    def MandarCartas(self):
        pass

class CampesinoMilitar(PersonaLibre):

    def MandarCartas(self):
        print("Carta escrita de algun tema libre!")

class PresoComun(PersonaLibre):
    def MandarCartas(self):
        print("Carta escrita de algun tema libre mandada desde la cárcel")

class PresoPolitico:
    def Escribir(self):
        print("Puede escribir algo")
        
    def Leer(self):
        print("Puede leer articulos dados por los presidirios")

class Ayudadapter(PersonaLibre):

    def __init__(self):
        self._PresoPolitico = PresoPolitico()

    def MandarCartas(self):
        print("Carta escrita denunciando los abusos de las cárceles")

class Escritos:
    def __init__(self):
        self.Armando = Ayudadapter()
        self.Ulises = PresoComun()
        self.Pedro = CampesinoMilitar()

        self.Armando.MandarCartas()
        self.Ulises.MandarCartas()
        self.Pedro.MandarCartas()

cuba = Escritos()
            
