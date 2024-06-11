import json
from singleton.recuperadorSingleton import recuperadorTokenSingleton
from common.cadenaComando import CuentaBancaria, ComandoPago, CadenaPagos
from common.iterator import PagosIterator

class GestorPagos:
    def __init__(self, json_file):
        # Cargar los datos del archivo JSON
        with open(json_file, 'r') as file:
            self.sitedata = json.load(file)

        self.cuentas = {
            "token1": CuentaBancaria("token1", self.sitedata["token1"]["saldo"]),
            "token2": CuentaBancaria("token2", self.sitedata["token2"]["saldo"])
        }

        self.recuperador = recuperadorTokenSingleton()
        self.pagos_realizados = []

        self.cadena_pagos = CadenaPagos([
            ComandoPago(self.cuentas["token1"]),
            ComandoPago(self.cuentas["token2"])
        ])

    def realizar_pago(self, pedido, monto_pago):
        banco_seleccionado = self.seleccionar_banco(pedido)
        clave = self.recuperador.get_token('sitedata.json', banco_seleccionado)

        if self.cuentas[banco_seleccionado].saldo >= monto_pago:
            print(f"Pedido {pedido}: Pago de ${monto_pago} realizado con éxito utilizando el token {banco_seleccionado}")
            self.cuentas[banco_seleccionado].saldo -= monto_pago
            self.pagos_realizados.append((pedido, monto_pago, banco_seleccionado, clave))
        else:
            print(f"Pedido {pedido}: Error - Saldo insuficiente en el token {banco_seleccionado}")

    def listar_pagos(self):
        print("Lista de pagos realizados:")
        for pago in PagosIterator(self.pagos_realizados):
            print(f"Pedido {pago[0]}: Pago de ${pago[1]} realizado utilizando el token {pago[2]}")

    def guardar_datos(self, json_file):
        # Guardar los datos actualizados en el archivo JSON
        for banco, cuenta in self.cuentas.items():
            self.sitedata[banco]["saldo"] = cuenta.saldo
        with open(json_file, 'w') as file:
            json.dump(self.sitedata, file, indent=4)

    def seleccionar_banco(self, pedido):
        # Obtener los bancos disponibles
        bancos = list(self.sitedata.keys())
        # Seleccionar el banco basado en el número de pedido (alternar entre bancos)
        indice_banco = pedido % len(bancos)
        return bancos[indice_banco]
