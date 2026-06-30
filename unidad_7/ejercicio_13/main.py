# -*- coding: utf-8 -*-
from votacion import contar_votos

votos = ["A", "B", "A", "C", "A", "B"]
conteo, ganadora = contar_votos(votos)
print("Conteo:", conteo)
print("Ganadora:", ganadora)
