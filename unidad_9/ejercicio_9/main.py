# -*- coding: utf-8 -*-
from archivos import copiar

with open("original.txt", "w", encoding="utf-8") as f:
    f.write("Contenido a copiar")

copiar("original.txt", "copia.txt")
print("Copia:", open("copia.txt", encoding="utf-8").read())
