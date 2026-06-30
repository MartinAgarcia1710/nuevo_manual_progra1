# -*- coding: utf-8 -*-
from biblioteca import (agregar_libro, prestar, devolver,
                        disponibles, buscar_por_autor, guardar)


def demo():
    catalogo = []
    agregar_libro(catalogo, "El Aleph", "Borges")
    agregar_libro(catalogo, "Ficciones", "Borges")
    agregar_libro(catalogo, "Rayuela", "Cortazar")
    prestar(catalogo, "El Aleph")
    print("Disponibles:", disponibles(catalogo))
    print("De Borges:", buscar_por_autor(catalogo, "Borges"))
    devolver(catalogo, "El Aleph")
    print("Disponibles tras devolución:", disponibles(catalogo))
    guardar("catalogo.csv", catalogo)


if __name__ == "__main__":
    demo()
