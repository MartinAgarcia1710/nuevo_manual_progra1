# -*- coding: utf-8 -*-
def a_entero(texto):
    """Convierte texto a entero; devuelve None si no es válido."""
    try:
        return int(texto)
    except ValueError:
        print(f"'{texto}' no es un número entero válido.")
        return None
