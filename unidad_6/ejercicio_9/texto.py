# -*- coding: utf-8 -*-
def contar_vocales(texto):
    """Cuenta las vocales de un texto."""
    cantidad = 0
    for letra in texto.lower():
        if letra in "aeiou":
            cantidad += 1
    return cantidad
