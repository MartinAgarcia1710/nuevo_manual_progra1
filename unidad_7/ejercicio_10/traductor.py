# -*- coding: utf-8 -*-
DICCIONARIO = {"hola": "hello", "gato": "cat", "perro": "dog", "casa": "house", "sol": "sun"}

def traducir(palabra):
    return DICCIONARIO.get(palabra.lower(), "(sin traducción)")
