# -*- coding: utf-8 -*-
def total(carrito, precios):
    """Calcula el total del carrito (producto -> cantidad) con un dict de precios."""
    return sum(precios[p] * cant for p, cant in carrito.items())
