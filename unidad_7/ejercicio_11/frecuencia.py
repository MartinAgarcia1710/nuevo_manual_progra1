# -*- coding: utf-8 -*-
def frecuencia_letras(palabra):
    """Diccionario letra -> cantidad de apariciones."""
    conteo = {}
    for letra in palabra:
        conteo[letra] = conteo.get(letra, 0) + 1
    return conteo
