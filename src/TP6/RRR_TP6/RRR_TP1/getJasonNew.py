
import sys
from original.recuperadorOriginal import recuperadorTokenOriginal
from singleton.recuperadorSingleton import recuperadorTokenSingleton
"""
Copyright UADERFCyT-IS2©2024 Todos los derechos reservados.
"""
VERS ='1.1'
def main():
    # Verificar si se proporcionan suficientes argumentos
    if len(sys.argv) == 2 and sys.argv[1] == "-v":
        print("Versión:", VERS)
        sys.exit(0)  # Salir con código 0 (éxito)
    elif len(sys.argv) != 4:
        print("Error: elegir una forma de implementacion")
        sys.exit(1)
    #obtener los argumentos de la consola
    jsonfile = sys.argv[1]
    jsonkey = sys.argv[2]
    implementation = sys.argv[3]
    if implementation not in ["original", "singleton"]:
        print("implementacion invalida, elegir singleton u original")
        sys.exit(1)
    #seleccionar la implementacion segun el argumento 3 de la consola
    if implementation == "original":
        recuperador = recuperadorTokenOriginal()
    elif implementation == "singleton":
        recuperador = recuperadorTokenSingleton()
    #obtener el toen con la implementacion que se selecciono en consola
    token = recuperador.get_token(jsonfile, jsonkey)
    #imprimir token
    print("Token: ", token)

if __name__ == "__main__":
    main()