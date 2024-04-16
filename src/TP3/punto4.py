#!/usr/bin/python3.7
#*--------------------------------------------------
#* factory.py
#* excerpt from https://refactoring.guru/design-patterns/factory/python/example
#*--------------------------------------------------
from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    #creacion factura

    @abstractmethod
    
    def tipo_factura(self):

        pass

    def some_operation(self) -> str:

        # crea el objeto con el metodo
        factura = self.tipo_factura()

        result = f"condicion factura creada: {factura.operation()}\n  "

        return result


class CreatorIVAResponable(Creator):

    def tipo_factura(self) -> Factura:
        return IVAResponsable()


class CreatorIVANoInscripto(Creator):
    def tipo_factura(self) -> Factura:
        return IVANoInscripto()

class CreatorIVAExento(Creator):
    def tipo_factura(self) -> Factura:
        return IVAExento()

class Factura(ABC):


    @abstractmethod
    def operation(self) -> str:
        pass



class IVAResponsable(Factura):
    def operation(self) -> str:
        return "{IVA Responsable, impuesto 21%}"


class IVANoInscripto(Factura):
    def operation(self) -> str:
        return "{IVA No Inscripto, impuesto 10,5%}"

class IVAExento(Factura):
    def operation(self) -> str:
        return "{IVA Exento, impuesto 2,5z%}"


def client_code(creator: Creator) -> None:

    print(f"Importe total = $100.000.\n"
          f"{creator.some_operation()}", end="")



if __name__ == "__main__":
    while True:
        metodo = input("seleccionar la condicion frente al IVA : Responsable (R) - no inscripto (N) - exento (E)): ")
        if metodo == 'R':
            client_code(CreatorIVAResponable())
            break
        elif metodo == 'N':   
            client_code(CreatorIVANoInscripto())
            break
        elif metodo == 'E': 
            client_code(CreatorIVAExento())
            break
        else:
            print('ingresar solo la letra, o un valor valido')
        