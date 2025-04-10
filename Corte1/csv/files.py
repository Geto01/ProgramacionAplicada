import csv
import random

# Generar números aleatorios entre 0 y 1
numeros_aleatorios = [[random.randint(0, 1) for i in range(5)] for i in range(3)]

# Crear y escribir en el archivo CSV con los números aleatorios
with open("numeros.csv", "w", newline="") as numero:
    writer = csv.writer(numero, delimiter=";")
    writer.writerows(numeros_aleatorios)

# lista de nombres y apellidos
names = [ 
    ["julian", "rodriguez", "camila", "camelo"],
    ["jorge", "torres", "maria", "ortega"],
    ["alan", "gutierrez", "sara", "jimena"],
    ["elias", "taboada", "valentina", "girata"]
]

# Crear y escribir en el archivo CSV con los nombres y apellidos
with open("names.csv","w", newline="") as w:
    writer= csv.writer(w, delimiter=";")
    writer.writerows(names)

# Leer el archivo CSV de nombres y apellidos
with open("names.csv") as r:
    reader= csv.reader(r, delimiter=";")
    for row in reader:
      print("Nombre: {0}, Apellido: {1}, Nombre: {2}, Apellido: {3}".format(row[0],row[1],row[2],row[3]))