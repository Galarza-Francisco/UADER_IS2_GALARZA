import json
from common.gestorPagos import GestorPagos

class ControladorCuentas:
    def __init__(self, json_file):
        self.gestor_pagos = GestorPagos(json_file)
        self.json_file = json_file

    def realizar_pago(self, pedido, monto_pago):
        self.gestor_pagos.realizar_pago(pedido, monto_pago)

    def listar_pagos(self):
        self.gestor_pagos.listar_pagos()

    def guardar_datos(self):
        self.gestor_pagos.guardar_datos(self.json_file)
