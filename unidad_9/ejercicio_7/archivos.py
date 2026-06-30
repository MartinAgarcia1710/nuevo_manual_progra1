# -*- coding: utf-8 -*-
def contar_apariciones(nombre, palabra):
    """Cuenta cuántas veces aparece una palabra en el archivo."""
    with open(nombre, "r", encoding="utf-8") as f:
        texto = f.read()
    return texto.lower().split().count(palabra.lower())
