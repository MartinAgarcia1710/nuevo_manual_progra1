# -*- coding: utf-8 -*-
import csv
from archivos_csv import leer_csv

with open("personas.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows([["nombre", "edad"], ["Ana", 30]])

for fila in leer_csv("personas.csv"):
    print(fila)
