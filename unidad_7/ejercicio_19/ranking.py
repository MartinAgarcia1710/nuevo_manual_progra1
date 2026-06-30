# -*- coding: utf-8 -*-
def ordenar(puntajes):
    """Devuelve la lista (jugador, puntaje) ordenada de mayor a menor."""
    return sorted(puntajes.items(), key=lambda par: par[1], reverse=True)
