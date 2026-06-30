# -*- coding: utf-8 -*-
def invertir(texto):
    """Devuelve la cadena invertida de forma recursiva."""
    if texto == "":
        return ""
    return texto[-1] + invertir(texto[:-1])
