
import sys
from common.controladorCuentas import ControladorCuentas

"""
Copyright UADERFCyT-IS2©2024 Todos los derechos reservados.
"""
VERS = '1.2'

def main():
    # Verificar si estan todos los argumentos
    if len(sys.argv) == 2 and sys.argv[1] == "-v":
        print("Versión:", VERS)
        sys.exit(0)  # Salir con código 0 (éxito)
    elif len(sys.argv) != 4:
        print("Error: Debe proporcionar el número de pedido, el monto del pago y el archivo JSON")
        sys.exit(1)

    #obtener nro de pedido y el monto de pagos
    pedido = int(sys.argv[1])
    monto_pago = float(sys.argv[2])
    json_file = sys.argv[3]

    # Crear una instancia del controlador de cuentas
    controlador = ControladorCuentas(json_file)

    # hace el pago
    controlador.realizar_pago(pedido, monto_pago)

    # Guardar llos datos en el json
    controlador.guardar_datos()

    # Lista pagos realizados
    controlador.listar_pagos()

if __name__ == "__main__":
    main()
