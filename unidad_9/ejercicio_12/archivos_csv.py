# -*- coding: utf-8 -*-
import csv

def leer_csv(nombre):
    with open(nombre, "r", encoding="utf-8") as f:
        return [fila for fila in csv.reader(f)]
