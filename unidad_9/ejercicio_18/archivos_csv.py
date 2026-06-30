# -*- coding: utf-8 -*-
import csv

def csv_a_diccionario(nombre):
    """Lee un CSV de producto,precio y lo carga en un diccionario."""
    precios = {}
    with open(nombre, "r", encoding="utf-8") as f:
        for fila in csv.reader(f):
            precios[fila[0]] = int(fila[1])
    return precios
