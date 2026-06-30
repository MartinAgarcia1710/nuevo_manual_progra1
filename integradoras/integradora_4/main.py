# -*- coding: utf-8 -*-
from inventario import alta, baja, valor_total, guardar_csv


def demo():
    inventario = {}
    alta(inventario, "lapiz", 100, 50)
    alta(inventario, "cuaderno", 800, 20)
    alta(inventario, "goma", 150, 30)
    baja(inventario, "goma")
    print("Valor total del inventario: $", valor_total(inventario))
    guardar_csv("inventario.csv", inventario)
    print("Inventario guardado en inventario.csv")


if __name__ == "__main__":
    demo()
