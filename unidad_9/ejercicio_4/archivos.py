# -*- coding: utf-8 -*-
def agregar_linea(nombre, texto):
    """Agrega una línea al final sin borrar el contenido."""
    with open(nombre, "a", encoding="utf-8") as f:
        f.write(texto + "\n")
