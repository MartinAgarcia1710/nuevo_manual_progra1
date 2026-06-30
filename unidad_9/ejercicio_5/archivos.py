# -*- coding: utf-8 -*-
def contar_lineas(nombre):
    """Cuenta las líneas de un archivo."""
    with open(nombre, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)
