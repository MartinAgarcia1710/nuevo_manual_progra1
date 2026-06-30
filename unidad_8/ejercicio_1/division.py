# -*- coding: utf-8 -*-
def dividir_seguro(a, b):
    """Divide a por b manejando la división por cero."""
    try:
        return a / b
    except ZeroDivisionError:
        return "No se puede dividir por cero"
