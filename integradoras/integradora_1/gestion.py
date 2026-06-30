# -*- coding: utf-8 -*-
"""Lógica del sistema de gestión de notas."""


def agregar_alumno(alumnos, nombre, notas):
    alumnos[nombre] = notas
    return alumnos


def promedio(notas):
    return sum(notas) / len(notas) if notas else 0


def aprobados(alumnos, minimo=6):
    return [n for n, notas in alumnos.items() if promedio(notas) >= minimo]


def guardar_resultados(nombre_archivo, alumnos):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        for nombre, notas in alumnos.items():
            f.write(f"{nombre}: promedio {promedio(notas):.2f}\n")
