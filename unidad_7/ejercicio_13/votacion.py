# -*- coding: utf-8 -*-
def contar_votos(votos):
    """Cuenta los votos y devuelve el conteo y la opción ganadora."""
    conteo = {}
    for v in votos:
        conteo[v] = conteo.get(v, 0) + 1
    ganadora = max(conteo, key=conteo.get)
    return conteo, ganadora
