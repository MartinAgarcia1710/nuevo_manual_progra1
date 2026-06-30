# -*- coding: utf-8 -*-
def multiplicar(a, b):
    """Multiplica dos números usando solo sumas, de forma recursiva."""
    if b == 0:
        return 0
    return a + multiplicar(a, b - 1)
