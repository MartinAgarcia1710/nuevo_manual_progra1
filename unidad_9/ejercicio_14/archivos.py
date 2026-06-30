# -*- coding: utf-8 -*-
def contar_palabras(nombre):
    with open(nombre, "r", encoding="utf-8") as f:
        return len(f.read().split())
