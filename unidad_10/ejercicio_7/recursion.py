# -*- coding: utf-8 -*-
def suma_hasta(n):
    """Suma todos los enteros desde 1 hasta n."""
    if n == 0:
        return 0
    return n + suma_hasta(n - 1)
