# -*- coding: utf-8 -*-
def guardar_lista(nombre, lista):
    with open(nombre, "w", encoding="utf-8") as f:
        for item in lista:
            f.write(item + "\n")

def cargar_lista(nombre):
    with open(nombre, "r", encoding="utf-8") as f:
        return [linea.strip() for linea in f]
