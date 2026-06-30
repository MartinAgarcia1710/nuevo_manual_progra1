# -*- coding: utf-8 -*-
"""Juego de adivinanza con ranking persistente."""
import os


def evaluar(secreto, intento):
    if intento == secreto:
        return "correcto"
    return "mas alto" if intento < secreto else "mas bajo"


def jugar_automatico(secreto, intentos):
    """Simula una partida con una lista de intentos. Devuelve cuántos hizo."""
    for i, intento in enumerate(intentos, 1):
        if evaluar(secreto, intento) == "correcto":
            return i
    return len(intentos)


def guardar_puntaje(archivo, nombre, intentos):
    with open(archivo, "a", encoding="utf-8") as f:
        f.write(f"{nombre},{intentos}\n")


def ranking(archivo):
    if not os.path.exists(archivo):
        return []
    puntajes = []
    with open(archivo, "r", encoding="utf-8") as f:
        for linea in f:
            nombre, intentos = linea.strip().split(",")
            puntajes.append((nombre, int(intentos)))
    return sorted(puntajes, key=lambda p: p[1])
