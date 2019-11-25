'''Patron de diseño Singleton
Obtenido del libro:EL gulum de las americas
Creado:Antonio Habacuc Aparicio Pérez
1217100848

Pero los abusos no solo eran de manera fisica si no tambien en la comida que se daba,
ya que sin importar el dia esta no cambiaba dando como resultado un suculento menú.
'''

class ComidaPrision(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = ("Macarrones hervidos, caldo grasoso, pedazo de pan. Identificador")+str(id(cls))
        return cls.instance

Lunes = ComidaPrision()
Martes = ComidaPrision()
Miercoles = ComidaPrision()
Jueves = ComidaPrision()
Viernes = ComidaPrision()
Sabado = ComidaPrision()
Domingo = ComidaPrision()

print("El menú dado a los presos sera \n"+
      "Lunes: "+ Lunes+
      "\nMartes: "+ Martes +
      "\nMiercoles: "+Miercoles+
      "\nJueves: "+Jueves+
      "\nViernes: "+Viernes+
      "\nSabado: "+ Sabado +
      "\nDomingo: "+ Domingo)
