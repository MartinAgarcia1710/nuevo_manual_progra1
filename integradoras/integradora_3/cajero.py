# -*- coding: utf-8 -*-
"""Lógica de un cajero automático simple."""


class SaldoInsuficiente(Exception):
    pass


def depositar(saldo, monto):
    if monto <= 0:
        raise ValueError("El monto debe ser positivo")
    return saldo + monto


def extraer(saldo, monto):
    if monto <= 0:
        raise ValueError("El monto debe ser positivo")
    if monto > saldo:
        raise SaldoInsuficiente("Saldo insuficiente")
    return saldo - monto


def registrar(archivo, operacion, monto):
    with open(archivo, "a", encoding="utf-8") as f:
        f.write(f"{operacion}: {monto}\n")
