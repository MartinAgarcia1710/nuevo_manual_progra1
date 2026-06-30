# -*- coding: utf-8 -*-
def leer_seguro(nombre):
    """Lee un archivo manejando el caso de que no exista."""
    try:
        with open(nombre, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "El archivo no existe todavía."
