# -*- coding: utf-8 -*-
from archivos import estadisticas

with open("numeros.txt", "w", encoding="utf-8") as f:
    f.write("5\n12\n3\n20\n8\n")

print(estadisticas("numeros.txt"))
