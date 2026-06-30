# -*- coding: utf-8 -*-
from agenda import guardar, cargar

guardar("agenda.txt", {"Ana": "111", "Leo": "222"})
print("Agenda cargada:", cargar("agenda.txt"))
