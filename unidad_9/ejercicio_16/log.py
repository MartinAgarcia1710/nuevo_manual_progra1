# -*- coding: utf-8 -*-
def registrar(nombre, mensaje):
    """Agrega una línea de registro al archivo."""
    with open(nombre, "a", encoding="utf-8") as f:
        f.write(mensaje + "\n")
