class Manejador: #clase base para manejar solicitudes 
    def __init__(self, sucesor=None):
        self.sucesor = sucesor

    def manejar_solicitud(self, numero):#metodo que se ejecuta por cada nro
        if self.sucesor:
            return self.sucesor.manejar_solicitud(numero)
        return f"El número {numero} no fue consumido"


class ManejadorPrimos(Manejador): #clase heredada y modifica el metodo para nros primso
    def manejar_solicitud(self, numero):
        if self.es_primo(numero):
            return f"El ManejadorPrimos consumió el número primo {numero}"
        else:
            return super().manejar_solicitud(numero)

    def es_primo(self, numero):
        if numero < 2:
            return False
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False
        return True


class ManejadorPares(Manejador):#clase heredada y modificada para pares
    def manejar_solicitud(self, numero):
        if numero % 2 == 0:
            return f"El ManejadorPares consumió el número par {numero}"
        else:
            return super().manejar_solicitud(numero)
        p


class ProcesadorNumeros: #da el orden de los manejadores
    def __init__(self):
        self.cadena = ManejadorPrimos(ManejadorPares())

    def procesar_numeros(self):
        for numero in range(1, 101):
            print()
            print(self.cadena.manejar_solicitud(numero))
            print()


if __name__ == "__main__":#creacion de instancia
    procesador = ProcesadorNumeros()
    procesador.procesar_numeros()
