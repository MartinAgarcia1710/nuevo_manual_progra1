# -*- coding: utf-8 -*-
from turnos import reservar, cancelar, listar, guardar, HorarioOcupado


def demo():
    turnos = {}
    reservar(turnos, "09:00", "Ana")
    reservar(turnos, "10:00", "Leo")
    try:
        reservar(turnos, "09:00", "Sol")
    except HorarioOcupado as e:
        print("Rechazado:", e)
    cancelar(turnos, "10:00")
    print("Turnos:", listar(turnos))
    guardar("turnos.txt", turnos)


if __name__ == "__main__":
    demo()
