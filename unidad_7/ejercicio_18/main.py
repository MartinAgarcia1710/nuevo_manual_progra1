# -*- coding: utf-8 -*-
from carrito import total

carrito = {"pan": 2, "leche": 1}
precios = {"pan": 800, "leche": 1200}
print("Total: $", total(carrito, precios))
