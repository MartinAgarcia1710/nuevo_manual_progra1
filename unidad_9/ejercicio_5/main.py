# -*- coding: utf-8 -*-
from archivos import contar_lineas

with open("datos.txt", "w", encoding="utf-8") as f:
    f.write("a\nb\nc\nd\n")

print("Cantidad de líneas:", contar_lineas("datos.txt"))
