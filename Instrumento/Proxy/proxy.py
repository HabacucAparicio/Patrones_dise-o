'''Patron de diseño Proxy
Obtenido del libro:EL gulum de las americas
Creado:Antonio Habacuc Aparicio Pérez
1217100848

Los presos politicos una vez instaurados en las cárceles tenian permitido el accesso
de un paquete que contenia articulos para la supervivencia de este, los familiares
llevaban el producto a la cárcel pero como solo tenian ese punto de accesso,
los regsitros policiacos de esta paquete provocaba que el preso sollo tuviera
lo que la policia quiciera.
'''

from abc import ABC, abstractmethod

class PaquetesPersonales(ABC):

    @abstractmethod
    def Lista(self):
        pass

class FamiliarPreso(PaquetesPersonales):
    def Lista(self):
        print("Lleva una lista de comida como:"+
              "Chorizo,Azúcar,Café,Chocolate,"+
              "Pastillas,Sal,Pan,Pasta Dental")
        
class PoliciaPoliticaProxy(PaquetesPersonales):
     def __init__(self,familiar_preso:FamiliarPreso):
        self._FamiliarPreso = FamiliarPreso()

     def Lista(self):

        if self.aprovarProductos():
            self._FamiliarPreso.Lista()
            self.accesoProductos()

     def aprovarProductos(self):
        print("La lista de productos permitidos solo sera: Sal,Pan,Pasta Dental,Pastillas")
        return True

     def accesoProductos (self):
        print("Tiren los productos restantes")


def PresoPolitico(PaquetesPersonales):
    PaquetesPersonales.Lista()

if __name__ == "__main__":
    print("Lo que manda la familia a un preso politico")
    Familiar = FamiliarPreso()
    PresoPolitico(Familiar)

    print("")

    print("Lo que entraga la Policia al preso politico")
    entrega = PoliciaPoliticaProxy(FamiliarPreso)
    PresoPolitico(entrega)

    
