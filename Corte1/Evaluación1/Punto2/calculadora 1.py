class Calculadora:
    def _init_(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: División por cero"

    def modulo(self, a, b):
        try:
            return a % b
        except ZeroDivisionError:
            return "Error: División por cero"

if __name__ == "__main__":
    calculadora = Calculadora()
    print(calculadora.add(5, 7))
    print(calculadora.subtract(45, 11))
    print(calculadora.multiply(3, 2))
    print(calculadora.divide(10, 4))
    print(calculadora.modulo(10, 3))