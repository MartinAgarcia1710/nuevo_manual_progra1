# -*- coding: utf-8 -*-
from registro import manejar

print(manejar(lambda: 10 / 0))
print(manejar(lambda: int("x")))
print(manejar(lambda: [1, 2][5]))
