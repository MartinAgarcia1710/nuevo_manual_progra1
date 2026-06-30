# -*- coding: utf-8 -*-
import os
from gastos import registrar, total_por_categoria


def demo():
    if os.path.exists("gastos.csv"):
        os.remove("gastos.csv")
    registrar("gastos.csv", "comida", 5000, "2026-06-01")
    registrar("gastos.csv", "transporte", 1200, "2026-06-02")
    registrar("gastos.csv", "comida", 3000, "2026-06-03")
    print("Totales por categoría:", total_por_categoria("gastos.csv"))


if __name__ == "__main__":
    demo()
