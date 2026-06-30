# -*- coding: utf-8 -*-
def dato_profundo(datos, clave1, clave2):
    """Accede a datos[clave1][clave2] manejando los KeyError."""
    try:
        return datos[clave1][clave2]
    except KeyError:
        return "Dato no encontrado"
