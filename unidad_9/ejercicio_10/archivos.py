# -*- coding: utf-8 -*-
def promedio_archivo(nombre):
    """Calcula el promedio de los números (uno por línea) de un archivo."""
    with open(nombre, "r", encoding="utf-8") as f:
        numeros = [float(linea) for linea in f if linea.strip()]
    return sum(numeros) / len(numeros) if numeros else 0
