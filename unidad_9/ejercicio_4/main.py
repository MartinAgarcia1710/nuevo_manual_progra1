# -*- coding: utf-8 -*-
from archivos import agregar_linea

with open("registro.txt", "w", encoding="utf-8") as f:
    f.write("Linea inicial\n")

agregar_linea("registro.txt", "Linea agregada")
print(open("registro.txt", encoding="utf-8").read())
