# -*- coding: utf-8 -*-
from inventario import listar

productos = {"pan": 800, "leche": 1200, "huevos": 2000}
for linea in listar(productos):
    print(linea)
