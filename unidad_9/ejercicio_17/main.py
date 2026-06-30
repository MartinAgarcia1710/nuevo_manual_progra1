# -*- coding: utf-8 -*-
from archivos import filtrar

with open("texto.txt", "w", encoding="utf-8") as f:
    f.write("error 1\nok\nerror 2\nlisto\n")

n = filtrar("texto.txt", "errores.txt", "error")
print(f"{n} líneas con 'error' guardadas.")
