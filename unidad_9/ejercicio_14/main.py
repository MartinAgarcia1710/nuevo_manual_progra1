# -*- coding: utf-8 -*-
from archivos import contar_palabras

with open("texto.txt", "w", encoding="utf-8") as f:
    f.write("hola mundo desde python en utn")

print("Palabras:", contar_palabras("texto.txt"))
