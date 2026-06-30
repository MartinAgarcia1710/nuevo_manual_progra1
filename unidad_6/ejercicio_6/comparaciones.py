# -*- coding: utf-8 -*-
def maximo(a, b, c):
    """Devuelve el mayor de tres números."""
    mayor = a
    if b > mayor:
        mayor = b
    if c > mayor:
        mayor = c
    return mayor
