# -*- coding: utf-8 -*-
def a_entero(texto):
    """Intenta convertir; devuelve (ok, valor)."""
    try:
        return True, int(texto)
    except ValueError:
        return False, None

def pedir_entero(mensaje):
    """Versión interactiva: insiste hasta obtener un entero válido."""
    while True:
        ok, valor = a_entero(input(mensaje))
        if ok:
            return valor
        print("Valor inválido, probá de nuevo.")
