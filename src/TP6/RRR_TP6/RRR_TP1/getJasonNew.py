import sys
from common.controladorCuentas import ControladorCuentas
"""
Francisco Galarza.
Copyright UADERFCyT-IS2©2024 Todos los derechos reservados.
"""
VERS = '1.2'
def main():
    """
    Función principal para manejar los pagos.
    Esta función verifica los argumentos de la consola,
    realiza el pago y lista los pagos realizados.
    """
    # Verificar si se proporcionan suficientes argumentos
    if len(sys.argv) == 2 and sys.argv[1] == "-v":
        print("Versión:", VERS)
        sys.exit(0)  # Salir con código 0 (éxito)
    elif len(sys.argv) != 3:
        print("Error: Debe proporcionar el número de pedido y el monto del pago")
        sys.exit(1)

    pedido = int(sys.argv[1])
    monto_pago = float(sys.argv[2])
    # Crear el controlador de cuentas
    controlador = ControladorCuentas('sitedata.json')
    # Realizar el pago
    controlador.realizar_pago(pedido, monto_pago)
    # Guardar los datos actualizados
    controlador.gestor_pagos.guardar_datos('sitedata.json')
    # Listar los pagos realizados
    controlador.gestor_pagos.listar_pagos()

if __name__ == "__main__":
    main()
