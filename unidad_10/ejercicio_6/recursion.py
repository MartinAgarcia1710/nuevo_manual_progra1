# -*- coding: utf-8 -*-
def contar_digitos(n):
    """Cuenta los dígitos de un número entero."""
    n = abs(n)
    if n < 10:
        return 1
    return 1 + contar_digitos(n // 10)
