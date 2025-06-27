#name: calculator.py
import tkinter as tk
from tkinter import ttk
from procesos import process

class Calculator:
    def __init__(self, root):
        self.engine = process()
        self.root = root
        self.root.title("Calculadora")
        self.create_widgets()

    def create_widgets(self):
        self.a_entry = ttk.Entry(self.root)
        self.a_entry.grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(self.root, text="Número A:").grid(row=0, column=0)

        self.b_entry = ttk.Entry(self.root)
        self.b_entry.grid(row=1, column=1, padx=5, pady=5)
        ttk.Label(self.root, text="Número B:").grid(row=1, column=0)

        self.result_label = ttk.Label(self.root, text="Resultado:")
        self.result_label.grid(row=2, column=0, columnspan=2)

        buttons = [
            ("Sumar", self.engine.add),
            ("Restar", self.engine.substract),
            ("Multiplicar", self.engine.multiply),
            ("Dividir", self.engine.divide),
            ("Módulo", self.engine.modulo)
        ]

        for idx, (text, func) in enumerate(buttons):
            ttk.Button(
                self.root,
                text=text,
                command=lambda f=func: self.calculate(f)
            ).grid(row=3 + idx, column=0, columnspan=2, sticky="ew", pady=2)

    def calculate(self, operation):
        try:
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            result = operation(a, b)
        except ValueError:
            result = "Entrada inválida"
        self.result_label.config(text=f"Resultado: {result}")