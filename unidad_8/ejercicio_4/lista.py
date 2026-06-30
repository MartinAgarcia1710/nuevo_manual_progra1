# -*- coding: utf-8 -*-
def acceder(lista, indice):
    """Accede a lista[indice] manejando el IndexError."""
    try:
        return lista[indice]
    except IndexError:
        return "Índice fuera de rango"
