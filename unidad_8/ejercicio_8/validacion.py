# -*- coding: utf-8 -*-
def validar_edad(edad):
    """Lanza ValueError si la edad no es válida; si no, la devuelve."""
    if edad < 0 or edad > 120:
        raise ValueError("Edad fuera de rango (0-120)")
    return edad
