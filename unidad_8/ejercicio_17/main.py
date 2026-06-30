# -*- coding: utf-8 -*-
from anidado import dato_profundo

agenda = {"Ana": {"tel": "111"}}
print(dato_profundo(agenda, "Ana", "tel"))
print(dato_profundo(agenda, "Ana", "correo"))
