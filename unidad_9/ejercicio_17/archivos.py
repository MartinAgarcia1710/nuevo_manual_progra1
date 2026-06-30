# -*- coding: utf-8 -*-
def filtrar(origen, destino, palabra):
    """Copia a destino solo las líneas de origen que contienen la palabra."""
    with open(origen, "r", encoding="utf-8") as f:
        lineas = [l for l in f if palabra in l]
    with open(destino, "w", encoding="utf-8") as f:
        f.writelines(lineas)
    return len(lineas)
