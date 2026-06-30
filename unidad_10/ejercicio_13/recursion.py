# -*- coding: utf-8 -*-
def suma_digitos(n):
    """Suma los dígitos de un número de forma recursiva."""
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)
