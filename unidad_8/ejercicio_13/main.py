# -*- coding: utf-8 -*-
from nota import validar_nota, NotaInvalida

for n in [8, 15]:
    try:
        print("Nota válida:", validar_nota(n))
    except NotaInvalida as e:
        print("Error:", e)
