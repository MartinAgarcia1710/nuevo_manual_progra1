# -*- coding: utf-8 -*-
def agregar(contactos, nombre, telefono):
    contactos[nombre] = telefono
    return contactos

def eliminar(contactos, nombre):
    if nombre in contactos:
        del contactos[nombre]
    return contactos
