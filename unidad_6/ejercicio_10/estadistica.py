# -*- coding: utf-8 -*-
def promedio(*notas):
    """Promedio de cualquier cantidad de notas."""
    if not notas:
        return 0
    return sum(notas) / len(notas)
