# -*- coding: utf-8 -*-
from cajero import depositar, extraer, registrar, SaldoInsuficiente


def demo():
    saldo = 1000
    saldo = depositar(saldo, 500); registrar("movimientos.txt", "deposito", 500)
    print("Saldo tras depósito:", saldo)
    saldo = extraer(saldo, 300); registrar("movimientos.txt", "extraccion", 300)
    print("Saldo tras extracción:", saldo)
    try:
        extraer(saldo, 99999)
    except SaldoInsuficiente as e:
        print("Operación rechazada:", e)


if __name__ == "__main__":
    demo()
