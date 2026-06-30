# -*- coding: utf-8 -*-
def contar(lista):
    """Cuenta los elementos de una lista sin usar len()."""
    if not lista:
        return 0
    return 1 + contar(lista[1:])
