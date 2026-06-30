# -*- coding: utf-8 -*-
from archivos_csv import escribir_csv

filas = [["nombre", "edad"], ["Ana", 30], ["Bruno", 25], ["Carla", 28]]
escribir_csv("personas.csv", filas)
print("personas.csv creado.")
