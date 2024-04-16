#!/usr/python
#*--------------------------------------------------
#* singleton.py
#* excerpt from https://refactoring.guru/design-patterns/singleton/python/example
#*--------------------------------------------------
from email.mime import base

class SingletonMeta(type): #constructor
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}  #define instancia
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances: # si instancia esta vacia, es la 1ra vez q llama
            instance = super().__call__(*args, **kwargs) #llama al super constructor
            cls._instances[cls] = instance 
        return cls._instances[cls]

class Impuestos(metaclass=SingletonMeta):
    def calcular_impuestos(self, base_imponible):
        iva = float(base_imponible) * 0.21
        iibb = float(base_imponible) * 0.05
        contribuciones_municipales = float(base_imponible) * 0.012

        total_impuestos = iva + iibb + contribuciones_municipales
        return total_impuestos

    @classmethod
    def getIVA(cls):
        return "21%"

    @classmethod
    def getIIBB(cls):
        return "5%"

    @classmethod
    def getContribucionesMunicipales(cls):
        return "1,2%"

if __name__ == "__main__":
    s1 = Impuestos()
    s2 = Impuestos()

    if id(s1) == id(s2):
        base_imponible = float(input("Ingrese un valor: "))
        print('Base imponible: ', base_imponible)
        print('Cálculo  IVA:', base_imponible, '+', Impuestos.getIVA(), '=', base_imponible + float(base_imponible) * 0.21)
        print('Cálculo IIBB:', base_imponible, '+', Impuestos.getIIBB(), '=', base_imponible + float(base_imponible) * 0.05)
        print('Cálculo imp. Municipales:', base_imponible, '+', Impuestos.getContribucionesMunicipales(), '=', base_imponible + float(base_imponible) * 0.012)
        print('Total de impuestos:', s1.calcular_impuestos(base_imponible))
    else:
        print("las variables tienen instancias diferentes")
