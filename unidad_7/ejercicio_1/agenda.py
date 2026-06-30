# -*- coding: utf-8 -*-
def buscar_telefono(contactos, nombre):
    """Devuelve el teléfono de un contacto o un aviso si no existe."""
    return contactos.get(nombre, "Contacto no encontrado")
