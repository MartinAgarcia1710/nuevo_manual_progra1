# -*- coding: utf-8 -*-
def tabla(n):
    """Devuelve la tabla de multiplicar de n como lista de textos."""
    return [f"{n} x {i} = {n * i}" for i in range(1, 11)]
