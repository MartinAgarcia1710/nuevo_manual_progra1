# -*- coding: utf-8 -*-
from archivos import a_mayusculas

with open("entrada.txt", "w", encoding="utf-8") as f:
    f.write("texto en minusculas")

a_mayusculas("entrada.txt", "salida.txt")
print(open("salida.txt", encoding="utf-8").read())
