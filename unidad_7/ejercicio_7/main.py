# -*- coding: utf-8 -*-
from agenda import agregar, eliminar

contactos = {}
agregar(contactos, "Ana", "111")
agregar(contactos, "Leo", "222")
print("Tras altas:", contactos)
eliminar(contactos, "Ana")
print("Tras baja:", contactos)
