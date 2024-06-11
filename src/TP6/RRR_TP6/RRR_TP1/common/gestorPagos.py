import json
from singleton.recuperadorSingleton import recuperadorTokenSingleton

class GestorPagos:
    def __init__(self, json_file):
        with open(json_file, 'r') as file:# Cargar los datos del  json
            self.sitedata = json.load(file)
        self.recuperador = recuperadorTokenSingleton()
        self.pagos_realizados = []

    def seleccionar_banco(self, pedido):
        bancos = list(self.sitedata.keys())  # Obtener los bancos disponibles
        indice_banco = pedido % len(bancos)         # Seleccionar el banco segun el nro pedido
        return bancos[indice_banco]

    def realizar_pago(self, pedido, monto_pago):
        banco_seleccionado = self.seleccionar_banco(pedido)
        clave = self.recuperador.get_token('sitedata.json', banco_seleccionado)
        
        if self.sitedata[banco_seleccionado]["saldo"] >= monto_pago:         # Verificar si el banco tiene saldo

            self.sitedata[banco_seleccionado]["saldo"] -= monto_pago             # Realiza pago y actualizar el saldo
            self.pagos_realizados.append((pedido, monto_pago, banco_seleccionado, clave))
            print(f"Pedido {pedido}: Pago de ${monto_pago} realizado con éxito ")
        else:
            print(f"Pedido {pedido}: Error - Saldo insuficiente en el banco {banco_seleccionado}")

    def listar_pagos(self):
        print("Lista de pagos realizados:")
        for pedido, monto_pago, banco, clave in self.pagos_realizados:
            print(f"Pedido {pedido}: Pago de ${monto_pago} realizado.")

    def guardar_datos(self, json_file):
        # guardar datos en el json
        with open(json_file, 'w') as file:
            json.dump(self.sitedata, file, indent=4)
