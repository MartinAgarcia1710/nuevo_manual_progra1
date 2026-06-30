# -*- coding: utf-8 -*-
def copiar(origen, destino):
    """Copia el contenido de un archivo en otro."""
    with open(origen, "r", encoding="utf-8") as f:
        contenido = f.read()
    with open(destino, "w", encoding="utf-8") as f:
        f.write(contenido)
