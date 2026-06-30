# -*- coding: utf-8 -*-
from archivos_json import guardar, leer

guardar("datos.json", {"nombre": "Ana", "notas": [7, 8, 10]})
recuperado = leer("datos.json")
print("Notas:", recuperado["notas"])
