# -*- coding: utf-8 -*-
from primos import es_primo

primos = [n for n in range(2, 51) if es_primo(n)]
print("Primos hasta 50:", primos)
