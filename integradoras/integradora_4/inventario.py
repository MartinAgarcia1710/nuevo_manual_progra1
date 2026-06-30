# -*- coding: utf-8 -*-
"""Gestor de inventario con persistencia en CSV."""
import csv


def alta(inventario, producto, precio, stock):
    inventario[producto] = {"precio": precio, "stock": stock}


def baja(inventario, producto):
    inventario.pop(producto, None)


def valor_total(inventario):
    return sum(d["precio"] * d["stock"] for d in inventario.values())


def guardar_csv(archivo, inventario):
    with open(archivo, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(["producto", "precio", "stock"])
        for p, d in inventario.items():
            escritor.writerow([p, d["precio"], d["stock"]])
