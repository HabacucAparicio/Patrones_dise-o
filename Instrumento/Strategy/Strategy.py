'''Patron de diseño Singleton
Obtenido del libro:EL gulum de las americas
Creado:Antonio Habacuc Aparicio Pérez
1217100848

AL hablar de abusso físicos en realida eran abusos físicos es por ello que esta esta represntacion del como le hacia para lograr el mayor terror en los presos
claro que ellos lo pensaban entre varios hombres
'''

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import random
    
class Castigos():

    def __init__(self, e: Estrategia)-> None:
        self._e = e
    
    @property
    def estrategia(self)-> Estrategia:
        return self._e

    @estrategia.setter
    def estrategia(self,e: Estrategia)-> None:

        self._e = e

    def como_castigar(self)-> None:
        print("Cual es el castigo que se debera aplicar al preso para que cambie su actitud")
        c = self._e.crear_castigo(["Pagar golpes","Pegar patadas","Golpes con machete","Picaduras con ballesta","Aislamiento",
                 "Tortura psicologica","Cadenasos","Dejarlos sin comida","Dejarlos sin agua","Balazo"])
        print(c)

class Estrategia(ABC):
    @abstractmethod
    def crear_castigo(self,datos: List)-> List:
        pass

class EA(Estrategia):
    def crear_castigo(self,datos: List )-> List:
        return sorted(datos)

class EB(Estrategia):
    def crear_castigo(self,datos: List)-> List:
        return list(reversed(sorted(datos)))
    
class EC(Estrategia):
    def crear_castigo(self,datos: List)-> List:
        cr = []
        i = 0

        while(i<10):
            nmaleatorio = random.randrange(1,10)
            cr.append(datos[i])
            i+=1
        return cr 


class EH(Estrategia):
    def crear_castigo(self,datos: List)-> List:
        return ("No los castigen")

if __name__ == "__main__":

    cas = Castigos(EA())
    print("Castigos sujeridos en orden")
    cas.como_castigar()
    print()

    print("Castigos sujeridos en orden invertido")
    cas.estrategia = EB()
    cas.como_castigar()
    print()
    
    print("Castigos sujeridos por dolor provocado")
    cas.estrategia = EC()
    cas.como_castigar()
    print()
          
    print("Castigos sujeridos por los familiares")
    cas.estrategia = EH()
    cas.como_castigar()
    print()          
    



    
