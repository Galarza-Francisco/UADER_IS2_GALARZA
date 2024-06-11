from common.gestorPagos import GestorPagos

class ControladorCuentas:
    def __init__(self, json_file):
        self.gestor_pagos = GestorPagos(json_file)

    def realizar_pago(self, pedido, monto_pago):
        self.gestor_pagos.realizar_pago(pedido, monto_pago)

    def listar_pagos(self):
        self.gestor_pagos.listar_pagos()
