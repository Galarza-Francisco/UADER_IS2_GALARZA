class CuentaBancaria:
    def __init__(self, nombre, saldo_inicial):
        self.nombre = nombre
        self.saldo = saldo_inicial

    def puede_realizar_pago(self, monto):
        return self.saldo >= monto

    def realizar_pago(self, monto):
        if self.puede_realizar_pago(monto):
            self.saldo -= monto
            return True
        return False

    def __str__(self):
        return f"{self.nombre}: ${self.saldo}"

class ComandoPago:
    def __init__(self, cuenta, siguiente_comando=None):
        self.cuenta = cuenta
        self.siguiente_comando = siguiente_comando

    def manejar_pago(self, pedido, monto):
        if self.cuenta.puede_realizar_pago(monto):
            self.cuenta.realizar_pago(monto)
            print(f"Pedido {pedido}: Pago de ${monto} realizado con éxito utilizando el token {self.cuenta.nombre}")
        elif self.siguiente_comando is not None:
            self.siguiente_comando.manejar_pago(pedido, monto)
        else:
            print(f"Pedido {pedido}: Error - Saldo insuficiente en todas las cuentas")

class CadenaPagos:
    def __init__(self, comandos):
        self.comandos = comandos

    def manejar_pago(self, pedido, monto):
        if self.comandos:
            self.comandos[0].manejar_pago(pedido, monto)

    def __str__(self):
        return "\n".join([str(comando.cuenta) for comando in self.comandos])
