# -*- coding: utf-8 -*-
from gestion import agregar_alumno, promedio, aprobados, guardar_resultados


def demo():
    alumnos = {}
    agregar_alumno(alumnos, "Ana", [7, 8, 10])
    agregar_alumno(alumnos, "Leo", [4, 5, 6])
    agregar_alumno(alumnos, "Sol", [9, 9, 8])
    for nombre, notas in alumnos.items():
        print(f"{nombre}: {promedio(notas):.2f}")
    print("Aprobados:", aprobados(alumnos))
    guardar_resultados("resultados.txt", alumnos)
    print("Resultados guardados en resultados.txt")


if __name__ == "__main__":
    demo()
