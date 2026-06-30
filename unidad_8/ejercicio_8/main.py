# -*- coding: utf-8 -*-
from validacion import validar_edad

for e in [30, -5]:
    try:
        print("Edad válida:", validar_edad(e))
    except ValueError as error:
        print("Error:", error)
