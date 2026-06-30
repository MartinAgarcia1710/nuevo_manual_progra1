# -*- coding: utf-8 -*-
def valida_password(texto):
    """La contraseña es válida si tiene al menos 8 caracteres y un número."""
    if len(texto) < 8:
        return False
    tiene_numero = any(c.isdigit() for c in texto)
    return tiene_numero
