# -*- coding: utf-8 -*-
def mostrar_inverso(lista):
    """Muestra los elementos de una lista en orden inverso."""
    if not lista:
        return
    print(lista[-1])
    mostrar_inverso(lista[:-1])
