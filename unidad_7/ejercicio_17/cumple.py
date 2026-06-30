# -*- coding: utf-8 -*-
def cumples_del_mes(agenda, mes):
    """Devuelve los nombres cuyo cumpleaños (dia, mes) cae en el mes dado."""
    return [nombre for nombre, (dia, m) in agenda.items() if m == mes]
