# -*- coding: utf-8 -*-
from menu import procesar_opcion

for t in ["1", "9", "abc"]:
    print(t, "->", procesar_opcion(t))
