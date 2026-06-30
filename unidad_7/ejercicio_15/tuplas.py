# -*- coding: utf-8 -*-
def intentar_modificar():
    """Demuestra que una tupla es inmutable y cómo convertirla a lista."""
    punto = (3, 5)
    try:
        punto[0] = 9
    except TypeError as e:
        mensaje = f"No se puede modificar la tupla: {e}"
    como_lista = list(punto)
    como_lista[0] = 9
    return mensaje, tuple(como_lista)
