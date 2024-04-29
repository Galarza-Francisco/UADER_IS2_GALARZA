import os
class IteradorCadena:
    def __init__(self, cadena):
        self.cadena = cadena
        self.posicion = 0
        self.direccion = 1  # 1 para sentido directo, -1 para sentido inverso

    def __iter__(self):
        return self

    def __next__(self):
        if 0 <= self.posicion < len(self.cadena):
            caracter = self.cadena[self.posicion]
            self.posicion += self.direccion
            return caracter
        else:
            raise StopIteration

    def invertir_direccion(self):
        self.direccion *= -1


class CadenaIterable:
    def __init__(self, cadena):
        self.cadena = cadena

    def iterador_directo(self):
        return IteradorCadena(self.cadena)

    def iterador_inverso(self):
        iterador = IteradorCadena(self.cadena)
        iterador.posicion = len(self.cadena) - 1
        iterador.direccion = -1
        return iterador


if __name__ == "__main__":
    cadena = "francisco"
    
    iterable = CadenaIterable(cadena)

    print("directo:")
    iterador_directo = iterable.iterador_directo()
    for caracter in iterador_directo:
        print(caracter)

    print("\ninverso:")
    iterador_inverso = iterable.iterador_inverso()
    for caracter in iterador_inverso:
        print(caracter)
