# cuenta_bancaria.py
class CuentaBancaria:
    def __init__(self):
        self.saldo = 0

    def ver_saldo(self):
        return f"Saldo actual: ${self.saldo}"

    def consignar(self, monto):
        if monto > 0:
            self.saldo += monto
            return f"Has consignado: ${monto}"
        return "No puedes consignar un monto negativo."

    def retirar(self, monto):
        if monto <= 0:
            return "No puedes retirar un monto negativo o cero."
        elif monto > self.saldo:
            return "Saldo insuficiente."
        self.saldo -= monto
        return f"Has retirado: ${monto}"



