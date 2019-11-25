'''Patron de diseño Factory
Obtenido del libro:EL gulum de las americas
Creado:Antonio Habacuc Aparicio Pérez
1217100848

A lo largo del libro se nos va contando como el autor tuvo dos claros bandos los
que lo ayudaban y querian, y los que lo queria ver sufrir, pero no solo en las
cárceles sino tambien fuera de ellas en el mundo que en muchos casos fue
representado en la misma Onu..

'''

from abc import ABC, abstractmethod

class Gulag_America(ABC):

    @abstractmethod
    def aliados(self):
        pass

    @abstractmethod
    def villanos(self):
         pass

class Carcel(Gulag_America):
        
    def aliados(self):
        return Boitel()

    def villanos(self):
        return Capitan_Mentiras()

class Onu(Gulag_America):
    
    def aliados(self):
        return Martha()

    def villanos(self):
        return Castro()

class Ayuda(ABC):
   @abstractmethod
   def Acciones(self):
       pass
    
   @abstractmethod
   def Platicas(self):
        pass
    
class NoAyuda(ABC):
   @abstractmethod
   def Mentiras(self):
       pass
   @abstractmethod
   def Castigos(self):
        pass

class Capitan_Mentiras(NoAyuda):
    
   def Mentiras(self):
       print("Desir que la OEA no habia mandado ninuna silla de ruedas")
       
   def Castigos(self):
       print("Dejarlo sin poder salir cuando estaba invalido")
       
class Castro(NoAyuda):
    
   def Mentiras(self):
       print("Desir que se le estaba dando un adecuado tratamiento")
       
   def Castigos(self):
       print("NO dejar que la familia saliera del pais")

class Boitel (Ayuda):

   def Acciones(self):
      print("Luchar junto a él en huelgas de hambre")
   
   def Platicas(self):
        print("Platicar con él de cualquier tema siendo un apoyo")

class Martha (Ayuda):
   def Acciones(self):
      print("Llevar el caso ante todo el mundo")
   
   def Platicas(self):
        print("Platica acerca de las irregularidades cometidas.")

class Valladares:
    def vida(self):

#########CARCEL##########################################        
        c_factory = Carcel()
        c_A = c_factory.aliados()
        c_A.Acciones()
        c_A.Platicas()

        C_E = c_factory.villanos()
        C_E.Mentiras()
        C_E.Castigos()        

##########ONU#########################################
        O_factory = Onu()
        O_a = O_factory.aliados()
        O_a.Acciones()
        O_a.Platicas()
#############NO SQL######################################
        O_E = O_factory.villanos()
        O_E.Mentiras()
        O_E.Castigos()   
v = Valladares()
v.vida()
