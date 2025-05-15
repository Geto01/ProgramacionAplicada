from operaciones_matematicas import OperacionesMatematicas

class CalculadoraUI:
    def __init__(self):
        self.operaciones = OperacionesMatematicas()

    def pedir_numeros(self):
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        return a, b

    def iniciar(self):
        while True:
            print("\n--- Menú de la Calculadora ---")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")
            print("5. Módulo")
            print("6. Salir")

            opcion = input("Elige una opción (1-6): ")

            if opcion == "6":
                print("👋 Gracias por usar la calculadora.")
                break

            a, b = self.pedir_numeros()

            if opcion == "1":
                print("Resultado:", self.operaciones.sumar(a, b))
            elif opcion == "2":
                print("Resultado:", self.operaciones.restar(a, b))
            elif opcion == "3":
                print("Resultado:", self.operaciones.multiplicar(a, b))
            elif opcion == "4":
                print("Resultado:", self.operaciones.dividir(a, b))
            elif opcion == "5":
                print("Resultado:", self.operaciones.modulo(a, b))
            else:
                print("❌ Opción no válida.")