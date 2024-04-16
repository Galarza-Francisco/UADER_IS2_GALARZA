import os
#*--------------------------------------------------------------------
#* La clase Director orquesta la construcción del objeto indicando 
#* el orden en que deben llamarse sus componentes, los mismos son
#* genéricos y dependerán del builder específico utilizado sus
#* valores concretos
#*--------------------------------------------------------------------
class Director:#dirige la contruccion del objeto, indicando el orden de sus comoponentes
   __builder = None
   
   def setBuilder(self, builder):
      self.__builder = builder


   def getAvion(self):
      avion = Avion() 
      # 1 fuselaje
      fuselaje = self.__builder.getBody()
      avion.setBody(fuselaje)
      
      
      # 2 motor
      turbinas = self.__builder.getTurbinas()
      avion.setTurbinas(turbinas)

      # 3 alas
      alas = self.__builder.getAlas()
      avion.setAlas(alas)

      # 4 aterrizaje
      tren = self.__builder.getTrenDeAterrizaje()
      avion.setTren(tren)

      # Retorna el avion 
      return avion


class Avion:
   def __init__(self):
      self.__turbinas = list()
      self.__alas = list()
      self.__tren = None
      self.__body = None

   def setBody(self, fuselaje):
      self.__body = fuselaje

   def setAlas(self, alas):
      self.__alas = alas

   def setTurbinas(self, turbinas):
      self.__turbinas = turbinas

   def setTren(self, tren):
      self.__tren = tren

   def specification(self):
      print ("fuselaje: %s" % (self.__body.shape))
      print ("Alas: %d" % (self.__alas.amount))
      print ("Turbinas: %d\'" % (self.__turbinas.amount))
      print ("Tren de aterrizaje: %d\'" % (self.__tren.amount))


class Builder:# clase que define la interface de los metodos que el builder especifico tien q implemtenar

      def getBody(self): pass
      def getTurbinas(self): pass
      def getAlas(self): pass
      def getTrenDeAterrizaje(self): pass


class AvionBuilder(Builder):#hoja de ruta para construir el avion -  tiene que tener todas estas partes
   
   def getTurbinas(self):
      turbinas = Turbinas()
      turbinas.amount = 4
      return turbinas
   
   def getAlas(self):
      alas = Alas()
      alas.amount = 2
      return alas

   def getTrenDeAterrizaje(self):
      tren = Tren()
      tren.amount = 1
      return tren  
   
   def getBody(self):
      fuselaje = Body()
      fuselaje.shape = "A001"
      return fuselaje


class Body: #definicion de partes genericas del avion
   shape = None

class Turbinas:
   amount = None

class Alas:
   amount = None

class Tren:
   amount = None



def main():

   avionBuilder = AvionBuilder() #instancia de clase resultado y guia de la construcccion
   director = Director()
  
   director.setBuilder(avionBuilder) #paso de la hora de ruta de la construccion de avion

   avion = director.getAvion() # obliga a agregar componentes de un avion segun la hoja de ruta


   avion.specification() #verifica si esta completa la consutrccion
   print ("\n\n")


if __name__ == "__main__":
   os.system("clear")
   print('construccion de avion aplicando patron Builder')
   print()
   main()