# -*- coding: utf-8 -*-
from encuesta import porcentajes, mas_votada, guardar_informe


def demo():
    respuestas = ["A", "B", "A", "C", "A", "B", "A"]
    print("Porcentajes:", porcentajes(respuestas))
    print("Más votada:", mas_votada(respuestas))
    guardar_informe("informe.txt", respuestas)
    print("Informe guardado en informe.txt")


if __name__ == "__main__":
    demo()
