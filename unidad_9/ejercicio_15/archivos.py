# -*- coding: utf-8 -*-
def a_mayusculas(origen, destino):
    with open(origen, "r", encoding="utf-8") as f:
        contenido = f.read()
    with open(destino, "w", encoding="utf-8") as f:
        f.write(contenido.upper())
