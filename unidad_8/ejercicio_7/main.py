# -*- coding: utf-8 -*-
from banco import extraer, SaldoInsuficiente

try:
    print("Nuevo saldo:", extraer(1000, 300))
    print("Nuevo saldo:", extraer(1000, 5000))
except SaldoInsuficiente as e:
    print("Rechazado:", e)
