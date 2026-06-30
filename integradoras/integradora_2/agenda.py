# -*- coding: utf-8 -*-
"""Agenda de contactos con persistencia en archivo."""
import os


def cargar(archivo):
    contactos = {}
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split(",")
                if len(partes) == 3:
                    nombre, tel, correo = partes
                    contactos[nombre] = {"tel": tel, "correo": correo}
    return contactos


def guardar(archivo, contactos):
    with open(archivo, "w", encoding="utf-8") as f:
        for nombre, datos in contactos.items():
            f.write(f"{nombre},{datos['tel']},{datos['correo']}\n")


def agregar(contactos, nombre, tel, correo):
    contactos[nombre] = {"tel": tel, "correo": correo}


def eliminar(contactos, nombre):
    contactos.pop(nombre, None)
