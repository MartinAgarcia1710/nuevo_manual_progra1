# -*- coding: utf-8 -*-
"""Registro de gastos personales con persistencia en CSV."""
import csv
import os


def registrar(archivo, categoria, monto, fecha):
    existe = os.path.exists(archivo)
    with open(archivo, "a", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        if not existe:
            escritor.writerow(["categoria", "monto", "fecha"])
        escritor.writerow([categoria, monto, fecha])


def total_por_categoria(archivo):
    totales = {}
    with open(archivo, "r", encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector, None)  # saltar cabecera
        for fila in lector:
            cat, monto, _ = fila
            totales[cat] = totales.get(cat, 0) + float(monto)
    return totales
