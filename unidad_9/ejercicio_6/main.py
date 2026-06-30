# -*- coding: utf-8 -*-
from archivos import guardar_lista, cargar_lista

guardar_lista("nombres.txt", ["Ana", "Bruno", "Carla"])
print("Recuperados:", cargar_lista("nombres.txt"))
