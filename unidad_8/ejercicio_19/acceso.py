# -*- coding: utf-8 -*-
def verificar(intentos, clave_correcta, maximo=3):
    """Recibe una lista de intentos y devuelve si se logró el acceso."""
    for i, intento in enumerate(intentos[:maximo], 1):
        if intento == clave_correcta:
            return f"Acceso correcto en el intento {i}"
    return "Acceso bloqueado tras varios intentos"
