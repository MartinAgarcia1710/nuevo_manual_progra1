# -*- coding: utf-8 -*-
from archivos import promedio_archivo

with open("numeros.txt", "w", encoding="utf-8") as f:
    f.write("10\n20\n30\n40\n")

print("Promedio:", promedio_archivo("numeros.txt"))
