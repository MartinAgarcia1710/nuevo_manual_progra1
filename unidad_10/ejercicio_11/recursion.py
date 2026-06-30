# -*- coding: utf-8 -*-
def maximo(lista):
    """Devuelve el mayor elemento de una lista de forma recursiva."""
    if len(lista) == 1:
        return lista[0]
    resto = maximo(lista[1:])
    return lista[0] if lista[0] > resto else resto
