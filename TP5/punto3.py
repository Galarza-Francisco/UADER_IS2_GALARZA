from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

class ConcreteSubject(Subject):
    _state: int = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self._state)

    def some_business_logic(self, id) -> None:
        self._state = id
        print(f"Sujeto: cambio de estado a:  {self._state}")
        self.notify()

class Observer(ABC):
    _id: str

    def __init__(self, id: str):
        self._id = id

    @abstractmethod
    def update(self, state: int) -> None:
        pass

class ConcreteObserver(Observer):
    def update(self, state: int) -> None:
        if state == self._id:
            print(f"Suscriptor (ID: {self._id}): Reaccionó al evento")

if __name__ == "__main__":
    subject = ConcreteSubject()

    # Crear suscriptores con ID
    observers = [ConcreteObserver("1234"), ConcreteObserver("5678"), ConcreteObserver("9123"), ConcreteObserver("4567")]

    # Subscribir los observadores 
    for observer in observers:
        subject.attach(observer)

    #emitir 8 id, que 4 coincidan con los observadores
    ids_emitidos = ["1234", "1122", "9123", "9123", "3344", "9991", "4567", "6571"]
    for id_emitido in ids_emitidos:
        print(f"Emitiendo ID: {id_emitido}")
        subject.some_business_logic(id_emitido)

    # Desuscribir un observador
    subject.detach(observers[0])

    #emitir id de un observador para eliminarlo y ver si responde
    subject.some_business_logic("1234")
