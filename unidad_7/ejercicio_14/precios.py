# -*- coding: utf-8 -*-
def unir(d1, d2):
    """Combina dos diccionarios en uno nuevo."""
    resultado = d1.copy()
    resultado.update(d2)
    return resultado
