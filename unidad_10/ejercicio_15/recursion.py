# -*- coding: utf-8 -*-
def mcd(a, b):
    """Máximo común divisor (algoritmo de Euclides) recursivo."""
    if b == 0:
        return a
    return mcd(b, a % b)
