# -*- coding: utf-8 -*-
def actualizar(stock, producto, cantidad):
    """Suma (o resta) cantidad al stock de un producto."""
    stock[producto] = stock.get(producto, 0) + cantidad
    return stock
