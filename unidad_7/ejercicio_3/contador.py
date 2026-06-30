# -*- coding: utf-8 -*-
def contar_palabras(frase):
    """Devuelve un diccionario palabra -> cantidad de apariciones."""
    conteo = {}
    for palabra in frase.split():
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo
