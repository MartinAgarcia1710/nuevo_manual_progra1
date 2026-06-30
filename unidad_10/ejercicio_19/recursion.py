# -*- coding: utf-8 -*-
def triangulo(n, i=1):
    """Dibuja un triángulo de n filas de asteriscos."""
    if i > n:
        return
    print("*" * i)
    triangulo(n, i + 1)
