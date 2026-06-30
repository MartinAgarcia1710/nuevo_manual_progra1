# -*- coding: utf-8 -*-
from stock import actualizar

stock = {"lapices": 10, "cuadernos": 5}
actualizar(stock, "lapices", 5)
actualizar(stock, "cuadernos", -2)
print(stock)
