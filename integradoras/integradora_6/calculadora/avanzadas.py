# -*- coding: utf-8 -*-
def potencia(base, exp):
    return base ** exp

def raiz(n):
    if n < 0:
        raise ValueError("No existe raíz real de un negativo")
    return n ** 0.5
