# -*- coding: utf-8 -*-
import csv

def escribir_csv(nombre, filas):
    with open(nombre, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerows(filas)
