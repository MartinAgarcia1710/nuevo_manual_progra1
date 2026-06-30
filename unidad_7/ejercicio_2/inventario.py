# -*- coding: utf-8 -*-
def listar(productos):
    """Devuelve una lista de textos producto: precio."""
    return [f"{p}: ${precio}" for p, precio in productos.items()]
