# -*- coding: utf-8 -*-
def factorial(n):
    """Factorial de n usando un bucle."""
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
