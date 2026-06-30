# -*- coding: utf-8 -*-
def leer_todo(nombre):
    """Devuelve el contenido completo de un archivo."""
    with open(nombre, "r", encoding="utf-8") as f:
        return f.read()
