#!/usr/bin/python3.7
#*--------------------------------------------------
#* factory.py
#* excerpt from https://refactoring.guru/design-patterns/factory/python/example
#*--------------------------------------------------
from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    #se crea la hambur

    @abstractmethod
    #metodo entrega
    def metodo_entrega(self):
        pass

    def some_operation(self) -> str:

        # crea el objeto
        hamburguesa = self.metodo_entrega()

        # uso del prod
        result = f"busqueda del pedido: {hamburguesa.operation()}\n"

        return result



class CreatorEntregaMostrador(Creator):

    def metodo_entrega(self) -> Hamburguesa:
        return EntregaMostrador()


class CreatorRetiradaPorCliente(Creator):
    def metodo_entrega(self) -> Hamburguesa:
        return RetiradaPorCliente()

class CreatorEnvioDelivery(Creator):
    def metodo_entrega(self) -> Hamburguesa:
        return EnvioDelivery()

class Hamburguesa(ABC):

    @abstractmethod
    def operation(self) -> str:
        pass


class EntregaMostrador(Hamburguesa):
    def operation(self) -> str:
        return "Entregada en mostrador"


class RetiradaPorCliente(Hamburguesa):
    def operation(self) -> str:
        return "Retirada por cliente"

class EnvioDelivery(Hamburguesa):
    def operation(self) -> str:
        return "Envío por delivery"


def client_code(creator: Creator) -> None:
    print(f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    while True:
        metodo = input("Ingrese el metodo de entrega para la hamburguesa (mostrador (M) - retiro (R) - delivery (D)) ")
        if metodo == 'M':
            client_code(CreatorEntregaMostrador())
            break
        elif metodo == 'R':   
            client_code(CreatorRetiradaPorCliente())
            break
        elif metodo == 'D': 
            client_code(CreatorEnvioDelivery())
            break
        else:
            print('ingrese solo la letra, elija una de las opciones que se muestran')
        