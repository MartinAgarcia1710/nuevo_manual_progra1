# -*- coding: utf-8 -*-
def convertir(texto):
    """Convierte un texto a Celsius->Fahrenheit manejando entradas inválidas."""
    try:
        c = float(texto)
        return c * 9 / 5 + 32
    except ValueError:
        return "Ingresá un número válido"
