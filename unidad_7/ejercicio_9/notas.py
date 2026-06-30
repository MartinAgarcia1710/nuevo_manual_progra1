# -*- coding: utf-8 -*-
def promedios(alumnos):
    """Recibe alumno -> lista de notas y devuelve alumno -> promedio."""
    return {a: sum(notas) / len(notas) for a, notas in alumnos.items()}
