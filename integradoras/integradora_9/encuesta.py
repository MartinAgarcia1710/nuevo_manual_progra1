# -*- coding: utf-8 -*-
"""Procesa respuestas de una encuesta de opción múltiple."""


def contar(respuestas):
    conteo = {}
    for r in respuestas:
        conteo[r] = conteo.get(r, 0) + 1
    return conteo


def porcentajes(respuestas):
    total = len(respuestas)
    conteo = contar(respuestas)
    return {opcion: round(c / total * 100, 1) for opcion, c in conteo.items()}


def mas_votada(respuestas):
    conteo = contar(respuestas)
    return max(conteo, key=conteo.get)


def guardar_informe(archivo, respuestas):
    with open(archivo, "w", encoding="utf-8") as f:
        for opcion, pct in porcentajes(respuestas).items():
            f.write(f"{opcion}: {pct}%\n")
