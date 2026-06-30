# -*- coding: utf-8 -*-
def buscar(lista, valor):
    """Indica si un valor está en la lista, de forma recursiva."""
    if not lista:
        return False
    if lista[0] == valor:
        return True
    return buscar(lista[1:], valor)
