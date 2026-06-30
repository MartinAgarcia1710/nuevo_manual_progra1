# -*- coding: utf-8 -*-
from ranking import ordenar

puntajes = {"Ana": 120, "Leo": 90, "Sol": 150}
for jugador, p in ordenar(puntajes):
    print(f"{jugador}: {p}")
