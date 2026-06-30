# -*- coding: utf-8 -*-
def contar_ocurrencias(lista, valor):
    """Cuenta cuántas veces aparece un valor en la lista."""
    if not lista:
        return 0
    actual = 1 if lista[0] == valor else 0
    return actual + contar_ocurrencias(lista[1:], valor)
