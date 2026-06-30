# -*- coding: utf-8 -*-
def calcular_edad(anio_texto, anio_actual=2026):
    """Calcula la edad manejando entradas no numéricas."""
    try:
        return anio_actual - int(anio_texto)
    except ValueError:
        return "Año inválido"
