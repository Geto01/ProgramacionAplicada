from cuenta_bancaria import CuentaBancaria

class CajeroUI:
    def __init__(self):
        self.cuenta = CuentaBancaria()

    def pedir_monto(self):
        while True:
            entrada = input("Ingresa un monto: ")
            try:
                return float(entrada)
            except ValueError:
                print("Por favor, ingresa un número válido.")

    def iniciar(self):
        while True:
            print("\n--- Cajero Automático ---")
            print("1. Ver saldo")
            print("2. Consignar dinero")
            print("3. Retirar dinero")
            print("4. Salir")

            opcion = input("Elige una opción (1-4): ")

            if opcion == "1":
                print(self.cuenta.ver_saldo())
            elif opcion == "2":
                monto = self.pedir_monto()
                print(self.cuenta.consignar(monto))
            elif opcion == "3":
                monto = self.pedir_monto()
                print(self.cuenta.retirar(monto))
            elif opcion == "4":
                print("Gracias por usar el cajero. ¡Hasta luego!")
                break
            else:
                print("❌ Opción inválida. Intenta de nuevo.")
