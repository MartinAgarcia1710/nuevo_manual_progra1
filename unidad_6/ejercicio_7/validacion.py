# -*- coding: utf-8 -*-
def edad_valida(edad):
    """Devuelve True si la edad está entre 0 y 120."""
    return 0 <= edad <= 120

def pedir_edad():
    """Pide una edad por teclado hasta que sea válida (uso interactivo)."""
    edad = int(input("Edad: "))
    while not edad_valida(edad):
        print("Edad inválida.")
        edad = int(input("Edad: "))
    return edad
