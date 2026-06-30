# -*- coding: utf-8 -*-
def sumar_validos(lista):
    """Suma solo los elementos que se pueden convertir a número."""
    total = 0
    for elemento in lista:
        try:
            total += float(elemento)
        except (ValueError, TypeError):
            pass
    return total
