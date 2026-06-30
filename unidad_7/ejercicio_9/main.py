# -*- coding: utf-8 -*-
from notas import promedios

alumnos = {"Ana": [7, 8, 10], "Leo": [4, 6, 5]}
for a, p in promedios(alumnos).items():
    print(f"{a}: {p:.2f}")
