# -*- coding: utf-8 -*-
"""Gestor de turnos evitando superposiciones."""


class HorarioOcupado(Exception):
    pass


def reservar(turnos, horario, nombre):
    if horario in turnos:
        raise HorarioOcupado(f"El horario {horario} ya está ocupado")
    turnos[horario] = nombre


def cancelar(turnos, horario):
    turnos.pop(horario, None)


def listar(turnos):
    return sorted(turnos.items())


def guardar(archivo, turnos):
    with open(archivo, "w", encoding="utf-8") as f:
        for horario, nombre in sorted(turnos.items()):
            f.write(f"{horario},{nombre}\n")
