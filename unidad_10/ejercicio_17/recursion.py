# -*- coding: utf-8 -*-
def potencias_de_dos(n, i=0):
    """Muestra las primeras n potencias de 2."""
    if i >= n:
        return
    print(2 ** i, end=" ")
    potencias_de_dos(n, i + 1)
