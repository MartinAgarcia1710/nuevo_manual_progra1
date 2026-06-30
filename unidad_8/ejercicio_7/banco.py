# -*- coding: utf-8 -*-
class SaldoInsuficiente(Exception):
    """Se lanza cuando el monto supera el saldo disponible."""
    pass

def extraer(saldo, monto):
    if monto > saldo:
        raise SaldoInsuficiente("No hay saldo suficiente")
    return saldo - monto
