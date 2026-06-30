# -*- coding: utf-8 -*-
from raiz import raiz_segura

for n in [16, -9]:
    try:
        print(f"raíz({n}) =", raiz_segura(n))
    except ValueError as e:
        print("Error:", e)
