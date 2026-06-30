# -*- coding: utf-8 -*-
import json

def guardar(nombre, datos):
    with open(nombre, "w", encoding="utf-8") as f:
        json.dump(datos, f)

def leer(nombre):
    with open(nombre, "r", encoding="utf-8") as f:
        return json.load(f)
