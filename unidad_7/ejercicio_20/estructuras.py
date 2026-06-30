# -*- coding: utf-8 -*-
def demostrar(datos):
    """Muestra el mismo conjunto de datos como lista, tupla, conjunto y dict."""
    como_lista = list(datos)
    como_tupla = tuple(datos)
    como_set = set(datos)
    como_dict = {i: v for i, v in enumerate(datos)}
    return como_lista, como_tupla, como_set, como_dict
