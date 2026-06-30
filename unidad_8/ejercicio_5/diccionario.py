# -*- coding: utf-8 -*-
def acceder(dic, clave):
    """Accede a dic[clave] manejando el KeyError."""
    try:
        return dic[clave]
    except KeyError:
        return "Clave inexistente"
