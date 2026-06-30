# -*- coding: utf-8 -*-
"""Sistema de gestión de una biblioteca con persistencia."""
import csv
import os


def agregar_libro(catalogo, titulo, autor):
    catalogo.append({"titulo": titulo, "autor": autor, "disponible": True})


def prestar(catalogo, titulo):
    for libro in catalogo:
        if libro["titulo"] == titulo and libro["disponible"]:
            libro["disponible"] = False
            return True
    return False


def devolver(catalogo, titulo):
    for libro in catalogo:
        if libro["titulo"] == titulo:
            libro["disponible"] = True
            return True
    return False


def disponibles(catalogo):
    return [l["titulo"] for l in catalogo if l["disponible"]]


def buscar_por_autor(catalogo, autor):
    return [l["titulo"] for l in catalogo if l["autor"] == autor]


def guardar(archivo, catalogo):
    with open(archivo, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        for l in catalogo:
            escritor.writerow([l["titulo"], l["autor"], l["disponible"]])
