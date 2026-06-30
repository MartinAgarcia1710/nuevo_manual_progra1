# -*- coding: utf-8 -*-
def procesar_opcion(texto):
    """Valida la opción del menú; devuelve un mensaje según el caso."""
    try:
        opcion = int(texto)
    except ValueError:
        return "La opción debe ser un número"
    if opcion in (1, 2, 3):
        return f"Opción {opcion} seleccionada"
    return "Opción fuera del menú"
