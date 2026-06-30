# -*- coding: utf-8 -*-
def calcular(a, b, op):
    """Calculadora robusta: maneja división por cero y operaciones inválidas."""
    try:
        if op == "+": return a + b
        if op == "-": return a - b
        if op == "*": return a * b
        if op == "/": return a / b
        return "Operación inválida"
    except ZeroDivisionError:
        return "No se puede dividir por cero"
