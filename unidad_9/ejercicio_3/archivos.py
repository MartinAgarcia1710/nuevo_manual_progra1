# -*- coding: utf-8 -*-
def mostrar_numerado(nombre):
    """Muestra cada línea del archivo precedida por su número."""
    with open(nombre, "r", encoding="utf-8") as f:
        for i, linea in enumerate(f, 1):
            print(f"{i}: {linea.strip()}")
