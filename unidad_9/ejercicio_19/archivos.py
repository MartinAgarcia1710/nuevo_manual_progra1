# -*- coding: utf-8 -*-
def estadisticas(nombre):
    """Devuelve cantidad, suma, máximo y mínimo de los números del archivo."""
    with open(nombre, "r", encoding="utf-8") as f:
        numeros = [float(l) for l in f if l.strip()]
    return {
        "cantidad": len(numeros),
        "suma": sum(numeros),
        "maximo": max(numeros),
        "minimo": min(numeros),
    }
