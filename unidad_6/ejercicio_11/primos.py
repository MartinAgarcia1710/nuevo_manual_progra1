# -*- coding: utf-8 -*-
def es_primo(n):
    """Devuelve True si n es primo."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
