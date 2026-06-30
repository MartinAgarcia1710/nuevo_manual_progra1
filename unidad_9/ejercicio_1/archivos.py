# -*- coding: utf-8 -*-
def escribir(nombre, lineas):
    """Escribe una lista de líneas en un archivo."""
    with open(nombre, "w", encoding="utf-8") as f:
        for linea in lineas:
            f.write(linea + "\n")
