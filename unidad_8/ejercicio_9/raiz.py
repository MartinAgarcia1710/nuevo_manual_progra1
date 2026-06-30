# -*- coding: utf-8 -*-
def raiz_segura(n):
    """Calcula la raíz cuadrada lanzando un error si n es negativo."""
    if n < 0:
        raise ValueError("No existe raíz real de un número negativo")
    return n ** 0.5
