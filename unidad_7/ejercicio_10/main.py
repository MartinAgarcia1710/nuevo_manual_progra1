# -*- coding: utf-8 -*-
from traductor import traducir

for p in ["hola", "gato", "auto"]:
    print(f"{p} -> {traducir(p)}")
