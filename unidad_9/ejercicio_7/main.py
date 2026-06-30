# -*- coding: utf-8 -*-
from archivos import contar_apariciones

with open("texto.txt", "w", encoding="utf-8") as f:
    f.write("el sol y el mar y el cielo")

print("'el' aparece:", contar_apariciones("texto.txt", "el"), "veces")
