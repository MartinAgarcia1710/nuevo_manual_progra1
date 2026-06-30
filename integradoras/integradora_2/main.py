# -*- coding: utf-8 -*-
from agenda import cargar, guardar, agregar, eliminar


def demo():
    contactos = cargar("contactos.txt")
    agregar(contactos, "Ana", "111-2222", "ana@mail.com")
    agregar(contactos, "Leo", "333-4444", "leo@mail.com")
    guardar("contactos.txt", contactos)
    print("Guardados:", list(contactos.keys()))
    recargada = cargar("contactos.txt")
    print("Recargada desde archivo:", recargada)


if __name__ == "__main__":
    demo()
