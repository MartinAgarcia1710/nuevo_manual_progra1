# -*- coding: utf-8 -*-
def es_palindromo(palabra):
    """Indica si una palabra es un palíndromo."""
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])
