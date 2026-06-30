# -*- coding: utf-8 -*-
def procesar(texto):
    """Demuestra try / except / finally."""
    salida = []
    try:
        numero = int(texto)
        salida.append(f"El doble es {numero * 2}")
    except ValueError:
        salida.append("No era un número")
    finally:
        salida.append("Proceso finalizado")
    return salida
