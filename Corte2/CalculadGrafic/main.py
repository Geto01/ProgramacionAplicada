# name: main.py
import tkinter as tk
from calculadora import Calculator

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()