#*--------------------------------------------------
#* proxy.py
#* excerpt from https://refactoring.guru/design-patterns/proxy/python/example
#*--------------------------------------------------

from abc import ABC, abstractmethod
import os
import sys

# Definicion de la interface ping - contiene la logica para hacer ping a un IP
class Ping(ABC):

    @abstractmethod
    def execute(self, string: str) -> None:
        pass

    @abstractmethod
    def executefree(self, string: str) -> None:
        pass


# Implementacion del metodo de la clase ping. para hacer los 10 intentos de ping
class RealPing(Ping):
    def execute(self, string: str) -> None:   #Execute toma un string como entrada y comprueba conexion con el comando ping del s.o
        if not string.startswith("192."): # validacion de la ip arranca con 192
            print("Dirección IP inválida")
            return
        for i in range(10): # si la ip es valida entra al ciclo y hace los ping al host
            response = os.system("ping -c 1 " + string)
            if response == 0: #si la response es o el host esta en linea sino el host esta desconectado     
                print(f"{string} está en línea.")
            else:
                print(f"{string} está desconectado.")
                sys.exit() #finaliza la ejecucion en el caso de estar desconectado el host.

    def executefree(self, string: str) -> None: #en este no se evalua la IP y dentro funciona igual que execute
        for i in range(10):
            response = os.system("ping -c 1 " + string)
            if response == 0:
                print(f"{string} está en línea.")
            else:
                print(f"{string} está desconectado.")
                sys.exit()

# Implementación de PingProxy que actúa como un proxy para RealPing
class PingProxy(Ping):
    def __init__(self):
        self._ping = RealPing()


    # Método para ejecutar la clase ping 
    def execute(self, string: str) -> None:
        if string == "192.168.0.254":
            self._ping.executefree("www.google.com")  # Si IP es 192.168.0.254,se hace ping a www.google.com
        else:
            self._ping.execute(string)  # En cualquier otro caso, ping normal

    # Método para ejecutar ping sin restriccion de IP
    def executefree(self, string: str) -> None:
        self._ping.executefree(string)

# Función cliente para demostrar el uso de Ping y PingProxy
def client_code(ping: Ping, string: str) -> None:
    ping.execute(string)

if __name__ == "__main__":
    proxy = PingProxy()

    # Uso 
    print("Ping a una dirección inválida:")
    print('ip:  8.8.8.8')
    client_code(proxy, "8.8.8.8")
    print()

    print("Ping a una dirección en línea (Google):")
    print('ip:  192.168.0.254')
    client_code(proxy, "192.168.0.254")
    print()

    print("Ping a una dirección desconectada:")
    print('ip: 192.168.0.255')
    client_code(proxy, "192.168.0.255")
