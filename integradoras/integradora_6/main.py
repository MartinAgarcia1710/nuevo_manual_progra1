# -*- coding: utf-8 -*-
from calculadora import basicas, avanzadas, estadistica


def demo():
    print("3 + 4 =", basicas.sumar(3, 4))
    print("2^10 =", avanzadas.potencia(2, 10))
    print("raíz(81) =", avanzadas.raiz(81))
    print("promedio:", estadistica.promedio([4, 8, 10, 6]))
    try:
        basicas.dividir(5, 0)
    except ZeroDivisionError as e:
        print("Error controlado:", e)


if __name__ == "__main__":
    demo()
