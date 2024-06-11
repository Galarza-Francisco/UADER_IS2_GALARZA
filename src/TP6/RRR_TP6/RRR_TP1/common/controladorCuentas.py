import json

class ControladorCuentas:
    def __init__(self, json_file): # Cargar los datos del JSON
        with open(json_file, 'r') as file:
            self.sitedata = json.load(file)
        self.pagos_realizados = []

    def realizar_pago(self, pedido, monto_pago):
        bancos = list(self.sitedata.keys())  # Obtener los bancos y lo saldos
        indice_banco = pedido % len(bancos)  # Seleccionar el banco segun el nro de pedido
        banco_seleccionado = bancos[indice_banco]

        if self.sitedata[banco_seleccionado]["saldo"] >= monto_pago: # Verificar saldo suficiente
            # Realizar el pago y actualizar el saldo
            self.sitedata[banco_seleccionado]["saldo"] -= monto_pago
            self.pagos_realizados.append((pedido, monto_pago, banco_seleccionado))
            print(f"Pedido {pedido}: Pago de ${monto_pago} realizado con éxito utilizando el banco {banco_seleccionado}")
        else:
            print(f"Pedido {pedido}: Error - Saldo insuficiente en el banco {banco_seleccionado}")

    def listar_pagos(self):
        print("Lista de pagos realizados:")
        for pedido, monto_pago, banco in self.pagos_realizados:
            print(f"Pedido {pedido}: Pago de ${monto_pago} realizado utilizando el banco {banco}")

    def guardar_datos(self, json_file):
        with open(json_file, 'w') as file: # Guardar los datos actualizados en el json
            json.dump(self.sitedata, file, indent=4)
