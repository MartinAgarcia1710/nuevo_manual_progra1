# -*- coding: utf-8 -*-
from validacion import edad_valida

for e in [25, -3, 150, 0, 120]:
    print(f"{e} -> válida: {edad_valida(e)}")
# Para la versión interactiva, descomentá:
# from validacion import pedir_edad
# print("Edad ingresada:", pedir_edad())
