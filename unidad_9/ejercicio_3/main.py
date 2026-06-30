# -*- coding: utf-8 -*-
from archivos import mostrar_numerado

with open("texto.txt", "w", encoding="utf-8") as f:
    f.write("uno\ndos\ntres\n")

mostrar_numerado("texto.txt")
