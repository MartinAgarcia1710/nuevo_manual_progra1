# -*- coding: utf-8 -*-
import csv
from archivos_csv import csv_a_diccionario

with open("precios.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows([["pan", 800], ["leche", 1200]])

print(csv_a_diccionario("precios.csv"))
