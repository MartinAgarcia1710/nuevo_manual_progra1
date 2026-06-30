# -*- coding: utf-8 -*-
def potencia(base, exp):
    """Calcula base^exp de forma recursiva."""
    if exp == 0:
        return 1
    return base * potencia(base, exp - 1)
