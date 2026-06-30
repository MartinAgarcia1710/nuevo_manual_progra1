# -*- coding: utf-8 -*-
def factorial_iterativo(n):
    """Factorial con un bucle."""
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def factorial_recursivo(n):
    """Factorial con recursión. Comparado con la versión iterativa:
    la recursiva es más corta y cercana a la definición matemática,
    pero usa más memoria por la pila de llamadas."""
    if n == 0:
        return 1
    return n * factorial_recursivo(n - 1)
