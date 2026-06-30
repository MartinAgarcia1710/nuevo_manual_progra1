# -*- coding: utf-8 -*-
def suma(lista):
    """Suma los elementos de una lista de forma recursiva."""
    if not lista:
        return 0
    return lista[0] + suma(lista[1:])
