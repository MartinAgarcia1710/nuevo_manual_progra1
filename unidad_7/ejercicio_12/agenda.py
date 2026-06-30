# -*- coding: utf-8 -*-
def datos_contacto(agenda, nombre):
    """Devuelve el diccionario de datos de un contacto."""
    return agenda.get(nombre, {})
