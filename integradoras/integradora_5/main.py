# -*- coding: utf-8 -*-
from juego import jugar_automatico, guardar_puntaje, ranking


def demo():
    secreto = 42
    intentos = jugar_automatico(secreto, [50, 30, 40, 42])
    print(f"Adivinado en {intentos} intentos")
    guardar_puntaje("ranking.txt", "Ana", intentos)
    guardar_puntaje("ranking.txt", "Leo", 7)
    print("Ranking:")
    for nombre, p in ranking("ranking.txt"):
        print(f"  {nombre}: {p} intentos")


if __name__ == "__main__":
    demo()
