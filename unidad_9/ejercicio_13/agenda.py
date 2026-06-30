# -*- coding: utf-8 -*-
def guardar(nombre, contactos):
    with open(nombre, "w", encoding="utf-8") as f:
        for n, tel in contactos.items():
            f.write(f"{n},{tel}\n")

def cargar(nombre):
    contactos = {}
    try:
        with open(nombre, "r", encoding="utf-8") as f:
            for linea in f:
                n, tel = linea.strip().split(",")
                contactos[n] = tel
    except FileNotFoundError:
        pass
    return contactos
