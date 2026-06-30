# -*- coding: utf-8 -*-
def factorial(n):
    """Factorial de n de forma recursiva."""
    if n == 0:
        return 1
    return n * factorial(n - 1)
