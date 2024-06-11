
"""import sys
from original.recuperadorOriginal import recuperadorTokenOriginal
from singleton.recuperadorSingleton import recuperadorTokenSingleton
"""
#Copyright UADERFCyT-IS2©2024 Todos los derechos reservados.
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
    main()"""

import sys
from common.controladorCuentas import ControladorCuentas


"""
Copyright UADERFCyT-IS2©2024 Todos los derechos reservados.
"""
VERS = '1.2'

def main():
    # Verificar si se proporcionan suficientes argumentos
    if len(sys.argv) == 2 and sys.argv[1] == "-v":
        print("Versión:", VERS)
        sys.exit(0)  # Salir con código 0 (éxito)
    elif len(sys.argv) != 4:
        print("Error: Debe proporcionar el número de pedido, el monto del pago y el archivo JSON")
        sys.exit(1)

    # Obtener el número de pedido y el monto del pago de los argumentos de la línea de comandos
    pedido = int(sys.argv[1])
    monto_pago = float(sys.argv[2])
    json_file = sys.argv[3]

    # Crear una instancia del controlador de cuentas
    controlador = ControladorCuentas(json_file)

    # Realizar el pago
    controlador.realizar_pago(pedido, monto_pago)

    # Guardar los datos actualizados en el archivo JSON
    controlador.guardar_datos(json_file)

    # Listar los pagos realizados
    controlador.listar_pagos()

if __name__ == "__main__":
    main()
