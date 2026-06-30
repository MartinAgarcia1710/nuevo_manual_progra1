# -*- coding: utf-8 -*-
def potencia(base, exp):
    """Calcula base^exp con un bucle."""
    resultado = 1
    for _ in range(exp):
        resultado *= base
    return resultado
