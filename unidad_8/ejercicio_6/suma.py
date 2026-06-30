# -*- coding: utf-8 -*-
def sumar_textos(a, b):
    """Convierte y suma dos textos manejando errores de conversión y tipo."""
    try:
        return int(a) + int(b)
    except ValueError:
        return "Error: alguno no es un número"
    except TypeError:
        return "Error: tipo inválido"
