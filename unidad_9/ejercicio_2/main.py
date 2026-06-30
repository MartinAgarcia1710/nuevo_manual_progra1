# -*- coding: utf-8 -*-
from archivos import leer_todo

with open("datos.txt", "w", encoding="utf-8") as f:
    f.write("Linea 1\nLinea 2\nLinea 3\n")

print(leer_todo("datos.txt"))
